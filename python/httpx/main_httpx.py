#!/usr/bin/env python3
"""
Demonstration of httpx and its advantages over requests.

httpx is a modern HTTP client for Python that offers:
- HTTP/2 support
- Async/await support
- Better timeout defaults
- Connection pooling by default
- Cleaner API for custom transports and authentication
"""

# /// script
# dependencies = [
#   "httpx[http2]",
#   "requests",
# ]
# ///

import asyncio
import time
import httpx
import requests


def demo_basic_requests():
    """Basic HTTP requests with httpx (similar to requests)"""
    print("=" * 60)
    print("1. BASIC REQUESTS - httpx API is similar to requests")
    print("=" * 60)

    # httpx has a requests-compatible API
    response = httpx.get("https://httpbin.org/get")
    print(f"Status Code: {response.status_code}")
    print(f"Content-Type: {response.headers.get('content-type')}")
    print(f"Response preview: {str(response.json())[:100]}...\n")


def demo_http2_support():
    """HTTP/2 support - a major advantage over requests"""
    print("=" * 60)
    print("2. HTTP/2 SUPPORT - httpx supports HTTP/2, requests does not")
    print("=" * 60)

    # httpx supports HTTP/2
    with httpx.Client(http2=True) as client:
        response = client.get("https://www.google.com")
        print(f"httpx - HTTP version: {response.http_version}")

    # requests only supports HTTP/1.1
    _ = requests.get("https://www.google.com")
    print("requests - HTTP version: HTTP/1.1 (no HTTP/2 support)")
    print()


def demo_timeout_defaults():
    """Better timeout handling - httpx has sensible defaults"""
    print("=" * 60)
    print("3. TIMEOUT DEFAULTS - httpx has safer defaults")
    print("=" * 60)

    # httpx has a default 5-second timeout (safer)
    print("httpx - Default timeout: 5 seconds")
    print("requests - Default timeout: None (waits forever!)")

    # Custom timeout with httpx
    client = httpx.Client(timeout=10.0)
    response = client.get("https://httpbin.org/delay/1")
    print(f"httpx custom timeout example - Response time: {response.elapsed.total_seconds():.2f}s")
    client.close()
    print()


async def demo_async_support():
    """Async/await support - httpx's killer feature"""
    print("=" * 60)
    print("4. ASYNC SUPPORT - httpx natively supports async/await")
    print("=" * 60)

    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
    ]

    # Synchronous requests (with requests or httpx.Client)
    print("Synchronous requests (sequential):")
    start = time.time()
    for url in urls:
        _ = requests.get(url)
    sync_time = time.time() - start
    print(f"  Total time: {sync_time:.2f} seconds")

    # Asynchronous requests (httpx only)
    print("\nAsynchronous requests (concurrent with httpx.AsyncClient):")
    start = time.time()
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in urls]
        _ = await asyncio.gather(*tasks)
    async_time = time.time() - start
    print(f"  Total time: {async_time:.2f} seconds")
    print(f"  Speedup: {sync_time/async_time:.1f}x faster!")
    print()


def demo_connection_pooling():
    """Connection pooling and keep-alive"""
    print("=" * 60)
    print("5. CONNECTION POOLING - Both support it, but httpx is cleaner")
    print("=" * 60)

    # httpx with connection pooling (automatic with Client)
    urls = ["https://httpbin.org/get"] * 5

    print("httpx - Connection pooling with Client context manager:")
    start = time.time()
    with httpx.Client() as client:
        for url in urls:
            _ = client.get(url)
    httpx_time = time.time() - start
    print(f"  Time: {httpx_time:.2f} seconds")

    print("\nrequests - Connection pooling with Session:")
    start = time.time()
    with requests.Session() as session:
        for url in urls:
            _ = session.get(url)
    requests_time = time.time() - start
    print(f"  Time: {requests_time:.2f} seconds")
    print()


def demo_streaming():
    """Streaming responses"""
    print("=" * 60)
    print("6. STREAMING - Both support streaming, httpx has cleaner API")
    print("=" * 60)

    # httpx streaming
    print("httpx - Streaming response:")
    with httpx.stream("GET", "https://httpbin.org/stream/3") as response:
        chunks = 0
        for line in response.iter_lines():
            chunks += 1
        print(f"  Received {chunks} chunks")

    # requests streaming
    print("\nrequests - Streaming response:")
    with requests.get("https://httpbin.org/stream/3", stream=True) as response:
        chunks = 0
        for line in response.iter_lines():
            chunks += 1
        print(f"  Received {chunks} chunks")
    print()


def demo_modern_api():
    """Modern API features"""
    print("=" * 60)
    print("7. MODERN API - httpx has more intuitive method signatures")
    print("=" * 60)

    # httpx allows passing params, headers, and data more cleanly
    with httpx.Client(
        base_url="https://httpbin.org",
        headers={"User-Agent": "httpx-demo/1.0"},
        timeout=30.0,
    ) as client:
        # All requests use the base_url and default headers
        response = client.get("/headers")
        print("httpx - Client with base_url and default headers:")
        print(f"  Request URL: {response.request.url}")
        print(f"  User-Agent: {response.json()['headers']['User-Agent']}")

    # requests requires more manual configuration
    print("\nrequests - Requires Session for similar functionality:")
    session = requests.Session()
    session.headers.update({"User-Agent": "requests-demo/1.0"})
    response = session.get("https://httpbin.org/headers")
    print(f"  User-Agent: {response.json()['headers']['User-Agent']}")
    session.close()
    print()


async def demo_async_context_managers():
    """Async context managers and better resource management"""
    print("=" * 60)
    print("8. ASYNC CONTEXT MANAGERS - httpx AsyncClient is fully async")
    print("=" * 60)

    # httpx AsyncClient with proper async context management
    async with httpx.AsyncClient() as client:
        response = await client.get("https://httpbin.org/get")
        print(f"httpx AsyncClient - Status: {response.status_code}")
        print("  Properly manages async resources with context managers")

    print("\nrequests - No async support at all")
    print("  Would need to use aiohttp or httpx instead")
    print()


def main():
    """Run all demonstrations"""
    print("\n")
    print("=" * 60)
    print(" " * 10 + "HTTPX vs REQUESTS COMPARISON")
    print("=" * 60)
    print()

    # Synchronous demos
    demo_basic_requests()
    demo_http2_support()
    demo_timeout_defaults()
    demo_connection_pooling()
    demo_streaming()
    demo_modern_api()

    # Async demos
    asyncio.run(demo_async_support())
    asyncio.run(demo_async_context_managers())

    # Summary
    print("=" * 60)
    print("SUMMARY - Why httpx is better than requests:")
    print("=" * 60)
    print("+ HTTP/2 support (requests only has HTTP/1.1)")
    print("+ Native async/await support (requests has none)")
    print("+ Better timeout defaults (5s vs infinite)")
    print("+ Cleaner API with base_url support")
    print("+ Modern Python 3.8+ async context managers")
    print("+ Better connection pooling out of the box")
    print("+ Full requests API compatibility for easy migration")
    print("+ Active development and maintenance")
    print()
    print("Recommendation: Use httpx for new projects!")
    print("=" * 60)


if __name__ == "__main__":
    main()
