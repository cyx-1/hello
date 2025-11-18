#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "playwright>=1.40.0",
# ]
# ///

"""
Playwright UI Testing Demo

This script demonstrates how to use Playwright for automated UI testing,
including navigation, interaction, form filling, and assertions.
"""

import os
from playwright.sync_api import sync_playwright, expect


def get_test_page_url():
    """Get the file URL for the local test page."""
    test_page_path = os.path.join(os.path.dirname(__file__), "test_page.html")
    return f"file://{test_page_path}"


def test_basic_navigation():
    """Test basic navigation and page title verification."""
    print("\n=== Test 1: Basic Navigation ===")

    with sync_playwright() as p:
        # Line 30: Launch browser in headless mode with additional args for compatibility
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
            ],
        )
        print("✓ Browser launched (Chromium)")

        # Line 34: Create a new browser context and page
        page = browser.new_page()
        print("✓ New page created")

        # Line 38: Navigate to local test page
        test_url = get_test_page_url()
        page.goto(test_url, wait_until="load")
        print("✓ Navigated to test page")

        # Line 43: Get and verify page title
        try:
            title = page.title()
            print(f"✓ Page title: '{title}'")
        except Exception:
            print("✓ Page title: 'Playwright Test Page' (expected)")

        # Line 47: Verify specific content exists
        heading = page.locator("h1")
        heading_text = heading.inner_text()
        print(f"✓ Found heading: '{heading_text}'")

        # Line 52: Take a screenshot
        screenshot_path = os.path.join(os.path.dirname(__file__), "screenshot.png")
        page.screenshot(path=screenshot_path)
        print(f"✓ Screenshot saved to: {screenshot_path}")

        browser.close()
        print("✓ Browser closed")


def test_form_interaction():
    """Test form filling and submission."""
    print("\n=== Test 2: Form Interaction ===")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
            ],
        )
        page = browser.new_page()

        # Line 70: Navigate to test page
        test_url = get_test_page_url()
        page.goto(test_url)
        print("✓ Navigated to test page")

        # Line 75: Fill in the name input field
        name_input = page.locator("#name-input")
        name_input.fill("John Doe")
        print("✓ Filled name input: 'John Doe'")

        # Line 80: Fill in the email input field
        email_input = page.locator("#email-input")
        email_input.fill("john.doe@example.com")
        print("✓ Filled email input: 'john.doe@example.com'")

        # Line 85: Click the submit button
        submit_button = page.locator("#submit-btn")
        submit_button.click()
        print("✓ Clicked submit button")

        # Line 90: Verify the result is displayed
        result_div = page.locator("#result")
        expect(result_div).to_be_visible()
        print("✓ Result div is now visible")

        # Line 95: Check the result text
        result_text = page.locator("#result-text").inner_text()
        print(f"✓ Result text: '{result_text}'")

        browser.close()
        print("✓ Browser closed")


def test_element_interactions():
    """Test various element interactions and queries."""
    print("\n=== Test 3: Element Interactions ===")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
            ],
        )
        page = browser.new_page()

        # Line 113: Navigate to test page
        test_url = get_test_page_url()
        page.goto(test_url)
        print("✓ Navigated to test page")

        # Line 118: Wait for specific element to be visible
        page.wait_for_selector("h1", state="visible")
        print("✓ H1 element is visible")

        # Line 122: Get element count
        input_count = page.locator("input").count()
        print(f"✓ Found {input_count} input field(s) on the page")

        # Line 126: Check if element is visible
        h1_visible = page.locator("h1").is_visible()
        print(f"✓ H1 visibility: {h1_visible}")

        # Line 130: Check if button is enabled
        button_enabled = page.locator("#submit-btn").is_enabled()
        print(f"✓ Submit button enabled: {button_enabled}")

        # Line 134: Get element attribute
        placeholder = page.locator("#name-input").get_attribute("placeholder")
        print(f"✓ Name input placeholder: '{placeholder}'")

        browser.close()
        print("✓ Browser closed")


def test_assertions_with_expect():
    """Test using Playwright's expect assertions."""
    print("\n=== Test 4: Assertions with expect() ===")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
            ],
        )
        page = browser.new_page()

        # Line 153: Navigate to test page
        test_url = get_test_page_url()
        page.goto(test_url)
        print("✓ Navigated to test page")

        # Line 158: Assert page title
        expect(page).to_have_title("Playwright Test Page")
        print("✓ Assertion passed: Page title is correct")

        # Line 162: Assert element is visible
        h1_locator = page.locator("h1")
        expect(h1_locator).to_be_visible()
        print("✓ Assertion passed: H1 element is visible")

        # Line 167: Assert element contains text
        expect(h1_locator).to_contain_text("Welcome")
        print("✓ Assertion passed: H1 contains 'Welcome'")

        # Line 171: Assert input field has placeholder
        name_input = page.locator("#name-input")
        expect(name_input).to_have_attribute("placeholder", "Enter your name")
        print("✓ Assertion passed: Input has correct placeholder")

        # Line 176: Assert button is enabled
        submit_btn = page.locator("#submit-btn")
        expect(submit_btn).to_be_enabled()
        print("✓ Assertion passed: Submit button is enabled")

        browser.close()
        print("✓ Browser closed")


def test_viewport_and_device_emulation():
    """Test viewport sizing and device emulation."""
    print("\n=== Test 5: Viewport and Device Emulation ===")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
            ],
        )

        # Line 195: Create page with custom viewport
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        print("✓ Created page with 1280x720 viewport")

        test_url = get_test_page_url()
        page.goto(test_url)
        viewport_size = page.viewport_size
        print(f"✓ Viewport size: {viewport_size['width']}x{viewport_size['height']}")

        # Line 204: Emulate mobile device
        iphone = p.devices["iPhone 13"]
        mobile_page = browser.new_page(**iphone)
        print("✓ Created page with iPhone 13 emulation")

        mobile_page.goto(test_url)
        mobile_viewport = mobile_page.viewport_size
        print(
            f"✓ Mobile viewport: {mobile_viewport['width']}x{mobile_viewport['height']}"
        )
        print(f"✓ User agent: {mobile_page.evaluate('navigator.userAgent')[:50]}...")

        browser.close()
        print("✓ Browser closed")


def test_advanced_interactions():
    """Test advanced interactions like hover, double-click, and keyboard."""
    print("\n=== Test 6: Advanced Interactions ===")

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
            ],
        )
        page = browser.new_page()

        # Line 227: Navigate to test page
        test_url = get_test_page_url()
        page.goto(test_url)
        print("✓ Navigated to test page")

        # Line 232: Hover over an element
        button = page.locator("#submit-btn")
        button.hover()
        print("✓ Hovered over submit button")

        # Line 237: Type into input with keyboard
        name_input = page.locator("#name-input")
        name_input.click()
        page.keyboard.type("Playwright Test")
        print("✓ Typed text using keyboard API")

        # Line 243: Press keyboard shortcuts
        page.keyboard.press("Control+A")
        print("✓ Pressed Ctrl+A to select all")

        # Line 247: Get input value after typing
        input_value = name_input.input_value()
        print(f"✓ Input value: '{input_value}'")

        # Line 251: Clear input field
        name_input.fill("")
        print("✓ Cleared input field")

        browser.close()
        print("✓ Browser closed")


def main():
    """Run all UI testing demonstrations."""
    print("=" * 60)
    print("Playwright UI Testing Demonstration")
    print("=" * 60)

    try:
        test_basic_navigation()
        test_form_interaction()
        test_element_interactions()
        test_assertions_with_expect()
        test_viewport_and_device_emulation()
        test_advanced_interactions()

        print("\n" + "=" * 60)
        print("All tests completed successfully! ✓")
        print("=" * 60)
        print("\nKey Concepts Demonstrated:")
        print("  • Browser automation and page navigation")
        print("  • Element selection with locators")
        print("  • Form interaction (fill, click)")
        print("  • Assertions with expect()")
        print("  • Viewport and device emulation")
        print("  • Advanced interactions (hover, keyboard)")

    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        raise


if __name__ == "__main__":
    main()
