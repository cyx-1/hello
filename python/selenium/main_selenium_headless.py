#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "selenium>=4.0.0",
# ]
# ///

"""
Selenium Headless Browser Control Example

This script demonstrates how to control a web browser in headless mode using Selenium.
Headless mode allows you to automate browser interactions without displaying a GUI,
which is useful for web scraping, automated testing, and CI/CD pipelines.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main():
    print("=" * 70)
    print("Selenium Headless Browser Control Demo")
    print("=" * 70)
    print()

    # Line 33: Configure Chrome options for headless mode
    print("[1] Configuring Chrome for headless mode...")
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # Use new headless mode
    chrome_options.add_argument("--no-sandbox")  # Required for running as root
    chrome_options.add_argument(
        "--disable-dev-shm-usage"
    )  # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--window-size=1920,1080")  # Set window size
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    )
    print("   ✓ Headless mode enabled")
    print("   ✓ Window size: 1920x1080")
    print("   ✓ GPU disabled for stability")
    print()

    # Line 48: Initialize the Chrome driver with headless options
    print("[2] Initializing Chrome WebDriver...")
    try:
        driver = webdriver.Chrome(options=chrome_options)
        print("   ✓ WebDriver initialized successfully")
    except Exception as e:
        print(f"   ✗ Error initializing WebDriver: {e}")
        print()
        print(
            "Note: This example requires Chrome/Chromium and ChromeDriver to be installed."
        )
        print("Install with: apt-get install chromium chromium-driver")
        return
    print()

    try:
        # Line 62: Navigate to a webpage
        print("[3] Navigating to example.com...")
        url = "https://example.com"
        driver.get(url)
        print(f"   ✓ Successfully loaded: {url}")
        print(f"   ✓ Page title: {driver.title}")
        print()

        # Line 70: Get page information
        print("[4] Extracting page information...")
        current_url = driver.current_url
        page_source_length = len(driver.page_source)
        print(f"   ✓ Current URL: {current_url}")
        print(f"   ✓ Page source length: {page_source_length} characters")
        print()

        # Line 79: Find elements on the page
        print("[5] Finding elements on the page...")
        try:
            # Wait for the h1 element to be present
            wait = WebDriverWait(driver, 10)
            h1_element = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
            print(f"   ✓ Found H1 element: '{h1_element.text}'")

            # Find all paragraph elements
            paragraphs = driver.find_elements(By.TAG_NAME, "p")
            print(f"   ✓ Found {len(paragraphs)} paragraph(s)")
            for i, p in enumerate(paragraphs, 1):
                text_preview = p.text[:60] + "..." if len(p.text) > 60 else p.text
                print(f"      Paragraph {i}: {text_preview}")
        except Exception as e:
            print(f"   ✗ Error finding elements: {e}")
        print()

        # Line 99: Execute JavaScript
        print("[6] Executing JavaScript in the page context...")
        js_result = driver.execute_script("return document.title;")
        print(f"   ✓ JavaScript returned: '{js_result}'")

        # Get scroll height
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        print(f"   ✓ Page scroll height: {scroll_height}px")
        print()

        # Line 109: Get browser capabilities and metadata
        print("[7] Browser metadata and capabilities...")
        capabilities = driver.capabilities
        print(f"   ✓ Browser: {capabilities.get('browserName', 'Unknown')}")
        print(f"   ✓ Browser version: {capabilities.get('browserVersion', 'Unknown')}")
        print(f"   ✓ Platform: {capabilities.get('platformName', 'Unknown')}")
        print()

        # Line 117: Take a screenshot (saved as PNG)
        print("[8] Taking a screenshot...")
        screenshot_path = "/tmp/selenium_headless_screenshot.png"
        driver.save_screenshot(screenshot_path)
        print(f"   ✓ Screenshot saved to: {screenshot_path}")
        print()

        # Line 124: Navigate to another page
        print("[9] Navigating to another page...")
        driver.get("https://www.wikipedia.org")
        print(f"   ✓ Navigated to: {driver.current_url}")
        print(f"   ✓ New page title: {driver.title}")
        print()

        # Line 131: Demonstrate back/forward navigation
        print("[10] Testing browser navigation (back/forward)...")
        driver.back()
        print(f"   ✓ After back(): {driver.current_url}")
        driver.forward()
        print(f"   ✓ After forward(): {driver.current_url}")
        print()

        # Line 139: Get cookies
        print("[11] Managing cookies...")
        cookies = driver.get_cookies()
        print(f"   ✓ Found {len(cookies)} cookie(s)")
        for i, cookie in enumerate(cookies[:3], 1):  # Show first 3 cookies
            print(f"      Cookie {i}: {cookie.get('name', 'unnamed')}")
        print()

        # Line 148: Demonstrate window management
        print("[12] Window management...")
        window_size = driver.get_window_size()
        print(
            f"   ✓ Current window size: {window_size['width']}x{window_size['height']}"
        )

        # Resize window
        driver.set_window_size(1280, 720)
        new_size = driver.get_window_size()
        print(f"   ✓ Resized to: {new_size['width']}x{new_size['height']}")
        print()

    finally:
        # Line 161: Clean up - always close the driver
        print("[13] Cleaning up...")
        driver.quit()
        print("   ✓ WebDriver closed successfully")
        print()

    print("=" * 70)
    print("Demo completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
