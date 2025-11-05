# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "boto3>=1.34.0",
# ]
# ///
"""
AWS Bedrock Python Example

This example demonstrates how to use AWS Bedrock to interact with
foundation models like Claude. It covers:
1. Basic text generation
2. Streaming responses
3. Conversation with system prompts
4. Image analysis (multimodal)
"""

import json
import os

import boto3
from botocore.exceptions import ClientError


def create_bedrock_client():
    """
    Create and return a Bedrock Runtime client.

    Line 20-28: Initialize the boto3 client for Bedrock Runtime.
    The client requires AWS credentials to be configured via environment
    variables, AWS config file, or IAM role.
    """
    # Line 26: Create Bedrock Runtime client
    bedrock_runtime = boto3.client(
        service_name="bedrock-runtime",
        region_name=os.getenv("AWS_REGION", "us-east-1"),
    )
    return bedrock_runtime


def basic_text_generation(client):
    """
    Demonstrate basic text generation with Claude on Bedrock.

    Line 36-63: Shows how to make a simple inference request.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 1: Basic Text Generation")
    print("=" * 80)

    # Line 44-52: Prepare the request body with messages format
    model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"

    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": "Explain quantum computing in 2-3 sentences.",
            }
        ],
    }

    try:
        # Line 58-59: Invoke the model
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body),
        )

        # Line 63-65: Parse and display the response
        response_body = json.loads(response["body"].read())
        assistant_message = response_body["content"][0]["text"]

        print("\nUser: Explain quantum computing in 2-3 sentences.")
        print(f"\nAssistant: {assistant_message}")

    except ClientError as e:
        print(f"Error: {e}")


def streaming_text_generation(client):
    """
    Demonstrate streaming responses from Claude on Bedrock.

    Line 78-110: Shows how to get streaming responses for real-time output.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 2: Streaming Text Generation")
    print("=" * 80)

    model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"

    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": "Write a haiku about artificial intelligence.",
            }
        ],
    }

    try:
        # Line 98-101: Invoke model with streaming
        response = client.invoke_model_with_response_stream(
            modelId=model_id,
            body=json.dumps(request_body),
        )

        print("\nUser: Write a haiku about artificial intelligence.")
        print("\nAssistant: ", end="", flush=True)

        # Line 107-116: Process the streaming response
        stream = response.get("body")
        if stream:
            for event in stream:
                chunk = event.get("chunk")
                if chunk:
                    chunk_obj = json.loads(chunk.get("bytes").decode())

                    if chunk_obj["type"] == "content_block_delta":
                        if chunk_obj["delta"]["type"] == "text_delta":
                            print(chunk_obj["delta"]["text"], end="", flush=True)

        print("\n")

    except ClientError as e:
        print(f"Error: {e}")


def conversation_with_system_prompt(client):
    """
    Demonstrate conversation with system prompts.

    Line 128-165: Shows how to use system prompts to guide model behavior.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 3: Conversation with System Prompt")
    print("=" * 80)

    model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"

    # Line 138-156: Request body with system prompt and multi-turn conversation
    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "system": "You are a helpful Python programming tutor. Keep answers concise.",
        "messages": [
            {
                "role": "user",
                "content": "What's a list comprehension?",
            },
            {
                "role": "assistant",
                "content": (
                    "A list comprehension is a concise way to create lists in Python."
                ),
            },
            {
                "role": "user",
                "content": "Give me a quick example.",
            },
        ],
    }

    try:
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body),
        )

        response_body = json.loads(response["body"].read())
        assistant_message = response_body["content"][0]["text"]

        print("\nSystem: You are a helpful Python programming tutor.")
        print("\nUser: What's a list comprehension?")
        print(
            "Assistant: A list comprehension is a concise way to create "
            "lists in Python."
        )
        print("\nUser: Give me a quick example.")
        print(f"Assistant: {assistant_message}")

    except ClientError as e:
        print(f"Error: {e}")


def image_analysis(client):
    """
    Demonstrate image analysis using Claude's vision capabilities.

    Line 180-230: Shows how to send images to Claude for analysis.
    """
    print("\n" + "=" * 80)
    print("EXAMPLE 4: Image Analysis (Multimodal)")
    print("=" * 80)

    model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"

    # Line 190-192: Create a simple red square image programmatically
    # For demo purposes, we'll use a base64-encoded 1x1 red pixel PNG
    red_pixel_png_base64 = (
        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8DwHwAF"
        "BQIAx8JMKwAAAABJRU5ErkJggg=="
    )

    # Line 197-212: Request body with image content
    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/png",
                            "data": red_pixel_png_base64,
                        },
                    },
                    {
                        "type": "text",
                        "text": "What color is this image?",
                    },
                ],
            }
        ],
    }

    try:
        response = client.invoke_model(
            modelId=model_id,
            body=json.dumps(request_body),
        )

        response_body = json.loads(response["body"].read())
        assistant_message = response_body["content"][0]["text"]

        print("\nUser: [Sends a 1x1 red pixel image] What color is this image?")
        print(f"Assistant: {assistant_message}")

    except ClientError as e:
        print(f"Error: {e}")


def main():
    """
    Main function to run all AWS Bedrock examples.

    Line 242-254: Orchestrates all example demonstrations.
    """
    print("AWS Bedrock Python Examples")
    print("This demonstrates various ways to interact with Claude via Bedrock\n")

    # Create Bedrock client
    client = create_bedrock_client()

    # Run examples
    basic_text_generation(client)
    streaming_text_generation(client)
    conversation_with_system_prompt(client)
    image_analysis(client)

    print("\n" + "=" * 80)
    print("All examples completed!")
    print("=" * 80)


if __name__ == "__main__":
    main()
