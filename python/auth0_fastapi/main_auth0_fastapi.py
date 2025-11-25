#!/usr/bin/env python3
# /// script
# dependencies = [
#   "fastapi",
#   "uvicorn",
#   "python-jose[cryptography]",
#   "requests",
# ]
# ///

"""
Auth0 Integration with FastAPI

This example demonstrates how to:
1. Set up a FastAPI application with Auth0 authentication
2. Create public and protected endpoints
3. Validate JWT tokens from Auth0
4. Extract user information from tokens
"""

import os
from typing import Annotated

import requests
import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt


# Auth0 Configuration (replace with your Auth0 domain and API identifier)
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN", "dev-example.us.auth0.com")
AUTH0_API_AUDIENCE = os.getenv("AUTH0_API_AUDIENCE", "https://api.example.com")
AUTH0_ISSUER = f"https://{AUTH0_DOMAIN}/"
AUTH0_ALGORITHMS = ["RS256"]


app = FastAPI(
    title="Auth0 FastAPI Integration",
    description="Example API with Auth0 JWT authentication",
    version="1.0.0",
)

security = HTTPBearer()


class Auth0JWTBearer:
    """
    Auth0 JWT token validator for FastAPI.

    This class handles:
    - Fetching JWKS (JSON Web Key Set) from Auth0
    - Validating JWT tokens
    - Extracting claims from valid tokens
    """

    def __init__(self, domain: str, api_audience: str):
        self.domain = domain
        self.api_audience = api_audience
        # Cache for JWKS to avoid repeated requests
        self._jwks = None

    def get_jwks(self):
        """Fetch the JWKS from Auth0's well-known endpoint."""
        if self._jwks is None:
            jwks_url = f"https://{self.domain}/.well-known/jwks.json"
            response = requests.get(jwks_url, timeout=10)
            response.raise_for_status()
            self._jwks = response.json()
        return self._jwks

    def verify_token(self, token: str) -> dict:
        """
        Verify and decode a JWT token from Auth0.

        Steps:
        1. Get the token header to find the key ID (kid)
        2. Find the matching public key from JWKS
        3. Verify the token signature
        4. Validate token claims (issuer, audience, expiration)

        Returns:
            dict: The decoded token payload with user claims

        Raises:
            HTTPException: If token validation fails
        """
        try:
            # Get the kid from the token header
            unverified_header = jwt.get_unverified_header(token)
            rsa_key = {}

            # Find the matching key from JWKS
            jwks = self.get_jwks()
            for key in jwks["keys"]:
                if key["kid"] == unverified_header["kid"]:
                    rsa_key = {
                        "kty": key["kty"],
                        "kid": key["kid"],
                        "use": key["use"],
                        "n": key["n"],
                        "e": key["e"],
                    }
                    break

            if not rsa_key:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Unable to find appropriate key",
                )

            # Verify the token
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=AUTH0_ALGORITHMS,
                audience=self.api_audience,
                issuer=AUTH0_ISSUER,
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
            )
        except jwt.JWTClaimsError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid claims. Please check the audience and issuer.",
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Unable to validate token: {str(e)}",
            )


# Initialize the Auth0 JWT validator
auth0_validator = Auth0JWTBearer(domain=AUTH0_DOMAIN, api_audience=AUTH0_API_AUDIENCE)


async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
) -> dict:
    """
    Dependency to extract and validate the current user from the JWT token.

    This can be used with FastAPI's dependency injection system to protect routes.
    """
    token = credentials.credentials
    return auth0_validator.verify_token(token)


# ============================================================================
# PUBLIC ENDPOINTS
# ============================================================================


@app.get("/")
async def root():
    """Public endpoint - no authentication required."""
    return {
        "message": "Welcome to the Auth0 FastAPI Integration Example",
        "status": "public",
        "endpoints": {
            "public": ["/", "/health", "/public/info"],
            "protected": ["/api/private", "/api/profile", "/api/admin"],
        },
    }


@app.get("/health")
async def health_check():
    """Health check endpoint - no authentication required."""
    return {"status": "healthy", "service": "auth0-fastapi-demo"}


@app.get("/public/info")
async def public_info():
    """Public information endpoint."""
    return {
        "message": "This is public information accessible to anyone",
        "auth0_domain": AUTH0_DOMAIN,
        "required_audience": AUTH0_API_AUDIENCE,
    }


# ============================================================================
# PROTECTED ENDPOINTS
# ============================================================================


@app.get("/api/private")
async def private_endpoint(user: Annotated[dict, Depends(get_current_user)]):
    """
    Protected endpoint - requires valid JWT token.

    The user parameter contains the decoded JWT payload.
    """
    return {
        "message": "This is a protected endpoint",
        "user_authenticated": True,
        "token_info": {
            "sub": user.get("sub"),
            "permissions": user.get("permissions", []),
        },
    }


@app.get("/api/profile")
async def get_profile(user: Annotated[dict, Depends(get_current_user)]):
    """
    Get user profile information from the JWT token.

    This endpoint demonstrates how to extract user information
    from the validated token.
    """
    return {
        "user_id": user.get("sub"),
        "email": user.get("email"),
        "email_verified": user.get("email_verified"),
        "permissions": user.get("permissions", []),
        "scope": user.get("scope", ""),
    }


@app.get("/api/admin")
async def admin_endpoint(user: Annotated[dict, Depends(get_current_user)]):
    """
    Admin endpoint - requires valid JWT token and admin permissions.

    This demonstrates how to implement role-based access control (RBAC).
    """
    # Check if user has admin permission
    permissions = user.get("permissions", [])
    if "admin:access" not in permissions:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions. Admin access required.",
        )

    return {
        "message": "Welcome to the admin area",
        "user_id": user.get("sub"),
        "admin_access": True,
    }


# ============================================================================
# DEMO MODE
# ============================================================================


@app.get("/demo/token-structure")
async def demo_token_structure():
    """
    Demonstrates the structure of a JWT token for educational purposes.

    In production, this endpoint should be removed.
    """
    return {
        "jwt_structure": {
            "header": {
                "description": "Algorithm and token type",
                "example": {"alg": "RS256", "typ": "JWT", "kid": "ABC123"},
            },
            "payload": {
                "description": "Claims and user data",
                "example": {
                    "iss": AUTH0_ISSUER,
                    "sub": "auth0|123456",
                    "aud": [AUTH0_API_AUDIENCE],
                    "iat": 1234567890,
                    "exp": 1234571490,
                    "scope": "read:profile write:profile",
                    "permissions": ["read:profile", "write:profile"],
                },
            },
            "signature": {
                "description": "Cryptographic signature to verify token authenticity"
            },
        },
        "how_to_get_token": {
            "step_1": "Create an Auth0 account at https://auth0.com",
            "step_2": "Create an API in Auth0 Dashboard",
            "step_3": "Create an Application (Machine to Machine or SPA)",
            "step_4": "Use Auth0's authentication endpoints to get a token",
            "example_curl": f"""
curl --request POST \\
  --url https://{AUTH0_DOMAIN}/oauth/token \\
  --header 'content-type: application/json' \\
  --data '{{"client_id":"YOUR_CLIENT_ID","client_secret":"YOUR_CLIENT_SECRET","audience":"{AUTH0_API_AUDIENCE}","grant_type":"client_credentials"}}'
            """,
        },
    }


def main():
    """
    Run the FastAPI application.

    The server will start on http://localhost:8000
    API documentation will be available at http://localhost:8000/docs
    """
    print("=" * 70)
    print("Auth0 FastAPI Integration Demo")
    print("=" * 70)
    print(f"\nAuth0 Domain: {AUTH0_DOMAIN}")
    print(f"API Audience: {AUTH0_API_AUDIENCE}")
    print(f"Issuer: {AUTH0_ISSUER}")
    print("\nStarting server at http://localhost:8000")
    print("API Documentation: http://localhost:8000/docs")
    print("\nPublic Endpoints:")
    print("  - GET /")
    print("  - GET /health")
    print("  - GET /public/info")
    print("  - GET /demo/token-structure")
    print("\nProtected Endpoints (require JWT token):")
    print("  - GET /api/private")
    print("  - GET /api/profile")
    print("  - GET /api/admin (requires admin permissions)")
    print("\n" + "=" * 70)
    print()

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")


if __name__ == "__main__":
    main()
