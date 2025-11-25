"""
AWS Lambda handler for Hello World HTTP endpoint.

This Lambda function is designed to work with API Gateway and responds
to HTTP requests with a simple "Hello, World!" message.
"""

import json


def lambda_handler(event, context):
    """
    Handle incoming HTTP requests via API Gateway.

    Args:
        event: API Gateway event containing HTTP request details
        context: Lambda context object with runtime information

    Returns:
        dict: API Gateway response format with statusCode, headers, and body
    """
    # Line 20: Extract HTTP method and path from the event
    http_method = event.get("httpMethod", "UNKNOWN")
    path = event.get("path", "/")

    # Line 24: Create response message
    message = {
        "message": "Hello, World!",
        "method": http_method,
        "path": path,
        "timestamp": context.request_id if context else "local-test",
    }

    # Line 32: Return API Gateway compatible response
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(message),
    }


if __name__ == "__main__":
    # Line 45: Test the handler locally
    test_event = {
        "httpMethod": "GET",
        "path": "/hello",
        "headers": {},
        "body": None,
    }

    class MockContext:
        """Mock Lambda context for local testing."""

        request_id = "test-request-123"

    # Line 58: Invoke handler and print response
    response = lambda_handler(test_event, MockContext())
    print("Lambda Response:")
    print(json.dumps(response, indent=2))
    print("\nParsed Body:")
    print(json.dumps(json.loads(response["body"]), indent=2))
