#!/usr/bin/env python3
"""
ASGI Application with Uvicorn and Pytest Testing

This demonstrates:
1. Building an ASGI application with FastAPI
2. Running it with Uvicorn server
3. Testing with pytest WITHOUT launching the server using TestClient

# /// script
# dependencies = [
#   "fastapi>=0.115.0",
#   "uvicorn>=0.32.0",
# ]
# ///
"""

from fastapi import FastAPI, HTTPException
from typing import Any, Dict, List

# Create the ASGI application
app = FastAPI(title="ASGI Demo API", version="1.0.0")

# In-memory database for demonstration
users_db: Dict[int, Dict[str, str]] = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
}


@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint returning welcome message."""
    return {"message": "Welcome to ASGI Demo API"}


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "healthy", "server": "uvicorn", "protocol": "ASGI"}


@app.get("/users")
async def list_users() -> List[Dict[str, Any]]:
    """List all users."""
    return [{"id": uid, **user} for uid, user in users_db.items()]


@app.get("/users/{user_id}")
async def get_user(user_id: int) -> Dict[str, Any]:
    """Get a specific user by ID."""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user_id, **users_db[user_id]}


@app.post("/users")
async def create_user(name: str, email: str) -> Dict[str, Any]:
    """Create a new user."""
    new_id = max(users_db.keys()) + 1 if users_db else 1
    users_db[new_id] = {"name": name, "email": email}
    return {"id": new_id, "name": name, "email": email}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int) -> Dict[str, str]:
    """Delete a user by ID."""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": f"User {user_id} deleted successfully"}


if __name__ == "__main__":
    import uvicorn

    print("Starting ASGI application with Uvicorn...")
    print("Access the API at: http://localhost:8000")
    print("View API docs at: http://localhost:8000/docs")

    # Run the ASGI app with Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
