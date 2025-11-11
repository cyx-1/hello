import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.*;
import org.springframework.stereotype.Service;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import jakarta.annotation.PostConstruct;

import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicLong;

/**
 * Spring Boot Example - Demonstrates core Spring Boot features:
 * - Auto-configuration with @SpringBootApplication
 * - RESTful API with @RestController
 * - Dependency Injection with @Autowired
 * - Service layer with @Service
 * - HTTP methods (GET, POST, PUT, DELETE)
 * - Embedded Tomcat server
 */
@SpringBootApplication
public class MainSpringBoot {

    public static void main(String[] args) {
        System.out.println("=== Starting Spring Boot Application ===");
        SpringApplication.run(MainSpringBoot.class, args);
    }
}

// Domain Model: Simple User class
class User {
    private Long id;
    private String name;
    private String email;
    private Date createdAt;

    public User() {
        this.createdAt = new Date();
    }

    public User(Long id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
        this.createdAt = new Date();
    }

    // Getters and Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public Date getCreatedAt() { return createdAt; }
    public void setCreatedAt(Date createdAt) { this.createdAt = createdAt; }

    @Override
    public String toString() {
        return "User{id=" + id + ", name='" + name + "', email='" + email + "'}";
    }
}

// Service Layer: Business logic for user management
@Service
class UserService {
    private final Map<Long, User> userDatabase = new ConcurrentHashMap<>();
    private final AtomicLong idGenerator = new AtomicLong(1);

    @PostConstruct
    public void init() {
        // Initialize with sample data
        System.out.println("Initializing UserService with sample data...");
        createUser("Alice Johnson", "alice@example.com");
        createUser("Bob Smith", "bob@example.com");
        System.out.println("Sample users created successfully");
    }

    public User createUser(String name, String email) {
        Long id = idGenerator.getAndIncrement();
        User user = new User(id, name, email);
        userDatabase.put(id, user);
        System.out.println("Created user: " + user);
        return user;
    }

    public List<User> getAllUsers() {
        return new ArrayList<>(userDatabase.values());
    }

    public Optional<User> getUserById(Long id) {
        return Optional.ofNullable(userDatabase.get(id));
    }

    public Optional<User> updateUser(Long id, String name, String email) {
        User user = userDatabase.get(id);
        if (user != null) {
            user.setName(name);
            user.setEmail(email);
            System.out.println("Updated user: " + user);
            return Optional.of(user);
        }
        return Optional.empty();
    }

    public boolean deleteUser(Long id) {
        User removed = userDatabase.remove(id);
        if (removed != null) {
            System.out.println("Deleted user: " + removed);
            return true;
        }
        return false;
    }

    public int getUserCount() {
        return userDatabase.size();
    }
}

// REST Controller: Handles HTTP requests
@RestController
@RequestMapping("/api/users")
class UserController {

    @Autowired
    private UserService userService;

    // GET /api/users - Get all users
    @GetMapping
    public ResponseEntity<List<User>> getAllUsers() {
        System.out.println("GET /api/users - Fetching all users");
        List<User> users = userService.getAllUsers();
        return ResponseEntity.ok(users);
    }

    // GET /api/users/{id} - Get user by ID
    @GetMapping("/{id}")
    public ResponseEntity<User> getUserById(@PathVariable Long id) {
        System.out.println("GET /api/users/" + id + " - Fetching user by ID");
        return userService.getUserById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // POST /api/users - Create new user
    @PostMapping
    public ResponseEntity<User> createUser(@RequestBody Map<String, String> userData) {
        System.out.println("POST /api/users - Creating new user");
        String name = userData.get("name");
        String email = userData.get("email");
        User user = userService.createUser(name, email);
        return ResponseEntity.ok(user);
    }

    // PUT /api/users/{id} - Update user
    @PutMapping("/{id}")
    public ResponseEntity<User> updateUser(@PathVariable Long id, @RequestBody Map<String, String> userData) {
        System.out.println("PUT /api/users/" + id + " - Updating user");
        String name = userData.get("name");
        String email = userData.get("email");
        return userService.updateUser(id, name, email)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // DELETE /api/users/{id} - Delete user
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        System.out.println("DELETE /api/users/" + id + " - Deleting user");
        boolean deleted = userService.deleteUser(id);
        return deleted ? ResponseEntity.ok().build() : ResponseEntity.notFound().build();
    }

    // GET /api/users/stats - Get user statistics
    @GetMapping("/stats")
    public ResponseEntity<Map<String, Object>> getStats() {
        System.out.println("GET /api/users/stats - Fetching statistics");
        Map<String, Object> stats = new HashMap<>();
        stats.put("totalUsers", userService.getUserCount());
        stats.put("timestamp", new Date());
        return ResponseEntity.ok(stats);
    }
}

// Health Check Controller
@RestController
@RequestMapping("/api")
class HealthController {

    @GetMapping("/health")
    public ResponseEntity<Map<String, String>> health() {
        System.out.println("GET /api/health - Health check requested");
        Map<String, String> response = new HashMap<>();
        response.put("status", "UP");
        response.put("message", "Spring Boot application is running");
        return ResponseEntity.ok(response);
    }
}
