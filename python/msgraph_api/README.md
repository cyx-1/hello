# Microsoft Graph API - Python Example

This example demonstrates how to authenticate and interact with Microsoft Graph API using Python, showcasing the device code flow authentication method and making API calls to retrieve user information and emails.

## Requirements

- **Python Version**: Python 3.9 or higher
- **Libraries**:
  - `msal` >= 1.31.0 (Microsoft Authentication Library)
  - `requests` >= 2.32.0

## Running the Example

```bash
uv run python python/msgraph_api/main_msgraph_api.py
```

## Key Source Code Sections

### 1. Authentication Configuration (Lines 19-25)

```python
19  # Microsoft Graph API configuration
20  CLIENT_ID = "14d82eec-204b-4c2f-b7e8-296a70dab67e"  # Public client ID for demo
21  TENANT_ID = "common"  # Use 'common' for multi-tenant, or specific tenant ID
22  AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
23  SCOPES = ["User.Read", "Mail.Read"]  # Permissions we're requesting
24  GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0"
```

**Lines 20-24** define the Microsoft identity platform configuration:
- `CLIENT_ID`: A public client ID for demonstration purposes
- `TENANT_ID`: Set to "common" to allow any Microsoft account (work/school or personal)
- `SCOPES`: Requests permissions to read user profile and emails

### 2. Device Code Flow Authentication (Lines 37-68)

```python
37  def authenticate_device_code_flow() -> Optional[Dict[str, Any]]:
38      """
39      Authenticate using device code flow.
40
41      This flow is ideal for devices without a browser or input-constrained devices.
42      The user needs to visit a URL and enter a code to authenticate.
43      """
44      # Line 37: Create a PublicClientApplication instance
45      app = msal.PublicClientApplication(
46          CLIENT_ID,
47          authority=AUTHORITY,
48      )
49
50      # Line 43: Initiate the device code flow
51      flow = app.initiate_device_flow(scopes=SCOPES)
52
53      if "user_code" not in flow:
54          print(f"❌ Failed to create device flow. Error: {json.dumps(flow, indent=2)}")
55          return None
56
57      # Line 49: Display instructions for user authentication
58      print("\n" + "=" * 70)
59      print("🔐 AUTHENTICATION REQUIRED")
60      print("=" * 70)
61      print(flow["message"])
62      print("=" * 70 + "\n")
63
64      # Line 56: Complete the device code flow by waiting for user authentication
65      result = app.acquire_token_by_device_flow(flow)
66
67      if "access_token" in result:
68          print("✅ Authentication successful!\n")
69          return result
```

**Line 45-48**: Creates a public client application with MSAL, which handles OAuth 2.0 authentication
**Line 51**: Initiates the device code flow, which generates a user code and verification URL
**Line 65**: Blocks until the user completes authentication in their browser, then retrieves the access token

### 3. Making Graph API Calls (Lines 78-98)

```python
78  def call_graph_api(endpoint: str, access_token: str) -> Optional[Dict[str, Any]]:
79      """
80      Make a GET request to Microsoft Graph API.
81
82      Args:
83          endpoint: The Graph API endpoint to call (e.g., '/me' or '/me/messages')
84          access_token: The OAuth access token for authentication
85
86      Returns:
87          JSON response from the API, or None if the request failed.
88      """
89      # Line 81: Prepare headers with the access token
90      headers = {
91          "Authorization": f"Bearer {access_token}",
92          "Content-Type": "application/json",
93      }
94
95      # Line 87: Make the API request
96      url = f"{GRAPH_API_ENDPOINT}{endpoint}"
97      response = requests.get(url, headers=headers)
98
99      if response.status_code == 200:
100         return response.json()
```

**Line 91**: Sets the authorization header with the Bearer token obtained from authentication
**Line 96-97**: Constructs the full URL and makes a GET request to the Graph API
**Line 99-100**: Returns the JSON response if successful

### 4. Main Execution Flow (Lines 143-184)

```python
143 def main() -> int:
144     """Main function to demonstrate Microsoft Graph API usage."""
145     print("\n" + "=" * 70)
146     print("Microsoft Graph API - Python Example")
147     print("=" * 70 + "\n")
148
149     # Line 147: Step 1 - Authenticate
150     print("Step 1: Authenticating...\n")
151     auth_result = authenticate_device_code_flow()
152
153     if not auth_result:
154         print("❌ Exiting due to authentication failure.\n")
155         return 1
156
157     access_token = auth_result["access_token"]
158
159     # Line 157: Step 2 - Get user profile
160     print("Step 2: Fetching user profile...\n")
161     profile = call_graph_api("/me", access_token)
162
163     if profile:
164         display_user_profile(profile)
165     else:
166         print("⚠️  Failed to fetch user profile.\n")
167
168     # Line 166: Step 3 - Get user's messages
169     print("Step 3: Fetching user's email messages...\n")
170     messages = call_graph_api(
171         "/me/messages?$top=5&$select=subject,from,receivedDateTime", access_token
172     )
173
174     if messages:
175         display_messages(messages)
176     else:
177         print("⚠️  Failed to fetch messages.\n")
```

**Line 151**: Initiates device code authentication
**Line 161**: Calls the `/me` endpoint to get the authenticated user's profile
**Line 170-171**: Calls the `/me/messages` endpoint with OData query parameters to get the top 5 messages

## Sample Output

### Phase 1: Authentication (corresponds to Lines 149-157)

```
======================================================================
Microsoft Graph API - Python Example
======================================================================

Step 1: Authenticating...

======================================================================
🔐 AUTHENTICATION REQUIRED
======================================================================
To sign in, use a web browser to open the page https://microsoft.com/devicelogin
and enter the code AB12CD34 to authenticate.
======================================================================

✅ Authentication successful!
```

**Output Annotation**: This corresponds to **lines 57-68** where the device code flow displays the authentication instructions. The user must:
1. Visit https://microsoft.com/devicelogin in a browser
2. Enter the code shown (e.g., "AB12CD34")
3. Sign in with their Microsoft account
4. The script waits until authentication completes

### Phase 2: User Profile Retrieval (corresponds to Lines 159-166)

```
Step 2: Fetching user profile...

👤 USER PROFILE
----------------------------------------------------------------------
   Display Name:      John Doe
   Email:             john.doe@contoso.com
   Job Title:         Senior Software Engineer
   Office Location:   Building 4
   User ID:           a1b2c3d4-e5f6-7890-abcd-ef1234567890
----------------------------------------------------------------------
```

**Output Annotation**: This output is generated by **lines 161-164**, which:
1. Call the Graph API `/me` endpoint (line 161) using the access token from line 157
2. Pass the response to `display_user_profile()` (line 164)
3. Display formatted user information from the Graph API response

The `/me` endpoint returns the authenticated user's profile information from Azure Active Directory.

### Phase 3: Email Messages Retrieval (corresponds to Lines 168-177)

```
Step 3: Fetching user's email messages...

📧 EMAIL MESSAGES (Showing first 5 messages)
----------------------------------------------------------------------

   [1] Subject: Quarterly Review Meeting
       From:     Sarah Johnson
       Received: 2025-01-15T14:30:22Z

   [2] Subject: Project Update - Q1 2025
       From:     Mike Williams
       Received: 2025-01-15T10:15:08Z

   [3] Subject: Team Lunch Tomorrow
       From:     Alice Brown
       Received: 2025-01-14T16:45:33Z

   [4] Subject: Code Review Request
       From:     Bob Smith
       Received: 2025-01-14T09:20:17Z

   [5] Subject: Welcome to Microsoft Graph!
       From:     Microsoft Graph Team
       Received: 2025-01-13T08:00:00Z

----------------------------------------------------------------------

======================================================================
✅ Microsoft Graph API demonstration completed successfully!
======================================================================
```

**Output Annotation**: This output is generated by **lines 170-176**, which:
1. Call the Graph API `/me/messages` endpoint (lines 170-171)
2. Use OData query parameters: `$top=5` to limit results and `$select` to specify fields
3. Pass the response to `display_messages()` (line 174)
4. Display the first 5 email messages with subject, sender, and received date

The OData query `$top=5&$select=subject,from,receivedDateTime` optimizes the API call by:
- Limiting results to 5 messages (`$top=5`)
- Requesting only the fields we need (`$select=...`) instead of the full message object

## How It Works

### Device Code Flow Authentication

The device code flow is a OAuth 2.0 authentication method ideal for:
- Command-line applications
- Devices without a web browser
- Input-constrained devices

**Process** (see lines 37-68):
1. Application requests a device code from Microsoft identity platform
2. User receives a code and URL
3. User navigates to the URL in any browser and enters the code
4. User authenticates and grants permissions
5. Application receives an access token

### Microsoft Graph API Calls

Once authenticated, the application uses the access token to make authorized requests:

1. **Get User Profile** (line 161): `GET /me`
   - Returns information about the signed-in user
   - Requires `User.Read` scope

2. **Get Messages** (lines 170-171): `GET /me/messages?$top=5&$select=subject,from,receivedDateTime`
   - Returns the user's email messages
   - Requires `Mail.Read` scope
   - Uses OData query parameters for filtering and pagination

### Error Handling

The example includes robust error handling:
- **Authentication failures** (lines 70-75): Display error details if authentication fails
- **API call failures** (lines 99-103): Check HTTP status codes and display error messages
- **Missing data handling** (throughout): Use `.get()` methods to safely access dictionary keys

## Security Notes

1. **Client ID**: The example uses a public client ID for demonstration. For production:
   - Register your own application in Azure AD
   - Use your own client ID
   - Configure appropriate redirect URIs

2. **Scopes**: Only request the minimum permissions needed:
   - `User.Read`: Read user profile
   - `Mail.Read`: Read user's mailbox

3. **Token Storage**: This example doesn't persist tokens. For production:
   - Use MSAL's token cache for better performance
   - Store tokens securely (encrypted storage)
   - Implement token refresh logic

## Additional Resources

- [Microsoft Graph API Documentation](https://docs.microsoft.com/en-us/graph/overview)
- [MSAL Python Documentation](https://msal-python.readthedocs.io/)
- [Device Code Flow Documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-device-code)
- [Graph Explorer (Test API calls)](https://developer.microsoft.com/en-us/graph/graph-explorer)

## Version Requirements

**Explicitly Required Versions:**

- **Python**: 3.9 or higher
  - Required for type hint features (`Dict`, `Optional`, etc.)

- **msal**: 1.31.0 or higher
  - Provides the `PublicClientApplication` and device code flow support
  - Earlier versions may have different API signatures

- **requests**: 2.32.0 or higher
  - Used for making HTTP requests to Graph API
  - Version 2.32.0+ includes important security updates

The inline script metadata (lines 8-13) ensures these dependencies are automatically installed when using `uv run`.
