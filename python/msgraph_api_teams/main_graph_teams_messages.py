#!/usr/bin/env python3
"""
Microsoft Graph API - Teams Channel and Group Chat Messages

This script demonstrates how to send and receive messages in Microsoft Teams
using the Microsoft Graph API. It covers both channel messages and group chat messages.
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
from typing import Any, Dict, List, Optional
from datetime import datetime

import msal
import requests


# Microsoft Graph API configuration for Teams
CLIENT_ID = "14d82eec-204b-4c2f-b7e8-296a70dab67e"  # Public client ID for demo
TENANT_ID = "common"  # Use 'common' for multi-tenant
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"

# Teams-specific scopes for channel and chat messages
SCOPES = [
    "User.Read",
    "Team.ReadBasic.All",  # Read team names and descriptions
    "Channel.ReadBasic.All",  # Read channel names and descriptions
    "ChannelMessage.Read.All",  # Read channel messages
    "ChannelMessage.Send",  # Send messages to channels
    "Chat.Read",  # Read user's chat messages
    "Chat.ReadWrite",  # Send and read chat messages
]

GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0"
GRAPH_BETA_ENDPOINT = "https://graph.microsoft.com/beta"


def authenticate_device_code_flow() -> Optional[Dict[str, Any]]:
    """
    Authenticate using device code flow with Teams-specific permissions.

    Returns:
        Dict containing the access token and other authentication details, or None if failed.
    """
    # Line 53: Create a PublicClientApplication instance
    app = msal.PublicClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
    )

    # Line 59: Initiate the device code flow with Teams scopes
    flow = app.initiate_device_flow(scopes=SCOPES)

    if "user_code" not in flow:
        print(f"❌ Failed to create device flow. Error: {json.dumps(flow, indent=2)}")
        return None

    # Line 65: Display instructions for user authentication
    print("\n" + "=" * 80)
    print("🔐 AUTHENTICATION REQUIRED - Microsoft Teams Access")
    print("=" * 80)
    print(flow["message"])
    print("\n⚠️  Important: You need permissions to access Teams in your organization")
    print("=" * 80 + "\n")

    # Line 73: Complete the device code flow
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


def call_graph_api(
    endpoint: str,
    access_token: str,
    method: str = "GET",
    data: Optional[Dict] = None,
    use_beta: bool = False,
) -> Optional[Dict[str, Any]]:
    """
    Make a request to Microsoft Graph API.

    Args:
        endpoint: The Graph API endpoint to call
        access_token: The OAuth access token for authentication
        method: HTTP method (GET, POST, etc.)
        data: Optional JSON data for POST requests
        use_beta: Whether to use the beta endpoint

    Returns:
        JSON response from the API, or None if the request failed.
    """
    # Line 105: Prepare headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }

    # Line 111: Construct the full URL
    base_url = GRAPH_BETA_ENDPOINT if use_beta else GRAPH_API_ENDPOINT
    url = f"{base_url}{endpoint}"

    # Line 115: Make the API request based on method
    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, json=data)
    else:
        print(f"❌ Unsupported HTTP method: {method}")
        return None

    # Line 124: Check response status
    if response.status_code in [200, 201]:
        return response.json() if response.text else {"status": "success"}
    else:
        print(f"❌ API call failed: {response.status_code}")
        print(f"   Endpoint: {endpoint}")
        print(f"   Response: {response.text}\n")
        return None


def list_teams(access_token: str) -> Optional[List[Dict[str, Any]]]:
    """
    List all Teams that the user is a member of.

    Returns:
        List of team objects, or None if the request failed.
    """
    # Line 141: Call the /me/joinedTeams endpoint
    print("📋 Listing Teams you are a member of...\n")
    result = call_graph_api("/me/joinedTeams", access_token)

    if not result:
        return None

    teams = result.get("value", [])

    # Line 149: Display teams information
    print(f"Found {len(teams)} Teams:\n")
    for idx, team in enumerate(teams, 1):
        team_id = team.get("id")
        team_name = team.get("displayName", "N/A")
        description = team.get("description", "No description")

        print(f"  [{idx}] {team_name}")
        print(f"      ID: {team_id}")
        print(f"      Description: {description}\n")

    return teams


def list_channels(team_id: str, access_token: str) -> Optional[List[Dict[str, Any]]]:
    """
    List all channels in a specific team.

    Args:
        team_id: The ID of the team

    Returns:
        List of channel objects, or None if the request failed.
    """
    # Line 174: Call the /teams/{id}/channels endpoint
    print("📺 Listing channels in team...\n")
    result = call_graph_api(f"/teams/{team_id}/channels", access_token)

    if not result:
        return None

    channels = result.get("value", [])

    # Line 183: Display channels information
    print(f"Found {len(channels)} channels:\n")
    for idx, channel in enumerate(channels, 1):
        channel_id = channel.get("id")
        channel_name = channel.get("displayName", "N/A")
        description = channel.get("description", "No description")

        print(f"  [{idx}] {channel_name}")
        print(f"      ID: {channel_id}")
        print(f"      Description: {description}\n")

    return channels


def send_channel_message(
    team_id: str, channel_id: str, message: str, access_token: str
) -> bool:
    """
    Send a message to a Teams channel.

    Args:
        team_id: The ID of the team
        channel_id: The ID of the channel
        message: The message content to send

    Returns:
        True if successful, False otherwise.
    """
    # Line 212: Prepare message payload
    endpoint = f"/teams/{team_id}/channels/{channel_id}/messages"

    message_data = {
        "body": {
            "content": message,
            "contentType": "text",  # Can also be "html"
        }
    }

    # Line 222: Send POST request to create message
    print("📤 Sending message to channel...\n")
    result = call_graph_api(endpoint, access_token, method="POST", data=message_data)

    if result:
        print("✅ Message sent successfully!")
        print(f"   Message ID: {result.get('id')}")
        print(f"   Created: {result.get('createdDateTime')}\n")
        return True
    else:
        return False


def read_channel_messages(
    team_id: str, channel_id: str, access_token: str, limit: int = 5
) -> Optional[List[Dict[str, Any]]]:
    """
    Read messages from a Teams channel.

    Args:
        team_id: The ID of the team
        channel_id: The ID of the channel
        limit: Maximum number of messages to retrieve

    Returns:
        List of message objects, or None if the request failed.
    """
    # Line 251: Call the messages endpoint with $top parameter
    endpoint = f"/teams/{team_id}/channels/{channel_id}/messages?$top={limit}"
    print(f"📥 Reading messages from channel (top {limit})...\n")

    result = call_graph_api(endpoint, access_token)

    if not result:
        return None

    messages = result.get("value", [])

    # Line 262: Display channel messages
    print(f"Found {len(messages)} messages:\n")
    for idx, msg in enumerate(messages, 1):
        msg_id = msg.get("id")
        created = msg.get("createdDateTime", "N/A")
        sender = msg.get("from", {}).get("user", {}).get("displayName", "Unknown")
        content = msg.get("body", {}).get("content", "")

        # Truncate long messages for display
        content_preview = content[:100] + "..." if len(content) > 100 else content

        print(f"  [{idx}] From: {sender}")
        print(f"      Created: {created}")
        print(f"      Message: {content_preview}")
        print(f"      ID: {msg_id}\n")

    return messages


def list_chats(access_token: str) -> Optional[List[Dict[str, Any]]]:
    """
    List all chats (1-on-1 and group chats) that the user is part of.

    Returns:
        List of chat objects, or None if the request failed.
    """
    # Line 289: Call the /me/chats endpoint
    print("💬 Listing your chats...\n")
    result = call_graph_api("/me/chats", access_token)

    if not result:
        return None

    chats = result.get("value", [])

    # Line 298: Display chats information
    print(f"Found {len(chats)} chats:\n")
    for idx, chat in enumerate(chats, 1):
        chat_id = chat.get("id")
        chat_type = chat.get("chatType", "N/A")  # oneOnOne, group, meeting
        topic = chat.get("topic") or f"({chat_type} chat)"
        created = chat.get("createdDateTime", "N/A")

        print(f"  [{idx}] {topic}")
        print(f"      ID: {chat_id}")
        print(f"      Type: {chat_type}")
        print(f"      Created: {created}\n")

    return chats


def send_chat_message(chat_id: str, message: str, access_token: str) -> bool:
    """
    Send a message to a chat (1-on-1 or group chat).

    Args:
        chat_id: The ID of the chat
        message: The message content to send

    Returns:
        True if successful, False otherwise.
    """
    # Line 325: Prepare message payload
    endpoint = f"/chats/{chat_id}/messages"

    message_data = {"body": {"content": message, "contentType": "text"}}

    # Line 335: Send POST request to create chat message
    print("📤 Sending message to chat...\n")
    result = call_graph_api(endpoint, access_token, method="POST", data=message_data)

    if result:
        print("✅ Chat message sent successfully!")
        print(f"   Message ID: {result.get('id')}")
        print(f"   Created: {result.get('createdDateTime')}\n")
        return True
    else:
        return False


def read_chat_messages(
    chat_id: str, access_token: str, limit: int = 10
) -> Optional[List[Dict[str, Any]]]:
    """
    Read messages from a chat.

    Args:
        chat_id: The ID of the chat
        limit: Maximum number of messages to retrieve

    Returns:
        List of message objects, or None if the request failed.
    """
    # Line 361: Call the chat messages endpoint
    endpoint = f"/chats/{chat_id}/messages?$top={limit}"
    print(f"📥 Reading messages from chat (top {limit})...\n")

    result = call_graph_api(endpoint, access_token)

    if not result:
        return None

    messages = result.get("value", [])

    # Line 371: Display chat messages
    print(f"Found {len(messages)} messages:\n")
    for idx, msg in enumerate(messages, 1):
        created = msg.get("createdDateTime", "N/A")
        sender = msg.get("from", {}).get("user", {}).get("displayName", "Unknown")
        content = msg.get("body", {}).get("content", "")
        msg_type = msg.get("messageType", "message")

        # Truncate long messages for display
        content_preview = content[:100] + "..." if len(content) > 100 else content

        print(f"  [{idx}] From: {sender} (Type: {msg_type})")
        print(f"      Created: {created}")
        print(f"      Message: {content_preview}\n")

    return messages


def main() -> int:
    """Main function to demonstrate Teams channel and chat message operations."""
    print("\n" + "=" * 80)
    print("Microsoft Graph API - Teams Channel & Chat Messages Demo")
    print("=" * 80 + "\n")

    # Line 396: Step 1 - Authenticate
    print("Step 1: Authenticating with Teams permissions...\n")
    auth_result = authenticate_device_code_flow()

    if not auth_result:
        print("❌ Exiting due to authentication failure.\n")
        return 1

    access_token = auth_result["access_token"]

    # Line 406: Step 2 - List Teams
    print("\n" + "=" * 80)
    print("Step 2: TEAMS - Listing your Teams")
    print("=" * 80 + "\n")

    teams = list_teams(access_token)

    if not teams or len(teams) == 0:
        print("⚠️  No Teams found or you don't have access to any Teams.")
        print("   Note: This demo requires you to be a member of at least one Team.\n")
    else:
        # Line 417: Step 3 - Work with the first team's channels
        print("=" * 80)
        print("Step 3: CHANNELS - Working with channels in the first Team")
        print("=" * 80 + "\n")

        first_team = teams[0]
        team_id = first_team["id"]
        team_name = first_team["displayName"]

        print(f"Selected Team: {team_name}\n")

        channels = list_channels(team_id, access_token)

        if channels and len(channels) > 0:
            # Line 431: Step 4 - Send a message to the General channel
            print("=" * 80)
            print("Step 4: SEND MESSAGE - Sending a message to a channel")
            print("=" * 80 + "\n")

            # Find the General channel (usually exists in every team)
            general_channel = next(
                (ch for ch in channels if ch.get("displayName") == "General"),
                channels[0],  # Fallback to first channel
            )

            channel_id = general_channel["id"]
            channel_name = general_channel["displayName"]

            print(f"Target Channel: {channel_name}\n")

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            demo_message = f"Hello from Microsoft Graph API! 🚀 (Demo at {timestamp})"

            send_channel_message(team_id, channel_id, demo_message, access_token)

            # Line 453: Step 5 - Read messages from the channel
            print("=" * 80)
            print("Step 5: READ MESSAGES - Reading messages from the channel")
            print("=" * 80 + "\n")

            read_channel_messages(team_id, channel_id, access_token, limit=5)

    # Line 461: Step 6 - List chats
    print("=" * 80)
    print("Step 6: CHATS - Listing your chats")
    print("=" * 80 + "\n")

    chats = list_chats(access_token)

    if chats and len(chats) > 0:
        # Line 469: Step 7 - Read messages from first chat
        print("=" * 80)
        print("Step 7: CHAT MESSAGES - Reading messages from first chat")
        print("=" * 80 + "\n")

        first_chat = chats[0]
        chat_id = first_chat["id"]
        chat_topic = first_chat.get("topic") or f"({first_chat.get('chatType')} chat)"

        print(f"Selected Chat: {chat_topic}\n")

        read_chat_messages(chat_id, access_token, limit=10)

        # Line 483: Step 8 - Optionally send a chat message
        print("=" * 80)
        print("Step 8: SEND CHAT MESSAGE - Sending a message to the chat")
        print("=" * 80 + "\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        demo_chat_message = f"Hello from Graph API! 👋 (Demo at {timestamp})"

        send_chat_message(chat_id, demo_chat_message, access_token)
    else:
        print(
            "⚠️  No chats found. You need to have at least one chat to test chat messages.\n"
        )

    # Line 496: Completion
    print("=" * 80)
    print("✅ Teams Channel & Chat Messages demonstration completed!")
    print("=" * 80 + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
