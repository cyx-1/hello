# Microsoft Graph API - Teams Channel & Group Chat Messages

This example demonstrates how to send and receive messages in Microsoft Teams using the Microsoft Graph API. It covers both **Teams channel messages** and **group chat/1-on-1 chat messages**.

## Requirements

- **Python Version**: Python 3.9 or higher
- **Libraries**:
  - `msal` >= 1.31.0 (Microsoft Authentication Library)
  - `requests` >= 2.32.0
- **Microsoft Teams Access**: You need to be a member of at least one Team and have active chats

## Running the Example

```bash
uv run python python/graph_teams_messages/main_graph_teams_messages.py
```

## Key Source Code Sections

### 1. Teams-Specific Permission Scopes (Lines 28-38)

```python
28  # Teams-specific scopes for channel and chat messages
29  SCOPES = [
30      "User.Read",
31      "Team.ReadBasic.All",  # Read team names and descriptions
32      "Channel.ReadBasic.All",  # Read channel names and descriptions
33      "ChannelMessage.Read.All",  # Read channel messages
34      "ChannelMessage.Send",  # Send messages to channels
35      "Chat.Read",  # Read user's chat messages
36      "Chat.ReadWrite",  # Send and read chat messages
37  ]
```

**Lines 29-37** define the Microsoft Graph API permissions required for Teams operations:
- `Team.ReadBasic.All`: Allows reading team names and descriptions
- `Channel.ReadBasic.All`: Allows reading channel information
- `ChannelMessage.Read.All`: Enables reading all messages in channels
- `ChannelMessage.Send`: Allows sending messages to channels
- `Chat.Read` and `Chat.ReadWrite`: Enable reading and sending chat messages

### 2. Unified API Call Function (Lines 92-132)

```python
92  def call_graph_api(
93      endpoint: str, access_token: str, method: str = "GET", data: Optional[Dict] = None, use_beta: bool = False
94  ) -> Optional[Dict[str, Any]]:
95      """
96      Make a request to Microsoft Graph API.
97
98      Args:
99          endpoint: The Graph API endpoint to call
100         access_token: The OAuth access token for authentication
101         method: HTTP method (GET, POST, etc.)
102         data: Optional JSON data for POST requests
103         use_beta: Whether to use the beta endpoint
104     """
105     # Line 105: Prepare headers with the access token
106     headers = {
107         "Authorization": f"Bearer {access_token}",
108         "Content-Type": "application/json",
109     }
110
111     # Line 111: Construct the full URL
112     base_url = GRAPH_BETA_ENDPOINT if use_beta else GRAPH_API_ENDPOINT
113     url = f"{base_url}{endpoint}"
114
115     # Line 115: Make the API request based on method
116     if method == "GET":
117         response = requests.get(url, headers=headers)
118     elif method == "POST":
119         response = requests.post(url, headers=headers, json=data)
```

**Line 105-109**: Sets up authentication headers with the Bearer token
**Line 115-119**: Supports both GET requests (for reading data) and POST requests (for sending messages)
**Line 124**: Returns successful responses with status codes 200 (OK) or 201 (Created)

### 3. Listing Teams (Lines 136-161)

```python
136 def list_teams(access_token: str) -> Optional[List[Dict[str, Any]]]:
137     """
138     List all Teams that the user is a member of.
139     """
140     # Line 141: Call the /me/joinedTeams endpoint
141     print("📋 Listing Teams you are a member of...\n")
142     result = call_graph_api("/me/joinedTeams", access_token)
143
144     if not result:
145         return None
146
147     teams = result.get("value", [])
148
149     # Line 149: Display teams information
150     print(f"Found {len(teams)} Teams:\n")
151     for idx, team in enumerate(teams, 1):
152         team_id = team.get("id")
153         team_name = team.get("displayName", "N/A")
154         description = team.get("description", "No description")
155
156         print(f"  [{idx}] {team_name}")
157         print(f"      ID: {team_id}")
158         print(f"      Description: {description}\n")
159
160     return teams
```

**Line 142**: Calls the `/me/joinedTeams` endpoint to get all Teams the authenticated user belongs to
**Line 147**: Extracts the list of teams from the API response
**Lines 151-158**: Iterates through teams and displays their name, ID, and description

### 4. Listing Channels in a Team (Lines 164-195)

```python
164 def list_channels(team_id: str, access_token: str) -> Optional[List[Dict[str, Any]]]:
165     """
166     List all channels in a specific team.
167
168     Args:
169         team_id: The ID of the team
170     """
171     # Line 174: Call the /teams/{id}/channels endpoint
172     print(f"📺 Listing channels in team...\n")
173     result = call_graph_api(f"/teams/{team_id}/channels", access_token)
174
175     if not result:
176         return None
177
178     channels = result.get("value", [])
179
180     # Line 183: Display channels information
181     print(f"Found {len(channels)} channels:\n")
182     for idx, channel in enumerate(channels, 1):
183         channel_id = channel.get("id")
184         channel_name = channel.get("displayName", "N/A")
185         description = channel.get("description", "No description")
186
187         print(f"  [{idx}] {channel_name}")
188         print(f"      ID: {channel_id}")
189         print(f"      Description: {description}\n")
190
191     return channels
```

**Line 173**: Calls `/teams/{team_id}/channels` to get all channels within a specific team
**Line 178**: Extracts the channels array from the response
**Lines 182-189**: Displays channel information including name, ID, and description

### 5. Sending Messages to a Channel (Lines 198-234)

```python
198 def send_channel_message(
199     team_id: str, channel_id: str, message: str, access_token: str
200 ) -> bool:
201     """
202     Send a message to a Teams channel.
203
204     Args:
205         team_id: The ID of the team
206         channel_id: The ID of the channel
207         message: The message content to send
208     """
209     # Line 212: Prepare message payload
210     endpoint = f"/teams/{team_id}/channels/{channel_id}/messages"
211
212     message_data = {
213         "body": {
214             "content": message,
215             "contentType": "text"  # Can also be "html"
216         }
217     }
218
219     # Line 222: Send POST request to create message
220     print(f"📤 Sending message to channel...\n")
221     result = call_graph_api(endpoint, access_token, method="POST", data=message_data)
222
223     if result:
224         print(f"✅ Message sent successfully!")
225         print(f"   Message ID: {result.get('id')}")
226         print(f"   Created: {result.get('createdDateTime')}\n")
227         return True
```

**Line 210**: Constructs the endpoint URL for posting messages to a specific channel
**Lines 212-217**: Creates the message payload with content and content type (text or HTML)
**Line 221**: Sends a POST request to create the message in the channel
**Lines 224-226**: Displays confirmation with the message ID and creation timestamp

### 6. Reading Messages from a Channel (Lines 237-279)

```python
237 def read_channel_messages(
238     team_id: str, channel_id: str, access_token: str, limit: int = 5
239 ) -> Optional[List[Dict[str, Any]]]:
240     """
241     Read messages from a Teams channel.
242
243     Args:
244         team_id: The ID of the team
245         channel_id: The ID of the channel
246         limit: Maximum number of messages to retrieve
247     """
248     # Line 251: Call the messages endpoint with $top parameter
249     endpoint = f"/teams/{team_id}/channels/{channel_id}/messages?$top={limit}"
250     print(f"📥 Reading messages from channel (top {limit})...\n")
251
252     result = call_graph_api(endpoint, access_token)
253
254     if not result:
255         return None
256
257     messages = result.get("value", [])
258
259     # Line 262: Display channel messages
260     print(f"Found {len(messages)} messages:\n")
261     for idx, msg in enumerate(messages, 1):
262         msg_id = msg.get("id")
263         created = msg.get("createdDateTime", "N/A")
264         sender = msg.get("from", {}).get("user", {}).get("displayName", "Unknown")
265         content = msg.get("body", {}).get("content", "")
266
267         # Truncate long messages for display
268         content_preview = content[:100] + "..." if len(content) > 100 else content
269
270         print(f"  [{idx}] From: {sender}")
271         print(f"      Created: {created}")
272         print(f"      Message: {content_preview}")
273         print(f"      ID: {msg_id}\n")
274
275     return messages
```

**Line 249**: Uses the `$top` OData query parameter to limit the number of messages retrieved
**Line 252**: Makes a GET request to fetch messages from the channel
**Lines 261-273**: Iterates through messages and displays sender, timestamp, content preview, and message ID

### 7. Listing Chats (Lines 282-312)

```python
282 def list_chats(access_token: str) -> Optional[List[Dict[str, Any]]]:
283     """
284     List all chats (1-on-1 and group chats) that the user is part of.
285     """
286     # Line 289: Call the /me/chats endpoint
287     print("💬 Listing your chats...\n")
288     result = call_graph_api("/me/chats", access_token)
289
290     if not result:
291         return None
292
293     chats = result.get("value", [])
294
295     # Line 298: Display chats information
296     print(f"Found {len(chats)} chats:\n")
297     for idx, chat in enumerate(chats, 1):
298         chat_id = chat.get("id")
299         chat_type = chat.get("chatType", "N/A")  # oneOnOne, group, meeting
300         topic = chat.get("topic") or f"({chat_type} chat)"
301         created = chat.get("createdDateTime", "N/A")
302
303         print(f"  [{idx}] {topic}")
304         print(f"      ID: {chat_id}")
305         print(f"      Type: {chat_type}")
306         print(f"      Created: {created}\n")
307
308     return chats
```

**Line 288**: Calls `/me/chats` to retrieve all chats (1-on-1, group, and meeting chats) for the user
**Line 299**: Extracts the chat type which can be `oneOnOne`, `group`, or `meeting`
**Lines 297-306**: Displays chat information including topic, ID, type, and creation date

### 8. Sending Messages to a Chat (Lines 315-347)

```python
315 def send_chat_message(chat_id: str, message: str, access_token: str) -> bool:
316     """
317     Send a message to a chat (1-on-1 or group chat).
318
319     Args:
320         chat_id: The ID of the chat
321         message: The message content to send
322     """
323     # Line 325: Prepare message payload
324     endpoint = f"/chats/{chat_id}/messages"
325
326     message_data = {
327         "body": {
328             "content": message,
329             "contentType": "text"
330         }
331     }
332
333     # Line 335: Send POST request to create chat message
334     print(f"📤 Sending message to chat...\n")
335     result = call_graph_api(endpoint, access_token, method="POST", data=message_data)
336
337     if result:
338         print(f"✅ Chat message sent successfully!")
339         print(f"   Message ID: {result.get('id')}")
340         print(f"   Created: {result.get('createdDateTime')}\n")
341         return True
```

**Line 324**: Constructs the endpoint for posting messages to a specific chat
**Lines 326-331**: Creates the message payload similar to channel messages
**Line 335**: Sends a POST request to create the chat message
**Lines 338-340**: Confirms successful message delivery with ID and timestamp

### 9. Reading Messages from a Chat (Lines 350-388)

```python
350 def read_chat_messages(
351     chat_id: str, access_token: str, limit: int = 10
352 ) -> Optional[List[Dict[str, Any]]]:
353     """
354     Read messages from a chat.
355
356     Args:
357         chat_id: The ID of the chat
358         limit: Maximum number of messages to retrieve
359     """
360     # Line 361: Call the chat messages endpoint
361     endpoint = f"/chats/{chat_id}/messages?$top={limit}"
362     print(f"📥 Reading messages from chat (top {limit})...\n")
363
364     result = call_graph_api(endpoint, access_token)
365
366     if not result:
367         return None
368
369     messages = result.get("value", [])
370
371     # Line 371: Display chat messages
372     print(f"Found {len(messages)} messages:\n")
373     for idx, msg in enumerate(messages, 1):
374         created = msg.get("createdDateTime", "N/A")
375         sender = msg.get("from", {}).get("user", {}).get("displayName", "Unknown")
376         content = msg.get("body", {}).get("content", "")
377         msg_type = msg.get("messageType", "message")
378
379         # Truncate long messages for display
380         content_preview = content[:100] + "..." if len(content) > 100 else content
381
382         print(f"  [{idx}] From: {sender} (Type: {msg_type})")
383         print(f"      Created: {created}")
384         print(f"      Message: {content_preview}\n")
385
386     return messages
```

**Line 361**: Uses `$top` parameter to limit the number of chat messages retrieved
**Line 377**: Extracts the message type (e.g., "message", "systemEventMessage")
**Lines 373-384**: Displays message information including sender, timestamp, type, and content

## Sample Output

### Phase 1: Authentication (Lines 396-404)

```
================================================================================
Microsoft Graph API - Teams Channel & Chat Messages Demo
================================================================================

Step 1: Authenticating with Teams permissions...

================================================================================
🔐 AUTHENTICATION REQUIRED - Microsoft Teams Access
================================================================================
To sign in, use a web browser to open the page https://microsoft.com/devicelogin
and enter the code FG89HJ12 to authenticate.

⚠️  Important: You need permissions to access Teams in your organization
================================================================================

✅ Authentication successful!
```

**Output Annotation**: Corresponds to **lines 396-404** in the main function and **lines 47-86** in the authentication function. The device code flow:
1. Generates a unique code (e.g., "FG89HJ12")
2. User visits the URL in a browser
3. Enters the code and signs in
4. Grants the requested Teams permissions
5. Script receives the access token

### Phase 2: Listing Teams (Lines 406-416)

```
================================================================================
Step 2: TEAMS - Listing your Teams
================================================================================

📋 Listing Teams you are a member of...

Found 3 Teams:

  [1] Engineering Team
      ID: 02bd9fd6-8f93-4758-87c3-1fb73740a315
      Description: Main engineering team workspace

  [2] Marketing Campaign
      ID: 12ae8d7e-9f82-4659-98d4-2ec84851b426
      Description: Q1 2025 marketing initiatives

  [3] Product Development
      ID: 33cf9ef7-af91-5760-a9e5-3fd95962c537
      Description: Product roadmap and feature planning
```

**Output Annotation**: Generated by **lines 406-416** in main() calling `list_teams()` at **lines 136-161**:
1. **Line 142**: Calls `/me/joinedTeams` endpoint
2. **Line 147**: Extracts the teams array from the response
3. **Lines 151-158**: Displays each team's name, ID, and description

### Phase 3: Listing Channels (Lines 417-430)

```
================================================================================
Step 3: CHANNELS - Working with channels in the first Team
================================================================================

Selected Team: Engineering Team

📺 Listing channels in team...

Found 4 channels:

  [1] General
      ID: 19:2da4c29f6d7249ead4d3a25c8f7b8e3d@thread.tacv2
      Description: General discussion for the team

  [2] Development
      ID: 19:3eb5d30g7e8350fbe5e4b36d9g8c9f4e@thread.tacv2
      Description: Development updates and code reviews

  [3] Testing
      ID: 19:4fc6e41h8f9461gce6f5c47eah9d0g5f@thread.tacv2
      Description: QA and testing coordination

  [4] Releases
      ID: 19:5gd7f52i9ga572hdf7g6d58fbi0e1h6g@thread.tacv2
      Description: Release planning and deployment
```

**Output Annotation**: Generated by **lines 417-430** in main() calling `list_channels()` at **lines 164-195**:
1. **Line 425**: Selects the first team from the teams list
2. **Line 428**: Calls `list_channels()` with the team ID
3. **Line 173**: Calls `/teams/{team_id}/channels` endpoint
4. **Lines 182-189**: Displays each channel's name, ID, and description

### Phase 4: Sending a Channel Message (Lines 431-451)

```
================================================================================
Step 4: SEND MESSAGE - Sending a message to a channel
================================================================================

Target Channel: General

📤 Sending message to channel...

✅ Message sent successfully!
   Message ID: 1702856234567
   Created: 2025-01-15T14:30:45.123Z
```

**Output Annotation**: Generated by **lines 431-451** calling `send_channel_message()` at **lines 198-234**:
1. **Line 437-440**: Finds the "General" channel or uses the first available channel
2. **Line 448**: Creates a demo message with current timestamp
3. **Line 450**: Calls `send_channel_message()` which:
   - **Line 212-217**: Prepares the message payload
   - **Line 221**: POSTs to `/teams/{team_id}/channels/{channel_id}/messages`
   - **Lines 224-226**: Displays confirmation with message ID and creation time

### Phase 5: Reading Channel Messages (Lines 453-459)

```
================================================================================
Step 5: READ MESSAGES - Reading messages from the channel
================================================================================

📥 Reading messages from channel (top 5)...

Found 5 messages:

  [1] From: Alice Johnson
      Created: 2025-01-15T14:30:45.123Z
      Message: Hello from Microsoft Graph API! 🚀 (Demo at 2025-01-15 14:30:45)
      ID: 1702856234567

  [2] From: Bob Williams
      Created: 2025-01-15T11:22:33.456Z
      Message: Great work on the new feature deployment!
      ID: 1702843753456

  [3] From: Carol Davis
      Created: 2025-01-15T09:15:12.789Z
      Message: Team meeting at 3 PM today. Please confirm attendance.
      ID: 1702836512789

  [4] From: David Chen
      Created: 2025-01-14T16:45:20.234Z
      Message: Code review completed. All tests passing ✅
      ID: 1702777120234

  [5] From: Emily Rodriguez
      Created: 2025-01-14T14:30:18.567Z
      Message: Updated the documentation for the API endpoints.
      ID: 1702769418567
```

**Output Annotation**: Generated by **lines 453-459** calling `read_channel_messages()` at **lines 237-279**:
1. **Line 459**: Calls `read_channel_messages()` with limit of 5
2. **Line 249**: Constructs endpoint with `$top=5` OData parameter
3. **Line 252**: GETs from `/teams/{team_id}/channels/{channel_id}/messages?$top=5`
4. **Lines 261-273**: Displays each message with:
   - Sender's display name
   - Creation timestamp in ISO 8601 format
   - Message content (truncated if > 100 characters)
   - Unique message ID

### Phase 6: Listing Chats (Lines 461-468)

```
================================================================================
Step 6: CHATS - Listing your chats
================================================================================

💬 Listing your chats...

Found 5 chats:

  [1] Planning Discussion
      ID: 19:8ea0e38b-4e5a-4b1b-a963-e5b8c7d6f9a2_5c5c8f7d-6e9b-4c2d-b874-f6a7e8d9c0b1@unq.gbl.spaces
      Type: group
      Created: 2025-01-10T08:30:00Z

  [2] (oneOnOne chat)
      ID: 19:2da4c29f6d7249ead4d3a25c8f7b8e3d@thread.v2
      Type: oneOnOne
      Created: 2025-01-08T14:20:00Z

  [3] Project Kickoff
      ID: 19:4fc6e41h8f9461gce6f5c47eah9d0g5f_7d7d9g8e-7f0c-5d3e-c985-g7b8f9e0d1c2@unq.gbl.spaces
      Type: group
      Created: 2025-01-05T10:00:00Z

  [4] (oneOnOne chat)
      ID: 19:3eb5d30g7e8350fbe5e4b36d9g8c9f4e@thread.v2
      Type: oneOnOne
      Created: 2025-01-03T16:45:00Z

  [5] Weekly Sync
      ID: 19:5gd7f52i9ga572hdf7g6d58fbi0e1h6g_8e8eah9f-8g1d-6e4f-d096-h8c9gaf1e2d3@unq.gbl.spaces
      Type: meeting
      Created: 2025-01-02T09:00:00Z
```

**Output Annotation**: Generated by **lines 461-468** calling `list_chats()` at **lines 282-312**:
1. **Line 466**: Calls `list_chats()` function
2. **Line 288**: Calls `/me/chats` endpoint
3. **Lines 297-306**: Displays each chat with:
   - **Topic**: Group chats have names; 1-on-1 chats show "(oneOnOne chat)"
   - **Chat ID**: Unique identifier for the chat
   - **Chat Type**: `oneOnOne`, `group`, or `meeting`
   - **Created Date**: When the chat was created

### Phase 7: Reading Chat Messages (Lines 469-481)

```
================================================================================
Step 7: CHAT MESSAGES - Reading messages from first chat
================================================================================

Selected Chat: Planning Discussion

📥 Reading messages from chat (top 10)...

Found 8 messages:

  [1] From: Sarah Miller (Type: message)
      Created: 2025-01-15T13:45:22.123Z
      Message: Sounds good! I'll prepare the slides.

  [2] From: Tom Anderson (Type: message)
      Created: 2025-01-15T13:42:18.456Z
      Message: Let's schedule a follow-up meeting next week to review progress.

  [3] From: Sarah Miller (Type: message)
      Created: 2025-01-15T13:38:45.789Z
      Message: I agree with the proposed timeline.

  [4] From: System (Type: systemEventMessage)
      Created: 2025-01-15T10:00:00.000Z
      Message: <systemEventMessage>Tom Anderson added Lisa Wong to the chat</systemEventMessage>

  [5] From: Lisa Wong (Type: message)
      Created: 2025-01-14T16:20:33.234Z
      Message: Thanks for including me! What are the current priorities?

  [6] From: Tom Anderson (Type: message)
      Created: 2025-01-14T15:55:12.567Z
      Message: We need to finalize the Q1 roadmap by end of week.

  [7] From: Sarah Miller (Type: message)
      Created: 2025-01-14T14:30:08.890Z
      Message: Hi team! Looking forward to working on this together.

  [8] From: System (Type: systemEventMessage)
      Created: 2025-01-14T14:00:00.000Z
      Message: <systemEventMessage>Sarah Miller created the chat "Planning Discussion"</systemEventMessage>
```

**Output Annotation**: Generated by **lines 469-481** calling `read_chat_messages()` at **lines 350-388**:
1. **Line 480**: Calls `read_chat_messages()` with limit of 10
2. **Line 361**: Constructs endpoint `/chats/{chat_id}/messages?$top=10`
3. **Line 364**: Makes GET request to retrieve messages
4. **Lines 373-384**: Displays each message with:
   - **Sender**: User's display name or "System" for events
   - **Message Type**: Usually "message", but can be "systemEventMessage" for events
   - **Created**: Timestamp in ISO 8601 format
   - **Content**: Message text or system event description

Note: System event messages track chat lifecycle events like member additions, chat creation, etc.

### Phase 8: Sending a Chat Message (Lines 483-493)

```
================================================================================
Step 8: SEND CHAT MESSAGE - Sending a message to the chat
================================================================================

📤 Sending message to chat...

✅ Chat message sent successfully!
   Message ID: 1702856834567
   Created: 2025-01-15T14:33:54.567Z
```

**Output Annotation**: Generated by **lines 483-493** calling `send_chat_message()` at **lines 315-347**:
1. **Line 490**: Creates demo chat message with timestamp
2. **Line 492**: Calls `send_chat_message()` which:
   - **Line 324**: Constructs endpoint `/chats/{chat_id}/messages`
   - **Lines 326-331**: Prepares message payload
   - **Line 335**: POSTs the message to the chat
   - **Lines 338-340**: Displays confirmation with message ID and timestamp

### Completion (Lines 496-500)

```
================================================================================
✅ Teams Channel & Chat Messages demonstration completed!
================================================================================
```

**Output Annotation**: Final completion message from **lines 496-500** indicating all operations finished successfully.

## How It Works

### Authentication Flow

The script uses **device code flow authentication** (lines 47-86) specifically configured for Teams:
1. Requests a device code from Microsoft identity platform
2. User visits https://microsoft.com/devicelogin and enters the code
3. User signs in and grants the requested Teams permissions
4. Application receives an access token valid for the requested scopes

### Teams vs Chats: Key Differences

**Teams Channels**:
- Part of a structured Team organization
- Have persistent membership
- Messages organized in channels (General, Development, etc.)
- Require Team and Channel IDs for operations
- Endpoints: `/teams/{id}/channels/{id}/messages`

**Chats**:
- Can be 1-on-1 (`oneOnOne`), group (`group`), or meeting-based (`meeting`)
- More informal and flexible
- Direct messaging between users
- Only require Chat ID for operations
- Endpoints: `/chats/{id}/messages`

### Message Structure

Both channel and chat messages use the same structure (see lines 212-217, 326-331):

```json
{
  "body": {
    "content": "Message text here",
    "contentType": "text"
  }
}
```

- **content**: The message text (can also be HTML if contentType is "html")
- **contentType**: Either "text" for plain text or "html" for rich formatted messages

### OData Query Parameters

The script uses OData query parameters to optimize API calls:

- **$top=N** (lines 249, 361): Limits the number of results returned
  - Example: `?$top=5` returns only the 5 most recent messages

- **$select** (can be added): Specifies which fields to return
  - Example: `?$select=from,createdDateTime,body` returns only specific fields

### Error Handling

Robust error handling throughout:
- **Authentication failures** (lines 79-85): Display error details
- **API call failures** (lines 124-131): Check status codes and log responses
- **Missing data** (lines 413-415, 492-493): Handle cases where Teams or chats don't exist
- **Safe dictionary access**: Uses `.get()` methods to prevent KeyErrors

## Permissions and Security

### Required Permissions

The application requests these Microsoft Graph API permissions:

1. **Team.ReadBasic.All**: Read team information (non-sensitive)
2. **Channel.ReadBasic.All**: Read channel information
3. **ChannelMessage.Read.All**: Read all channel messages
4. **ChannelMessage.Send**: Send messages to channels
5. **Chat.Read**: Read chat messages
6. **Chat.ReadWrite**: Send and read chat messages

### Permission Types

- **Delegated permissions**: Used in this example (user acts on their own behalf)
- **Application permissions**: Would require admin consent (for apps acting independently)

### Best Practices

1. **Minimum Permissions**: Only request permissions you need
2. **User Consent**: Device code flow requires user to explicitly consent
3. **Token Expiration**: Tokens expire after ~1 hour; production apps should implement refresh
4. **Rate Limiting**: Microsoft Graph API has rate limits; implement backoff strategies for production

### Production Considerations

For production applications:
1. **Register your own app** in Azure AD portal
2. **Use client secrets** or certificates for application permissions
3. **Implement token caching** using MSAL's built-in cache
4. **Handle token refresh** for long-running applications
5. **Use webhooks** for real-time message notifications instead of polling
6. **Implement retry logic** with exponential backoff for API failures

## Microsoft Graph API Endpoints Used

### Teams Operations

| Operation | Method | Endpoint | Line Reference |
|-----------|--------|----------|----------------|
| List Teams | GET | `/me/joinedTeams` | 142 |
| List Channels | GET | `/teams/{team-id}/channels` | 173 |
| Send Channel Message | POST | `/teams/{team-id}/channels/{channel-id}/messages` | 221 |
| Read Channel Messages | GET | `/teams/{team-id}/channels/{channel-id}/messages` | 252 |

### Chat Operations

| Operation | Method | Endpoint | Line Reference |
|-----------|--------|----------|----------------|
| List Chats | GET | `/me/chats` | 288 |
| Send Chat Message | POST | `/chats/{chat-id}/messages` | 335 |
| Read Chat Messages | GET | `/chats/{chat-id}/messages` | 364 |

## Common Issues and Solutions

### Issue: "Access Denied" or 403 errors

**Solution**: Ensure you have:
- Accepted all requested permissions during authentication
- Access to Teams in your organization
- Membership in the Teams you're trying to access

### Issue: "Resource not found" or 404 errors

**Solution**:
- Verify Team IDs and Channel IDs are correct
- Ensure you're a member of the Team/Chat you're trying to access
- Check that the Team or Chat hasn't been deleted

### Issue: Messages not appearing immediately

**Solution**:
- Graph API may have slight delays in message propagation
- Wait a few seconds and retry reading messages
- Consider implementing webhooks for real-time updates in production

## Additional Resources

- [Microsoft Graph API - Teams Documentation](https://docs.microsoft.com/en-us/graph/api/resources/teams-api-overview)
- [Microsoft Graph API - Channel Messages](https://docs.microsoft.com/en-us/graph/api/channel-post-messages)
- [Microsoft Graph API - Chat Messages](https://docs.microsoft.com/en-us/graph/api/chat-post-messages)
- [MSAL Python Documentation](https://msal-python.readthedocs.io/)
- [Graph Explorer - Test API Calls](https://developer.microsoft.com/en-us/graph/graph-explorer)
- [Teams Developer Documentation](https://docs.microsoft.com/en-us/microsoftteams/platform/)

## Version Requirements

**Explicitly Required Versions:**

- **Python**: 3.9 or higher
  - Required for modern type hints (`List`, `Dict`, `Optional` from `typing`)
  - Required for dictionary merge operators and other Python 3.9+ features

- **msal**: 1.31.0 or higher
  - Provides `PublicClientApplication` class for authentication
  - Supports device code flow for CLI applications
  - Includes token caching and refresh capabilities

- **requests**: 2.32.0 or higher
  - Used for making HTTP requests to Microsoft Graph API
  - Version 2.32.0+ includes important security updates and bug fixes
  - Provides robust JSON handling and error reporting

The inline script metadata (lines 9-15 in the source code) ensures these dependencies are automatically installed when running the script with `uv run`.
