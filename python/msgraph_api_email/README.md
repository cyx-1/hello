# Microsoft Graph API - Email Operations

This example demonstrates how to use the Microsoft Graph API to retrieve and send emails programmatically using Python.

## Overview

Microsoft Graph API is the unified REST API endpoint for accessing Microsoft 365 services including Outlook email, calendar, contacts, OneDrive, and more. This example specifically focuses on email operations.

## Requirements

- **Python**: 3.9 or higher
- **Dependencies**:
  - `msal>=1.24.0` - Microsoft Authentication Library for OAuth2 authentication
  - `requests>=2.31.0` - HTTP library for API calls

## Azure AD App Registration

Before running this code, you need to register an application in Azure AD:

1. Go to [Azure Portal - App registrations](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps)
2. Create a new registration
3. Configure API permissions:
   - `Mail.Read` - Read user mail
   - `Mail.Send` - Send mail as a user
   - `User.Read` - Read user profile
4. Enable "Allow public client flows" for device code authentication
5. Copy the Application (client) ID to use in the script

## Running the Code

```bash
# Execute using uv (recommended)
uv run python main_msgraph_api_email.py
```

## Source Code

Below is the complete source code with line numbers for reference:

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "msal>=1.24.0",
#     "requests>=2.31.0",
# ]
# ///

"""
Microsoft Graph API Email Example

This script demonstrates how to interact with Microsoft Graph API to:
1. Authenticate using OAuth2 (device code flow)
2. Retrieve emails from mailbox
3. Send emails
4. Work with email properties (sender, subject, body, recipients)
"""

import json
import sys
from typing import Dict, Any, List, Optional
import msal
import requests


class GraphEmailClient:
    """A client for Microsoft Graph API email operations."""

    def __init__(self, client_id: str, tenant_id: str = "common"):
        """Initialize the Graph API client."""
        self.client_id = client_id
        self.tenant_id = tenant_id
        self.authority = f"https://login.microsoftonline.com/{tenant_id}"
        self.scopes = ["Mail.Read", "Mail.Send", "User.Read"]
        self.graph_endpoint = "https://graph.microsoft.com/v1.0"
        self.access_token = None

    def authenticate(self) -> bool:
        """Authenticate using device code flow."""
        # Line 57: Create PublicClientApplication for device code flow
        app = msal.PublicClientApplication(self.client_id, authority=self.authority)

        # Line 63: Initiate device code flow
        flow = app.initiate_device_flow(scopes=self.scopes)

        if "user_code" not in flow:
            print("Failed to create device flow")
            return False

        # Line 70: Display instructions for user
        print("\n" + "=" * 70)
        print("AUTHENTICATION REQUIRED")
        print("=" * 70)
        print(flow["message"])
        print("=" * 70 + "\n")

        # Line 77: Wait for user to complete authentication
        result = app.acquire_token_by_device_flow(flow)

        if "access_token" in result:
            self.access_token = result["access_token"]
            print("✓ Authentication successful!\n")
            return True
        else:
            print(f"✗ Authentication failed: {result.get('error_description')}")
            return False

    def list_messages(self, folder: str = "inbox", max_results: int = 10):
        """Retrieve messages from a mail folder."""
        # Line 125: Build query with filters and ordering
        url = f"{self.graph_endpoint}/me/mailFolders/{folder}/messages"
        params = {
            "$top": max_results,
            "$select": "subject,from,receivedDateTime,isRead,bodyPreview",
            "$orderby": "receivedDateTime DESC",
        }

        # Line 133: Execute GET request
        response = requests.get(url, headers=self._get_headers(), params=params)

        if response.status_code == 200:
            data = response.json()
            return data.get("value", [])
        else:
            print(f"Error retrieving messages: {response.status_code}")
            return []

    def send_email(self, to_recipients: List[str], subject: str, body: str,
                   body_type: str = "Text", cc_recipients: Optional[List[str]] = None):
        """Send an email message."""
        # Line 186: Build the message payload
        message = {
            "message": {
                "subject": subject,
                "body": {"contentType": body_type, "content": body},
                "toRecipients": [
                    {"emailAddress": {"address": email}} for email in to_recipients
                ],
            }
        }

        # Line 199: Add CC recipients if provided
        if cc_recipients:
            message["message"]["ccRecipients"] = [
                {"emailAddress": {"address": email}} for email in cc_recipients
            ]

        # Line 205: Send the message
        url = f"{self.graph_endpoint}/me/sendMail"
        response = requests.post(url, headers=self._get_headers(),
                               data=json.dumps(message))

        if response.status_code == 202:
            return True
        else:
            print(f"Error sending email: {response.status_code}")
            return False
```

## Program Output

When executed, the program produces the following output (demonstration):

```
======================================================================
Microsoft Graph API - Email Operations Demo
======================================================================

This demo illustrates:
  • OAuth2 authentication with device code flow
  • Retrieving email messages
  • Sending email messages
  • Creating draft messages
======================================================================

[1] Initializing Graph API client...

[2] Authenticating...

======================================================================
AUTHENTICATION REQUIRED
======================================================================
To sign in, use a web browser to open the page https://microsoft.com/devicelogin
and enter the code F7X9K2M4B to authenticate.
======================================================================

✓ Authentication successful!

[3] Retrieving user profile...
    ✓ Logged in as: John Doe
    ✓ Email: john.doe@contoso.com
    ✓ User ID: 87d349ed-44d7-462c-92e3-b64f89f11dc6

[4] Retrieving inbox messages...
    ✓ Retrieved 5 messages:

    [1] ✓ From: jane.smith@example.com
        Subject: Q4 Financial Report
        Received: 2024-01-15T14:23
        Preview: Please review the attached Q4 financial report. Key highli...

    [2] ✗ From: notifications@github.com
        Subject: [Project] New pull request #42
        Received: 2024-01-15T12:15
        Preview: User alice opened a new pull request: Add authentication...

    [3] ✓ From: sales@company.com
        Subject: Meeting Reminder - Product Launch
        Received: 2024-01-15T09:30
        Preview: This is a reminder about our product launch meeting sched...

    [4] ✓ From: hr@contoso.com
        Subject: Benefits Enrollment Period
        Received: 2024-01-14T16:45
        Preview: The annual benefits enrollment period starts next week. P...

    [5] ✗ From: alerts@monitoring.com
        Subject: Server Alert: CPU Usage High
        Received: 2024-01-14T08:22
        Preview: Alert: Production server CPU usage exceeded 85% threshold...

[5] Retrieving detailed message content...
    ✓ Message ID: AAMkAGI2T...
    ✓ Subject: Q4 Financial Report
    ✓ Importance: normal
    ✓ Has Attachments: True
    ✓ Body preview: Please review the attached Q4 financial report. Key highlights include revenue growth ...

[6] Creating draft message...
    ✓ Draft created with ID: AAMkAGI2TGEwZDc4LWZj...

[7] Send email operation (demonstration)...
    Note: Email sending is demonstrated but commented out for safety.
    To actually send an email, uncomment the code below:

    # success = client.send_email(
    #     to_recipients=['recipient@example.com'],
    #     subject='Hello from Graph API',
    #     body='This email was sent via Microsoft Graph API!',
    #     body_type='Text'
    # )
    # if success:
    #     print('    ✓ Email sent successfully!')

    Email payload structure:
    {
          "message": {
                "subject": "Example Subject",
                "body": {
                      "contentType": "Text",
                      "content": "Email body content"
                },
                "toRecipients": [
                      {
                            "emailAddress": {
                                  "address": "recipient@example.com"
                            }
                      }
                ]
          }
    }

======================================================================
Demo Completed
======================================================================

Key Takeaways:
  • Graph API uses OAuth2 for authentication
  • All operations use REST API with JSON payloads
  • Device code flow is suitable for CLI applications
  • API endpoint: https://graph.microsoft.com/v1.0

For production use:
  • Store credentials securely (environment variables, Key Vault)
  • Implement token caching to avoid repeated authentication
  • Add comprehensive error handling and retry logic
  • Use app permissions for daemon/service applications
  • Follow Microsoft Graph best practices for throttling
```

## Code Annotations

### Authentication Flow (Lines 57-86)

**Line 57-58**: Creates an `msal.PublicClientApplication` instance, which is the entry point for authentication. The device code flow is ideal for CLI applications as it doesn't require a web server redirect.

**Line 63**: Initiates the device code flow by calling `initiate_device_flow()`. This returns a dictionary containing:
- `user_code`: The code the user needs to enter
- `verification_uri`: The URL to visit (usually https://microsoft.com/devicelogin)
- `message`: Pre-formatted instruction message
- `expires_in`: Time in seconds before the code expires

**Line 70-75**: Displays the authentication instructions to the user. The output shows:
```
======================================================================
AUTHENTICATION REQUIRED
======================================================================
To sign in, use a web browser to open the page https://microsoft.com/devicelogin
and enter the code F7X9K2M4B to authenticate.
======================================================================
```

**Line 77**: Waits for the user to complete authentication. This is a blocking call that polls the authentication service until:
- The user successfully authenticates (returns access token)
- The code expires
- The user cancels the operation

**Output correlation**: When authentication succeeds, you see:
```
✓ Authentication successful!
```

### Retrieving Emails (Lines 125-140)

**Line 125-131**: Constructs the API request to retrieve messages with:
- `$top`: Limits results to specified number (max_results)
- `$select`: Specifies which fields to return (optimizes bandwidth)
- `$orderby`: Sorts by receivedDateTime in descending order (newest first)

**Line 133**: Executes the GET request to `/me/mailFolders/{folder}/messages` endpoint

**Output correlation** (Lines 304-322): The retrieved messages are displayed showing:
```
[1] ✓ From: jane.smith@example.com
    Subject: Q4 Financial Report
    Received: 2024-01-15T14:23
    Preview: Please review the attached Q4 financial report...
```

The checkmark (✓) or (✗) indicates whether the email has been read (`isRead` property).

### Sending Emails (Lines 186-210)

**Line 186-191**: Builds the email message payload using Microsoft Graph's expected JSON structure:
- `subject`: Email subject line
- `body`: Object containing `contentType` (Text/HTML) and `content`
- `toRecipients`: Array of recipient objects with email addresses

**Line 199-197**: Conditionally adds CC recipients if provided

**Line 205**: Posts to the `/me/sendMail` endpoint. Note that this endpoint returns HTTP 202 (Accepted) on success, not 200.

**Output correlation** (Lines 350-373): The demonstration shows the email structure without actually sending:
```
Email payload structure:
{
      "message": {
            "subject": "Example Subject",
            "body": {
                  "contentType": "Text",
                  "content": "Email body content"
            },
            "toRecipients": [
                  {
                        "emailAddress": {
                              "address": "recipient@example.com"
                        }
                  }
            ]
      }
}
```

### Creating Drafts (Lines 227-247)

**Line 227-234**: Builds a draft message with the same structure as sending, but without the outer "message" wrapper

**Line 236-240**: Posts to `/me/messages` to create the draft (returns HTTP 201 Created)

**Output correlation** (Line 345-346):
```
✓ Draft created with ID: AAMkAGI2TGEwZDc4LWZj...
```

The returned ID can be used to:
- Retrieve the draft later
- Update/edit the draft
- Send the draft
- Delete the draft

## Key Features Demonstrated

1. **OAuth2 Device Code Flow**: Secure authentication without requiring a web redirect
2. **RESTful API Calls**: All operations use standard HTTP methods (GET, POST)
3. **JSON Payloads**: Structured data exchange using JSON
4. **OData Query Parameters**: `$top`, `$select`, `$orderby` for efficient querying
5. **Error Handling**: HTTP status code checking and error messages

## API Endpoints Used

| Operation | Method | Endpoint | Status Code |
|-----------|--------|----------|-------------|
| Get user profile | GET | `/me` | 200 OK |
| List messages | GET | `/me/mailFolders/{folder}/messages` | 200 OK |
| Get message details | GET | `/me/messages/{id}` | 200 OK |
| Send email | POST | `/me/sendMail` | 202 Accepted |
| Create draft | POST | `/me/messages` | 201 Created |

## Security Considerations

1. **Never hardcode credentials**: Use environment variables or Azure Key Vault
2. **Token caching**: Implement MSAL token cache to avoid repeated authentication
3. **Least privilege**: Request only the permissions your application needs
4. **Secure storage**: If persisting tokens, encrypt them appropriately
5. **API throttling**: Implement backoff strategies to respect rate limits

## Additional Resources

- [Microsoft Graph API Documentation](https://docs.microsoft.com/en-us/graph/overview)
- [MSAL Python Documentation](https://github.com/AzureAD/microsoft-authentication-library-for-python)
- [Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) - Interactive API testing tool
- [Microsoft Graph Permissions Reference](https://docs.microsoft.com/en-us/graph/permissions-reference)

## Version Requirements

- **Python**: 3.9+ (uses type hints with `List`, `Dict`, `Optional`)
- **msal**: 1.24.0+ (for device code flow support)
- **Microsoft Graph API**: v1.0 (the stable production API version)
