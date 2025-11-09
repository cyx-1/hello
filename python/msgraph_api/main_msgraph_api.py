#!/usr/bin/env python3
"""
Microsoft Graph API Python Example

This script demonstrates how to authenticate and interact with Microsoft Graph API
using the Microsoft Authentication Library (MSAL) and the device code flow.
"""

# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "msal>=1.31.0",
#     "requests>=2.32.0",
# ]
# ///

import json
import sys
from typing import Any, Dict, Optional

import msal
import requests


# Microsoft Graph API configuration
CLIENT_ID = "14d82eec-204b-4c2f-b7e8-296a70dab67e"  # Public client ID for demo
TENANT_ID = "common"  # Use 'common' for multi-tenant, or specific tenant ID
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
SCOPES = ["User.Read", "Mail.Read"]  # Permissions we're requesting
GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0"


def authenticate_device_code_flow() -> Optional[Dict[str, Any]]:
    """
    Authenticate using device code flow.

    This flow is ideal for devices without a browser or input-constrained devices.
    The user needs to visit a URL and enter a code to authenticate.

    Returns:
        Dict containing the access token and other authentication details, or None if failed.
    """
    # Line 37: Create a PublicClientApplication instance
    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
    )

    # Line 43: Initiate the device code flow
    flow = app.initiate_device_flow(scopes=SCOPES)

    if "user_code" not in flow:
        print(f"❌ Failed to create device flow. Error: {json.dumps(flow, indent=2)}")
        return None

    # Line 49: Display instructions for user authentication
    print("\n" + "=" * 70)
    print("🔐 AUTHENTICATION REQUIRED")
    print("=" * 70)
    print(flow["message"])
    print("=" * 70 + "\n")

    # Line 56: Complete the device code flow by waiting for user authentication
    result = app.acquire_token_by_device_flow(flow)

    if "access_token" in result:
        print("✅ Authentication successful!\n")
        return result
    else:
        error = result.get("error")
        error_description = result.get("error_description")
        print("❌ Authentication failed!")
        print(f"   Error: {error}")
        print(f"   Description: {error_description}\n")
        return None


def call_graph_api(endpoint: str, access_token: str) -> Optional[Dict[str, Any]]:
    """
    Make a GET request to Microsoft Graph API.

    Args:
        endpoint: The Graph API endpoint to call (e.g., '/me' or '/me/messages')
        access_token: The OAuth access token for authentication

    Returns:
        JSON response from the API, or None if the request failed.
    """
    # Line 81: Prepare headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    # Line 87: Make the API request
    url = f"{GRAPH_API_ENDPOINT}{endpoint}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"❌ API call failed: {response.status_code}")
        print(f"   Response: {response.text}\n")
        return None


def display_user_profile(profile: Dict[str, Any]) -> None:
    """Display user profile information in a formatted manner."""
    print("👤 USER PROFILE")
    print("-" * 70)
    print(f"   Display Name:      {profile.get('displayName', 'N/A')}")
    print(f"   Email:             {profile.get('userPrincipalName', 'N/A')}")
    print(f"   Job Title:         {profile.get('jobTitle', 'N/A')}")
    print(f"   Office Location:   {profile.get('officeLocation', 'N/A')}")
    print(f"   User ID:           {profile.get('id', 'N/A')}")
    print("-" * 70 + "\n")


def display_messages(messages_data: Dict[str, Any]) -> None:
    """Display email messages in a formatted manner."""
    messages = messages_data.get("value", [])

    print(f"📧 EMAIL MESSAGES (Showing first {len(messages)} messages)")
    print("-" * 70)

    if not messages:
        print("   No messages found.\n")
        return

    for idx, message in enumerate(messages[:5], 1):  # Show only first 5
        subject = message.get("subject", "No Subject")
        sender = message.get("from", {}).get("emailAddress", {}).get("name", "Unknown")
        received = message.get("receivedDateTime", "N/A")

        print(f"\n   [{idx}] Subject: {subject}")
        print(f"       From:     {sender}")
        print(f"       Received: {received}")

    print("\n" + "-" * 70 + "\n")


def main() -> int:
    """Main function to demonstrate Microsoft Graph API usage."""
    print("\n" + "=" * 70)
    print("Microsoft Graph API - Python Example")
    print("=" * 70 + "\n")

    # Line 147: Step 1 - Authenticate
    print("Step 1: Authenticating...\n")
    auth_result = authenticate_device_code_flow()

    if not auth_result:
        print("❌ Exiting due to authentication failure.\n")
        return 1

    access_token = auth_result["access_token"]

    # Line 157: Step 2 - Get user profile
    print("Step 2: Fetching user profile...\n")
    profile = call_graph_api("/me", access_token)

    if profile:
        display_user_profile(profile)
    else:
        print("⚠️  Failed to fetch user profile.\n")

    # Line 166: Step 3 - Get user's messages
    print("Step 3: Fetching user's email messages...\n")
    messages = call_graph_api(
        "/me/messages?$top=5&$select=subject,from,receivedDateTime", access_token
    )

    if messages:
        display_messages(messages)
    else:
        print("⚠️  Failed to fetch messages.\n")

    print("=" * 70)
    print("✅ Microsoft Graph API demonstration completed successfully!")
    print("=" * 70 + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
