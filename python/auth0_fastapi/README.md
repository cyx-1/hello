# Auth0 Integration with FastAPI

This example demonstrates how to integrate Auth0 authentication with FastAPI, implementing JWT token validation, protected endpoints, and role-based access control (RBAC).

## Requirements

- **Python**: 3.11+ (uses modern type hints with `Annotated`)
- **uv**: For dependency management and running the script
- **Dependencies** (automatically managed via inline script metadata):
  - `fastapi` - Modern web framework
  - `uvicorn` - ASGI server
  - `python-jose[cryptography]` - JWT token validation
  - `requests` - HTTP client for JWKS retrieval

## Running the Application

```bash
uv run main_auth0_fastapi.py
```

The `uv run` command will automatically install all dependencies specified in the inline script metadata and run the application.

## Code Structure Overview

### 1. Inline Script Metadata (Lines 1-9)

```python
#!/usr/bin/env python3
# /// script
# dependencies = [
#   "fastapi",
#   "uvicorn",
#   "python-jose[cryptography]",
#   "requests",
# ]
# ///
```

**Purpose**: Uses PEP 723 inline script metadata to declare dependencies. The `uv` tool reads this metadata and automatically creates an isolated environment with these packages.

### 2. Auth0 Configuration (Lines 31-35)

```python
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN", "dev-example.us.auth0.com")
AUTH0_API_AUDIENCE = os.getenv("AUTH0_API_AUDIENCE", "https://api.example.com")
AUTH0_ISSUER = f"https://{AUTH0_DOMAIN}/"
AUTH0_ALGORITHMS = ["RS256"]
```

**Purpose**: Configures Auth0 settings. Uses environment variables for production, with defaults for demonstration.

- `AUTH0_DOMAIN`: Your Auth0 tenant domain (e.g., `dev-yourname.us.auth0.com`)
- `AUTH0_API_AUDIENCE`: The API identifier from your Auth0 API configuration
- `AUTH0_ISSUER`: The expected token issuer (must match token's `iss` claim)
- `AUTH0_ALGORITHMS`: Cryptographic algorithms allowed for JWT verification

### 3. Auth0JWTBearer Class (Lines 48-138)

This is the core authentication logic. Let's break down the key methods:

#### JWKS Retrieval (Lines 59-66)

```python
def get_jwks(self):
    """Fetch the JWKS from Auth0's well-known endpoint."""
    if self._jwks is None:
        jwks_url = f"https://{self.domain}/.well-known/jwks.json"
        response = requests.get(jwks_url, timeout=10)
        response.raise_for_status()
        self._jwks = response.json()
    return self._jwks
```

**Purpose**: Fetches the JSON Web Key Set (JWKS) from Auth0. JWKS contains the public keys needed to verify JWT signatures. The result is cached to avoid repeated network calls.

#### Token Verification (Lines 68-138)

```python
def verify_token(self, token: str) -> dict:
    # Step 1: Extract the key ID from token header (Lines 83-84)
    unverified_header = jwt.get_unverified_header(token)
    rsa_key = {}

    # Step 2: Find matching public key from JWKS (Lines 87-99)
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

    # Step 3: Verify the signature and claims (Lines 106-112)
    payload = jwt.decode(
        token,
        rsa_key,
        algorithms=AUTH0_ALGORITHMS,
        audience=self.api_audience,
        issuer=AUTH0_ISSUER,
    )
```

**How it works**:
1. JWT tokens contain a `kid` (key ID) in the header
2. We fetch JWKS from Auth0 which contains multiple public keys
3. Find the matching key using the `kid`
4. Use that public key to verify the token's signature
5. Validate claims: issuer, audience, expiration

### 4. FastAPI Dependency Injection (Lines 144-153)

```python
async def get_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)],
) -> dict:
    """
    Dependency to extract and validate the current user from the JWT token.
    """
    token = credentials.credentials
    return auth0_validator.verify_token(token)
```

**Purpose**: FastAPI dependency that:
1. Extracts the `Authorization: Bearer <token>` header
2. Validates the JWT token
3. Returns the decoded token payload (user claims)

This can be injected into any route to make it protected.

### 5. Public Endpoints (Lines 160-186)

```python
@app.get("/")
async def root():
    """Public endpoint - no authentication required."""
    return {
        "message": "Welcome to the Auth0 FastAPI Integration Example",
        "endpoints": {
            "public": ["/", "/health", "/public/info"],
            "protected": ["/api/private", "/api/profile", "/api/admin"],
        },
    }
```

**Purpose**: Demonstrates endpoints that don't require authentication. Anyone can access these.

### 6. Protected Endpoints (Lines 193-220)

```python
@app.get("/api/private")
async def private_endpoint(user: Annotated[dict, Depends(get_current_user)]):
    """Protected endpoint - requires valid JWT token."""
    return {
        "message": "This is a protected endpoint",
        "user_authenticated": True,
        "token_info": {
            "sub": user.get("sub"),
            "permissions": user.get("permissions", []),
        },
    }
```

**Purpose**: The `Depends(get_current_user)` parameter makes this endpoint protected. FastAPI will:
1. Check for `Authorization` header
2. Extract the JWT token
3. Validate it using Auth0's public keys
4. Pass the decoded user claims to the function

If the token is missing, invalid, or expired, FastAPI returns a 401 Unauthorized error.

### 7. Role-Based Access Control (Lines 239-253)

```python
@app.get("/api/admin")
async def admin_endpoint(user: Annotated[dict, Depends(get_current_user)]):
    """Admin endpoint - requires valid JWT token and admin permissions."""
    permissions = user.get("permissions", [])
    if "admin:access" not in permissions:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions. Admin access required.",
        )
    return {"message": "Welcome to the admin area", "admin_access": True}
```

**Purpose**: Demonstrates RBAC by checking for specific permissions in the token. This endpoint:
1. First validates the JWT (via `get_current_user`)
2. Then checks if the user has `admin:access` permission
3. Returns 403 Forbidden if permission is missing

## Application Startup Output

When you run the application:

```bash
$ uv run main_auth0_fastapi.py
```

**Expected Output**:

```
======================================================================
Auth0 FastAPI Integration Demo
======================================================================

Auth0 Domain: dev-example.us.auth0.com
API Audience: https://api.example.com
Issuer: https://dev-example.us.auth0.com/

Starting server at http://localhost:8000
API Documentation: http://localhost:8000/docs

Public Endpoints:
  - GET /
  - GET /health
  - GET /public/info
  - GET /demo/token-structure

Protected Endpoints (require JWT token):
  - GET /api/private
  - GET /api/profile
  - GET /api/admin (requires admin permissions)

======================================================================

INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

**Explanation**:
- Lines 280-296 in the code generate this startup message
- Shows configured Auth0 domain and audience
- Lists all available endpoints
- Uvicorn starts the ASGI server on port 8000

## Testing the API

### 1. Test Public Endpoint

```bash
$ curl http://localhost:8000/
```

**Response**:
```json
{
  "message": "Welcome to the Auth0 FastAPI Integration Example",
  "status": "public",
  "endpoints": {
    "public": ["/", "/health", "/public/info"],
    "protected": ["/api/private", "/api/profile", "/api/admin"]
  }
}
```

**Explanation**: This endpoint (lines 160-174) is public and returns information about available endpoints. No authentication required.

### 2. Test Protected Endpoint Without Token

```bash
$ curl http://localhost:8000/api/private
```

**Response**:
```json
{
  "detail": "Not authenticated"
}
```

**HTTP Status**: `401 Unauthorized`

**Explanation**: FastAPI's `HTTPBearer` security (line 43) automatically rejects requests without an `Authorization` header.

### 3. Test Protected Endpoint With Invalid Token

```bash
$ curl -H "Authorization: Bearer invalid_token_here" http://localhost:8000/api/private
```

**Response**:
```json
{
  "detail": "Unable to validate token: Not enough segments"
}
```

**HTTP Status**: `401 Unauthorized`

**Explanation**: The `verify_token` method (lines 68-138) attempts to decode the JWT and fails, raising an HTTPException with 401 status.

### 4. Test Protected Endpoint With Valid Token

First, get a token from Auth0:

```bash
$ curl --request POST \
  --url https://dev-example.us.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data '{
    "client_id":"YOUR_CLIENT_ID",
    "client_secret":"YOUR_CLIENT_SECRET",
    "audience":"https://api.example.com",
    "grant_type":"client_credentials"
  }'
```

**Response**:
```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFCQzEyMyJ9...",
  "token_type": "Bearer",
  "expires_in": 86400
}
```

Then use the token:

```bash
$ curl -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFCQzEyMyJ9..." \
  http://localhost:8000/api/private
```

**Response**:
```json
{
  "message": "This is a protected endpoint",
  "user_authenticated": true,
  "token_info": {
    "sub": "auth0|abc123def456",
    "permissions": ["read:profile", "write:profile"]
  }
}
```

**HTTP Status**: `200 OK`

**Explanation**:
1. The JWT token is extracted from the `Authorization` header (line 152)
2. `verify_token` fetches JWKS from Auth0 (lines 59-66)
3. Finds the matching public key using the token's `kid` (lines 87-99)
4. Verifies the signature and validates claims (lines 106-112)
5. Returns the decoded payload to the endpoint function (line 153)
6. The endpoint returns user information (lines 193-205)

### 5. Test Admin Endpoint Without Permissions

Using a valid token that lacks `admin:access` permission:

```bash
$ curl -H "Authorization: Bearer <valid_token_without_admin>" \
  http://localhost:8000/api/admin
```

**Response**:
```json
{
  "detail": "Insufficient permissions. Admin access required."
}
```

**HTTP Status**: `403 Forbidden`

**Explanation**:
1. Token is valid, so `get_current_user` succeeds (lines 144-153)
2. The endpoint checks for `admin:access` permission (lines 245-249)
3. Permission is missing, so raises 403 Forbidden
4. This demonstrates the difference between authentication (401) and authorization (403)

### 6. View Interactive API Documentation

Navigate to: `http://localhost:8000/docs`

**What you'll see**:
- Automatically generated Swagger UI
- All endpoints with descriptions
- Try-it-out functionality
- Schema definitions
- Authorization button to add JWT tokens

**How it works**: FastAPI automatically generates OpenAPI documentation from your route definitions, type hints, and docstrings.

## JWT Token Structure

A JWT token from Auth0 consists of three parts separated by dots (`.`):

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkFCQzEyMyJ9.  ← Header
eyJpc3MiOiJodHRwczovL2Rldi1leGFtcGxlLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHwxMjM0NTYiLCJhdWQiOlsiaHR0cHM6Ly9hcGkuZXhhbXBsZS5jb20iXSwiaWF0IjoxNzAwMDAwMDAwLCJleHAiOjE3MDAwODY0MDAsInNjb3BlIjoicmVhZDpwcm9maWxlIHdyaXRlOnByb2ZpbGUiLCJwZXJtaXNzaW9ucyI6WyJyZWFkOnByb2ZpbGUiLCJ3cml0ZTpwcm9maWxlIl19.  ← Payload
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c  ← Signature
```

### Header (decoded):
```json
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "ABC123"
}
```
- `alg`: Algorithm used (RS256 = RSA with SHA-256)
- `typ`: Token type (JWT)
- `kid`: Key ID - identifies which public key to use for verification

### Payload (decoded):
```json
{
  "iss": "https://dev-example.us.auth0.com/",
  "sub": "auth0|123456",
  "aud": ["https://api.example.com"],
  "iat": 1700000000,
  "exp": 1700086400,
  "scope": "read:profile write:profile",
  "permissions": ["read:profile", "write:profile"]
}
```
- `iss`: Issuer - must match `AUTH0_ISSUER` (validated at line 111)
- `sub`: Subject - unique user identifier
- `aud`: Audience - must match `AUTH0_API_AUDIENCE` (validated at line 110)
- `iat`: Issued at timestamp
- `exp`: Expiration timestamp (automatically validated by python-jose)
- `scope`: Space-separated list of scopes
- `permissions`: Array of permissions (for RBAC, checked at line 245)

### Signature:
- Created by signing (Header + Payload) with Auth0's private key
- We verify it using Auth0's public key from JWKS (lines 106-112)
- If signature is invalid, the token has been tampered with

## Setting Up Auth0

To use this example with your own Auth0 account:

1. **Create Auth0 Account**: Sign up at https://auth0.com

2. **Create an API**:
   - Go to Applications → APIs
   - Click "Create API"
   - Set Name: "My API"
   - Set Identifier: "https://api.example.com" (use this as `AUTH0_API_AUDIENCE`)

3. **Create an Application**:
   - Go to Applications → Applications
   - Click "Create Application"
   - Choose "Machine to Machine" or "Single Page Application"
   - Authorize it to access your API

4. **Get Credentials**:
   - Note your Auth0 domain (e.g., `dev-yourname.us.auth0.com`)
   - Note your Client ID and Client Secret

5. **Set Environment Variables**:
   ```bash
   export AUTH0_DOMAIN="dev-yourname.us.auth0.com"
   export AUTH0_API_AUDIENCE="https://api.example.com"
   ```

6. **Run the Application**:
   ```bash
   uv run main_auth0_fastapi.py
   ```

## Security Considerations

1. **HTTPS in Production**: Always use HTTPS in production. JWT tokens should never be transmitted over unencrypted connections.

2. **Environment Variables**: Store Auth0 credentials in environment variables or a secure vault, never hardcode them.

3. **Token Expiration**: Auth0 tokens expire automatically. The `exp` claim is validated by python-jose (line 114).

4. **JWKS Caching**: This implementation caches JWKS (line 62). In production, implement cache invalidation and periodic refresh.

5. **Rate Limiting**: Add rate limiting to prevent abuse of authentication endpoints.

6. **CORS**: Configure CORS properly if your API is accessed from browsers:
   ```python
   from fastapi.middleware.cors import CORSMiddleware
   app.add_middleware(CORSMiddleware, allow_origins=["https://yourfrontend.com"])
   ```

## Key Features Demonstrated

1. ✅ **JWT Token Validation**: Verifying tokens using Auth0's public keys
2. ✅ **JWKS Retrieval**: Fetching and caching JSON Web Key Sets
3. ✅ **Protected Endpoints**: Using FastAPI dependency injection for authentication
4. ✅ **User Information Extraction**: Getting user claims from validated tokens
5. ✅ **Role-Based Access Control**: Checking permissions for authorization
6. ✅ **Error Handling**: Proper HTTP status codes (401 vs 403)
7. ✅ **Interactive Documentation**: Auto-generated Swagger UI at `/docs`
8. ✅ **Modern Python**: Type hints with `Annotated`, async/await

## Common Issues and Solutions

### Issue: "Unable to find appropriate key"
**Cause**: The token's `kid` doesn't match any key in JWKS.
**Solution**: Ensure you're using a token from the correct Auth0 tenant.

### Issue: "Invalid claims. Please check the audience and issuer."
**Cause**: Token's `aud` or `iss` doesn't match configuration.
**Solution**: Verify `AUTH0_DOMAIN` and `AUTH0_API_AUDIENCE` match your Auth0 API settings.

### Issue: "Token has expired"
**Cause**: The token's `exp` claim is in the past.
**Solution**: Request a new token from Auth0.

## Additional Resources

- [Auth0 Documentation](https://auth0.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [python-jose Documentation](https://python-jose.readthedocs.io)
- [JWT.io Debugger](https://jwt.io) - Decode and inspect JWT tokens

---

**Last Updated**: 2025-11-25
