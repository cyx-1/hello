#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "requests>=2.31.0",
# ]
# ///

"""
Confluence Wiki API Python Example

This script demonstrates how to interact with Confluence's REST API using Python.
It covers common operations like authentication, managing spaces, creating/updating pages,
searching content, and working with attachments.
"""

import json
import requests
from typing import Dict, Any, List, Optional


class ConfluenceClient:
    """A simple Confluence API client using requests library."""

    def __init__(self, base_url: str, email: str, api_token: str):
        """
        Initialize Confluence client with credentials.

        Args:
            base_url: Confluence instance URL (e.g., 'https://your-domain.atlassian.net/wiki')
            email: Your Confluence account email
            api_token: API token generated from Atlassian account settings
        """
        self.base_url = base_url.rstrip('/')
        self.auth = (email, api_token)
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_space(self, space_key: str) -> Dict[str, Any]:
        """
        Get details of a specific Confluence space.

        Args:
            space_key: Space key (e.g., 'DEMO')

        Returns:
            Dictionary containing space details
        """
        url = f"{self.base_url}/rest/api/space/{space_key}"
        response = requests.get(url, headers=self.headers, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def get_all_spaces(self, limit: int = 25) -> Dict[str, Any]:
        """
        Get all spaces in the Confluence instance.

        Args:
            limit: Maximum number of spaces to return

        Returns:
            Dictionary containing list of spaces
        """
        url = f"{self.base_url}/rest/api/space"
        params = {"limit": limit}
        response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
        response.raise_for_status()
        return response.json()

    def get_page(self, page_id: str, expand: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Get details of a specific page.

        Args:
            page_id: Page ID
            expand: List of properties to expand (e.g., ['body.storage', 'version'])

        Returns:
            Dictionary containing page details
        """
        url = f"{self.base_url}/rest/api/content/{page_id}"
        params = {}
        if expand:
            params['expand'] = ','.join(expand)
        response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
        response.raise_for_status()
        return response.json()

    def get_page_by_title(self, space_key: str, title: str) -> Optional[Dict[str, Any]]:
        """
        Get a page by its title within a space.

        Args:
            space_key: Space key
            title: Page title

        Returns:
            Dictionary containing page details or None if not found
        """
        url = f"{self.base_url}/rest/api/content"
        params = {
            "spaceKey": space_key,
            "title": title,
            "expand": "body.storage,version"
        }
        response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
        response.raise_for_status()
        results = response.json()
        if results['results']:
            return results['results'][0]
        return None

    def create_page(self, space_key: str, title: str, body: str,
                    parent_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new Confluence page.

        Args:
            space_key: Space key where page will be created
            title: Page title
            body: Page content in storage format (HTML)
            parent_id: Optional parent page ID

        Returns:
            Dictionary containing created page details
        """
        url = f"{self.base_url}/rest/api/content"
        payload = {
            "type": "page",
            "title": title,
            "space": {"key": space_key},
            "body": {
                "storage": {
                    "value": body,
                    "representation": "storage"
                }
            }
        }
        if parent_id:
            payload["ancestors"] = [{"id": parent_id}]

        response = requests.post(url, headers=self.headers, auth=self.auth,
                                data=json.dumps(payload))
        response.raise_for_status()
        return response.json()

    def update_page(self, page_id: str, title: str, body: str, version: int) -> Dict[str, Any]:
        """
        Update an existing Confluence page.

        Args:
            page_id: Page ID to update
            title: New page title
            body: New page content in storage format (HTML)
            version: Current version number + 1

        Returns:
            Dictionary containing updated page details
        """
        url = f"{self.base_url}/rest/api/content/{page_id}"
        payload = {
            "type": "page",
            "title": title,
            "body": {
                "storage": {
                    "value": body,
                    "representation": "storage"
                }
            },
            "version": {"number": version}
        }
        response = requests.put(url, headers=self.headers, auth=self.auth,
                               data=json.dumps(payload))
        response.raise_for_status()
        return response.json()

    def delete_page(self, page_id: str) -> None:
        """
        Delete a Confluence page.

        Args:
            page_id: Page ID to delete
        """
        url = f"{self.base_url}/rest/api/content/{page_id}"
        response = requests.delete(url, headers=self.headers, auth=self.auth)
        response.raise_for_status()

    def search_content(self, cql: str, limit: int = 25) -> Dict[str, Any]:
        """
        Search for content using CQL (Confluence Query Language).

        Args:
            cql: CQL query string
            limit: Maximum number of results

        Returns:
            Dictionary containing search results
        """
        url = f"{self.base_url}/rest/api/content/search"
        params = {
            "cql": cql,
            "limit": limit
        }
        response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
        response.raise_for_status()
        return response.json()

    def get_page_children(self, page_id: str, expand: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Get child pages of a specific page.

        Args:
            page_id: Parent page ID
            expand: List of properties to expand

        Returns:
            Dictionary containing child pages
        """
        url = f"{self.base_url}/rest/api/content/{page_id}/child/page"
        params = {}
        if expand:
            params['expand'] = ','.join(expand)
        response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
        response.raise_for_status()
        return response.json()


def demonstrate_confluence_api():
    """Demonstrate various Confluence API operations."""

    # Configuration (replace with your actual credentials)
    # For security, use environment variables in production
    CONFLUENCE_URL = "https://your-domain.atlassian.net/wiki"
    EMAIL = "your-email@example.com"
    API_TOKEN = "your-api-token-here"

    print("=" * 70)
    print("Confluence Wiki API Python Example")
    print("=" * 70)

    # Initialize the Confluence client
    print("\n[1] Initializing Confluence client...")
    print(f"    Base URL: {CONFLUENCE_URL}")
    print(f"    Email: {EMAIL}")
    client = ConfluenceClient(CONFLUENCE_URL, EMAIL, API_TOKEN)

    # Example 1: Get all spaces
    print("\n[2] Fetching all spaces...")
    try:
        spaces = client.get_all_spaces(limit=5)
        print(f"    Total spaces: {spaces.get('size', 0)}")
        for space in spaces.get('results', []):
            print(f"    - {space['key']}: {space['name']}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 2: Get specific space details
    print("\n[3] Fetching space details...")
    try:
        space = client.get_space("DEMO")
        print(f"    Space Key: {space.get('key')}")
        print(f"    Space Name: {space.get('name')}")
        print(f"    Space Type: {space.get('type')}")
        print(f"    Space URL: {CONFLUENCE_URL}/spaces/{space.get('key')}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 3: Search for pages using CQL
    print("\n[4] Searching content with CQL...")
    try:
        cql_query = "type=page AND space=DEMO ORDER BY created DESC"
        print(f"    CQL: {cql_query}")
        results = client.search_content(cql_query, limit=5)
        print(f"    Total found: {results.get('totalSize', 0)}")
        print(f"    Returned: {len(results.get('results', []))}")
        for idx, page in enumerate(results.get('results', []), 1):
            print(f"    [{idx}] {page['id']}: {page['title']}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 4: Get page by title
    print("\n[5] Fetching page by title...")
    try:
        page = client.get_page_by_title("DEMO", "Home")
        if page:
            print(f"    Page ID: {page['id']}")
            print(f"    Page Title: {page['title']}")
            print(f"    Page Version: {page['version']['number']}")
            print(f"    Last Modified: {page['version']['when']}")
            print(f"    Modified By: {page['version']['by']['displayName']}")
        else:
            print("    Page not found")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 5: Create a new page
    print("\n[6] Creating a new page...")
    try:
        html_content = """
        <h1>Welcome to the API Test Page</h1>
        <p>This page was created using the Confluence REST API from Python.</p>
        <h2>Features Demonstrated</h2>
        <ul>
            <li>Page creation</li>
            <li>HTML content formatting</li>
            <li>API authentication</li>
        </ul>
        <p><strong>Created at:</strong> Using Python requests library</p>
        """
        new_page = client.create_page(
            space_key="DEMO",
            title="API Test Page - Python Example",
            body=html_content
        )
        print(f"    Created page ID: {new_page['id']}")
        print(f"    Page Title: {new_page['title']}")
        print(f"    Page URL: {CONFLUENCE_URL}/pages/viewpage.action?pageId={new_page['id']}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 6: Get page details with expanded properties
    print("\n[7] Fetching page with expanded properties...")
    try:
        page = client.get_page("123456", expand=['body.storage', 'version', 'space'])
        print(f"    Page ID: {page['id']}")
        print(f"    Page Title: {page['title']}")
        print(f"    Space: {page['space']['name']}")
        print(f"    Version: {page['version']['number']}")
        print(f"    Content length: {len(page['body']['storage']['value'])} characters")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 7: Update an existing page
    print("\n[8] Updating an existing page...")
    try:
        # First get the current page to get its version
        current_page = client.get_page_by_title("DEMO", "API Test Page - Python Example")
        if current_page:
            updated_content = """
            <h1>Updated API Test Page</h1>
            <p>This page was <strong>updated</strong> using the Confluence REST API.</p>
            <h2>Update Features</h2>
            <ul>
                <li>Version management</li>
                <li>Content replacement</li>
                <li>Automatic versioning</li>
            </ul>
            """
            updated_page = client.update_page(
                page_id=current_page['id'],
                title=current_page['title'],
                body=updated_content,
                version=current_page['version']['number'] + 1
            )
            print(f"    Updated page ID: {updated_page['id']}")
            print(f"    New version: {updated_page['version']['number']}")
        else:
            print("    Page not found for update")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 8: Get child pages
    print("\n[9] Fetching child pages...")
    try:
        children = client.get_page_children("123456")
        print(f"    Total child pages: {children.get('size', 0)}")
        for child in children.get('results', []):
            print(f"    - {child['id']}: {child['title']}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 9: Delete a page
    print("\n[10] Deleting a page...")
    try:
        page_to_delete = client.get_page_by_title("DEMO", "API Test Page - Python Example")
        if page_to_delete:
            client.delete_page(page_to_delete['id'])
            print(f"    Page '{page_to_delete['title']}' deleted successfully")
        else:
            print("    Page not found for deletion")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    print("\n" + "=" * 70)
    print("API Operations Completed")
    print("=" * 70)
    print("\nNote: This is a demonstration. Replace credentials with actual values.")
    print("For production use:")
    print("  - Store credentials in environment variables")
    print("  - Use proper error handling")
    print("  - Implement retry logic for network failures")
    print("  - Add rate limiting to respect API quotas")
    print("  - Validate content before creating/updating pages")


if __name__ == "__main__":
    demonstrate_confluence_api()
