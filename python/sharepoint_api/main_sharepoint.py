#!/usr/bin/env python3
"""
SharePoint API Python Example

This script demonstrates how to interact with SharePoint using the Office365-REST-Python-Client library.
It includes examples of authentication, file operations, and list management.

# /// script
# dependencies = [
#   "Office365-REST-Python-Client>=2.5.0",
#   "requests>=2.31.0"
# ]
# ///
"""


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 60}")
    print(f"  {title}")
    print(f"{'=' * 60}\n")


def demo_authentication() -> None:
    """Demonstrate different SharePoint authentication methods."""
    print_section("1. SharePoint Authentication Methods")

    # Method 1: User Credentials (username/password)
    print("Method 1: User Credentials Authentication")
    print("Code:")
    print("  ctx = ClientContext(site_url).with_credentials(")
    print("      UserCredential(username, password)")
    print("  )")
    print()

    # Method 2: Client Credentials (App-Only)
    print("Method 2: Client Credentials (App-Only)")
    print("Code:")
    print("  ctx = ClientContext(site_url).with_credentials(")
    print("      ClientCredential(client_id, client_secret)")
    print("  )")
    print()

    # Method 3: Certificate-based authentication
    print("Method 3: Certificate-Based Authentication")
    print("Code:")
    print(
        "  from office365.runtime.auth.providers.saml_token_provider import SamlTokenProvider"
    )
    print("  ctx = ClientContext(site_url).with_credentials(")
    print("      SamlTokenProvider(username, password)")
    print("  )")
    print()

    print("✓ Authentication methods overview completed")


def demo_site_information() -> None:
    """Demonstrate how to get SharePoint site information."""
    print_section("2. Getting SharePoint Site Information")

    print("Example: Retrieve site properties")
    print("Code:")
    print("  web = ctx.web")
    print("  ctx.load(web)")
    print("  ctx.execute_query()")
    print("  print(f'Site Title: {web.properties[\"Title\"]}')")
    print("  print(f'Site URL: {web.properties[\"Url\"]}')")
    print()

    print("Sample Output:")
    print("  Site Title: Contoso Team Site")
    print("  Site URL: https://contoso.sharepoint.com/sites/team")
    print("  Description: Main collaboration site")
    print()

    print("✓ Site information retrieval demonstrated")


def demo_list_operations() -> None:
    """Demonstrate SharePoint list operations."""
    print_section("3. Working with SharePoint Lists")

    print("Example 1: Get all lists in site")
    print("Code:")
    print("  lists = ctx.web.lists")
    print("  ctx.load(lists)")
    print("  ctx.execute_query()")
    print("  for lst in lists:")
    print(
        '      print(f\'List: {lst.properties["Title"]} (Items: {lst.properties["ItemCount"]})\')'
    )
    print()

    print("Sample Output:")
    print("  List: Documents (Items: 42)")
    print("  List: Tasks (Items: 15)")
    print("  List: Announcements (Items: 8)")
    print()

    print("Example 2: Get items from a specific list")
    print("Code:")
    print("  list_obj = ctx.web.lists.get_by_title('Tasks')")
    print("  items = list_obj.items")
    print("  ctx.load(items)")
    print("  ctx.execute_query()")
    print("  for item in items:")
    print(
        '      print(f\'Task: {item.properties["Title"]} - Status: {item.properties["Status"]}\')'
    )
    print()

    print("Sample Output:")
    print("  Task: Update documentation - Status: In Progress")
    print("  Task: Review code changes - Status: Completed")
    print("  Task: Deploy to production - Status: Not Started")
    print()

    print("Example 3: Create a new list item")
    print("Code:")
    print("  list_obj = ctx.web.lists.get_by_title('Tasks')")
    print("  item_properties = {")
    print("      'Title': 'New Task',")
    print("      'Status': 'Not Started',")
    print("      'Priority': 'High'")
    print("  }")
    print("  new_item = list_obj.add_item(item_properties)")
    print("  ctx.execute_query()")
    print("  print(f'Created item with ID: {new_item.properties[\"Id\"]}')")
    print()

    print("Sample Output:")
    print("  Created item with ID: 16")
    print()

    print("✓ List operations demonstrated")


def demo_file_operations() -> None:
    """Demonstrate SharePoint file operations."""
    print_section("4. Working with Files in Document Libraries")

    print("Example 1: Upload a file")
    print("Code:")
    print(
        "  target_folder = ctx.web.get_folder_by_server_relative_url('/sites/team/Shared Documents')"
    )
    print("  with open('report.pdf', 'rb') as file_content:")
    print("      target_file = target_folder.upload_file('report.pdf', file_content)")
    print("      ctx.execute_query()")
    print("  print(f'File uploaded: {target_file.properties[\"Name\"]}')")
    print()

    print("Sample Output:")
    print("  File uploaded: report.pdf")
    print("  Server Relative URL: /sites/team/Shared Documents/report.pdf")
    print()

    print("Example 2: List files in a folder")
    print("Code:")
    print(
        "  folder = ctx.web.get_folder_by_server_relative_url('/sites/team/Shared Documents')"
    )
    print("  files = folder.files")
    print("  ctx.load(files)")
    print("  ctx.execute_query()")
    print("  for file in files:")
    print(
        '      print(f\'File: {file.properties["Name"]} ({file.properties["Length"]} bytes)\')'
    )
    print()

    print("Sample Output:")
    print("  File: report.pdf (1,245,632 bytes)")
    print("  File: presentation.pptx (3,456,789 bytes)")
    print("  File: data.xlsx (524,288 bytes)")
    print()

    print("Example 3: Download a file")
    print("Code:")
    print("  file_url = '/sites/team/Shared Documents/report.pdf'")
    print("  file = ctx.web.get_file_by_server_relative_url(file_url)")
    print("  content = file.read()")
    print("  ctx.execute_query()")
    print("  with open('downloaded_report.pdf', 'wb') as local_file:")
    print("      local_file.write(content.value)")
    print("  print(f'Downloaded {len(content.value)} bytes')")
    print()

    print("Sample Output:")
    print("  Downloaded 1245632 bytes")
    print("  File saved as: downloaded_report.pdf")
    print()

    print("Example 4: Get file properties and metadata")
    print("Code:")
    print("  file_url = '/sites/team/Shared Documents/report.pdf'")
    print("  file = ctx.web.get_file_by_server_relative_url(file_url)")
    print("  ctx.load(file)")
    print("  ctx.execute_query()")
    print("  print(f'Name: {file.properties[\"Name\"]}')")
    print("  print(f'Size: {file.properties[\"Length\"]} bytes')")
    print("  print(f'Created: {file.properties[\"TimeCreated\"]}')")
    print("  print(f'Modified: {file.properties[\"TimeLastModified\"]}')")
    print()

    print("Sample Output:")
    print("  Name: report.pdf")
    print("  Size: 1245632 bytes")
    print("  Created: 2024-01-15T10:30:00Z")
    print("  Modified: 2024-01-20T14:45:00Z")
    print()

    print("Example 5: Delete a file")
    print("Code:")
    print("  file_url = '/sites/team/Shared Documents/old_report.pdf'")
    print("  file = ctx.web.get_file_by_server_relative_url(file_url)")
    print("  file.delete_object()")
    print("  ctx.execute_query()")
    print("  print('File deleted successfully')")
    print()

    print("Sample Output:")
    print("  File deleted successfully")
    print()

    print("✓ File operations demonstrated")


def demo_folder_operations() -> None:
    """Demonstrate SharePoint folder operations."""
    print_section("5. Working with Folders")

    print("Example 1: Create a new folder")
    print("Code:")
    print(
        "  parent_folder = ctx.web.get_folder_by_server_relative_url('/sites/team/Shared Documents')"
    )
    print("  new_folder = parent_folder.folders.add('2024_Reports')")
    print("  ctx.execute_query()")
    print("  print(f'Folder created: {new_folder.properties[\"Name\"]}')")
    print()

    print("Sample Output:")
    print("  Folder created: 2024_Reports")
    print("  Server Relative URL: /sites/team/Shared Documents/2024_Reports")
    print()

    print("Example 2: List all folders")
    print("Code:")
    print(
        "  folder = ctx.web.get_folder_by_server_relative_url('/sites/team/Shared Documents')"
    )
    print("  subfolders = folder.folders")
    print("  ctx.load(subfolders)")
    print("  ctx.execute_query()")
    print("  for subfolder in subfolders:")
    print("      print(f'Folder: {subfolder.properties[\"Name\"]}')")
    print()

    print("Sample Output:")
    print("  Folder: 2024_Reports")
    print("  Folder: Templates")
    print("  Folder: Archive")
    print()

    print("✓ Folder operations demonstrated")


def demo_search() -> None:
    """Demonstrate SharePoint search functionality."""
    print_section("6. SharePoint Search")

    print("Example: Search for documents")
    print("Code:")
    print("  from office365.sharepoint.search.query.query import SearchQuery")
    print("  search = ctx.search()")
    print('  query_text = "filetype:pdf status:approved"')
    print("  result = search.query(query_text)")
    print("  ctx.execute_query()")
    print("  for row in result.PrimaryQueryResult.RelevantResults.Table.Rows:")
    print('      print(f\'Title: {row.Cells["Title"]} - Path: {row.Cells["Path"]}\')')
    print()

    print("Sample Output:")
    print(
        "  Title: Q4 Financial Report - Path: /sites/team/Shared Documents/report_q4.pdf"
    )
    print(
        "  Title: Annual Review 2023 - Path: /sites/team/Shared Documents/annual_2023.pdf"
    )
    print()

    print("✓ Search functionality demonstrated")


def demo_permissions() -> None:
    """Demonstrate SharePoint permissions management."""
    print_section("7. Managing Permissions")

    print("Example 1: Get current user permissions")
    print("Code:")
    print("  current_user = ctx.web.current_user")
    print("  ctx.load(current_user)")
    print("  ctx.execute_query()")
    print("  print(f'Current User: {current_user.properties[\"Title\"]}')")
    print("  print(f'Email: {current_user.properties[\"Email\"]}')")
    print()

    print("Sample Output:")
    print("  Current User: John Doe")
    print("  Email: john.doe@contoso.com")
    print()

    print("Example 2: Check user permissions on a file")
    print("Code:")
    print(
        "  file = ctx.web.get_file_by_server_relative_url('/sites/team/Shared Documents/report.pdf')"
    )
    print("  list_item = file.listItemAllFields")
    print("  permissions = list_item.get_user_effective_permissions(user_email)")
    print("  ctx.execute_query()")
    print("  print(f'Can Edit: {permissions.has(PermissionKind.EditListItems)}')")
    print("  print(f'Can Delete: {permissions.has(PermissionKind.DeleteListItems)}')")
    print()

    print("Sample Output:")
    print("  Can Edit: True")
    print("  Can Delete: False")
    print()

    print("✓ Permissions management demonstrated")


def demo_metadata() -> None:
    """Demonstrate working with SharePoint metadata."""
    print_section("8. Working with Metadata and Properties")

    print("Example 1: Update file metadata")
    print("Code:")
    print(
        "  file = ctx.web.get_file_by_server_relative_url('/sites/team/Shared Documents/report.pdf')"
    )
    print("  list_item = file.listItemAllFields")
    print("  list_item.set_property('Category', 'Financial')")
    print("  list_item.set_property('Status', 'Approved')")
    print("  list_item.update()")
    print("  ctx.execute_query()")
    print("  print('Metadata updated successfully')")
    print()

    print("Sample Output:")
    print("  Metadata updated successfully")
    print("  Category: Financial")
    print("  Status: Approved")
    print()

    print("Example 2: Read file metadata")
    print("Code:")
    print(
        "  file = ctx.web.get_file_by_server_relative_url('/sites/team/Shared Documents/report.pdf')"
    )
    print("  list_item = file.listItemAllFields")
    print("  ctx.load(list_item)")
    print("  ctx.execute_query()")
    print("  print(f'Title: {list_item.properties[\"Title\"]}')")
    print("  print(f'Category: {list_item.properties[\"Category\"]}')")
    print("  print(f'Status: {list_item.properties[\"Status\"]}')")
    print()

    print("Sample Output:")
    print("  Title: Q4 Financial Report")
    print("  Category: Financial")
    print("  Status: Approved")
    print()

    print("✓ Metadata operations demonstrated")


def demo_version_history() -> None:
    """Demonstrate working with file version history."""
    print_section("9. File Version History")

    print("Example: Get version history of a file")
    print("Code:")
    print(
        "  file = ctx.web.get_file_by_server_relative_url('/sites/team/Shared Documents/report.pdf')"
    )
    print("  versions = file.versions")
    print("  ctx.load(versions)")
    print("  ctx.execute_query()")
    print("  for version in versions:")
    print("      print(f'Version {version.properties[\"VersionLabel\"]} - '")
    print("            f'Modified by {version.properties[\"CreatedBy\"]} - '")
    print("            f'{version.properties[\"Created\"]}')")
    print()

    print("Sample Output:")
    print("  Version 1.0 - Modified by john.doe@contoso.com - 2024-01-15T10:30:00Z")
    print("  Version 2.0 - Modified by jane.smith@contoso.com - 2024-01-18T14:20:00Z")
    print("  Version 3.0 - Modified by john.doe@contoso.com - 2024-01-20T14:45:00Z")
    print()

    print("✓ Version history operations demonstrated")


def demo_error_handling() -> None:
    """Demonstrate error handling best practices."""
    print_section("10. Error Handling Best Practices")

    print("Example: Proper error handling")
    print("Code:")
    print("  try:")
    print("      file = ctx.web.get_file_by_server_relative_url(file_url)")
    print("      ctx.load(file)")
    print("      ctx.execute_query()")
    print("      print(f'File found: {file.properties[\"Name\"]}')")
    print("  except Exception as e:")
    print("      if '404' in str(e):")
    print("          print(f'File not found: {file_url}')")
    print("      elif '403' in str(e):")
    print("          print(f'Access denied: {file_url}')")
    print("      else:")
    print("          print(f'Error: {e}')")
    print()

    print("Sample Output (file not found):")
    print("  File not found: /sites/team/Shared Documents/missing.pdf")
    print()

    print("Sample Output (access denied):")
    print("  Access denied: /sites/team/Confidential/secret.pdf")
    print()

    print("✓ Error handling demonstrated")


def main() -> None:
    """Main function to run all SharePoint API demonstrations."""
    print("\n" + "=" * 60)
    print("  SharePoint Python API Demonstration")
    print("  Using Office365-REST-Python-Client Library")
    print("=" * 60)
    print("\nThis demonstration shows various SharePoint operations:")
    print("  • Authentication methods")
    print("  • Site information retrieval")
    print("  • List operations (create, read, update)")
    print("  • File operations (upload, download, delete)")
    print("  • Folder management")
    print("  • Search functionality")
    print("  • Permissions management")
    print("  • Metadata handling")
    print("  • Version history")
    print("  • Error handling")
    print()

    # Run all demonstrations
    demo_authentication()
    demo_site_information()
    demo_list_operations()
    demo_file_operations()
    demo_folder_operations()
    demo_search()
    demo_permissions()
    demo_metadata()
    demo_version_history()
    demo_error_handling()

    print_section("Summary")
    print("✓ All SharePoint API operations demonstrated successfully!")
    print()
    print("Key Takeaways:")
    print("  1. Office365-REST-Python-Client supports multiple authentication methods")
    print("  2. All operations follow a pattern: get object → load → execute_query()")
    print("  3. File operations require server-relative URLs")
    print("  4. Metadata is accessed through listItemAllFields property")
    print("  5. Always implement proper error handling for production code")
    print()
    print("Next Steps:")
    print("  • Replace demo credentials with actual SharePoint credentials")
    print("  • Adjust site URLs to match your SharePoint environment")
    print("  • Implement required business logic")
    print("  • Add comprehensive error handling and logging")
    print("  • Consider implementing retry logic for network operations")
    print()
    print("Documentation: https://github.com/vgrem/Office365-REST-Python-Client")
    print()


if __name__ == "__main__":
    main()
