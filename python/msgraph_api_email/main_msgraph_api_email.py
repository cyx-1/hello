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

Microsoft Graph API is the unified API endpoint for accessing Microsoft 365 services
including Outlook email, calendar, contacts, and more.
"""

import json
import sys
from typing import Dict, Any, List, Optional
import msal
import requests


class GraphEmailClient:
    """A client for Microsoft Graph API email operations."""

    def __init__(self, client_id: str, tenant_id: str = "common"):
        """
        Initialize the Graph API client.

        Args:
            client_id: Azure AD application (client) ID
            tenant_id: Azure AD tenant ID (default: "common" for multi-tenant)
        """
        self.client_id = client_id
        self.tenant_id = tenant_id
        self.authority = f"https://login.microsoftonline.com/{tenant_id}"
        self.scopes = ["Mail.Read", "Mail.Send", "User.Read"]
        self.graph_endpoint = "https://graph.microsoft.com/v1.0"
        self.access_token = None

    def authenticate(self) -> bool:
        """
        Authenticate using device code flow.

        This is interactive - user will need to visit a URL and enter a code.

        Returns:
            True if authentication successful, False otherwise
        """
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

    def _get_headers(self) -> Dict[str, str]:
        """Get HTTP headers with authorization token."""
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def get_user_profile(self) -> Optional[Dict[str, Any]]:
        """
        Get the authenticated user's profile information.

        Returns:
            User profile data or None if request fails
        """
        # Line 104: Call /me endpoint to get user profile
        url = f"{self.graph_endpoint}/me"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting user profile: {response.status_code}")
            return None

    def list_messages(
        self, folder: str = "inbox", max_results: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Retrieve messages from a mail folder.

        Args:
            folder: Folder name (inbox, sentitems, drafts, etc.)
            max_results: Maximum number of messages to retrieve

        Returns:
            List of message objects
        """
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

    def get_message_details(self, message_id: str) -> Optional[Dict[str, Any]]:
        """
        Get detailed information about a specific message.

        Args:
            message_id: The message ID

        Returns:
            Message details or None if request fails
        """
        # Line 154: Retrieve full message details
        url = f"{self.graph_endpoint}/me/messages/{message_id}"
        response = requests.get(url, headers=self._get_headers())

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error getting message details: {response.status_code}")
            return None

    def send_email(
        self,
        to_recipients: List[str],
        subject: str,
        body: str,
        body_type: str = "Text",
        cc_recipients: Optional[List[str]] = None,
    ) -> bool:
        """
        Send an email message.

        Args:
            to_recipients: List of recipient email addresses
            subject: Email subject
            body: Email body content
            body_type: "Text" or "HTML"
            cc_recipients: Optional list of CC recipients

        Returns:
            True if sent successfully, False otherwise
        """
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
        response = requests.post(
            url, headers=self._get_headers(), data=json.dumps(message)
        )

        if response.status_code == 202:
            return True
        else:
            print(f"Error sending email: {response.status_code}")
            print(response.text)
            return False

    def create_draft(
        self, to_recipients: List[str], subject: str, body: str, body_type: str = "Text"
    ) -> Optional[str]:
        """
        Create a draft email message.

        Args:
            to_recipients: List of recipient email addresses
            subject: Email subject
            body: Email body content
            body_type: "Text" or "HTML"

        Returns:
            Draft message ID if successful, None otherwise
        """
        # Line 240: Build draft message
        draft = {
            "subject": subject,
            "body": {"contentType": body_type, "content": body},
            "toRecipients": [
                {"emailAddress": {"address": email}} for email in to_recipients
            ],
        }

        # Line 251: Create the draft
        url = f"{self.graph_endpoint}/me/messages"
        response = requests.post(
            url, headers=self._get_headers(), data=json.dumps(draft)
        )

        if response.status_code == 201:
            draft_data = response.json()
            return draft_data.get("id")
        else:
            print(f"Error creating draft: {response.status_code}")
            return None


def demonstrate_graph_api():
    """Demonstrate Microsoft Graph API email operations."""

    # Configuration
    # Register your app at https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps
    # Grant permissions: Mail.Read, Mail.Send, User.Read
    CLIENT_ID = "your-client-id-here"
    TENANT_ID = "common"  # Use "common" for multi-tenant or your specific tenant ID

    print("=" * 70)
    print("Microsoft Graph API - Email Operations Demo")
    print("=" * 70)
    print("\nThis demo illustrates:")
    print("  • OAuth2 authentication with device code flow")
    print("  • Retrieving email messages")
    print("  • Sending email messages")
    print("  • Creating draft messages")
    print("=" * 70)

    # Line 288: Initialize the Graph API client
    print("\n[1] Initializing Graph API client...")
    client = GraphEmailClient(CLIENT_ID, TENANT_ID)

    # Line 292: Authenticate
    print("\n[2] Authenticating...")
    if not client.authenticate():
        print("Authentication failed. Exiting.")
        sys.exit(1)

    # Line 298: Get user profile
    print("\n[3] Retrieving user profile...")
    user = client.get_user_profile()
    if user:
        print(f"    ✓ Logged in as: {user.get('displayName')}")
        print(f"    ✓ Email: {user.get('userPrincipalName')}")
        print(f"    ✓ User ID: {user.get('id')}")
    else:
        print("    ✗ Failed to retrieve user profile")

    # Line 308: List inbox messages
    print("\n[4] Retrieving inbox messages...")
    messages = client.list_messages(folder="inbox", max_results=5)
    if messages:
        print(f"    ✓ Retrieved {len(messages)} messages:\n")
        for idx, msg in enumerate(messages, 1):
            sender = (
                msg.get("from", {}).get("emailAddress", {}).get("address", "Unknown")
            )
            subject = msg.get("subject", "(No subject)")
            received = msg.get("receivedDateTime", "")
            is_read = "✓" if msg.get("isRead") else "✗"
            print(f"    [{idx}] {is_read} From: {sender}")
            print(f"        Subject: {subject}")
            print(f"        Received: {received[:19]}")
            preview = msg.get("bodyPreview", "")[:60]
            print(f"        Preview: {preview}...")
            print()
    else:
        print("    ✗ No messages retrieved")

    # Line 327: Get details of first message
    if messages:
        print("\n[5] Retrieving detailed message content...")
        message_id = messages[0].get("id")
        details = client.get_message_details(message_id)
        if details:
            print(f"    ✓ Message ID: {details.get('id')}")
            print(f"    ✓ Subject: {details.get('subject')}")
            print(f"    ✓ Importance: {details.get('importance')}")
            print(f"    ✓ Has Attachments: {details.get('hasAttachments')}")
            body_preview = details.get("body", {}).get("content", "")[:100]
            print(f"    ✓ Body preview: {body_preview}...")
        else:
            print("    ✗ Failed to retrieve message details")

    # Line 343: Create a draft message
    print("\n[6] Creating draft message...")
    draft_id = client.create_draft(
        to_recipients=["example@example.com"],
        subject="Test Email from Graph API",
        body="This is a test email created using Microsoft Graph API.",
        body_type="Text",
    )
    if draft_id:
        print(f"    ✓ Draft created with ID: {draft_id}")
    else:
        print("    ✗ Failed to create draft")

    # Line 356: Send an email (commented out by default for safety)
    print("\n[7] Send email operation (demonstration)...")
    print("    Note: Email sending is demonstrated but commented out for safety.")
    print("    To actually send an email, uncomment the code below:")
    print("    ")
    print("    # success = client.send_email(")
    print("    #     to_recipients=['recipient@example.com'],")
    print("    #     subject='Hello from Graph API',")
    print("    #     body='This email was sent via Microsoft Graph API!',")
    print("    #     body_type='Text'")
    print("    # )")
    print("    # if success:")
    print("    #     print('    ✓ Email sent successfully!')")

    # Demonstrate the email sending capability (without actually sending)
    print("\n    Email payload structure:")
    email_structure = {
        "message": {
            "subject": "Example Subject",
            "body": {"contentType": "Text", "content": "Email body content"},
            "toRecipients": [{"emailAddress": {"address": "recipient@example.com"}}],
        }
    }
    print(f"    {json.dumps(email_structure, indent=6)}")

    print("\n" + "=" * 70)
    print("Demo Completed")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("  • Graph API uses OAuth2 for authentication")
    print("  • All operations use REST API with JSON payloads")
    print("  • Device code flow is suitable for CLI applications")
    print("  • API endpoint: https://graph.microsoft.com/v1.0")
    print("\nFor production use:")
    print("  • Store credentials securely (environment variables, Key Vault)")
    print("  • Implement token caching to avoid repeated authentication")
    print("  • Add comprehensive error handling and retry logic")
    print("  • Use app permissions for daemon/service applications")
    print("  • Follow Microsoft Graph best practices for throttling")


if __name__ == "__main__":
    demonstrate_graph_api()
