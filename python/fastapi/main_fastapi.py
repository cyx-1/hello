# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "fastapi>=0.115.0",
#     "uvicorn>=0.32.0",
#     "httpx>=0.28.0",
# ]
# ///
"""
FastAPI Web Framework Example: Modern, Fast, and Type-Safe API Development

This example demonstrates the key features of FastAPI:
1. Basic API setup and path operations
2. Path parameters and query parameters
3. Request body with Pydantic models
4. Different HTTP methods (GET, POST, PUT, DELETE)
5. Response models and status codes
6. Dependency injection
7. Background tasks
8. Async/await support
9. Automatic API documentation

FastAPI is a modern web framework for building APIs with Python 3.7+
based on standard Python type hints.
"""

import asyncio
import time
from contextlib import asynccontextmanager
from typing import Optional

import httpx
import uvicorn
from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field


# ============================================================================
# Data Models using Pydantic
# ============================================================================


class Item(BaseModel):
    """Example data model for an item."""

    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)
    tax: Optional[float] = Field(None, ge=0)


class ItemResponse(BaseModel):
    """Response model with computed fields."""

    name: str
    price: float
    total_price: float


class User(BaseModel):
    """User model."""

    username: str
    email: str
    full_name: Optional[str] = None


# ============================================================================
# In-memory database (for demonstration)
# ============================================================================

items_db = {}
users_db = {}
task_log = []


# ============================================================================
# Dependency Injection Examples
# ============================================================================


def get_current_timestamp() -> str:
    """Dependency that provides current timestamp."""
    return time.strftime("%Y-%m-%d %H:%M:%S")


async def verify_token(token: str = Query(None)) -> bool:
    """Simulated token verification (dependency)."""
    if token == "secret-token":
        return True
    return False


# ============================================================================
# Lifespan Event Handler
# ============================================================================


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events."""
    # Startup
    print("\n" + "=" * 70)
    print("🚀 FastAPI Application Starting Up")
    print("=" * 70)
    items_db["sample"] = {"name": "Sample Item", "price": 29.99, "tax": 2.99}
    print("✅ Initialized database with sample data")

    yield  # Application runs

    # Shutdown
    print("\n" + "=" * 70)
    print("🛑 FastAPI Application Shutting Down")
    print("=" * 70)


# ============================================================================
# FastAPI Application Instance
# ============================================================================

app = FastAPI(
    title="FastAPI Demo",
    description="A comprehensive demonstration of FastAPI features",
    version="1.0.0",
    lifespan=lifespan,
)


# ============================================================================
# Path Operations (Route Handlers)
# ============================================================================


@app.get("/")
async def root():
    """Root endpoint - simplest possible route."""
    return {"message": "Welcome to FastAPI!", "docs": "/docs"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    """
    Example of path parameters and query parameters.

    - item_id: Path parameter (required, must be an integer)
    - q: Query parameter (optional, can be a string)
    """
    result = {"item_id": item_id}
    if q:
        result["query"] = q
    return result


@app.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    """
    Create a new item with request body validation.

    - Uses Pydantic model for automatic validation
    - Returns a response model with computed fields
    - Sets custom status code (201 Created)
    """
    total_price = item.price + (item.tax or 0)
    items_db[item.name] = item.model_dump()

    return ItemResponse(name=item.name, price=item.price, total_price=total_price)


@app.get("/items/")
async def list_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    sort: bool = Query(False),
):
    """
    List items with query parameters and validation.

    - skip: Offset for pagination (>= 0)
    - limit: Number of items to return (1-100)
    - sort: Whether to sort by name
    """
    item_list = list(items_db.values())

    if sort:
        item_list = sorted(item_list, key=lambda x: x.get("name", ""))

    return {"items": item_list[skip : skip + limit], "total": len(items_db)}


@app.put("/items/{item_name}")
async def update_item(item_name: str, item: Item):
    """Update an existing item (PUT method)."""
    if item_name not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )

    items_db[item_name] = item.model_dump()
    return {"message": f"Item '{item_name}' updated successfully", "item": item}


@app.delete("/items/{item_name}")
async def delete_item(item_name: str):
    """Delete an item (DELETE method)."""
    if item_name not in items_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )

    del items_db[item_name]
    return {"message": f"Item '{item_name}' deleted successfully"}


@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User, timestamp: str = Depends(get_current_timestamp)):
    """
    Create a user with dependency injection.

    - Uses Depends() to inject the current timestamp
    - Demonstrates how dependencies can provide computed values
    """
    user_data = user.model_dump()
    user_data["created_at"] = timestamp
    users_db[user.username] = user_data

    return {"message": "User created", "user": user_data}


def write_log(message: str):
    """Background task function."""
    time.sleep(1)  # Simulate slow operation
    task_log.append({"message": message, "timestamp": time.time()})


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    """
    Demonstrate background tasks.

    - The background task runs after the response is sent
    - Client doesn't wait for the task to complete
    """
    background_tasks.add_task(write_log, f"Notification sent to {email}")
    return {"message": "Notification scheduled", "email": email}


@app.get("/logs/")
async def get_logs():
    """Retrieve the background task log."""
    return {"logs": task_log, "count": len(task_log)}


@app.get("/async-demo")
async def async_demo():
    """
    Demonstrate async/await capabilities.

    FastAPI handles both sync and async functions, but async
    functions allow for concurrent operations without blocking.
    """
    start = time.time()

    # Simulate multiple async operations
    async def fetch_data(delay: float, data_id: int):
        await asyncio.sleep(delay)
        return {"id": data_id, "data": f"Result {data_id}"}

    # Run three operations concurrently (total time ~0.3s, not 0.6s)
    results = await asyncio.gather(
        fetch_data(0.2, 1), fetch_data(0.3, 2), fetch_data(0.1, 3)
    )

    duration = time.time() - start

    return {
        "results": results,
        "duration": f"{duration:.3f}s",
        "message": "Three async operations completed concurrently!",
    }


@app.get("/protected")
async def protected_route(authorized: bool = Depends(verify_token)):
    """
    Protected route using dependency injection for auth.

    Try: /protected?token=secret-token
    """
    if not authorized:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token",
        )
    return {"message": "Access granted to protected resource!"}


# ============================================================================
# Client demonstration function
# ============================================================================


async def demonstrate_api():
    """
    Demonstrate the FastAPI application by making requests.

    This function starts the server and makes HTTP requests to showcase
    all the features.
    """

    def print_section(title: str):
        """Print a formatted section header."""
        print(f"\n{'=' * 70}")
        print(f"{title}")
        print(f"{'=' * 70}\n")

    # Give server time to start
    await asyncio.sleep(2)

    base_url = "http://127.0.0.1:8000"

    async with httpx.AsyncClient() as client:
        print_section("EXAMPLE 1: Root Endpoint (GET /)")
        response = await client.get(f"{base_url}/")
        print("Request:  GET /")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: @app.get('/') returns welcome message (main_fastapi.py:104)")

        print_section("EXAMPLE 2: Path Parameters (GET /items/{item_id})")
        response = await client.get(f"{base_url}/items/42")
        print("Request:  GET /items/42")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: @app.get('/items/{{item_id}}') - item_id extracted from URL")
        print("      (main_fastapi.py:110)")

        print_section("EXAMPLE 3: Query Parameters (GET /items/100?q=search)")
        response = await client.get(f"{base_url}/items/100?q=search")
        print("Request:  GET /items/100?q=search")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: Optional query parameter 'q' (main_fastapi.py:110)")

        print_section("EXAMPLE 4: POST with Request Body")
        item_data = {
            "name": "Laptop",
            "description": "High-performance laptop",
            "price": 1299.99,
            "tax": 104.00,
        }
        response = await client.post(f"{base_url}/items/", json=item_data)
        print("Request:  POST /items/")
        print(f"Body:     {item_data}")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: Pydantic model validates input automatically")
        print("      (main_fastapi.py:127)")

        print_section("EXAMPLE 5: Validation Error (Invalid Data)")
        invalid_data = {"name": "Invalid", "price": -10}  # Negative price!
        try:
            response = await client.post(f"{base_url}/items/", json=invalid_data)
            print("Request:  POST /items/")
            print(f"Body:     {invalid_data}")
            print(f"Status:   {response.status_code}")
            print(f"Response: {response.json()}")
            print("Code: Field validation with 'gt=0' catches negative price")
            print("      (main_fastapi.py:39)")
        except httpx.HTTPStatusError:
            print("Validation error caught!")

        print_section("EXAMPLE 6: List Items with Query Parameters")
        # Add more items first
        await client.post(
            f"{base_url}/items/",
            json={"name": "Mouse", "price": 25.99, "tax": 2.00},
        )
        await client.post(
            f"{base_url}/items/",
            json={"name": "Keyboard", "price": 79.99, "tax": 6.40},
        )

        response = await client.get(f"{base_url}/items/?skip=0&limit=5&sort=true")
        print("Request:  GET /items/?skip=0&limit=5&sort=true")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: Query parameters with validation (main_fastapi.py:147)")

        print_section("EXAMPLE 7: PUT - Update an Item")
        update_data = {
            "name": "Laptop",
            "description": "Updated description",
            "price": 1199.99,
            "tax": 96.00,
        }
        response = await client.put(f"{base_url}/items/Laptop", json=update_data)
        print("Request:  PUT /items/Laptop")
        print(f"Body:     {update_data}")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: PUT method updates existing resource (main_fastapi.py:167)")

        print_section("EXAMPLE 8: Dependency Injection")
        user_data = {
            "username": "johndoe",
            "email": "john@example.com",
            "full_name": "John Doe",
        }
        response = await client.post(f"{base_url}/users/", json=user_data)
        print("Request:  POST /users/")
        print(f"Body:     {user_data}")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: Depends(get_current_timestamp) injects timestamp")
        print("      (main_fastapi.py:187)")

        print_section("EXAMPLE 9: Background Tasks")
        response = await client.post(f"{base_url}/send-notification/user@example.com")
        print("Request:  POST /send-notification/user@example.com")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: background_tasks.add_task() runs after response")
        print("      (main_fastapi.py:206)")

        # Wait for background task
        await asyncio.sleep(2)

        response = await client.get(f"{base_url}/logs/")
        print("\nRequest:  GET /logs/")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Background task completed and logged!")

        print_section("EXAMPLE 10: Async/Await - Concurrent Operations")
        response = await client.get(f"{base_url}/async-demo")
        print("Request:  GET /async-demo")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: asyncio.gather() runs multiple operations concurrently")
        print("      (main_fastapi.py:226)")

        print_section("EXAMPLE 11: Protected Route - No Token (401)")
        response = await client.get(f"{base_url}/protected")
        print("Request:  GET /protected")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: Depends(verify_token) checks authentication")
        print("      (main_fastapi.py:246)")

        print_section("EXAMPLE 12: Protected Route - With Valid Token (200)")
        response = await client.get(f"{base_url}/protected?token=secret-token")
        print("Request:  GET /protected?token=secret-token")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: Valid token grants access (main_fastapi.py:246)")

        print_section("EXAMPLE 13: DELETE an Item")
        response = await client.delete(f"{base_url}/items/Mouse")
        print("Request:  DELETE /items/Mouse")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: DELETE method removes resource (main_fastapi.py:179)")

        print_section("EXAMPLE 14: 404 Not Found Error")
        response = await client.get(f"{base_url}/items/NonExistent")
        print("Request:  GET /items/NonExistent")
        print(f"Status:   {response.status_code}")
        print(f"Response: {response.json()}")
        print("Code: HTTPException raises proper error responses")

        print("\n" + "=" * 70)
        print("✨ All FastAPI demonstrations completed!")
        print("=" * 70)
        print("\n📚 Additional Features:")
        print("  • Automatic API documentation at /docs (Swagger UI)")
        print("  • Alternative docs at /redoc (ReDoc)")
        print("  • OpenAPI schema at /openapi.json")
        print("  • Type safety with Python type hints")
        print("  • High performance (comparable to NodeJS and Go)")
        print("=" * 70 + "\n")


async def run_server():
    """Run the FastAPI server."""
    config = uvicorn.Config(
        app, host="127.0.0.1", port=8000, log_level="warning", loop="asyncio"
    )
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    """Main entry point - runs server and demonstration concurrently."""
    print("\n🚀 FastAPI Examples - Modern Python Web Framework\n")

    # Run server and demo concurrently
    server_task = asyncio.create_task(run_server())
    demo_task = asyncio.create_task(demonstrate_api())

    # Wait for demo to complete
    await demo_task

    # Cancel server
    server_task.cancel()
    try:
        await server_task
    except asyncio.CancelledError:
        print("Server stopped.")


if __name__ == "__main__":
    asyncio.run(main())
