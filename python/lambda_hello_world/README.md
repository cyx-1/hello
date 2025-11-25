# AWS Lambda Hello World with CloudFormation

This example demonstrates the simplest Python code to deploy an AWS Lambda function with an HTTP endpoint using CloudFormation YAML configuration.

## Overview

- **Lambda Handler**: Python function that responds to HTTP requests
- **API Gateway**: Provides HTTP endpoint to invoke the Lambda
- **CloudFormation**: Infrastructure as Code for automated deployment

## Source Code

### Lambda Handler (main_lambda_hello_world.py)

```python
     1  """
     2  AWS Lambda handler for Hello World HTTP endpoint.
     3
     4  This Lambda function is designed to work with API Gateway and responds
     5  to HTTP requests with a simple "Hello, World!" message.
     6  """
     7
     8  import json
     9
    10
    11  def lambda_handler(event, context):
    12      """
    13      Handle incoming HTTP requests via API Gateway.
    14
    15      Args:
    16          event: API Gateway event containing HTTP request details
    17          context: Lambda context object with runtime information
    18
    19      Returns:
    20          dict: API Gateway response format with statusCode, headers, and body
    21      """
    22      # Line 20: Extract HTTP method and path from the event
    23      http_method = event.get("httpMethod", "UNKNOWN")
    24      path = event.get("path", "/")
    25
    26      # Line 24: Create response message
    27      message = {
    28          "message": "Hello, World!",
    29          "method": http_method,
    30          "path": path,
    31          "timestamp": context.request_id if context else "local-test",
    32      }
    33
    34      # Line 32: Return API Gateway compatible response
    35      return {
    36          "statusCode": 200,
    37          "headers": {
    38              "Content-Type": "application/json",
    39              "Access-Control-Allow-Origin": "*",
    40          },
    41          "body": json.dumps(message),
    42      }
```

## Local Testing

Run the handler locally to verify it works:

```bash
uv run python main_lambda_hello_world.py
```

### Local Test Output

```
Lambda Response:
{
  "statusCode": 200,                                    # Line 36: HTTP 200 OK status
  "headers": {
    "Content-Type": "application/json",                 # Line 38: JSON response type
    "Access-Control-Allow-Origin": "*"                  # Line 39: CORS enabled
  },
  "body": "{\"message\": \"Hello, World!\", \"method\": \"GET\", \"path\": \"/hello\", \"timestamp\": \"test-request-123\"}"
}

Parsed Body:
{
  "message": "Hello, World!",                           # Line 28: Main greeting message
  "method": "GET",                                      # Line 23: HTTP method extracted from event
  "path": "/hello",                                     # Line 24: Request path
  "timestamp": "test-request-123"                       # Line 31: Request ID from context
}
```

### Code Annotations

- **Lines 23-24**: The handler extracts the HTTP method and path from the API Gateway event object
- **Lines 27-32**: A response message dictionary is constructed with greeting, method, path, and timestamp
- **Lines 35-42**: The response follows API Gateway's proxy integration format requiring `statusCode`, `headers`, and `body` fields
- **Line 41**: The body must be a JSON string, not a dictionary, so we use `json.dumps()`

## CloudFormation Template Structure

The `cloudformation.yaml` defines these AWS resources:

1. **LambdaExecutionRole** (Lines 6-19): IAM role allowing Lambda to write CloudWatch logs
2. **HelloWorldFunction** (Lines 22-56): Lambda function with inline Python code
3. **HelloWorldApi** (Lines 59-66): API Gateway REST API
4. **ApiResource & ApiMethod** (Lines 69-91): Proxy resource handling all HTTP methods and paths
5. **RootMethod** (Lines 94-104): Handles requests to the root path `/`
6. **ApiDeployment & ApiStage** (Lines 107-122): Deploys API to `prod` stage
7. **LambdaApiPermission** (Lines 125-132): Grants API Gateway permission to invoke Lambda

## Deployment Instructions

### Prerequisites

- AWS CLI configured with credentials (`aws configure`)
- Sufficient IAM permissions to create Lambda, API Gateway, and IAM resources

### Deploy the Stack

```bash
# Create the CloudFormation stack
aws cloudformation create-stack \
  --stack-name hello-world-lambda \
  --template-body file://cloudformation.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --region us-east-1

# Wait for stack creation to complete
aws cloudformation wait stack-create-complete \
  --stack-name hello-world-lambda \
  --region us-east-1

# Get the API endpoint URL
aws cloudformation describe-stacks \
  --stack-name hello-world-lambda \
  --region us-east-1 \
  --query 'Stacks[0].Outputs[?OutputKey==`ApiEndpoint`].OutputValue' \
  --output text
```

### Test the Deployed Endpoint

```bash
# Replace with your actual API endpoint from the output above
curl https://YOUR_API_ID.execute-api.us-east-1.amazonaws.com/prod/

# Or test a specific path
curl https://YOUR_API_ID.execute-api.us-east-1.amazonaws.com/prod/hello
```

### Expected HTTP Response

```json
{
  "message": "Hello, World!",
  "method": "GET",
  "path": "/",
  "timestamp": "actual-request-id-from-aws"
}
```

## Update Existing Stack

If you modify the Lambda code, update the stack:

```bash
aws cloudformation update-stack \
  --stack-name hello-world-lambda \
  --template-body file://cloudformation.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --region us-east-1
```

## Delete the Stack

Clean up all resources:

```bash
aws cloudformation delete-stack \
  --stack-name hello-world-lambda \
  --region us-east-1
```

## Technical Requirements

- **Python Version**: Python 3.12 (as specified in cloudformation.yaml Line 27)
- **AWS Lambda Runtime**: python3.12
- **Dependencies**: None (uses only Python standard library)

## Key Features

1. **Zero Dependencies**: Uses only Python standard library (`json`)
2. **API Gateway Proxy Integration**: Simplifies request/response handling
3. **CORS Enabled**: Allows cross-origin requests from any domain
4. **Infrastructure as Code**: Complete deployment defined in YAML
5. **Inline Code**: Lambda code embedded in CloudFormation for simplicity

## Architecture

```
HTTP Request → API Gateway → Lambda Function → JSON Response
                   ↓
         (CloudFormation manages all resources)
```

The API Gateway acts as the HTTP endpoint, receiving requests and forwarding them to the Lambda function. The Lambda processes the request and returns a JSON response, which API Gateway sends back to the client.

## Notes

- The CloudFormation template includes inline Lambda code for simplicity
- For production use, consider uploading code as a ZIP file to S3
- The `ANY` method on the API Gateway resource accepts all HTTP methods (GET, POST, PUT, DELETE, etc.)
- The `{proxy+}` path captures all sub-paths under the API
