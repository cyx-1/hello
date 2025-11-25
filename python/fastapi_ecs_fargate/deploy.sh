#!/bin/bash
# Deployment script for FastAPI ECS/Fargate application

set -e  # Exit on error

# Configuration
AWS_REGION="us-east-1"
AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
ECR_REPOSITORY_NAME="fastapi-ecs-demo"
IMAGE_TAG="${1:-latest}"
STACK_NAME="fastapi-ecs-demo-stack"

echo "========================================="
echo "FastAPI ECS/Fargate Deployment Script"
echo "========================================="
echo "Region: $AWS_REGION"
echo "Account: $AWS_ACCOUNT_ID"
echo "Image Tag: $IMAGE_TAG"
echo "========================================="

# Step 1: Create ECR repository if it doesn't exist
echo ""
echo "Step 1: Checking ECR repository..."
if ! aws ecr describe-repositories --repository-names "$ECR_REPOSITORY_NAME" --region "$AWS_REGION" &> /dev/null; then
    echo "Creating ECR repository: $ECR_REPOSITORY_NAME"
    aws ecr create-repository \
        --repository-name "$ECR_REPOSITORY_NAME" \
        --region "$AWS_REGION" \
        --image-scanning-configuration scanOnPush=true
else
    echo "ECR repository already exists: $ECR_REPOSITORY_NAME"
fi

ECR_URI="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPOSITORY_NAME}"
IMAGE_URI="${ECR_URI}:${IMAGE_TAG}"

# Step 2: Authenticate Docker to ECR
echo ""
echo "Step 2: Authenticating Docker to ECR..."
aws ecr get-login-password --region "$AWS_REGION" | \
    docker login --username AWS --password-stdin "$ECR_URI"

# Step 3: Build Docker image
echo ""
echo "Step 3: Building Docker image..."
docker build -t "$ECR_REPOSITORY_NAME:$IMAGE_TAG" .

# Step 4: Tag image for ECR
echo ""
echo "Step 4: Tagging image for ECR..."
docker tag "$ECR_REPOSITORY_NAME:$IMAGE_TAG" "$IMAGE_URI"

# Step 5: Push image to ECR
echo ""
echo "Step 5: Pushing image to ECR..."
docker push "$IMAGE_URI"

# Step 6: Deploy CloudFormation stack
echo ""
echo "Step 6: Deploying CloudFormation stack..."
if aws cloudformation describe-stacks --stack-name "$STACK_NAME" --region "$AWS_REGION" &> /dev/null; then
    echo "Updating existing stack: $STACK_NAME"
    aws cloudformation update-stack \
        --stack-name "$STACK_NAME" \
        --template-body file://cloudformation.yaml \
        --parameters ParameterKey=ImageUri,ParameterValue="$IMAGE_URI" \
        --capabilities CAPABILITY_NAMED_IAM \
        --region "$AWS_REGION"

    echo "Waiting for stack update to complete..."
    aws cloudformation wait stack-update-complete \
        --stack-name "$STACK_NAME" \
        --region "$AWS_REGION"
else
    echo "Creating new stack: $STACK_NAME"
    aws cloudformation create-stack \
        --stack-name "$STACK_NAME" \
        --template-body file://cloudformation.yaml \
        --parameters ParameterKey=ImageUri,ParameterValue="$IMAGE_URI" \
        --capabilities CAPABILITY_NAMED_IAM \
        --region "$AWS_REGION"

    echo "Waiting for stack creation to complete..."
    aws cloudformation wait stack-create-complete \
        --stack-name "$STACK_NAME" \
        --region "$AWS_REGION"
fi

# Step 7: Get outputs
echo ""
echo "Step 7: Retrieving stack outputs..."
LOAD_BALANCER_URL=$(aws cloudformation describe-stacks \
    --stack-name "$STACK_NAME" \
    --region "$AWS_REGION" \
    --query 'Stacks[0].Outputs[?OutputKey==`LoadBalancerURL`].OutputValue' \
    --output text)

echo ""
echo "========================================="
echo "Deployment Complete!"
echo "========================================="
echo "Application URL: $LOAD_BALANCER_URL"
echo "Health Check: $LOAD_BALANCER_URL/health"
echo "API Docs: $LOAD_BALANCER_URL/docs"
echo "========================================="
