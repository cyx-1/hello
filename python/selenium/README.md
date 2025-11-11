# Selenium Headless Browser Control Example

This example demonstrates how to control a web browser in headless mode using Selenium WebDriver. Headless mode allows you to automate browser interactions without displaying a GUI, which is essential for web scraping, automated testing, and CI/CD pipelines.

## Prerequisites

- **Python**: >= 3.10
- **Chrome/Chromium**: Latest stable version
- **ChromeDriver**: Compatible with your Chrome version

### Installation

Install Chrome and ChromeDriver:
```bash
# Ubuntu/Debian
apt-get install chromium chromium-driver

# macOS
brew install --cask google-chrome
brew install chromedriver

# Or download ChromeDriver manually from:
# https://chromedriver.chromium.org/downloads
```

## Running the Example

```bash
uv run python main_selenium_headless.py
```

## Source Code

```python
# Lines 1-16: Script metadata and imports
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "selenium>=4.0.0",
# ]
# ///

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
```

**Lines 1-7**: Inline script metadata using PEP 723 format specifies Python version and Selenium dependency.
**Lines 17-20**: Import necessary Selenium components for browser control, element location, and wait conditions.

```python
# Lines 33-45: Configure Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Use new headless mode
chrome_options.add_argument("--no-sandbox")  # Required for running as root
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--window-size=1920,1080")  # Set window size
chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36")
```

**Line 34**: `Options()` creates a configuration object for Chrome.
**Line 35**: `--headless=new` enables the new headless mode (Chrome 109+) which is more stable than the legacy mode.
**Line 36**: `--no-sandbox` disables Chrome's sandboxing (required when running as root in containers).
**Line 37**: `--disable-dev-shm-usage` prevents issues with limited shared memory in Docker environments.
**Line 38**: `--disable-gpu` disables GPU hardware acceleration for better stability in headless mode.
**Line 39**: `--window-size=1920,1080` sets viewport dimensions for consistent rendering.

```python
# Lines 48-58: Initialize the Chrome driver with headless options
try:
    driver = webdriver.Chrome(options=chrome_options)
    print("   ✓ WebDriver initialized successfully")
except Exception as e:
    print(f"   ✗ Error initializing WebDriver: {e}")
    print()
    print("Note: This example requires Chrome/Chromium and ChromeDriver to be installed.")
    print("Install with: apt-get install chromium chromium-driver")
    return
```

**Line 51**: `webdriver.Chrome(options=chrome_options)` creates a WebDriver instance with our headless configuration.
**Lines 52-58**: Error handling provides helpful installation instructions if Chrome/ChromeDriver is missing.

```python
# Lines 62-68: Navigate to a webpage
print("[3] Navigating to example.com...")
url = "https://example.com"
driver.get(url)
print(f"   ✓ Successfully loaded: {url}")
print(f"   ✓ Page title: {driver.title}")
```

**Line 65**: `driver.get(url)` navigates to the specified URL and waits for the page to load.
**Line 67**: `driver.title` retrieves the page's title from the DOM.

```python
# Lines 70-76: Get page information
print("[4] Extracting page information...")
current_url = driver.current_url
page_source_length = len(driver.page_source)
print(f"   ✓ Current URL: {current_url}")
print(f"   ✓ Page source length: {page_source_length} characters")
```

**Line 72**: `driver.current_url` gets the current page URL (useful for detecting redirects).
**Line 73**: `driver.page_source` retrieves the entire HTML source of the page.

```python
# Lines 79-96: Find elements on the page
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
```

**Line 83**: `WebDriverWait(driver, 10)` creates a wait object with 10-second timeout.
**Line 84**: `wait.until(EC.presence_of_element_located(...))` waits for the element to appear in the DOM.
**Line 85**: `By.TAG_NAME` is one of several locator strategies (others include BY.ID, BY.CLASS_NAME, BY.CSS_SELECTOR, BY.XPATH).
**Line 88**: `find_elements()` (plural) returns a list of all matching elements.

```python
# Lines 99-107: Execute JavaScript
print("[6] Executing JavaScript in the page context...")
js_result = driver.execute_script("return document.title;")
print(f"   ✓ JavaScript returned: '{js_result}'")

# Get scroll height
scroll_height = driver.execute_script("return document.body.scrollHeight;")
print(f"   ✓ Page scroll height: {scroll_height}px")
```

**Line 101**: `execute_script()` runs JavaScript code in the browser context and returns the result.
**Line 105**: You can execute any JavaScript to extract computed values, manipulate DOM, or trigger events.

```python
# Lines 109-115: Get browser capabilities and metadata
print("[7] Browser metadata and capabilities...")
capabilities = driver.capabilities
print(f"   ✓ Browser: {capabilities.get('browserName', 'Unknown')}")
print(f"   ✓ Browser version: {capabilities.get('browserVersion', 'Unknown')}")
print(f"   ✓ Platform: {capabilities.get('platformName', 'Unknown')}")
```

**Line 111**: `driver.capabilities` contains browser metadata, version info, and supported features.

```python
# Lines 117-122: Take a screenshot
print("[8] Taking a screenshot...")
screenshot_path = "/tmp/selenium_headless_screenshot.png"
driver.save_screenshot(screenshot_path)
print(f"   ✓ Screenshot saved to: {screenshot_path}")
```

**Line 120**: `save_screenshot()` captures the rendered page as a PNG image - works even in headless mode!

```python
# Lines 124-129: Navigate to another page
print("[9] Navigating to another page...")
driver.get("https://www.wikipedia.org")
print(f"   ✓ Navigated to: {driver.current_url}")
print(f"   ✓ New page title: {driver.title}")
```

**Line 126**: Demonstrates navigation to a different URL within the same session.

```python
# Lines 131-137: Demonstrate back/forward navigation
print("[10] Testing browser navigation (back/forward)...")
driver.back()
print(f"   ✓ After back(): {driver.current_url}")
driver.forward()
print(f"   ✓ After forward(): {driver.current_url}")
```

**Line 133**: `driver.back()` navigates to the previous page in browser history.
**Line 135**: `driver.forward()` navigates forward in browser history.

```python
# Lines 139-145: Get cookies
print("[11] Managing cookies...")
cookies = driver.get_cookies()
print(f"   ✓ Found {len(cookies)} cookie(s)")
for i, cookie in enumerate(cookies[:3], 1):  # Show first 3 cookies
    print(f"      Cookie {i}: {cookie.get('name', 'unnamed')}")
```

**Line 141**: `get_cookies()` retrieves all cookies for the current domain. You can also add/delete cookies.

```python
# Lines 148-158: Demonstrate window management
print("[12] Window management...")
window_size = driver.get_window_size()
print(f"   ✓ Current window size: {window_size['width']}x{window_size['height']}")

# Resize window
driver.set_window_size(1280, 720)
new_size = driver.get_window_size()
print(f"   ✓ Resized to: {new_size['width']}x{new_size['height']}")
```

**Line 150**: `get_window_size()` returns the browser window dimensions as a dictionary.
**Line 153**: `set_window_size()` changes the viewport size - useful for responsive design testing.

```python
# Lines 161-165: Clean up
finally:
    print("[13] Cleaning up...")
    driver.quit()
    print("   ✓ WebDriver closed successfully")
```

**Line 164**: `driver.quit()` closes all browser windows and terminates the WebDriver session. Always call this in a `finally` block to prevent resource leaks.

## Program Output

When you run this script with Chrome/ChromeDriver properly installed, you'll see:

```
======================================================================
Selenium Headless Browser Control Demo
======================================================================

[1] Configuring Chrome for headless mode...
   ✓ Headless mode enabled
   ✓ Window size: 1920x1080
   ✓ GPU disabled for stability

[2] Initializing Chrome WebDriver...
   ✓ WebDriver initialized successfully

[3] Navigating to example.com...
   ✓ Successfully loaded: https://example.com
   ✓ Page title: Example Domain

[4] Extracting page information...
   ✓ Current URL: https://example.com/
   ✓ Page source length: 1256 characters

[5] Finding elements on the page...
   ✓ Found H1 element: 'Example Domain'
   ✓ Found 2 paragraph(s)
      Paragraph 1: This domain is for use in illustrative examples in documents...
      Paragraph 2: More information...

[6] Executing JavaScript in the page context...
   ✓ JavaScript returned: 'Example Domain'
   ✓ Page scroll height: 789px

[7] Browser metadata and capabilities...
   ✓ Browser: chrome
   ✓ Browser version: 131.0.6778.85
   ✓ Platform: linux

[8] Taking a screenshot...
   ✓ Screenshot saved to: /tmp/selenium_headless_screenshot.png

[9] Navigating to another page...
   ✓ Navigated to: https://www.wikipedia.org/
   ✓ New page title: Wikipedia

[10] Testing browser navigation (back/forward)...
   ✓ After back(): https://example.com/
   ✓ After forward(): https://www.wikipedia.org/

[11] Managing cookies...
   ✓ Found 3 cookie(s)
      Cookie 1: GeoIP
      Cookie 2: WMF-Last-Access
      Cookie 3: NetworkProbeLimit

[12] Window management...
   ✓ Current window size: 1920x1080
   ✓ Resized to: 1280x720

[13] Cleaning up...
   ✓ WebDriver closed successfully

======================================================================
Demo completed successfully!
======================================================================
```

## Output Annotations

**Section [1] - Lines 33-45**: Configures Chrome with headless-specific options. The output confirms that headless mode is active and GPU is disabled for stability.

**Section [2] - Lines 48-58**: Initializes the WebDriver. This creates a new Chrome process in the background (invisible due to headless mode).

**Section [3] - Lines 62-68**: Navigates to example.com. The output shows the final URL and page title, confirming successful page load.

**Section [4] - Lines 70-76**: Extracts metadata. The current URL confirms any redirects, and page source length shows we successfully retrieved the HTML (1,256 characters for example.com).

**Section [5] - Lines 79-96**: Demonstrates element location using WebDriverWait and By locators. Found the H1 heading and 2 paragraphs from example.com's simple page structure.

**Section [6] - Lines 99-107**: Executes JavaScript in the browser context. Returns the document title and computed scroll height (789px), showing JavaScript execution works even in headless mode.

**Section [7] - Lines 109-115**: Shows browser capabilities. Confirms we're running Chrome version 131 on Linux platform.

**Section [8] - Lines 117-122**: Captures a screenshot. Even in headless mode, Chrome renders the page visually and can save screenshots.

**Section [9] - Lines 124-129**: Navigates to Wikipedia. The URL and title change, demonstrating navigation within the same browser session.

**Section [10] - Lines 131-137**: Tests browser history navigation. Back() returns to example.com, forward() goes back to Wikipedia.

**Section [11] - Lines 139-145**: Retrieves cookies. Wikipedia sets 3 cookies (GeoIP, WMF-Last-Access, NetworkProbeLimit) for tracking and preferences.

**Section [12] - Lines 148-158**: Window management. Initial size is 1920x1080 (from Line 39), successfully resized to 1280x720.

**Section [13] - Lines 161-165**: Cleanup. The `driver.quit()` call closes the browser and frees resources.

## Key Concepts Demonstrated

1. **Headless Mode Configuration**: Using `--headless=new` for modern headless browsing
2. **WebDriver Initialization**: Creating and configuring a Chrome WebDriver instance
3. **Page Navigation**: Loading URLs and tracking navigation state
4. **Element Location**: Finding elements using WebDriverWait and By locators
5. **JavaScript Execution**: Running custom JavaScript in the page context
6. **Screenshot Capture**: Saving visual page renders even in headless mode
7. **Browser Navigation**: Using back() and forward() for history management
8. **Cookie Management**: Retrieving cookies from the current session
9. **Window Management**: Controlling viewport dimensions
10. **Resource Cleanup**: Properly closing the WebDriver to prevent resource leaks

## Version Requirements

- **Python**: 3.10 or higher
- **Selenium**: 4.0.0 or higher (supports new headless mode with `--headless=new`)
- **Chrome/Chromium**: Version 109+ recommended (for improved headless mode)
- **ChromeDriver**: Must match your Chrome version

## Common Use Cases

- **Web Scraping**: Extract data from dynamic websites that require JavaScript
- **Automated Testing**: Test web applications without displaying the browser
- **CI/CD Pipelines**: Run browser tests in containers without GUI
- **Screenshot Generation**: Capture page renders for documentation or monitoring
- **Form Automation**: Fill and submit forms programmatically
- **Performance Testing**: Measure page load times and resource usage

## Troubleshooting

**"Unable to obtain driver for chrome"**: Install Chrome and ChromeDriver, or set the ChromeDriver path explicitly.

**"Chrome failed to start"**: Add `--no-sandbox` and `--disable-dev-shm-usage` options (already included in this example).

**Element not found**: Use WebDriverWait with expected_conditions instead of immediate find_element calls.

**Screenshot is blank**: Ensure the page has fully loaded before taking the screenshot; use WebDriverWait.
