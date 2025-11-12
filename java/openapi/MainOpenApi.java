package openapi;

import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.info.Contact;
import io.swagger.v3.oas.annotations.info.Info;
import io.swagger.v3.oas.annotations.info.License;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.atomic.AtomicLong;

/**
 * MainOpenApi demonstrates OpenAPI/Swagger documentation in Spring Boot.
 *
 * This example showcases:
 * - OpenAPI annotations for API documentation
 * - REST endpoint definitions
 * - Request/response model documentation
 * - HTTP method handling (GET, POST, PUT, DELETE)
 * - API versioning and metadata
 */
@SpringBootApplication
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
public class MainOpenApi {

    public static void main(String[] args) {
        System.out.println("=== OpenAPI Documentation Example ===");                          // Line 53
        System.out.println("Starting Spring Boot application with OpenAPI support...");        // Line 54
        System.out.println();                                                                   // Line 55

        SpringApplication.run(MainOpenApi.class, args);                                         // Line 57

        System.out.println();                                                                   // Line 59
        System.out.println("Application started successfully!");                                // Line 60
        System.out.println("OpenAPI documentation available at: http://localhost:8080/v3/api-docs"); // Line 61
        System.out.println("Swagger UI available at: http://localhost:8080/swagger-ui.html");  // Line 62
    }
}

/**
 * User model class with schema documentation
 */
@Schema(description = "User entity representing a system user")
class User {

    @Schema(description = "Unique identifier of the user", example = "1", accessMode = Schema.AccessMode.READ_ONLY)
    private Long id;

    @Schema(description = "Username of the user", example = "johndoe", required = true)
    private String username;

    @Schema(description = "Email address of the user", example = "john.doe@example.com", required = true)
    private String email;

    @Schema(description = "Full name of the user", example = "John Doe")
    private String fullName;

    public User() {}

    public User(Long id, String username, String email, String fullName) {
        this.id = id;
        this.username = username;
        this.email = email;
        this.fullName = fullName;
    }

    // Getters and setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getUsername() { return username; }
    public void setUsername(String username) { this.username = username; }

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }

    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }

    @Override
    public String toString() {
        return String.format("User{id=%d, username='%s', email='%s', fullName='%s'}",
            id, username, email, fullName);
    }
}

/**
 * REST Controller with OpenAPI annotations
 */
@RestController
@RequestMapping("/api/users")
@Tag(name = "User Management", description = "APIs for managing users in the system")
class UserController {

    private final List<User> users = new ArrayList<>();
    private final AtomicLong counter = new AtomicLong();

    public UserController() {
        // Initialize with sample data
        users.add(new User(counter.incrementAndGet(), "alice", "alice@example.com", "Alice Smith"));      // Line 129
        users.add(new User(counter.incrementAndGet(), "bob", "bob@example.com", "Bob Johnson"));          // Line 130
        users.add(new User(counter.incrementAndGet(), "charlie", "charlie@example.com", "Charlie Brown")); // Line 131
    }

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
        System.out.println("[GET /api/users] Retrieving all users. Count: " + users.size());   // Line 151
        return ResponseEntity.ok(users);                                                        // Line 152
    }

    @Operation(
        summary = "Get user by ID",
        description = "Retrieves a specific user by their unique identifier"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "User found",
            content = @Content(
                mediaType = "application/json",
                schema = @Schema(implementation = User.class)
            )
        ),
        @ApiResponse(
            responseCode = "404",
            description = "User not found",
            content = @Content
        )
    })
    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(
        @Parameter(description = "ID of the user to retrieve", required = true)
        @PathVariable Long id
    ) {
        System.out.println("[GET /api/users/" + id + "] Retrieving user by ID: " + id);        // Line 180
        Optional<User> user = users.stream()                                                    // Line 181
            .filter(u -> u.getId().equals(id))                                                  // Line 182
            .findFirst();                                                                       // Line 183

        if (user.isPresent()) {                                                                 // Line 185
            System.out.println("[GET /api/users/" + id + "] User found: " + user.get());       // Line 186
            return ResponseEntity.ok(user.get());                                               // Line 187
        } else {                                                                                // Line 188
            System.out.println("[GET /api/users/" + id + "] User not found");                  // Line 189
            return ResponseEntity.notFound().build();                                           // Line 190
        }                                                                                       // Line 191
    }

    @Operation(
        summary = "Create a new user",
        description = "Creates a new user in the system"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "201",
            description = "User created successfully",
            content = @Content(
                mediaType = "application/json",
                schema = @Schema(implementation = User.class)
            )
        ),
        @ApiResponse(
            responseCode = "400",
            description = "Invalid input",
            content = @Content
        )
    })
    @PostMapping
    public ResponseEntity<User> createUser(
        @io.swagger.v3.oas.annotations.parameters.RequestBody(
            description = "User object to be created",
            required = true,
            content = @Content(schema = @Schema(implementation = User.class))
        )
        @RequestBody User user
    ) {
        user.setId(counter.incrementAndGet());                                                  // Line 223
        users.add(user);                                                                        // Line 224
        System.out.println("[POST /api/users] Created new user: " + user);                     // Line 225
        return ResponseEntity.status(HttpStatus.CREATED).body(user);                            // Line 226
    }

    @Operation(
        summary = "Update an existing user",
        description = "Updates user information for a specific user ID"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "User updated successfully",
            content = @Content(
                mediaType = "application/json",
                schema = @Schema(implementation = User.class)
            )
        ),
        @ApiResponse(
            responseCode = "404",
            description = "User not found",
            content = @Content
        )
    })
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
        System.out.println("[PUT /api/users/" + id + "] Updating user with ID: " + id);        // Line 261
        Optional<User> existingUser = users.stream()                                            // Line 262
            .filter(u -> u.getId().equals(id))                                                  // Line 263
            .findFirst();                                                                       // Line 264

        if (existingUser.isPresent()) {                                                         // Line 266
            User user = existingUser.get();                                                     // Line 267
            user.setUsername(updatedUser.getUsername());                                        // Line 268
            user.setEmail(updatedUser.getEmail());                                              // Line 269
            user.setFullName(updatedUser.getFullName());                                        // Line 270
            System.out.println("[PUT /api/users/" + id + "] User updated: " + user);           // Line 271
            return ResponseEntity.ok(user);                                                     // Line 272
        } else {                                                                                // Line 273
            System.out.println("[PUT /api/users/" + id + "] User not found");                  // Line 274
            return ResponseEntity.notFound().build();                                           // Line 275
        }                                                                                       // Line 276
    }

    @Operation(
        summary = "Delete a user",
        description = "Deletes a user from the system by their ID"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "204",
            description = "User deleted successfully",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "404",
            description = "User not found",
            content = @Content
        )
    })
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(
        @Parameter(description = "ID of the user to delete", required = true)
        @PathVariable Long id
    ) {
        System.out.println("[DELETE /api/users/" + id + "] Deleting user with ID: " + id);     // Line 302
        boolean removed = users.removeIf(u -> u.getId().equals(id));                            // Line 303

        if (removed) {                                                                          // Line 305
            System.out.println("[DELETE /api/users/" + id + "] User deleted successfully");    // Line 306
            return ResponseEntity.noContent().build();                                          // Line 307
        } else {                                                                                // Line 308
            System.out.println("[DELETE /api/users/" + id + "] User not found");               // Line 309
            return ResponseEntity.notFound().build();                                           // Line 310
        }                                                                                       // Line 311
    }
}
