# FastAPI Deployment to AWS ECS with Fargate using CloudFormation

This example demonstrates how to deploy a production-ready FastAPI application to AWS ECS (Elastic Container Service) using Fargate (serverless containers) with infrastructure defined in CloudFormation YAML.

## Architecture Overview

```
Internet
    ↓
Application Load Balancer (ALB)
    ↓
ECS Service (Fargate)
    ↓
Multiple ECS Tasks (Containers)
```

## Key Components

1. **FastAPI Application** (`main_fastapi_ecs.py`) - RESTful API with health checks
2. **Dockerfile** - Container image definition using Python 3.11 and uv
3. **CloudFormation Template** (`cloudformation.yaml`) - Complete AWS infrastructure as code
4. **Deployment Script** (`deploy.sh`) - Automated build and deployment

## Prerequisites

- Python 3.11 or higher
- Docker installed locally
- AWS CLI configured with appropriate credentials
- AWS account with permissions for ECS, ECR, VPC, CloudFormation, IAM

## Source Code Overview

### FastAPI Application (`main_fastapi_ecs.py`)

**Key Sections:**

**Lines 21-27: FastAPI Application Initialization**
```python
app = FastAPI(
    title="FastAPI ECS Demo",
    description="Demo API for AWS ECS/Fargate deployment",
    version="1.0.0",
)
```

**Lines 62-75: Health Check Endpoint**
```python
@app.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Health check endpoint used by AWS ECS/ALB target group health checks."""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow().isoformat(),
        service="fastapi-ecs-demo",
    )
```
This endpoint is critical for:
- ALB target group health checks (cloudformation.yaml:227-230)
- ECS task health monitoring (cloudformation.yaml:332-339)
- Container health checks (Dockerfile:24-26)

**Lines 87-90: List Items Endpoint**
```python
@app.get("/items", response_model=List[Item])
async def list_items() -> List[Item]:
    """Retrieve all items from the database."""
    return list(items_db.values())
```

**Lines 148-156: Application Entry Point**
```python
uvicorn.run(
    app,
    host="0.0.0.0",  # Listen on all interfaces for container networking
    port=8000,       # Standard port, mapped in ECS task definition
    log_level="info",
)
```
The port 8000 corresponds to:
- Container port exposure (Dockerfile:17)
- ECS task definition port mapping (cloudformation.yaml:322-324)
- Target group configuration (cloudformation.yaml:221)

## Local Testing

**Step 1: Run the application locally**
```bash
uv run python main_fastapi_ecs.py
```

**Output:**
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

**Step 2: Test health endpoint**
```bash
curl http://localhost:8000/health
```

**Output (corresponds to lines 62-75):**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-25T12:34:56.789012",
  "service": "fastapi-ecs-demo"
}
```

**Step 3: Test items endpoint**
```bash
curl http://localhost:8000/items
```

**Output (corresponds to lines 54-59, 87-90):**
```json
[
  {
    "id": 1,
    "name": "Widget",
    "description": "A useful widget",
    "price": 19.99
  },
  {
    "id": 2,
    "name": "Gadget",
    "description": "An amazing gadget",
    "price": 29.99
  }
]
```

**Step 4: Test interactive API documentation**
Visit `http://localhost:8000/docs` for Swagger UI

## Docker Container

### Dockerfile Overview

**Lines 1-2: Base Image**
```dockerfile
FROM python:3.11-slim
```
Uses official Python 3.11 slim image for smaller size.

**Lines 7-8: Install uv**
```dockerfile
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
```
Installs uv for fast package management.

**Lines 13-15: Install Dependencies**
```dockerfile
RUN uv pip install --system fastapi>=0.115.0 uvicorn[standard]>=0.32.0
```
Matches dependencies from inline script metadata (main_fastapi_ecs.py:4-6).

**Lines 20-22: Security Best Practice**
```dockerfile
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser
```
Runs container as non-root user for security.

**Lines 24-26: Health Check**
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"
```
Docker-level health check calling the /health endpoint.

### Build and Test Docker Image Locally

```bash
docker build -t fastapi-ecs-demo .
docker run -p 8000:8000 fastapi-ecs-demo
```

**Output:**
```
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

## CloudFormation Template Architecture

The `cloudformation.yaml` file defines the complete AWS infrastructure:

### Network Infrastructure (Lines 55-159)

**VPC Configuration:**
- 1 VPC with CIDR 10.0.0.0/16 (line 55-64)
- 2 Public Subnets for ALB (lines 81-103)
- 2 Private Subnets for ECS tasks (lines 105-125)
- Internet Gateway for public internet access (lines 66-78)

**Why Private Subnets for ECS?**
Tasks run in private subnets for security, with internet access via NAT Gateway (for pulling ECR images). The ALB in public subnets handles incoming traffic.

### Security Groups (Lines 160-198)

**ALB Security Group (lines 160-174):**
```yaml
SecurityGroupIngress:
  - IpProtocol: tcp
    FromPort: 80
    ToPort: 80
    CidrIp: 0.0.0.0/0  # Allow HTTP from internet
```

**ECS Security Group (lines 176-190):**
```yaml
SecurityGroupIngress:
  - IpProtocol: tcp
    FromPort: !Ref ContainerPort  # 8000
    ToPort: !Ref ContainerPort
    SourceSecurityGroupId: !Ref ALBSecurityGroup  # Only from ALB
```

### Application Load Balancer (Lines 201-246)

**Load Balancer (lines 201-215):**
- Internet-facing
- Deployed in public subnets across 2 AZs for high availability

**Target Group (lines 217-235):**
```yaml
TargetType: ip  # Required for Fargate (line 225)
HealthCheckPath: /health  # Calls main_fastapi_ecs.py:62-75
HealthCheckIntervalSeconds: 30
HealthyThresholdCount: 2
UnhealthyThresholdCount: 3
```

### ECS Cluster (Lines 248-262)

```yaml
CapacityProviders:
  - FARGATE
  - FARGATE_SPOT
DefaultCapacityProviderStrategy:
  - CapacityProvider: FARGATE
    Weight: 1
```
Fargate = serverless containers (no EC2 management required).

### IAM Roles (Lines 264-297)

**Task Execution Role (lines 264-280):**
- Used by ECS agent to pull ECR images
- Write logs to CloudWatch
- Managed policy: `AmazonECSTaskExecutionRolePolicy`

**Task Role (lines 282-297):**
- Permissions for the application itself
- Can be extended to access S3, DynamoDB, etc.

### ECS Task Definition (Lines 306-344)

**Resource Allocation (lines 314-316):**
```yaml
Cpu: !Ref TaskCpu      # Default: 256 (.25 vCPU)
Memory: !Ref TaskMemory  # Default: 512 MB
```

**Container Configuration (lines 318-339):**
```yaml
Image: !Ref ImageUri  # ECR image pushed by deploy.sh
PortMappings:
  - ContainerPort: 8000  # Matches main_fastapi_ecs.py:154
```

**Logging (lines 325-329):**
```yaml
LogConfiguration:
  LogDriver: awslogs
  Options:
    awslogs-group: !Ref LogGroup  # /ecs/fastapi-ecs-demo
    awslogs-region: !Ref AWS::Region
```

### ECS Service (Lines 346-374)

**Service Configuration:**
```yaml
DesiredCount: !Ref DesiredCount  # Default: 2 tasks
LaunchType: FARGATE
NetworkConfiguration:
  AwsvpcConfiguration:
    AssignPublicIp: DISABLED  # Tasks in private subnets
    Subnets:
      - !Ref PrivateSubnet1
      - !Ref PrivateSubnet2
```

**Deployment Strategy (lines 369-371):**
```yaml
DeploymentConfiguration:
  MaximumPercent: 200          # Can run 2x tasks during deployment
  MinimumHealthyPercent: 100   # Always maintain full capacity
```
This enables rolling deployments with zero downtime.

## Deployment Process

### Using the Deployment Script

```bash
chmod +x deploy.sh
./deploy.sh
```

**Step-by-step output with source code correlation:**

**Step 1: Create ECR Repository**
```
Step 1: Checking ECR repository...
Creating ECR repository: fastapi-ecs-demo
```
Creates repository to store Docker images (deploy.sh:22-30).

**Step 2: Docker Authentication**
```
Step 2: Authenticating Docker to ECR...
Login Succeeded
```
Authenticates Docker to push images to ECR (deploy.sh:36-38).

**Step 3: Build Docker Image**
```
Step 3: Building Docker image...
[+] Building 45.2s (10/10) FINISHED
 => [1/5] FROM docker.io/library/python:3.11-slim
 => [2/5] WORKDIR /app
 => [3/5] COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
 => [4/5] COPY main_fastapi_ecs.py .
 => [5/5] RUN uv pip install --system fastapi>=0.115.0 uvicorn[standard]>=0.32.0
```
Builds image following Dockerfile instructions (deploy.sh:42-44).

**Step 4: Tag Image**
```
Step 4: Tagging image for ECR...
```
Tags image with ECR URI (deploy.sh:48-50).

**Step 5: Push to ECR**
```
Step 5: Pushing image to ECR...
The push refers to repository [123456789.dkr.ecr.us-east-1.amazonaws.com/fastapi-ecs-demo]
latest: digest: sha256:abc123... size: 1234
```
Pushes image to ECR (deploy.sh:54-56).

**Step 6: Deploy CloudFormation Stack**
```
Step 6: Deploying CloudFormation stack...
Creating new stack: fastapi-ecs-demo-stack
Waiting for stack creation to complete...
```
Creates all AWS resources defined in cloudformation.yaml (deploy.sh:60-86).

**CloudFormation creates resources in this order:**
1. VPC and networking (cloudformation.yaml:55-159)
2. Security groups (cloudformation.yaml:160-198)
3. Load balancer and target group (cloudformation.yaml:201-246)
4. ECS cluster (cloudformation.yaml:248-262)
5. IAM roles (cloudformation.yaml:264-297)
6. CloudWatch log group (cloudformation.yaml:299-304)
7. Task definition (cloudformation.yaml:306-344)
8. ECS service (cloudformation.yaml:346-374)

**Step 7: Retrieve Outputs**
```
Step 7: Retrieving stack outputs...

=========================================
Deployment Complete!
=========================================
Application URL: http://fastapi-ecs-demo-alb-123456789.us-east-1.elb.amazonaws.com
Health Check: http://fastapi-ecs-demo-alb-123456789.us-east-1.elb.amazonaws.com/health
API Docs: http://fastapi-ecs-demo-alb-123456789.us-east-1.elb.amazonaws.com/docs
=========================================
```
Displays ALB URL from CloudFormation outputs (deploy.sh:89-110).

## Testing Deployed Application

**Test health endpoint:**
```bash
curl http://[ALB-URL]/health
```

**Output:**
```json
{
  "status": "healthy",
  "timestamp": "2025-11-25T12:34:56.789012",
  "service": "fastapi-ecs-demo"
}
```
This response comes from the container running in ECS Fargate, routed through:
1. ALB (cloudformation.yaml:201-215)
2. Target Group (cloudformation.yaml:217-235)
3. ECS Service (cloudformation.yaml:346-374)
4. ECS Task (cloudformation.yaml:306-344)
5. FastAPI app (main_fastapi_ecs.py:62-75)

**Test items endpoint:**
```bash
curl http://[ALB-URL]/items
```

**Output:**
```json
[
  {"id": 1, "name": "Widget", "description": "A useful widget", "price": 19.99},
  {"id": 2, "name": "Gadget", "description": "An amazing gadget", "price": 29.99}
]
```

**Create new item:**
```bash
curl -X POST http://[ALB-URL]/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Doodad", "description": "A fantastic doodad", "price": 39.99}'
```

**Output:**
```json
{
  "id": 3,
  "name": "Doodad",
  "description": "A fantastic doodad",
  "price": 39.99
}
```
Created by the POST endpoint (main_fastapi_ecs.py:102-116).

## Monitoring and Logs

**View ECS task logs in CloudWatch:**
```bash
aws logs tail /ecs/fastapi-ecs-demo --follow
```

**Sample log output:**
```
2025-11-25 12:34:56 INFO:     Started server process [1]
2025-11-25 12:34:56 INFO:     Waiting for application startup.
2025-11-25 12:34:56 INFO:     Application startup complete.
2025-11-25 12:34:56 INFO:     Uvicorn running on http://0.0.0.0:8000
2025-11-25 12:35:01 INFO:     10.0.11.5:54321 - "GET /health HTTP/1.1" 200 OK
2025-11-25 12:35:15 INFO:     10.0.11.5:54322 - "GET /items HTTP/1.1" 200 OK
```

Log configuration is defined in cloudformation.yaml:325-329, logs sent to group created at lines 299-304.

## Resource Scaling

**Scale the service to 4 tasks:**
```bash
aws cloudformation update-stack \
  --stack-name fastapi-ecs-demo-stack \
  --template-body file://cloudformation.yaml \
  --parameters ParameterKey=ImageUri,UsePreviousValue=true \
               ParameterKey=DesiredCount,ParameterValue=4 \
  --capabilities CAPABILITY_NAMED_IAM
```

The ECS service (cloudformation.yaml:346-374) will automatically:
1. Launch 2 additional tasks
2. Register them with the target group
3. ALB distributes traffic across all 4 tasks

## Cost Considerations

**Fargate Pricing (as of 2025):**
- vCPU: ~$0.04048 per vCPU per hour
- Memory: ~$0.004445 per GB per hour

**For default configuration (0.25 vCPU, 0.5 GB, 2 tasks):**
- Per task: (0.25 × $0.04048) + (0.5 × $0.004445) = ~$0.012 per hour
- 2 tasks: ~$0.024 per hour = ~$17.28 per month

**Additional costs:**
- Application Load Balancer: ~$16-25 per month
- Data transfer: varies by usage
- CloudWatch Logs: minimal for low volume

## Cleanup

**Delete all resources:**
```bash
aws cloudformation delete-stack --stack-name fastapi-ecs-demo-stack
aws ecr delete-repository --repository-name fastapi-ecs-demo --force
```

## Key Features Demonstrated

✅ **Serverless Containers**: No EC2 instance management with Fargate
✅ **High Availability**: Multi-AZ deployment across 2 availability zones
✅ **Auto-healing**: Unhealthy tasks automatically replaced
✅ **Zero-downtime Deployments**: Rolling updates maintain 100% capacity
✅ **Load Balancing**: ALB distributes traffic across healthy tasks
✅ **Security**: Tasks in private subnets, non-root container user
✅ **Observability**: CloudWatch logs for monitoring
✅ **Infrastructure as Code**: Complete stack in CloudFormation YAML

## Version Requirements

- **Python**: 3.11 or higher (for modern type hints with `|` syntax)
- **FastAPI**: 0.115.0 or higher
- **Uvicorn**: 0.32.0 or higher (with standard extras for production)
- **Docker**: Any recent version supporting multi-stage builds
- **AWS CLI**: v2 recommended

## Architecture Benefits

1. **Scalability**: Easily scale from 1 to 100+ tasks
2. **Reliability**: AWS manages infrastructure, automatic health checks
3. **Security**: VPC isolation, security groups, IAM roles
4. **Cost-effective**: Pay only for running tasks (Fargate pricing)
5. **Developer-friendly**: Focus on code, not infrastructure management

## Next Steps

- Add HTTPS support with ACM certificate
- Implement auto-scaling based on CPU/memory/request count
- Add RDS database for persistent storage
- Configure custom domain with Route 53
- Implement CI/CD pipeline with GitHub Actions or AWS CodePipeline
- Add container insights for advanced monitoring
