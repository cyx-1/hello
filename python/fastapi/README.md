# FastAPI Illustration

This example demonstrates FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Features Demonstrated

1. **Basic API Setup** - Creating a FastAPI application instance
2. **Path Parameters** - Extracting values from URL paths
3. **Query Parameters** - Handling URL query strings with validation
4. **Request Body Validation** - Using Pydantic models for automatic data validation
5. **HTTP Methods** - GET, POST, PUT, DELETE operations
6. **Response Models** - Custom response structures
7. **Dependency Injection** - Sharing logic across routes
8. **Background Tasks** - Non-blocking operations after response
9. **Async/Await** - Concurrent request handling
10. **Error Handling** - HTTP exceptions and validation errors
11. **Authentication** - Protected routes with token verification

## Key Source Code Sections

### 1. Data Models (Lines 30-47)

```python
class Item(BaseModel):
    """Example data model for an item."""
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)  # Line 39: Must be greater than 0
    tax: Optional[float] = Field(None, ge=0)

class ItemResponse(BaseModel):
    """Response model with computed fields."""
    name: str
    price: float
    total_price: float
```

### 2. FastAPI Application Instance (Lines 108-114)

```python
app = FastAPI(
    title="FastAPI Demo",
    description="A comprehensive demonstration of FastAPI features",
    version="1.0.0",
    lifespan=lifespan,
)
```

### 3. Simple GET Route (Lines 121-124)

```python
@app.get("/")  # Line 121: Decorator defines route
async def root():
    """Root endpoint - simplest possible route."""
    return {"message": "Welcome to FastAPI!", "docs": "/docs"}
```

### 4. Path Parameters (Lines 127-137)

```python
@app.get("/items/{item_id}")  # Line 127: {item_id} is a path parameter
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
```

### 5. POST with Request Body Validation (Lines 140-151)

```python
@app.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):  # Line 141: Pydantic model validates automatically
    """
    Create a new item with request body validation.
    - Uses Pydantic model for automatic validation
    - Returns a response model with computed fields
    - Sets custom status code (201 Created)
    """
    total_price = item.price + (item.tax or 0)
    items_db[item.name] = item.model_dump()
    return ItemResponse(name=item.name, price=item.price, total_price=total_price)
```

### 6. Query Parameters with Validation (Lines 154-168)

```python
@app.get("/items/")
async def list_items(
    skip: int = Query(0, ge=0),  # Line 156: Must be >= 0
    limit: int = Query(10, ge=1, le=100),  # Line 157: Between 1 and 100
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
```

### 7. Dependency Injection (Lines 187-198)

```python
@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User, timestamp: str = Depends(get_current_timestamp)):
    # Line 188: Depends() injects the timestamp from get_current_timestamp()
    """
    Create a user with dependency injection.
    - Uses Depends() to inject the current timestamp
    - Demonstrates how dependencies can provide computed values
    """
    user_data = user.model_dump()
    user_data["created_at"] = timestamp  # Timestamp injected by dependency
    users_db[user.username] = user_data
    return {"message": "User created", "user": user_data}
```

### 8. Background Tasks (Lines 206-214)

```python
@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    # Line 207: BackgroundTasks parameter enables async task scheduling
    """
    Demonstrate background tasks.
    - The background task runs after the response is sent
    - Client doesn't wait for the task to complete
    """
    background_tasks.add_task(write_log, f"Notification sent to {email}")
    return {"message": "Notification scheduled", "email": email}
```

### 9. Async Operations (Lines 226-239)

```python
@app.get("/async-demo")
async def async_demo():
    """Demonstrate async/await capabilities."""
    start = time.time()

    # Simulate multiple async operations
    async def fetch_data(delay: float, data_id: int):
        await asyncio.sleep(delay)
        return {"id": data_id, "data": f"Result {data_id}"}

    # Line 235: Run three operations concurrently (total time ~0.3s, not 0.6s)
    results = await asyncio.gather(
        fetch_data(0.2, 1), fetch_data(0.3, 2), fetch_data(0.1, 3)
    )

    duration = time.time() - start
    return {
        "results": results,
        "duration": f"{duration:.3f}s",
        "message": "Three async operations completed concurrently!",
    }
```

### 10. Protected Routes (Lines 246-255)

```python
@app.get("/protected")
async def protected_route(authorized: bool = Depends(verify_token)):
    # Line 247: Depends(verify_token) checks the token before allowing access
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
```

## Program Output

```
🚀 FastAPI Examples - Modern Python Web Framework


======================================================================
🚀 FastAPI Application Starting Up
======================================================================
✅ Initialized database with sample data

======================================================================
EXAMPLE 1: Root Endpoint (GET /)
======================================================================

Request:  GET /
Status:   200
Response: {'message': 'Welcome to FastAPI!', 'docs': '/docs'}
Code: @app.get('/') returns welcome message (main_fastapi.py:104)
```
**📝 Annotation:** The simplest FastAPI route. The `@app.get("/")` decorator (line 121) registers the function as a GET handler. FastAPI automatically converts the returned dictionary to JSON.

---

```
======================================================================
EXAMPLE 2: Path Parameters (GET /items/{item_id})
======================================================================

Request:  GET /items/42
Status:   200
Response: {'item_id': 42}
Code: @app.get('/items/{{item_id}}') - item_id extracted from URL
      (main_fastapi.py:110)
```
**📝 Annotation:** Path parameters are defined in curly braces `{item_id}` (line 127). FastAPI automatically extracts and validates the value - since `item_id: int` is declared, it must be an integer.

---

```
======================================================================
EXAMPLE 3: Query Parameters (GET /items/100?q=search)
======================================================================

Request:  GET /items/100?q=search
Status:   200
Response: {'item_id': 100, 'query': 'search'}
Code: Optional query parameter 'q' (main_fastapi.py:110)
```
**📝 Annotation:** Query parameters are function parameters not in the path. `q: Optional[str] = None` (line 127) makes it optional. FastAPI parses `?q=search` from the URL automatically.

---

```
======================================================================
EXAMPLE 4: POST with Request Body
======================================================================

Request:  POST /items/
Body:     {'name': 'Laptop', 'description': 'High-performance laptop', 'price': 1299.99, 'tax': 104.0}
Status:   201
Response: {'name': 'Laptop', 'price': 1299.99, 'total_price': 1403.99}
Code: Pydantic model validates input automatically
      (main_fastapi.py:127)
```
**📝 Annotation:** The `Item` Pydantic model (lines 30-39) validates the request body automatically. The `status_code=status.HTTP_201_CREATED` (line 140) returns 201 instead of the default 200. The computed `total_price` is calculated in the endpoint (line 148).

---

```
======================================================================
EXAMPLE 5: Validation Error (Invalid Data)
======================================================================

Request:  POST /items/
Body:     {'name': 'Invalid', 'price': -10}
Status:   422
Response: {'detail': [{'type': 'greater_than', 'loc': ['body', 'price'], 'msg': 'Input should be greater than 0', 'input': -10, 'ctx': {'gt': 0.0}}]}
Code: Field validation with 'gt=0' catches negative price
      (main_fastapi.py:39)
```
**📝 Annotation:** When validation fails, FastAPI automatically returns a 422 Unprocessable Entity status with detailed error information. The `Field(..., gt=0)` constraint (line 39) enforces that price must be positive.

---

```
======================================================================
EXAMPLE 6: List Items with Query Parameters
======================================================================

Request:  GET /items/?skip=0&limit=5&sort=true
Status:   200
Response: {'items': [{'name': 'Keyboard', 'description': None, 'price': 79.99, 'tax': 6.4}, {'name': 'Laptop', 'description': 'High-performance laptop', 'price': 1299.99, 'tax': 104.0}, {'name': 'Mouse', 'description': None, 'price': 25.99, 'tax': 2.0}, {'name': 'Sample Item', 'price': 29.99, 'tax': 2.99}], 'total': 4}
Code: Query parameters with validation (main_fastapi.py:147)
```
**📝 Annotation:** Multiple query parameters with constraints: `Query(0, ge=0)` means default 0, must be >= 0 (line 156). `Query(10, ge=1, le=100)` means default 10, must be between 1 and 100 (line 157). Items are sorted alphabetically by name when `sort=true`.

---

```
======================================================================
EXAMPLE 7: PUT - Update an Item
======================================================================

Request:  PUT /items/Laptop
Body:     {'name': 'Laptop', 'description': 'Updated description', 'price': 1199.99, 'tax': 96.0}
Status:   200
Response: {'message': "Item 'Laptop' updated successfully", 'item': {'name': 'Laptop', 'description': 'Updated description', 'price': 1199.99, 'tax': 96.0}}
Code: PUT method updates existing resource (main_fastapi.py:167)
```
**📝 Annotation:** The `@app.put()` decorator (line 171) handles PUT requests for updates. The endpoint checks if the item exists (line 172) and raises a 404 HTTPException if not found.

---

```
======================================================================
EXAMPLE 8: Dependency Injection
======================================================================

Request:  POST /users/
Body:     {'username': 'johndoe', 'email': 'john@example.com', 'full_name': 'John Doe'}
Status:   201
Response: {'message': 'User created', 'user': {'username': 'johndoe', 'email': 'john@example.com', 'full_name': 'John Doe', 'created_at': '2025-11-04 15:01:55'}}
Code: Depends(get_current_timestamp) injects timestamp
      (main_fastapi.py:187)
```
**📝 Annotation:** `Depends(get_current_timestamp)` (line 188) is a dependency that executes before the handler and injects its return value. This allows sharing common logic (like timestamps, auth, database connections) across routes. The timestamp is automatically added without the client sending it.

---

```
======================================================================
EXAMPLE 9: Background Tasks
======================================================================

Request:  POST /send-notification/user@example.com
Status:   200
Response: {'message': 'Notification scheduled', 'email': 'user@example.com'}
Code: background_tasks.add_task() runs after response
      (main_fastapi.py:206)

Request:  GET /logs/
Status:   200
Response: {'logs': [{'message': 'Notification sent to user@example.com', 'timestamp': 1762268516.4941607}], 'count': 1}
Background task completed and logged!
```
**📝 Annotation:** `background_tasks.add_task()` (line 214) schedules a function to run *after* sending the response to the client. The response is immediate (doesn't wait for the 1-second sleep in `write_log`). This is useful for tasks like sending emails, processing uploads, or logging that don't need to block the response.

---

```
======================================================================
EXAMPLE 10: Async/Await - Concurrent Operations
======================================================================

Request:  GET /async-demo
Status:   200
Response: {'results': [{'id': 1, 'data': 'Result 1'}, {'id': 2, 'data': 'Result 2'}, {'id': 3, 'data': 'Result 3'}], 'duration': '0.303s', 'message': 'Three async operations completed concurrently!'}
Code: asyncio.gather() runs multiple operations concurrently
      (main_fastapi.py:226)
```
**📝 Annotation:** `asyncio.gather()` (line 235) runs multiple async operations concurrently. The three fetches (0.2s, 0.3s, 0.1s) complete in ~0.3s total instead of 0.6s sequentially. FastAPI's async support enables handling thousands of concurrent requests efficiently.

---

```
======================================================================
EXAMPLE 11: Protected Route - No Token (401)
======================================================================

Request:  GET /protected
Status:   401
Response: {'detail': 'Invalid or missing token'}
Code: Depends(verify_token) checks authentication
      (main_fastapi.py:246)
```
**📝 Annotation:** The `verify_token` dependency (line 247) checks for a valid token. Without it, the endpoint raises an HTTP 401 Unauthorized exception (line 250).

---

```
======================================================================
EXAMPLE 12: Protected Route - With Valid Token (200)
======================================================================

Request:  GET /protected?token=secret-token
Status:   200
Response: {'message': 'Access granted to protected resource!'}
Code: Valid token grants access (main_fastapi.py:246)
```
**📝 Annotation:** When the correct token is provided (`token=secret-token`), the dependency returns `True` and access is granted. This pattern can be extended to JWT tokens, OAuth2, API keys, etc.

---

```
======================================================================
EXAMPLE 13: DELETE an Item
======================================================================

Request:  DELETE /items/Mouse
Status:   200
Response: {'message': "Item 'Mouse' deleted successfully"}
Code: DELETE method removes resource (main_fastapi.py:179)
```
**📝 Annotation:** The `@app.delete()` decorator (line 183) handles DELETE requests. The endpoint removes the item from the database and returns a success message.

---

```
======================================================================
✨ All FastAPI demonstrations completed!
======================================================================

📚 Additional Features:
  • Automatic API documentation at /docs (Swagger UI)
  • Alternative docs at /redoc (ReDoc)
  • OpenAPI schema at /openapi.json
  • Type safety with Python type hints
  • High performance (comparable to NodeJS and Go)
======================================================================
```
**📝 Annotation:** FastAPI automatically generates interactive API documentation at `/docs` (Swagger UI) and `/redoc` (ReDoc) based on your code. No extra configuration needed! The framework uses Python type hints for validation, serialization, and documentation.

## Running the Example

```bash
# Run the demonstration (starts server and makes test requests)
uv run python main_fastapi.py

# Or run the server manually (interactive mode)
uv run uvicorn main_fastapi:app --reload

# Then visit:
# - http://127.0.0.1:8000/docs for Swagger UI
# - http://127.0.0.1:8000/redoc for ReDoc
# - http://127.0.0.1:8000 for the API
```

## Requirements

- **Python Version**: 3.11 or higher
- **Key Dependencies**:
  - `fastapi>=0.115.0` - The web framework
  - `uvicorn>=0.32.0` - ASGI server for running FastAPI
  - `httpx>=0.28.0` - Async HTTP client for testing

## Key Concepts Illustrated

### 1. Type Safety & Automatic Validation
FastAPI uses Python type hints to:
- Validate request data automatically
- Generate API documentation
- Provide editor autocompletion
- Serialize/deserialize data

### 2. Pydantic Models
Pydantic models (lines 30-47) define data schemas with:
- Type validation
- Field constraints (min_length, gt, ge, le)
- Optional fields
- Default values

### 3. Dependency Injection
Dependencies (lines 62-69) provide reusable logic:
- Authentication/authorization
- Database connections
- Shared computations
- Request context

### 4. Async/Await
FastAPI fully supports async:
- Non-blocking I/O operations
- Concurrent request handling
- Compatible with async libraries
- Can mix sync and async functions

### 5. HTTP Methods
Complete REST API support:
- GET - Read data
- POST - Create resources
- PUT - Update resources
- DELETE - Remove resources

### 6. Error Handling
Automatic and manual error handling:
- Validation errors (422)
- HTTP exceptions (400, 401, 404, 500)
- Custom error responses
- Detailed error messages

## Why FastAPI?

1. **Fast**: Very high performance, on par with NodeJS and Go
2. **Fast to code**: Reduce development time by ~40%
3. **Fewer bugs**: Reduce human-induced errors by ~40%
4. **Intuitive**: Great editor support with autocompletion
5. **Easy**: Designed to be easy to learn and use
6. **Short**: Minimize code duplication
7. **Robust**: Production-ready code with automatic docs
8. **Standards-based**: Based on OpenAPI and JSON Schema

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
