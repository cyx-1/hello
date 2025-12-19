# SharePoint Python API Example

This example demonstrates how to interact with Microsoft SharePoint using Python and the `Office365-REST-Python-Client` library.

## Overview

The `Office365-REST-Python-Client` library provides a comprehensive Python API for working with SharePoint Online and SharePoint 2013/2016/2019. This example showcases:

- **Authentication**: Multiple methods including user credentials, client credentials, and certificate-based authentication
- **Site Operations**: Retrieving site information and properties
- **List Management**: Creating, reading, and updating SharePoint lists and list items
- **File Operations**: Uploading, downloading, listing, and deleting files
- **Folder Management**: Creating and navigating folder structures
- **Search**: Querying SharePoint content
- **Permissions**: Managing and checking user permissions
- **Metadata**: Working with file and list item metadata
- **Version History**: Accessing file version information
- **Error Handling**: Best practices for handling SharePoint API errors

## Requirements

- **Python Version**: Python 3.8 or higher
- **Library Version**: Office365-REST-Python-Client >= 2.5.0
- **Note**: This example uses inline script metadata for dependency management with `uv`

## Running the Example

```bash
uv run main_sharepoint.py
```

The `uv` tool will automatically install the required dependencies based on the inline script metadata.

## Source Code

Below is the complete source code with line numbers for reference:

### Lines 1-15: Import Statements and Script Metadata

```python
1   #!/usr/bin/env python3
2   """
3   SharePoint API Python Example
4
5   This script demonstrates how to interact with SharePoint using the Office365-REST-Python-Client library.
6   It includes examples of authentication, file operations, and list management.
7
8   # /// script
9   # dependencies = [
10  #   "Office365-REST-Python-Client>=2.5.0",
11  #   "requests>=2.31.0"
12  # ]
13  # ///
14  """
15
16  from office365.sharepoint.client_context import ClientContext
17  from office365.runtime.auth.user_credential import UserCredential
18  from office365.runtime.auth.client_credential import ClientCredential
19  from office365.sharepoint.files.file import File
20  from office365.sharepoint.listitems.listitem import ListItem
21  from typing import Optional
22  import io
```

**Lines 8-13**: Inline script metadata declares dependencies for `uv` to automatically install. This eliminates the need for `pyproject.toml` or manual pip installations.

**Lines 16-22**: Import core SharePoint API classes including `ClientContext` for session management, authentication providers, and file/list item types.

### Lines 25-29: Utility Function

```python
25  def print_section(title: str) -> None:
26      """Print a formatted section header."""
27      print(f"\n{'=' * 60}")
28      print(f"  {title}")
29      print(f"{'=' * 60}\n")
```

**Line 25**: Helper function to create consistent section headers in the output, improving readability.

### Lines 32-59: Authentication Methods (Lines 32-59)

```python
32  def demo_authentication() -> None:
33      """Demonstrate different SharePoint authentication methods."""
34      print_section("1. SharePoint Authentication Methods")
35
36      # Method 1: User Credentials (username/password)
37      print("Method 1: User Credentials Authentication")
38      print("Code:")
39      print("  ctx = ClientContext(site_url).with_credentials(")
40      print("      UserCredential(username, password)")
41      print("  )")
42      print()
43
44      # Method 2: Client Credentials (App-Only)
45      print("Method 2: Client Credentials (App-Only)")
46      print("Code:")
47      print("  ctx = ClientContext(site_url).with_credentials(")
48      print("      ClientCredential(client_id, client_secret)")
49      print("  )")
```

**Lines 39-41**: Shows `UserCredential` authentication - suitable for interactive scenarios with username/password.

**Lines 47-49**: Shows `ClientCredential` (App-Only) authentication - ideal for background services and automation.

### Output: Authentication Section

```
============================================================
  1. SharePoint Authentication Methods
============================================================

Method 1: User Credentials Authentication
Code:
  ctx = ClientContext(site_url).with_credentials(
      UserCredential(username, password)
  )

Method 2: Client Credentials (App-Only)
Code:
  ctx = ClientContext(site_url).with_credentials(
      ClientCredential(client_id, client_secret)
  )

Method 3: Certificate-Based Authentication
Code:
  from office365.runtime.auth.providers.saml_token_provider import SamlTokenProvider
  ctx = ClientContext(site_url).with_credentials(
      SamlTokenProvider(username, password)
  )

✓ Authentication methods overview completed
```

**Output Annotation**: The demonstration covers three authentication approaches, giving developers flexibility to choose based on their security requirements and deployment scenarios.

### Lines 62-84: Site Information (Lines 62-84)

```python
62  def demo_site_information() -> None:
63      """Demonstrate how to get SharePoint site information."""
64      print_section("2. Getting SharePoint Site Information")
65
66      print("Example: Retrieve site properties")
67      print("Code:")
68      print("  web = ctx.web")
69      print("  ctx.load(web)")
70      print("  ctx.execute_query()")
71      print("  print(f'Site Title: {web.properties[\"Title\"]}')")
72      print("  print(f'Site URL: {web.properties[\"Url\"]}')")
```

**Lines 68-70**: Demonstrates the standard pattern for SharePoint operations:
1. Get the object (`ctx.web`)
2. Load it (`ctx.load(web)`)
3. Execute the query (`ctx.execute_query()`)

**Lines 71-72**: Access properties via the `properties` dictionary after query execution.

### Output: Site Information Section

```
============================================================
  2. Getting SharePoint Site Information
============================================================

Example: Retrieve site properties
Code:
  web = ctx.web
  ctx.load(web)
  ctx.execute_query()
  print(f'Site Title: {web.properties["Title"]}')
  print(f'Site URL: {web.properties["Url"]}')

Sample Output:
  Site Title: Contoso Team Site
  Site URL: https://contoso.sharepoint.com/sites/team
  Description: Main collaboration site

✓ Site information retrieval demonstrated
```

**Output Annotation**: Shows how to retrieve basic site metadata, which is often the first operation after authentication.

### Lines 87-145: List Operations (Lines 87-145)

```python
99   print("Example 1: Get all lists in site")
100  print("Code:")
101  print("  lists = ctx.web.lists")
102  print("  ctx.load(lists)")
103  print("  ctx.execute_query()")
104  print("  for lst in lists:")
105  print("      print(f'List: {lst.properties[\"Title\"]} (Items: {lst.properties[\"ItemCount\"]})')")
```

**Lines 101-105**: Demonstrates retrieving all lists in a site and iterating through them.

```python
117  print("Example 2: Get items from a specific list")
118  print("Code:")
119  print("  list_obj = ctx.web.lists.get_by_title('Tasks')")
120  print("  items = list_obj.items")
121  print("  ctx.load(items)")
122  print("  ctx.execute_query()")
123  print("  for item in items:")
124  print("      print(f'Task: {item.properties[\"Title\"]} - Status: {item.properties[\"Status\"]}')")
```

**Line 119**: Shows how to get a specific list by title using `get_by_title()`.

**Lines 120-124**: Demonstrates retrieving and iterating through list items.

```python
135  print("Example 3: Create a new list item")
136  print("Code:")
137  print("  list_obj = ctx.web.lists.get_by_title('Tasks')")
138  print("  item_properties = {")
139  print("      'Title': 'New Task',")
140  print("      'Status': 'Not Started',")
141  print("      'Priority': 'High'")
142  print("  }")
143  print("  new_item = list_obj.add_item(item_properties)")
144  print("  ctx.execute_query()")
145  print("  print(f'Created item with ID: {new_item.properties[\"Id\"]}')")
```

**Lines 138-142**: Create item properties as a dictionary with field names and values.

**Line 143**: Use `add_item()` to create a new list item.

### Output: List Operations Section

```
============================================================
  3. Working with SharePoint Lists
============================================================

Example 1: Get all lists in site
Code:
  lists = ctx.web.lists
  ctx.load(lists)
  ctx.execute_query()
  for lst in lists:
      print(f'List: {lst.properties["Title"]} (Items: {lst.properties["ItemCount"]})')

Sample Output:
  List: Documents (Items: 42)
  List: Tasks (Items: 15)
  List: Announcements (Items: 8)

Example 2: Get items from a specific list
Code:
  list_obj = ctx.web.lists.get_by_title('Tasks')
  items = list_obj.items
  ctx.load(items)
  ctx.execute_query()
  for item in items:
      print(f'Task: {item.properties["Title"]} - Status: {item.properties["Status"]}')

Sample Output:
  Task: Update documentation - Status: In Progress
  Task: Review code changes - Status: Completed
  Task: Deploy to production - Status: Not Started

Example 3: Create a new list item
Code:
  list_obj = ctx.web.lists.get_by_title('Tasks')
  item_properties = {
      'Title': 'New Task',
      'Status': 'Not Started',
      'Priority': 'High'
  }
  new_item = list_obj.add_item(item_properties)
  ctx.execute_query()
  print(f'Created item with ID: {new_item.properties["Id"]}')

Sample Output:
  Created item with ID: 16

✓ List operations demonstrated
```

**Output Annotation**: The list operations section shows the three most common list operations: reading all lists (useful for discovery), querying specific list items (for data retrieval), and creating new items (for data insertion).

### Lines 148-234: File Operations (Lines 148-234)

```python
158  print("Example 1: Upload a file")
159  print("Code:")
160  print("  target_folder = ctx.web.get_folder_by_server_relative_url('/sites/team/Shared Documents')")
161  print("  with open('report.pdf', 'rb') as file_content:")
162  print("      target_file = target_folder.upload_file('report.pdf', file_content)")
163  print("      ctx.execute_query()")
164  print("  print(f'File uploaded: {target_file.properties[\"Name\"]}')")
```

**Line 160**: Use `get_folder_by_server_relative_url()` with server-relative paths (starting with `/sites/`).

**Line 162**: Upload files using `upload_file()` with file name and binary content.

```python
176  print("Example 2: List files in a folder")
177  print("Code:")
178  print("  folder = ctx.web.get_folder_by_server_relative_url('/sites/team/Shared Documents')")
179  print("  files = folder.files")
180  print("  ctx.load(files)")
181  print("  ctx.execute_query()")
182  print("  for file in files:")
183  print("      print(f'File: {file.properties[\"Name\"]} ({file.properties[\"Length\"]} bytes)')")
```

**Lines 179-183**: List all files in a folder, accessing properties like `Name` and `Length`.

```python
194  print("Example 3: Download a file")
195  print("Code:")
196  print("  file_url = '/sites/team/Shared Documents/report.pdf'")
197  print("  file = ctx.web.get_file_by_server_relative_url(file_url)")
198  print("  content = file.read()")
199  print("  ctx.execute_query()")
200  print("  with open('downloaded_report.pdf', 'wb') as local_file:")
201  print("      local_file.write(content.value)")
202  print("  print(f'Downloaded {len(content.value)} bytes')")
```

**Line 198**: Use `file.read()` to download file content.

**Line 201**: Access the binary content via `content.value`.

### Output: File Operations Section

```
============================================================
  4. Working with Files in Document Libraries
============================================================

Example 1: Upload a file
Code:
  target_folder = ctx.web.get_folder_by_server_relative_url('/sites/team/Shared Documents')
  with open('report.pdf', 'rb') as file_content:
      target_file = target_folder.upload_file('report.pdf', file_content)
      ctx.execute_query()
  print(f'File uploaded: {target_file.properties["Name"]}')

Sample Output:
  File uploaded: report.pdf
  Server Relative URL: /sites/team/Shared Documents/report.pdf

Example 2: List files in a folder
Code:
  folder = ctx.web.get_folder_by_server_relative_url('/sites/team/Shared Documents')
  files = folder.files
  ctx.load(files)
  ctx.execute_query()
  for file in files:
      print(f'File: {file.properties["Name"]} ({file.properties["Length"]} bytes)')

Sample Output:
  File: report.pdf (1,245,632 bytes)
  File: presentation.pptx (3,456,789 bytes)
  File: data.xlsx (524,288 bytes)

Example 3: Download a file
Code:
  file_url = '/sites/team/Shared Documents/report.pdf'
  file = ctx.web.get_file_by_server_relative_url(file_url)
  content = file.read()
  ctx.execute_query()
  with open('downloaded_report.pdf', 'wb') as local_file:
      local_file.write(content.value)
  print(f'Downloaded {len(content.value)} bytes')

Sample Output:
  Downloaded 1245632 bytes
  File saved as: downloaded_report.pdf
```

**Output Annotation**: File operations are critical for document management. The examples show the complete lifecycle: uploading new files, discovering existing files, downloading files for local processing, and managing file metadata.

### Lines 311-336: Metadata Operations (Lines 311-336)

```python
318  print("Example 1: Update file metadata")
319  print("Code:")
320  print("  file = ctx.web.get_file_by_server_relative_url('/sites/team/Shared Documents/report.pdf')")
321  print("  list_item = file.listItemAllFields")
322  print("  list_item.set_property('Category', 'Financial')")
323  print("  list_item.set_property('Status', 'Approved')")
324  print("  list_item.update()")
325  print("  ctx.execute_query()")
326  print("  print('Metadata updated successfully')")
```

**Line 321**: Access file metadata through `listItemAllFields` property.

**Lines 322-323**: Set custom metadata fields using `set_property()`.

**Line 324**: Call `update()` before `execute_query()` to persist changes.

### Output: Metadata Section

```
============================================================
  8. Working with Metadata and Properties
============================================================

Example 1: Update file metadata
Code:
  file = ctx.web.get_file_by_server_relative_url('/sites/team/Shared Documents/report.pdf')
  list_item = file.listItemAllFields
  list_item.set_property('Category', 'Financial')
  list_item.set_property('Status', 'Approved')
  list_item.update()
  ctx.execute_query()
  print('Metadata updated successfully')

Sample Output:
  Metadata updated successfully
  Category: Financial
  Status: Approved
```

**Output Annotation**: Metadata management is essential for document classification and searchability in SharePoint.

### Lines 378-397: Error Handling (Lines 378-397)

```python
381  print("Example: Proper error handling")
382  print("Code:")
383  print("  try:")
384  print("      file = ctx.web.get_file_by_server_relative_url(file_url)")
385  print("      ctx.load(file)")
386  print("      ctx.execute_query()")
387  print("      print(f'File found: {file.properties[\"Name\"]}')")
388  print("  except Exception as e:")
389  print("      if '404' in str(e):")
390  print("          print(f'File not found: {file_url}')")
391  print("      elif '403' in str(e):")
392  print("          print(f'Access denied: {file_url}')")
393  print("      else:")
394  print("          print(f'Error: {e}')")
```

**Lines 383-394**: Demonstrates proper exception handling for SharePoint API calls, checking for common HTTP status codes (404 for not found, 403 for access denied).

### Output: Error Handling Section

```
============================================================
  10. Error Handling Best Practices
============================================================

Example: Proper error handling
Code:
  try:
      file = ctx.web.get_file_by_server_relative_url(file_url)
      ctx.load(file)
      ctx.execute_query()
      print(f'File found: {file.properties["Name"]}')
  except Exception as e:
      if '404' in str(e):
          print(f'File not found: {file_url}')
      elif '403' in str(e):
          print(f'Access denied: {file_url}')
      else:
          print(f'Error: {e}')

Sample Output (file not found):
  File not found: /sites/team/Shared Documents/missing.pdf

Sample Output (access denied):
  Access denied: /sites/team/Confidential/secret.pdf

✓ Error handling demonstrated
```

**Output Annotation**: Production code should always include robust error handling to gracefully handle network issues, permission problems, and missing resources.

### Lines 400-445: Main Function and Summary

```python
400  def main() -> None:
401      """Main function to run all SharePoint API demonstrations."""
402      print("\n" + "=" * 60)
403      print("  SharePoint Python API Demonstration")
404      print("  Using Office365-REST-Python-Client Library")
405      print("=" * 60)
```

**Lines 400-405**: Main entry point that orchestrates all demonstrations.

### Output: Summary Section

```
============================================================
  Summary
============================================================

✓ All SharePoint API operations demonstrated successfully!

Key Takeaways:
  1. Office365-REST-Python-Client supports multiple authentication methods
  2. All operations follow a pattern: get object → load → execute_query()
  3. File operations require server-relative URLs
  4. Metadata is accessed through listItemAllFields property
  5. Always implement proper error handling for production code

Next Steps:
  • Replace demo credentials with actual SharePoint credentials
  • Adjust site URLs to match your SharePoint environment
  • Implement required business logic
  • Add comprehensive error handling and logging
  • Consider implementing retry logic for network operations

Documentation: https://github.com/vgrem/Office365-REST-Python-Client
```

**Output Annotation**: The summary provides actionable next steps for developers to adapt this example to their specific SharePoint environment.

## Key Concepts

### The SharePoint API Pattern

All SharePoint operations follow a consistent three-step pattern:

1. **Get the object**: Retrieve the SharePoint object (web, list, file, folder)
2. **Load**: Mark the object for loading with `ctx.load(object)`
3. **Execute**: Execute the query with `ctx.execute_query()`

This pattern optimizes network calls by batching multiple operations together.

### Server-Relative URLs

SharePoint uses server-relative URLs for identifying resources. These always start with `/sites/` or `/` and include the full path to the resource:

- `/sites/team/Shared Documents` - Folder path
- `/sites/team/Shared Documents/report.pdf` - File path

### Metadata Management

Files in SharePoint are actually list items with attached content. To access or modify metadata:

1. Get the file object
2. Access `file.listItemAllFields`
3. Use `set_property()` to update fields
4. Call `update()` and `execute_query()`

## Authentication Setup

For production use, you'll need to configure authentication:

### User Credentials

```python
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

site_url = "https://your-tenant.sharepoint.com/sites/your-site"
username = "user@your-tenant.com"
password = "your-password"

ctx = ClientContext(site_url).with_credentials(
    UserCredential(username, password)
)
```

### App-Only (Client Credentials)

1. Register an application in Azure AD
2. Grant SharePoint API permissions
3. Create a client secret
4. Use the credentials:

```python
from office365.runtime.auth.client_credential import ClientCredential

client_id = "your-client-id"
client_secret = "your-client-secret"

ctx = ClientContext(site_url).with_credentials(
    ClientCredential(client_id, client_secret)
)
```

## Common Use Cases

1. **Document Management**: Upload reports, download templates, organize files
2. **Workflow Automation**: Create tasks, update statuses, track progress
3. **Data Integration**: Extract SharePoint data to other systems
4. **Content Migration**: Bulk upload/download operations
5. **Metadata Management**: Classify and tag documents

## Troubleshooting

### Common Issues

1. **Authentication Errors (401/403)**:
   - Verify credentials are correct
   - Check user has appropriate permissions
   - Ensure app registration is configured correctly

2. **File Not Found (404)**:
   - Verify server-relative URL is correct
   - Check file/folder exists
   - Ensure proper URL encoding for special characters

3. **Permission Errors**:
   - User needs at least read access for queries
   - Contribute access required for uploads
   - Full control needed for permission management

## Resources

- **Library Documentation**: https://github.com/vgrem/Office365-REST-Python-Client
- **SharePoint REST API**: https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/get-to-know-the-sharepoint-rest-service
- **Azure AD App Registration**: https://learn.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app

## Version Information

- **Python**: Requires Python 3.8 or higher
- **Library**: Office365-REST-Python-Client 2.5.0 or higher
- **SharePoint**: Compatible with SharePoint Online and SharePoint 2013/2016/2019

---

*Last updated: 2024-01-20*
