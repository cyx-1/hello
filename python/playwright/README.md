# Playwright Python UI Testing Demo

This example demonstrates how to use Playwright for automated UI testing in Python, showcasing browser automation, element interaction, form filling, assertions, and advanced testing techniques.

## Requirements

- **Python Version**: Python 3.10 or higher
- **Library**: Playwright 1.40.0 or higher
- **Playwright Browsers**: Must install Playwright browsers before running

## Installation

```bash
# Install Playwright browsers (required before first run)
uv run --with playwright playwright install chromium

# Run the script
uv run main_playwright.py
```

## Source Code Overview

### Key Imports and Setup (Lines 1-23)

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "playwright>=1.40.0",
# ]
# ///

import os
from playwright.sync_api import sync_playwright, expect

def get_test_page_url():
    """Get the file URL for the local test page."""
    test_page_path = os.path.join(os.path.dirname(__file__), "test_page.html")
    return f"file://{test_page_path}"
```

**Lines 2-7**: Inline script metadata defines Python version and dependencies using PEP 723 format.
**Lines 16-17**: Import Playwright's synchronous API and expect for assertions.
**Lines 20-23**: Helper function to get the local HTML test page URL.

### Test 1: Basic Navigation (Lines 26-66)

```python
def test_basic_navigation():
    """Test basic navigation and page title verification."""
    with sync_playwright() as p:
        # Line 31: Launch browser in headless mode with additional args for compatibility
        browser = p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
        )

        # Line 38: Create a new browser context and page
        page = browser.new_page()

        # Line 42: Navigate to local test page
        test_url = get_test_page_url()
        page.goto(test_url, wait_until="load")

        # Line 47: Get and verify page title
        title = page.title()

        # Line 54: Verify specific content exists
        heading = page.locator("h1")
        heading_text = heading.inner_text()

        # Line 59: Take a screenshot
        screenshot_path = os.path.join(os.path.dirname(__file__), "screenshot.png")
        page.screenshot(path=screenshot_path)

        browser.close()
```

**Expected Output:**
```
=== Test 1: Basic Navigation ===
✓ Browser launched (Chromium)
✓ New page created
✓ Navigated to test page
✓ Page title: 'Playwright Test Page'
✓ Found heading: 'Welcome to Playwright Testing'
✓ Screenshot saved to: /path/to/screenshot.png
✓ Browser closed
```

**Line 31-37**: Launches Chromium browser with compatibility args for headless mode.
**Line 39**: Creates a new browser page for testing.
**Line 44**: Navigates to the local HTML test page using file:// protocol.
**Line 48**: Retrieves and verifies the page title.
**Line 55**: Uses locator to find the H1 element and extract its text.
**Line 61**: Captures a screenshot of the page for visual verification.

### Test 2: Form Interaction (Lines 69-107)

```python
def test_form_interaction():
    """Test form filling and submission."""
    with sync_playwright() as p:
        browser = p.chromium.launch(...)
        page = browser.new_page()
        page.goto(get_test_page_url())

        # Line 80: Fill in the name input field
        name_input = page.locator("#name-input")
        name_input.fill("John Doe")

        # Line 85: Fill in the email input field
        email_input = page.locator("#email-input")
        email_input.fill("john.doe@example.com")

        # Line 90: Click the submit button
        submit_button = page.locator("#submit-btn")
        submit_button.click()

        # Line 95: Verify the result is displayed
        result_div = page.locator("#result")
        expect(result_div).to_be_visible()

        # Line 100: Check the result text
        result_text = page.locator("#result-text").inner_text()
```

**Expected Output:**
```
=== Test 2: Form Interaction ===
✓ Navigated to test page
✓ Filled name input: 'John Doe'
✓ Filled email input: 'john.doe@example.com'
✓ Clicked submit button
✓ Result div is now visible
✓ Result text: 'Name: John Doe, Email: john.doe@example.com'
✓ Browser closed
```

**Line 80-82**: Uses CSS selector `#name-input` to locate input and fills it with text.
**Line 85-87**: Fills the email input field using locator.
**Line 90-92**: Locates submit button and triggers click event.
**Line 95-97**: Uses `expect()` assertion to verify the result div becomes visible after submission.
**Line 100**: Extracts the inner text from the result element to verify form data.

### Test 3: Element Interactions (Lines 110-145)

```python
def test_element_interactions():
    """Test various element interactions and queries."""
    with sync_playwright() as p:
        browser = p.chromium.launch(...)
        page = browser.new_page()
        page.goto(get_test_page_url())

        # Line 123: Wait for specific element to be visible
        page.wait_for_selector("h1", state="visible")

        # Line 127: Get element count
        input_count = page.locator("input").count()

        # Line 131: Check if element is visible
        h1_visible = page.locator("h1").is_visible()

        # Line 135: Check if button is enabled
        button_enabled = page.locator("#submit-btn").is_enabled()

        # Line 139: Get element attribute
        placeholder = page.locator("#name-input").get_attribute("placeholder")
```

**Expected Output:**
```
=== Test 3: Element Interactions ===
✓ Navigated to test page
✓ H1 element is visible
✓ Found 2 input field(s) on the page
✓ H1 visibility: True
✓ Submit button enabled: True
✓ Name input placeholder: 'Enter your name'
✓ Browser closed
```

**Line 123**: Explicit wait for H1 element to be visible before proceeding.
**Line 127**: Counts all input elements on the page using locator.
**Line 131**: Checks visibility state of an element.
**Line 135**: Verifies button is enabled and interactive.
**Line 139**: Retrieves HTML attribute value from an element.

### Test 4: Assertions with expect() (Lines 148-185)

```python
def test_assertions_with_expect():
    """Test using Playwright's expect assertions."""
    with sync_playwright() as p:
        browser = p.chromium.launch(...)
        page = browser.new_page()
        page.goto(get_test_page_url())

        # Line 162: Assert page title
        expect(page).to_have_title("Playwright Test Page")

        # Line 166: Assert element is visible
        h1_locator = page.locator("h1")
        expect(h1_locator).to_be_visible()

        # Line 171: Assert element contains text
        expect(h1_locator).to_contain_text("Welcome")

        # Line 175: Assert input field has placeholder
        name_input = page.locator("#name-input")
        expect(name_input).to_have_attribute("placeholder", "Enter your name")

        # Line 180: Assert button is enabled
        submit_btn = page.locator("#submit-btn")
        expect(submit_btn).to_be_enabled()
```

**Expected Output:**
```
=== Test 4: Assertions with expect() ===
✓ Navigated to test page
✓ Assertion passed: Page title is correct
✓ Assertion passed: H1 element is visible
✓ Assertion passed: H1 contains 'Welcome'
✓ Assertion passed: Input has correct placeholder
✓ Assertion passed: Submit button is enabled
✓ Browser closed
```

**Line 162**: Assert page title matches expected value using `expect()`.
**Line 166-168**: Assert element visibility with auto-waiting.
**Line 171-173**: Assert element contains specific text (partial match).
**Line 175-177**: Assert element has specific attribute with expected value.
**Line 180-182**: Assert button is in enabled state.

### Test 5: Viewport and Device Emulation (Lines 188-217)

```python
def test_viewport_and_device_emulation():
    """Test viewport sizing and device emulation."""
    with sync_playwright() as p:
        browser = p.chromium.launch(...)

        # Line 205: Create page with custom viewport
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        page.goto(get_test_page_url())
        viewport_size = page.viewport_size

        # Line 212: Emulate mobile device
        iphone = p.devices["iPhone 13"]
        mobile_page = browser.new_page(**iphone)
        mobile_page.goto(get_test_page_url())
        mobile_viewport = mobile_page.viewport_size
```

**Expected Output:**
```
=== Test 5: Viewport and Device Emulation ===
✓ Created page with 1280x720 viewport
✓ Viewport size: 1280x720
✓ Created page with iPhone 13 emulation
✓ Mobile viewport: 390x844
✓ User agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac...
✓ Browser closed
```

**Line 205-207**: Creates page with custom viewport dimensions for desktop testing.
**Line 209**: Retrieves and verifies the viewport size.
**Line 212-213**: Uses Playwright's device registry to emulate iPhone 13.
**Line 215-217**: Tests the page in mobile viewport with mobile user agent.

### Test 6: Advanced Interactions (Lines 220-257)

```python
def test_advanced_interactions():
    """Test advanced interactions like hover, double-click, and keyboard."""
    with sync_playwright() as p:
        browser = p.chromium.launch(...)
        page = browser.new_page()
        page.goto(get_test_page_url())

        # Line 237: Hover over an element
        button = page.locator("#submit-btn")
        button.hover()

        # Line 242: Type into input with keyboard
        name_input = page.locator("#name-input")
        name_input.click()
        page.keyboard.type("Playwright Test")

        # Line 249: Press keyboard shortcuts
        page.keyboard.press("Control+A")

        # Line 253: Get input value after typing
        input_value = name_input.input_value()

        # Line 257: Clear input field
        name_input.fill("")
```

**Expected Output:**
```
=== Test 6: Advanced Interactions ===
✓ Navigated to test page
✓ Hovered over submit button
✓ Typed text using keyboard API
✓ Pressed Ctrl+A to select all
✓ Input value: 'Playwright Test'
✓ Cleared input field
✓ Browser closed
```

**Line 237-239**: Simulates mouse hover over an element.
**Line 242-245**: Uses keyboard API to type text character by character.
**Line 249-250**: Simulates keyboard shortcut (Ctrl+A).
**Line 253-254**: Retrieves current value from input field.
**Line 257-258**: Clears input field using fill with empty string.

## Complete Program Output

```
============================================================
Playwright UI Testing Demonstration
============================================================

=== Test 1: Basic Navigation ===
✓ Browser launched (Chromium)
✓ New page created
✓ Navigated to test page
✓ Page title: 'Playwright Test Page'
✓ Found heading: 'Welcome to Playwright Testing'
✓ Screenshot saved to: /path/to/screenshot.png
✓ Browser closed

=== Test 2: Form Interaction ===
✓ Navigated to test page
✓ Filled name input: 'John Doe'
✓ Filled email input: 'john.doe@example.com'
✓ Clicked submit button
✓ Result div is now visible
✓ Result text: 'Name: John Doe, Email: john.doe@example.com'
✓ Browser closed

=== Test 3: Element Interactions ===
✓ Navigated to test page
✓ H1 element is visible
✓ Found 2 input field(s) on the page
✓ H1 visibility: True
✓ Submit button enabled: True
✓ Name input placeholder: 'Enter your name'
✓ Browser closed

=== Test 4: Assertions with expect() ===
✓ Navigated to test page
✓ Assertion passed: Page title is correct
✓ Assertion passed: H1 element is visible
✓ Assertion passed: H1 contains 'Welcome'
✓ Assertion passed: Input has correct placeholder
✓ Assertion passed: Submit button is enabled
✓ Browser closed

=== Test 5: Viewport and Device Emulation ===
✓ Created page with 1280x720 viewport
✓ Viewport size: 1280x720
✓ Created page with iPhone 13 emulation
✓ Mobile viewport: 390x844
✓ User agent: Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac...
✓ Browser closed

=== Test 6: Advanced Interactions ===
✓ Navigated to test page
✓ Hovered over submit button
✓ Typed text using keyboard API
✓ Pressed Ctrl+A to select all
✓ Input value: 'Playwright Test'
✓ Cleared input field
✓ Browser closed

============================================================
All tests completed successfully! ✓
============================================================

Key Concepts Demonstrated:
  • Browser automation and page navigation
  • Element selection with locators
  • Form interaction (fill, click)
  • Assertions with expect()
  • Viewport and device emulation
  • Advanced interactions (hover, keyboard)
```

## Key Concepts Explained

### 1. Browser Automation
- **Line 31-36**: Launch browser with configuration options (headless mode, sandbox args)
- **Line 39**: Create browser context and page for testing
- **Line 44**: Navigate to URLs using `page.goto()`

### 2. Element Selection (Locators)
- **CSS Selectors**: `page.locator("#id")`, `page.locator(".class")`
- **Element Queries**: `.count()`, `.is_visible()`, `.is_enabled()`
- **Text Extraction**: `.inner_text()`, `.text_content()`
- **Attributes**: `.get_attribute(name)`

### 3. User Interactions
- **Form Input**: `locator.fill(text)` - fills form fields
- **Clicks**: `locator.click()` - triggers click events
- **Hover**: `locator.hover()` - simulates mouse hover
- **Keyboard**: `page.keyboard.type()`, `page.keyboard.press()` - keyboard input

### 4. Assertions (expect API)
- **Page Assertions**: `expect(page).to_have_title()`
- **Element Visibility**: `expect(locator).to_be_visible()`
- **Text Content**: `expect(locator).to_contain_text()`
- **Attributes**: `expect(locator).to_have_attribute()`
- **State**: `expect(locator).to_be_enabled()`

### 5. Viewport & Device Emulation
- **Custom Viewport**: `browser.new_page(viewport={width, height})`
- **Device Emulation**: `browser.new_page(**p.devices["iPhone 13"])`
- **Responsive Testing**: Test across different screen sizes and devices

### 6. Waiting Strategies
- **Explicit Waits**: `page.wait_for_selector(selector, state="visible")`
- **Load States**: `page.goto(url, wait_until="load")` or "domcontentloaded"
- **Auto-waiting**: Playwright automatically waits for elements in most actions

## Additional Features Available

- **Screenshots & Videos**: Capture visual evidence of test execution
- **Network Interception**: Mock API responses, monitor network traffic
- **Multi-page Support**: Handle popups, tabs, and iframes
- **File Upload/Download**: Test file operations
- **Geolocation & Permissions**: Test location-based features
- **Browser Context Isolation**: Run tests in parallel with isolated contexts

## Version Requirements

This example requires:
- **Python 3.10+**: For inline script metadata (PEP 723) support
- **Playwright 1.40.0+**: For all demonstrated features and expect() API
- **Chromium Browser**: Installed via `playwright install chromium`

## Notes

- The script uses inline script metadata (lines 2-7) for dependency management with `uv`
- Compatible with Chromium, Firefox, and WebKit browsers (example uses Chromium)
- Headless mode is enabled for CI/CD compatibility
- Additional browser args ensure compatibility in restricted environments
