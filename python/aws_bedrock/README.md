# AWS Bedrock Python Example

This example demonstrates how to use AWS Bedrock to interact with Claude foundation models. It covers basic text generation, streaming responses, conversation with system prompts, and image analysis.

## Requirements

- **Python Version**: Python 3.9 or higher
- **AWS Account**: Active AWS account with Bedrock access
- **AWS Credentials**: Configured via environment variables, AWS config file, or IAM role
- **AWS Region**: Bedrock must be available in your region (e.g., us-east-1, us-west-2)
- **Model Access**: You must have access to Claude models in AWS Bedrock (request access through AWS Console if needed)

## Installation

This project uses `uv` for dependency management:

```bash
# Install dependencies
uv sync

# Run the example
uv run python main_aws_bedrock.py
```

## AWS Configuration

Before running, ensure AWS credentials are configured:

```bash
# Option 1: Environment variables
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_REGION=us-east-1

# Option 2: AWS CLI configuration
aws configure
```

## Source Code Overview

### Creating the Bedrock Client

```python
21→def create_bedrock_client():
22→    """
23→    Create and return a Bedrock Runtime client.
24→
25→    Line 20-28: Initialize the boto3 client for Bedrock Runtime.
26→    The client requires AWS credentials to be configured via environment
27→    variables, AWS config file, or IAM role.
28→    """
29→    # Line 26: Create Bedrock Runtime client
30→    bedrock_runtime = boto3.client(
31→        service_name="bedrock-runtime",
32→        region_name=os.getenv("AWS_REGION", "us-east-1"),
33→    )
34→    return bedrock_runtime
```

**Lines 30-33**: Creates a boto3 client for the `bedrock-runtime` service. This client will be used to invoke foundation models.

### Example 1: Basic Text Generation

```python
47→    # Line 44-52: Prepare the request body with messages format
48→    model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"
49→
50→    request_body = {
51→        "anthropic_version": "bedrock-2023-05-31",
52→        "max_tokens": 1024,
53→        "messages": [
54→            {
55→                "role": "user",
56→                "content": "Explain quantum computing in 2-3 sentences.",
57→            }
58→        ],
59→    }
60→
61→    try:
62→        # Line 58-59: Invoke the model
63→        response = client.invoke_model(
64→            modelId=model_id,
65→            body=json.dumps(request_body),
66→        )
67→
68→        # Line 63-65: Parse and display the response
69→        response_body = json.loads(response["body"].read())
70→        assistant_message = response_body["content"][0]["text"]
```

**Line 48**: Specifies the Claude 3.5 Sonnet model ID for AWS Bedrock.

**Lines 50-59**: Constructs the request body with the messages format, which is the standard API format for Claude.

**Lines 63-66**: Calls `invoke_model()` to synchronously invoke Claude and get a response.

**Lines 69-70**: Parses the JSON response and extracts the assistant's text message.

### Example 2: Streaming Text Generation

```python
102→    try:
103→        # Line 98-101: Invoke model with streaming
104→        response = client.invoke_model_with_response_stream(
105→            modelId=model_id,
106→            body=json.dumps(request_body),
107→        )
108→
109→        print("\nUser: Write a haiku about artificial intelligence.")
110→        print("\nAssistant: ", end="", flush=True)
111→
112→        # Line 107-116: Process the streaming response
113→        stream = response.get("body")
114→        if stream:
115→            for event in stream:
116→                chunk = event.get("chunk")
117→                if chunk:
118→                    chunk_obj = json.loads(chunk.get("bytes").decode())
119→
120→                    if chunk_obj["type"] == "content_block_delta":
121→                        if chunk_obj["delta"]["type"] == "text_delta":
122→                            print(chunk_obj["delta"]["text"], end="", flush=True)
```

**Lines 104-107**: Uses `invoke_model_with_response_stream()` instead of `invoke_model()` to get streaming responses.

**Lines 115-122**: Iterates through the stream events, extracting text deltas and printing them in real-time for a streaming effect.

### Example 3: Conversation with System Prompt

```python
142→    # Line 138-156: Request body with system prompt and multi-turn conversation
143→    request_body = {
144→        "anthropic_version": "bedrock-2023-05-31",
145→        "max_tokens": 1024,
146→        "system": "You are a helpful Python programming tutor. Keep answers concise.",
147→        "messages": [
148→            {
149→                "role": "user",
150→                "content": "What's a list comprehension?",
151→            },
152→            {
153→                "role": "assistant",
154→                "content": (
155→                    "A list comprehension is a concise way to create "
156→                    "lists in Python."
157→                ),
158→            },
159→            {
160→                "role": "user",
161→                "content": "Give me a quick example.",
162→            },
163→        ],
164→    }
```

**Line 146**: Sets a system prompt to guide Claude's behavior and tone.

**Lines 147-163**: Shows a multi-turn conversation where the assistant's previous response is included in the messages array.

### Example 4: Image Analysis (Multimodal)

```python
194→    # Line 190-192: Create a simple red square image programmatically
195→    # For demo purposes, we'll use a base64-encoded 1x1 red pixel PNG
196→    red_pixel_png_base64 = (
197→        "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8DwHwAF"
198→        "BQIAx8JMKwAAAABJRU5ErkJggg=="
199→    )
200→
201→    # Line 197-212: Request body with image content
202→    request_body = {
203→        "anthropic_version": "bedrock-2023-05-31",
204→        "max_tokens": 1024,
205→        "messages": [
206→            {
207→                "role": "user",
208→                "content": [
209→                    {
210→                        "type": "image",
211→                        "source": {
212→                            "type": "base64",
213→                            "media_type": "image/png",
214→                            "data": red_pixel_png_base64,
215→                        },
216→                    },
217→                    {
218→                        "type": "text",
219→                        "text": "What color is this image?",
220→                    },
221→                ],
222→            }
223→        ],
224→    }
```

**Lines 196-199**: Contains a base64-encoded PNG image (a 1x1 red pixel for demonstration).

**Lines 208-221**: Shows the multimodal message format where content is an array containing both image and text elements.

**Lines 209-216**: Image content block with base64-encoded image data.

**Lines 217-220**: Text content block with the question about the image.

## Example Output

*Note: This is example output. Actual responses may vary. Running this code requires valid AWS credentials and Bedrock access.*

```
AWS Bedrock Python Examples
This demonstrates various ways to interact with Claude via Bedrock

================================================================================
EXAMPLE 1: Basic Text Generation
================================================================================

User: Explain quantum computing in 2-3 sentences.
Assistant: Quantum computing harnesses quantum mechanical phenomena like superposition and entanglement to process information. Unlike classical bits, quantum bits (qubits) can exist in multiple states simultaneously, allowing quantum computers to solve certain complex problems exponentially faster. This technology shows promise for cryptography, drug discovery, and optimization.

Output Line Annotations:
- Lines 210-217: Header and user prompt for Example 1
- Above text: Claude's response from line 70-71 in source code

================================================================================
EXAMPLE 2: Streaming Text Generation
================================================================================

User: Write a haiku about artificial intelligence.
Assistant: Silicon dreams awake,
Neural pathways come alive—
Mind meets machine's grace.

Output Line Annotations:
- Lines 225-228: Example 2 demonstrates streaming output (Lines 107-122 in source)
- The haiku appears character-by-character in real-time via streaming API

================================================================================
EXAMPLE 3: Conversation with System Prompt
================================================================================

System: You are a helpful Python programming tutor.

User: What's a list comprehension?
Assistant: A list comprehension is a concise way to create lists in Python.

User: Give me a quick example.
Assistant: Here's a simple example: `squares = [x**2 for x in range(10)]`
This creates a list of squares from 0 to 81. It's equivalent to writing a for
loop but more readable and often faster.

Output Line Annotations:
- Lines 231-241: Shows multi-turn conversation with system prompt
- System prompt (Line 146) guides Claude to be a concise Python tutor
- Previous assistant message included in conversation context (Lines 152-157)
- Final response demonstrates Claude following the system prompt directive

================================================================================
EXAMPLE 4: Image Analysis (Multimodal)
================================================================================

User: [Sends a 1x1 red pixel image] What color is this image?
Assistant: This image appears to be red. It's a very small image (appears to be just a single pixel), but the color is definitely red.

Output Line Annotations:
- Lines 244-247: Image analysis example using multimodal capabilities
- Image sent as base64-encoded PNG (Lines 196-199)
- Content array contains both image and text (Lines 208-221)
- Claude successfully identifies the color from the base64 image data

================================================================================
All examples completed!
================================================================================
```

## Key Concepts Demonstrated

### 1. Bedrock Client Setup (Lines 30-34)
The `boto3.client()` creates a connection to AWS Bedrock Runtime service. AWS credentials must be configured before running.

### 2. Message Format (Lines 50-59)
Claude on Bedrock uses the Messages API format with:
- `anthropic_version`: API version
- `max_tokens`: Maximum response length
- `messages`: Array of user/assistant messages

### 3. Streaming vs Non-Streaming (Lines 63-66 vs 104-107)
- `invoke_model()`: Returns complete response at once
- `invoke_model_with_response_stream()`: Returns response in chunks for real-time display

### 4. System Prompts (Line 146)
System prompts guide Claude's personality and behavior across the conversation.

### 5. Multimodal Input (Lines 208-221)
Images can be sent as base64-encoded data within the content array alongside text.

## Troubleshooting

### AWS Credentials Not Configured
```
Error: The config profile (default) could not be found
```
**Solution**: Run `aws configure` or set AWS environment variables

### Bedrock Access Denied
```
Error: AccessDeniedException: User is not authorized to perform: bedrock:InvokeModel
```
**Solution**: Request model access in AWS Console → Bedrock → Model access

### Model Not Available in Region
```
Error: ValidationException: The model ID is not supported in this region
```
**Solution**: Use a region where Claude models are available (us-east-1, us-west-2, etc.)

## Additional Resources

- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Anthropic Claude Documentation](https://docs.anthropic.com/)
- [Boto3 Bedrock Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html)
