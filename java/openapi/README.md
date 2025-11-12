# OpenAPI Example in Java

This example demonstrates how to use OpenAPI (formerly Swagger) annotations to document REST APIs in a Spring Boot application.

## Overview

OpenAPI is a specification for building and documenting RESTful APIs. This example shows:
- **OpenAPI annotations** for API documentation
- **REST endpoint definitions** with proper HTTP methods
- **Request/response model documentation** with schema definitions
- **Automatic API documentation generation** accessible via Swagger UI
- **Complete CRUD operations** (Create, Read, Update, Delete)

## Requirements

- **Java 17** or higher
- **Spring Boot 3.2.0** - Modern Spring Boot framework
- **Springdoc OpenAPI 2.3.0** - Library for OpenAPI 3.0 documentation with Spring Boot
- **Maven** for dependency management

## Key Features Demonstrated

### 1. API Metadata Definition (Lines 38-51)

```java
@OpenAPIDefinition(
    info = @Info(
        title = "User Management API",
        version = "1.0.0",
        description = "A sample REST API demonstrating OpenAPI documentation with Spring Boot",
        contact = @Contact(
            name = "API Support",
            email = "support@example.com",
            url = "https://example.com/support"
        ),
        license = @License(
            name = "Apache 2.0",
            url = "https://www.apache.org/licenses/LICENSE-2.0.html"
        )
    )
)
```

**Purpose:** Defines global API metadata including title, version, description, contact information, and license. This information appears at the top of the generated OpenAPI documentation.

### 2. Model Schema Documentation (Lines 69-86)

```java
@Schema(description = "User entity representing a system user")
class User {

    @Schema(description = "Unique identifier of the user",
            example = "1",
            accessMode = Schema.AccessMode.READ_ONLY)
    private Long id;

    @Schema(description = "Username of the user",
            example = "johndoe",
            required = true)
    private String username;

    @Schema(description = "Email address of the user",
            example = "john.doe@example.com",
            required = true)
    private String email;

    @Schema(description = "Full name of the user",
            example = "John Doe")
    private String fullName;
    // ... getters and setters
}
```

**Purpose:** Documents the data model with descriptions, examples, and validation rules. The `@Schema` annotation helps generate comprehensive model documentation in the OpenAPI specification.

### 3. Controller Tag Definition (Line 119)

```java
@Tag(name = "User Management",
     description = "APIs for managing users in the system")
class UserController {
```

**Purpose:** Groups related endpoints together under a common tag in the API documentation, making it easier to navigate.

### 4. GET All Users Endpoint (Lines 133-152)

```java
@Operation(
    summary = "Get all users",
    description = "Retrieves a list of all users in the system"
)
@ApiResponses(value = {
    @ApiResponse(
        responseCode = "200",
        description = "Successfully retrieved list of users",
        content = @Content(
            mediaType = "application/json",
            schema = @Schema(implementation = User.class)
        )
    )
})
@GetMapping
public ResponseEntity<List<User>> getAllUsers() {
    System.out.println("[GET /api/users] Retrieving all users. Count: " + users.size());
    return ResponseEntity.ok(users);
}
```

**Purpose:** Documents a GET endpoint that returns all users. The `@Operation` provides a summary and description, while `@ApiResponses` documents the response structure.

### 5. GET User by ID Endpoint (Lines 154-191)

```java
@GetMapping("/{id}")
public ResponseEntity<User> getUserById(
    @Parameter(description = "ID of the user to retrieve", required = true)
    @PathVariable Long id
) {
    System.out.println("[GET /api/users/" + id + "] Retrieving user by ID: " + id);
    Optional<User> user = users.stream()
        .filter(u -> u.getId().equals(id))
        .findFirst();

    if (user.isPresent()) {
        System.out.println("[GET /api/users/" + id + "] User found: " + user.get());
        return ResponseEntity.ok(user.get());
    } else {
        System.out.println("[GET /api/users/" + id + "] User not found");
        return ResponseEntity.notFound().build();
    }
}
```

**Purpose:** Demonstrates path parameter documentation with `@Parameter` and handling both success (200) and not found (404) responses.

### 6. POST Create User Endpoint (Lines 193-226)

```java
@PostMapping
public ResponseEntity<User> createUser(
    @io.swagger.v3.oas.annotations.parameters.RequestBody(
        description = "User object to be created",
        required = true,
        content = @Content(schema = @Schema(implementation = User.class))
    )
    @RequestBody User user
) {
    user.setId(counter.incrementAndGet());
    users.add(user);
    System.out.println("[POST /api/users] Created new user: " + user);
    return ResponseEntity.status(HttpStatus.CREATED).body(user);
}
```

**Purpose:** Shows how to document request body parameters and return a 201 (CREATED) status code for successful resource creation.

### 7. PUT Update User Endpoint (Lines 228-276)

```java
@PutMapping("/{id}")
public ResponseEntity<User> updateUser(
    @Parameter(description = "ID of the user to update", required = true)
    @PathVariable Long id,
    @io.swagger.v3.oas.annotations.parameters.RequestBody(
        description = "Updated user object",
        required = true,
        content = @Content(schema = @Schema(implementation = User.class))
    )
    @RequestBody User updatedUser
) {
    System.out.println("[PUT /api/users/" + id + "] Updating user with ID: " + id);
    Optional<User> existingUser = users.stream()
        .filter(u -> u.getId().equals(id))
        .findFirst();

    if (existingUser.isPresent()) {
        User user = existingUser.get();
        user.setUsername(updatedUser.getUsername());
        user.setEmail(updatedUser.getEmail());
        user.setFullName(updatedUser.getFullName());
        System.out.println("[PUT /api/users/" + id + "] User updated: " + user);
        return ResponseEntity.ok(user);
    } else {
        System.out.println("[PUT /api/users/" + id + "] User not found");
        return ResponseEntity.notFound().build();
    }
}
```

**Purpose:** Demonstrates updating existing resources with both path parameter and request body documentation.

### 8. DELETE User Endpoint (Lines 278-311)

```java
@DeleteMapping("/{id}")
public ResponseEntity<Void> deleteUser(
    @Parameter(description = "ID of the user to delete", required = true)
    @PathVariable Long id
) {
    System.out.println("[DELETE /api/users/" + id + "] Deleting user with ID: " + id);
    boolean removed = users.removeIf(u -> u.getId().equals(id));

    if (removed) {
        System.out.println("[DELETE /api/users/" + id + "] User deleted successfully");
        return ResponseEntity.noContent().build();
    } else {
        System.out.println("[DELETE /api/users/" + id + "] User not found");
        return ResponseEntity.notFound().build();
    }
}
```

**Purpose:** Shows how to document DELETE operations that return 204 (NO CONTENT) on success.

## Running the Application

### Build and Run

```bash
cd java/openapi
mvn clean package
mvn spring-boot:run
```

### Expected Console Output on Startup

```
=== OpenAPI Documentation Example ===
Starting Spring Boot application with OpenAPI support...

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v3.2.0)

[INFO] Starting MainOpenApi...
[INFO] Tomcat initialized with port(s): 8080 (http)
[INFO] Starting service [Tomcat]
[INFO] Starting Servlet engine: [Apache Tomcat/10.1.16]
[INFO] Initializing Spring embedded WebApplicationContext
[INFO] Root WebApplicationContext: initialization completed
[INFO] Started MainOpenApi in 2.345 seconds

Application started successfully!
OpenAPI documentation available at: http://localhost:8080/v3/api-docs
Swagger UI available at: http://localhost:8080/swagger-ui.html
```

**Line References:**
- **Line 53**: Prints the header banner
- **Line 54**: Announces application startup
- **Line 57**: Starts the Spring Boot application
- **Line 61**: Shows where to access the raw OpenAPI JSON/YAML documentation
- **Line 62**: Shows where to access the interactive Swagger UI

## API Testing Examples

### 1. Get All Users

**Request:**
```bash
curl http://localhost:8080/api/users
```

**Console Output (Line 151):**
```
[GET /api/users] Retrieving all users. Count: 3
```

**Response:**
```json
[
  {
    "id": 1,
    "username": "alice",
    "email": "alice@example.com",
    "fullName": "Alice Smith"
  },
  {
    "id": 2,
    "username": "bob",
    "email": "bob@example.com",
    "fullName": "Bob Johnson"
  },
  {
    "id": 3,
    "username": "charlie",
    "email": "charlie@example.com",
    "fullName": "Charlie Brown"
  }
]
```

**Explanation:** The controller initializes with 3 sample users (Lines 129-131), and the GET endpoint retrieves all of them.

### 2. Get User by ID (Success Case)

**Request:**
```bash
curl http://localhost:8080/api/users/1
```

**Console Output (Lines 180, 186):**
```
[GET /api/users/1] Retrieving user by ID: 1
[GET /api/users/1] User found: User{id=1, username='alice', email='alice@example.com', fullName='Alice Smith'}
```

**Response:**
```json
{
  "id": 1,
  "username": "alice",
  "email": "alice@example.com",
  "fullName": "Alice Smith"
}
```

**Explanation:** Lines 181-183 filter the user list to find the user with ID 1. Line 185 checks if user exists, Line 186 logs the found user, and Line 187 returns it.

### 3. Get User by ID (Not Found Case)

**Request:**
```bash
curl http://localhost:8080/api/users/999
```

**Console Output (Lines 180, 189):**
```
[GET /api/users/999] Retrieving user by ID: 999
[GET /api/users/999] User not found
```

**Response:**
```
HTTP/1.1 404 Not Found
```

**Explanation:** When the user is not found (Line 188), Line 189 logs the error and Line 190 returns a 404 response.

### 4. Create New User

**Request:**
```bash
curl -X POST http://localhost:8080/api/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "david",
    "email": "david@example.com",
    "fullName": "David Wilson"
  }'
```

**Console Output (Line 225):**
```
[POST /api/users] Created new user: User{id=4, username='david', email='david@example.com', fullName='David Wilson'}
```

**Response:**
```json
{
  "id": 4,
  "username": "david",
  "email": "david@example.com",
  "fullName": "David Wilson"
}
```

**Explanation:** Line 223 generates a new ID using the atomic counter. Line 224 adds the user to the list. Line 225 logs the created user. Line 226 returns the user with a 201 CREATED status.

### 5. Update User

**Request:**
```bash
curl -X PUT http://localhost:8080/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "username": "alice_updated",
    "email": "alice.new@example.com",
    "fullName": "Alice Smith Jr."
  }'
```

**Console Output (Lines 261, 271):**
```
[PUT /api/users/1] Updating user with ID: 1
[PUT /api/users/1] User updated: User{id=1, username='alice_updated', email='alice.new@example.com', fullName='Alice Smith Jr.'}
```

**Response:**
```json
{
  "id": 1,
  "username": "alice_updated",
  "email": "alice.new@example.com",
  "fullName": "Alice Smith Jr."
}
```

**Explanation:** Lines 262-264 find the existing user. Lines 268-270 update the user's fields. Line 271 logs the update. Line 272 returns the updated user.

### 6. Delete User (Success Case)

**Request:**
```bash
curl -X DELETE http://localhost:8080/api/users/2
```

**Console Output (Lines 302, 306):**
```
[DELETE /api/users/2] Deleting user with ID: 2
[DELETE /api/users/2] User deleted successfully
```

**Response:**
```
HTTP/1.1 204 No Content
```

**Explanation:** Line 303 removes the user from the list. Line 305 checks if removal succeeded. Line 306 logs success. Line 307 returns 204 NO CONTENT.

### 7. Delete User (Not Found Case)

**Request:**
```bash
curl -X DELETE http://localhost:8080/api/users/999
```

**Console Output (Lines 302, 309):**
```
[DELETE /api/users/999] Deleting user with ID: 999
[DELETE /api/users/999] User not found
```

**Response:**
```
HTTP/1.1 404 Not Found
```

**Explanation:** When the user doesn't exist (Line 308), Line 309 logs the error and Line 310 returns 404.

## Accessing OpenAPI Documentation

### 1. Raw OpenAPI Specification

Access the machine-readable OpenAPI specification:

**JSON format:**
```
http://localhost:8080/v3/api-docs
```

**YAML format:**
```
http://localhost:8080/v3/api-docs.yaml
```

**Sample OpenAPI JSON Output:**
```json
{
  "openapi": "3.0.1",
  "info": {
    "title": "User Management API",
    "description": "A sample REST API demonstrating OpenAPI documentation with Spring Boot",
    "contact": {
      "name": "API Support",
      "url": "https://example.com/support",
      "email": "support@example.com"
    },
    "license": {
      "name": "Apache 2.0",
      "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    },
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "http://localhost:8080",
      "description": "Generated server url"
    }
  ],
  "tags": [
    {
      "name": "User Management",
      "description": "APIs for managing users in the system"
    }
  ],
  "paths": {
    "/api/users": {
      "get": {
        "tags": ["User Management"],
        "summary": "Get all users",
        "description": "Retrieves a list of all users in the system",
        "operationId": "getAllUsers",
        "responses": {
          "200": {
            "description": "Successfully retrieved list of users",
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/User"
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "components": {
    "schemas": {
      "User": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier of the user",
            "format": "int64",
            "readOnly": true
          },
          "username": {
            "type": "string",
            "description": "Username of the user"
          },
          "email": {
            "type": "string",
            "description": "Email address of the user"
          },
          "fullName": {
            "type": "string",
            "description": "Full name of the user"
          }
        }
      }
    }
  }
}
```

### 2. Swagger UI

Access the interactive API documentation interface:
```
http://localhost:8080/swagger-ui.html
```

**Features of Swagger UI:**
- **Interactive documentation** - Try out API calls directly from the browser
- **Request/response examples** - See sample requests and responses
- **Model schemas** - View data structure definitions
- **Parameter documentation** - Understand required and optional parameters
- **Response codes** - See all possible HTTP response codes

## Key OpenAPI Annotations Used

| Annotation | Purpose | Example Usage |
|------------|---------|---------------|
| `@OpenAPIDefinition` | Define global API metadata | API title, version, description, contact |
| `@Info` | Provide API information | Title, version, description, license |
| `@Tag` | Group related endpoints | Organize endpoints by functionality |
| `@Operation` | Document an endpoint | Summary, description of operation |
| `@ApiResponses` | Document possible responses | Success and error responses |
| `@ApiResponse` | Document a specific response | HTTP status code, description, schema |
| `@Parameter` | Document path/query parameters | Parameter description, required flag |
| `@RequestBody` | Document request body | Body description, schema |
| `@Schema` | Document data models | Model properties, validation rules |

## Benefits of OpenAPI

1. **Automatic Documentation Generation** - Documentation stays in sync with code
2. **Interactive API Exploration** - Swagger UI allows testing without external tools
3. **Client Code Generation** - Generate client SDKs in multiple languages
4. **Contract-First Development** - Define API contracts before implementation
5. **Standardization** - Use industry-standard specification (OpenAPI 3.0)
6. **Validation** - Ensure requests/responses match the specification
7. **Team Collaboration** - Share clear API contracts with frontend/backend teams

## Summary

This example demonstrates a complete OpenAPI implementation in Java using:
- **Spring Boot 3.2.0** for the web framework
- **Springdoc OpenAPI 2.3.0** for OpenAPI documentation generation
- **Java 17** for modern Java features

The example shows all CRUD operations with comprehensive OpenAPI annotations, making the API self-documenting and easy to understand for both developers and consumers.
