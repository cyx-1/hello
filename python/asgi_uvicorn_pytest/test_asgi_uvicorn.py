#!/usr/bin/env python3
"""
Pytest tests for ASGI application WITHOUT launching the server.

This demonstrates how to test an ASGI application using TestClient,
which directly calls the ASGI app without starting an HTTP server.

# /// script
# dependencies = [
#   "fastapi>=0.115.0",
#   "uvicorn>=0.32.0",
#   "pytest>=8.3.0",
#   "httpx>=0.27.0",
# ]
# ///
"""

import pytest
from fastapi.testclient import TestClient
from main_asgi_uvicorn import app, users_db


@pytest.fixture(autouse=True)
def reset_database():
    """Reset the database before each test."""
    users_db.clear()
    users_db.update({
        1: {"name": "Alice", "email": "alice@example.com"},
        2: {"name": "Bob", "email": "bob@example.com"},
    })
    yield
    users_db.clear()


# Create TestClient - NO SERVER REQUIRED!
# TestClient directly calls the ASGI application without HTTP overhead
client = TestClient(app)


def test_root_endpoint():
    """Test the root endpoint returns welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to ASGI Demo API"}
    print("✓ Root endpoint test passed")


def test_health_check():
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["server"] == "uvicorn"
    assert data["protocol"] == "ASGI"
    print("✓ Health check test passed")


def test_list_users():
    """Test listing all users."""
    response = client.get("/users")
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 2
    assert users[0]["name"] == "Alice"
    assert users[1]["name"] == "Bob"
    print("✓ List users test passed")


def test_get_user_success():
    """Test getting a specific user that exists."""
    response = client.get("/users/1")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 1
    assert user["name"] == "Alice"
    assert user["email"] == "alice@example.com"
    print("✓ Get user success test passed")


def test_get_user_not_found():
    """Test getting a user that doesn't exist returns 404."""
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
    print("✓ Get user not found test passed")


def test_create_user():
    """Test creating a new user."""
    response = client.post("/users?name=Charlie&email=charlie@example.com")
    assert response.status_code == 200
    user = response.json()
    assert user["id"] == 3  # Should be next available ID
    assert user["name"] == "Charlie"
    assert user["email"] == "charlie@example.com"

    # Verify the user was actually created
    verify_response = client.get("/users/3")
    assert verify_response.status_code == 200
    print("✓ Create user test passed")


def test_delete_user_success():
    """Test deleting an existing user."""
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "User 1 deleted successfully"

    # Verify the user was actually deleted
    verify_response = client.get("/users/1")
    assert verify_response.status_code == 404
    print("✓ Delete user success test passed")


def test_delete_user_not_found():
    """Test deleting a user that doesn't exist."""
    response = client.delete("/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"
    print("✓ Delete user not found test passed")


def test_asgi_app_characteristics():
    """
    Demonstrate that we're testing the ASGI app directly.
    No server is running - TestClient calls the ASGI app in-process.
    """
    # Multiple rapid requests - no network latency!
    responses = [client.get("/health") for _ in range(10)]
    assert all(r.status_code == 200 for r in responses)
    print("✓ ASGI direct testing - 10 requests with zero network overhead")


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("Testing ASGI Application WITHOUT launching server")
    print("=" * 60 + "\n")

    # Run pytest programmatically
    pytest.main([__file__, "-v", "--tb=short"])
