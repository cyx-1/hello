# ASGI with Uvicorn and Pytest Testing (No Server Required)

This demonstration illustrates:
1. **ASGI Application** - Building an async web application with FastAPI
2. **Uvicorn Server** - Running ASGI apps with a production-ready server
3. **Pytest Testing** - Testing ASGI apps WITHOUT launching a server using TestClient

## Key Concept: Testing Without a Server

The TestClient from FastAPI/Starlette allows you to test ASGI applications **directly** without starting an HTTP server. This means:
- ✅ No network overhead - tests run in-process
- ✅ Faster test execution
- ✅ No port conflicts or server cleanup needed
- ✅ Full access to application state for testing

## Main Application Code

**File: `main_asgi_uvicorn.py`**

```python
 1  #!/usr/bin/env python3
 2  """
 3  ASGI Application with Uvicorn and Pytest Testing
 4
 5  This demonstrates:
 6  1. Building an ASGI application with FastAPI
 7  2. Running it with Uvicorn server
 8  3. Testing with pytest WITHOUT launching the server using TestClient
 9
10  # /// script
11  # dependencies = [
12  #   "fastapi>=0.115.0",
13  #   "uvicorn>=0.32.0",
14  # ]
15  # ///
16  """
17
18  from fastapi import FastAPI, HTTPException
19  from typing import Any, Dict, List
20
21  # Create the ASGI application
22  app = FastAPI(title="ASGI Demo API", version="1.0.0")
23
24  # In-memory database for demonstration
25  users_db: Dict[int, Dict[str, str]] = {
26      1: {"name": "Alice", "email": "alice@example.com"},
27      2: {"name": "Bob", "email": "bob@example.com"},
28  }
29
30
31  @app.get("/")
32  async def root() -> Dict[str, str]:
33      """Root endpoint returning welcome message."""
34      return {"message": "Welcome to ASGI Demo API"}
35
36
37  @app.get("/health")
38  async def health_check() -> Dict[str, str]:
39      """Health check endpoint."""
40      return {"status": "healthy", "server": "uvicorn", "protocol": "ASGI"}
41
42
43  @app.get("/users")
44  async def list_users() -> List[Dict[str, Any]]:
45      """List all users."""
46      return [{"id": uid, **user} for uid, user in users_db.items()]
47
48
49  @app.get("/users/{user_id}")
50  async def get_user(user_id: int) -> Dict[str, Any]:
51      """Get a specific user by ID."""
52      if user_id not in users_db:
53          raise HTTPException(status_code=404, detail="User not found")
54      return {"id": user_id, **users_db[user_id]}
55
56
57  @app.post("/users")
58  async def create_user(name: str, email: str) -> Dict[str, Any]:
59      """Create a new user."""
60      new_id = max(users_db.keys()) + 1 if users_db else 1
61      users_db[new_id] = {"name": name, "email": email}
62      return {"id": new_id, "name": name, "email": email}
63
64
65  @app.delete("/users/{user_id}")
66  async def delete_user(user_id: int) -> Dict[str, str]:
67      """Delete a user by ID."""
68      if user_id not in users_db:
69          raise HTTPException(status_code=404, detail="User not found")
70      del users_db[user_id]
71      return {"message": f"User {user_id} deleted successfully"}
72
73
74  if __name__ == "__main__":
75      import uvicorn
76
77      print("Starting ASGI application with Uvicorn...")
78      print("Access the API at: http://localhost:8000")
79      print("View API docs at: http://localhost:8000/docs")
80
81      # Run the ASGI app with Uvicorn
82      uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
```

### Code Annotations

**Lines 10-15**: Inline script metadata using [PEP 723](https://peps.python.org/pep-0723/) format. This allows `uv run` to automatically install dependencies without needing a `pyproject.toml`.

**Line 22**: Creates the ASGI application instance. FastAPI is built on top of Starlette and implements the ASGI (Asynchronous Server Gateway Interface) specification.

**Lines 25-28**: In-memory database for demonstration. In production, you'd use a real database.

**Lines 31-34**: Async route handler (line 32). The `async def` syntax is key to ASGI - it allows handling multiple requests concurrently without blocking.

**Lines 49-54**: Demonstrates HTTP error handling (line 53). FastAPI's `HTTPException` is converted to proper HTTP responses.

**Line 82**: `uvicorn.run()` starts the ASGI server. Uvicorn is a lightning-fast ASGI server implementation using uvloop and httptools.

## Test Code (Testing Without Server)

**File: `test_asgi_uvicorn.py`**

```python
 1  #!/usr/bin/env python3
 2  """
 3  Pytest tests for ASGI application WITHOUT launching the server.
 4
 5  This demonstrates how to test an ASGI application using TestClient,
 6  which directly calls the ASGI app without starting an HTTP server.
 7
 8  # /// script
 9  # dependencies = [
10  #   "fastapi>=0.115.0",
11  #   "uvicorn>=0.32.0",
12  #   "pytest>=8.3.0",
13  #   "httpx>=0.27.0",
14  # ]
15  # ///
16  """
17
18  import pytest
19  from fastapi.testclient import TestClient
20  from main_asgi_uvicorn import app, users_db
21
22
23  @pytest.fixture(autouse=True)
24  def reset_database():
25      """Reset the database before each test."""
26      users_db.clear()
27      users_db.update({
28          1: {"name": "Alice", "email": "alice@example.com"},
29          2: {"name": "Bob", "email": "bob@example.com"},
30      })
31      yield
32      users_db.clear()
33
34
35  # Create TestClient - NO SERVER REQUIRED!
36  # TestClient directly calls the ASGI application without HTTP overhead
37  client = TestClient(app)
38
39
40  def test_root_endpoint():
41      """Test the root endpoint returns welcome message."""
42      response = client.get("/")
43      assert response.status_code == 200
44      assert response.json() == {"message": "Welcome to ASGI Demo API"}
45      print("✓ Root endpoint test passed")
46
47
48  def test_health_check():
49      """Test the health check endpoint."""
50      response = client.get("/health")
51      assert response.status_code == 200
52      data = response.json()
53      assert data["status"] == "healthy"
54      assert data["server"] == "uvicorn"
55      assert data["protocol"] == "ASGI"
56      print("✓ Health check test passed")
57
58
59  def test_list_users():
60      """Test listing all users."""
61      response = client.get("/users")
62      assert response.status_code == 200
63      users = response.json()
64      assert len(users) == 2
65      assert users[0]["name"] == "Alice"
66      assert users[1]["name"] == "Bob"
67      print("✓ List users test passed")
68
69
70  def test_get_user_success():
71      """Test getting a specific user that exists."""
72      response = client.get("/users/1")
73      assert response.status_code == 200
74      user = response.json()
75      assert user["id"] == 1
76      assert user["name"] == "Alice"
77      assert user["email"] == "alice@example.com"
78      print("✓ Get user success test passed")
79
80
81  def test_get_user_not_found():
82      """Test getting a user that doesn't exist returns 404."""
83      response = client.get("/users/999")
84      assert response.status_code == 404
85      assert response.json()["detail"] == "User not found"
86      print("✓ Get user not found test passed")
87
88
89  def test_create_user():
90      """Test creating a new user."""
91      response = client.post("/users?name=Charlie&email=charlie@example.com")
92      assert response.status_code == 200
93      user = response.json()
94      assert user["id"] == 3  # Should be next available ID
95      assert user["name"] == "Charlie"
96      assert user["email"] == "charlie@example.com"
97
98      # Verify the user was actually created
99      verify_response = client.get("/users/3")
100     assert verify_response.status_code == 200
101     print("✓ Create user test passed")
102
103
104 def test_delete_user_success():
105     """Test deleting an existing user."""
106     response = client.delete("/users/1")
107     assert response.status_code == 200
108     assert response.json()["message"] == "User 1 deleted successfully"
109
110     # Verify the user was actually deleted
111     verify_response = client.get("/users/1")
112     assert verify_response.status_code == 404
113     print("✓ Delete user success test passed")
114
115
116 def test_delete_user_not_found():
117     """Test deleting a user that doesn't exist."""
118     response = client.delete("/users/999")
119     assert response.status_code == 404
120     assert response.json()["detail"] == "User not found"
121     print("✓ Delete user not found test passed")
122
123
124 def test_asgi_app_characteristics():
125     """
126     Demonstrate that we're testing the ASGI app directly.
127     No server is running - TestClient calls the ASGI app in-process.
128     """
129     # Multiple rapid requests - no network latency!
130     responses = [client.get("/health") for _ in range(10)]
131     assert all(r.status_code == 200 for r in responses)
132     print("✓ ASGI direct testing - 10 requests with zero network overhead")
```

### Test Code Annotations

**Lines 8-15**: Inline dependencies include `pytest` and `httpx`. The `httpx` library is used internally by TestClient for ASGI communication.

**Line 19**: Import `TestClient` from FastAPI - this is the key to testing without a server!

**Lines 23-32**: Pytest fixture with `autouse=True` ensures the database is reset before each test. This provides test isolation.

**Line 37**: **Critical Line** - Create TestClient instance. This wraps your ASGI app and provides an HTTP client interface, but **NO SERVER IS STARTED**. All requests go directly to the ASGI callable.

**Line 42**: Use `client.get()` just like you would with requests, but it calls the ASGI app directly in-process.

**Lines 99-100**: Tests can make multiple requests in sequence to verify state changes.

**Lines 129-131**: Demonstrates the performance benefit - 10 requests with zero network latency because there's no actual HTTP connection.

## Running the Code

### Option 1: Run the Server

```bash
$ uv run main_asgi_uvicorn.py
```

**Output:**
```
Starting ASGI application with Uvicorn...
Access the API at: http://localhost:8000
View API docs at: http://localhost:8000/docs
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Option 2: Run Tests (No Server Required!)

```bash
$ uv run test_asgi_uvicorn.py
```

**Output:**
```
============================================================
Testing ASGI Application WITHOUT launching server
============================================================

============================= test session starts ==============================
platform linux -- Python 3.11.14, pytest-9.0.1, pluggy-1.6.0 -- /python3
cachedir: .pytest_cache
rootdir: /home/user/hello/python/asgi_uvicorn_pytest
plugins: anyio-4.11.0
collecting ... collected 9 items

test_asgi_uvicorn.py::test_root_endpoint PASSED                          [ 11%]
test_asgi_uvicorn.py::test_health_check PASSED                           [ 22%]
test_asgi_uvicorn.py::test_list_users PASSED                             [ 33%]
test_asgi_uvicorn.py::test_get_user_success PASSED                       [ 44%]
test_asgi_uvicorn.py::test_get_user_not_found PASSED                     [ 55%]
test_asgi_uvicorn.py::test_create_user PASSED                            [ 66%]
test_asgi_uvicorn.py::test_delete_user_success PASSED                    [ 77%]
test_asgi_uvicorn.py::test_delete_user_not_found PASSED                  [ 88%]
test_asgi_uvicorn.py::test_asgi_app_characteristics PASSED               [100%]

========================= 9 passed, 1 warning in 0.13s =========================
```

### Output Analysis

- **Line: `collecting ... collected 9 items`** - Pytest discovers all test functions (those starting with `test_`)
- **All tests PASSED** - Each test successfully validates the ASGI app behavior
- **`in 0.13s`** - Tests complete in milliseconds because there's no server startup/shutdown overhead
- **No server logs** - Notice there are NO uvicorn server logs (like "Started server process") because no server was started!

## Key Concepts Demonstrated

### 1. ASGI (Asynchronous Server Gateway Interface)
- Modern Python web standard for async applications
- Successor to WSGI, designed for async/await
- See `async def` handlers in lines 32, 38, 44, 50, 58, 66 of main_asgi_uvicorn.py

### 2. Uvicorn
- Lightning-fast ASGI server implementation
- Uses `uvloop` (libuv-based event loop) for high performance
- Invoked on line 82 of main_asgi_uvicorn.py

### 3. TestClient - Testing Without Server
- **How it works**: TestClient implements the ASGI interface and calls your app directly
- **Benefits**: No network overhead, instant test execution, no port conflicts
- **Key difference**: `client.get("/")` calls the ASGI app function directly, not via HTTP
- Created on line 37 of test_asgi_uvicorn.py

### 4. FastAPI
- Modern web framework built on ASGI
- Automatic OpenAPI documentation (available at `/docs` when server runs)
- Type hints provide automatic validation and serialization

## Technical Notes

- **Python Version**: Works with Python 3.7+ (async/await support required)
- **No pyproject.toml**: Uses PEP 723 inline script metadata for dependency management
- **TestClient vs Requests**: TestClient has the same API as `requests`, but doesn't use network
- **Async Testing**: TestClient handles the async event loop automatically - you can use regular `def` test functions, not `async def`

## Why This Approach Matters

Traditional testing might start a server in a subprocess or background thread:
```python
# Traditional approach (NOT recommended for unit tests)
server = subprocess.Popen(["uvicorn", "main:app"])
response = requests.get("http://localhost:8000")  # Actual HTTP request
server.kill()
```

Problems with traditional approach:
- ❌ Slow - server startup/shutdown takes time
- ❌ Port conflicts - tests might fail if port is in use
- ❌ Cleanup issues - servers might not terminate properly
- ❌ Network dependency - requires working network stack

TestClient approach:
- ✅ Fast - no server overhead
- ✅ Reliable - no port conflicts
- ✅ Clean - no process management
- ✅ Pure - tests run in same process, easy to debug

## References

- [ASGI Specification](https://asgi.readthedocs.io/)
- [FastAPI Testing Documentation](https://fastapi.tiangolo.com/tutorial/testing/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [PEP 723 - Inline Script Metadata](https://peps.python.org/pep-0723/)
