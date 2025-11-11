# Spring Boot REST API Example

This example demonstrates the core features of **Spring Boot 3.2.0**, a powerful framework for building production-ready applications with minimal configuration.

## Requirements

- **Java 17** or higher
- **Maven 3.6+** for dependency management
- **Spring Boot 3.2.0**

## Running the Application

```bash
cd java/springboot
mvn clean package
mvn spring-boot:run
```

Or run directly:
```bash
mvn clean compile
java -cp target/classes:$(mvn dependency:build-classpath -Dmdep.outputFile=/dev/stdout -q) MainSpringBoot
```

The application will start on `http://localhost:8080`

---

## Source Code Overview

### Main Application Class (Lines 1-24)

```java
1   import org.springframework.boot.SpringApplication;
2   import org.springframework.boot.autoconfigure.SpringBootApplication;
3   import org.springframework.web.bind.annotation.*;
4   import org.springframework.stereotype.Service;
5   import org.springframework.beans.factory.annotation.Autowired;
6   import org.springframework.http.ResponseEntity;
7   import jakarta.annotation.PostConstruct;
8
9   import java.util.*;
10  import java.util.concurrent.ConcurrentHashMap;
11  import java.util.concurrent.atomic.AtomicLong;
12
13  /**
14   * Spring Boot Example - Demonstrates core Spring Boot features:
15   * - Auto-configuration with @SpringBootApplication
16   * - RESTful API with @RestController
17   * - Dependency Injection with @Autowired
18   * - Service layer with @Service
19   * - HTTP methods (GET, POST, PUT, DELETE)
20   * - Embedded Tomcat server
21   */
22  @SpringBootApplication
23  public class MainSpringBoot {
24
25      public static void main(String[] args) {
26          System.out.println("=== Starting Spring Boot Application ===");
27          SpringApplication.run(MainSpringBoot.class, args);
28      }
29  }
```

**Line 22**: `@SpringBootApplication` - This single annotation combines:
- `@Configuration`: Marks the class as a source of bean definitions
- `@EnableAutoConfiguration`: Enables Spring Boot's auto-configuration mechanism
- `@ComponentScan`: Scans for components in the current package and sub-packages

**Line 27**: `SpringApplication.run()` - Bootstraps the application, creates ApplicationContext, and starts the embedded Tomcat server

---

### Domain Model: User Class (Lines 31-62)

```java
31  // Domain Model: Simple User class
32  class User {
33      private Long id;
34      private String name;
35      private String email;
36      private Date createdAt;
37
38      public User() {
39          this.createdAt = new Date();
40      }
41
42      public User(Long id, String name, String email) {
43          this.id = id;
44          this.name = name;
45          this.email = email;
46          this.createdAt = new Date();
47      }
48
49      // Getters and Setters
50      public Long getId() { return id; }
51      public void setId(Long id) { this.id = id; }
52      public String getName() { return name; }
53      public void setName(String name) { this.name = name; }
54      public String getEmail() { return email; }
55      public void setEmail(String email) { this.email = email; }
56      public Date getCreatedAt() { return createdAt; }
57      public void setCreatedAt(Date createdAt) { this.createdAt = createdAt; }
58
59      @Override
60      public String toString() {
61          return "User{id=" + id + ", name='" + name + "', email='" + email + "'}";
62      }
63  }
```

**Lines 32-63**: Simple POJO (Plain Old Java Object) representing a User entity
- Automatically serialized to JSON by Spring Boot using Jackson
- `createdAt` field tracks when the user was created

---

### Service Layer: UserService (Lines 65-115)

```java
65  // Service Layer: Business logic for user management
66  @Service
67  class UserService {
68      private final Map<Long, User> userDatabase = new ConcurrentHashMap<>();
69      private final AtomicLong idGenerator = new AtomicLong(1);
70
71      @PostConstruct
72      public void init() {
73          // Initialize with sample data
74          System.out.println("Initializing UserService with sample data...");
75          createUser("Alice Johnson", "alice@example.com");
76          createUser("Bob Smith", "bob@example.com");
77          System.out.println("Sample users created successfully");
78      }
79
80      public User createUser(String name, String email) {
81          Long id = idGenerator.getAndIncrement();
82          User user = new User(id, name, email);
83          userDatabase.put(id, user);
84          System.out.println("Created user: " + user);
85          return user;
86      }
87
88      public List<User> getAllUsers() {
89          return new ArrayList<>(userDatabase.values());
90      }
91
92      public Optional<User> getUserById(Long id) {
93          return Optional.ofNullable(userDatabase.get(id));
94      }
95
96      public Optional<User> updateUser(Long id, String name, String email) {
97          User user = userDatabase.get(id);
98          if (user != null) {
99              user.setName(name);
100             user.setEmail(email);
101             System.out.println("Updated user: " + user);
102             return Optional.of(user);
103         }
104         return Optional.empty();
105     }
106
107     public boolean deleteUser(Long id) {
108         User removed = userDatabase.remove(id);
109         if (removed != null) {
110             System.out.println("Deleted user: " + removed);
111             return true;
112         }
113         return false;
114     }
115
116     public int getUserCount() {
117         return userDatabase.size();
118     }
119 }
```

**Line 66**: `@Service` - Marks this class as a Spring-managed service component
- Spring creates a singleton instance automatically
- Available for dependency injection into other components

**Line 68**: `ConcurrentHashMap` - Thread-safe in-memory database for demo purposes
**Line 69**: `AtomicLong` - Thread-safe ID generator

**Line 71**: `@PostConstruct` - Method runs after dependency injection is complete
- Initializes the service with sample data
- Perfect for setup logic that requires dependencies

---

### REST Controller: UserController (Lines 121-179)

```java
121 // REST Controller: Handles HTTP requests
122 @RestController
123 @RequestMapping("/api/users")
124 class UserController {
125
126     @Autowired
127     private UserService userService;
128
129     // GET /api/users - Get all users
130     @GetMapping
131     public ResponseEntity<List<User>> getAllUsers() {
132         System.out.println("GET /api/users - Fetching all users");
133         List<User> users = userService.getAllUsers();
134         return ResponseEntity.ok(users);
135     }
136
137     // GET /api/users/{id} - Get user by ID
138     @GetMapping("/{id}")
139     public ResponseEntity<User> getUserById(@PathVariable Long id) {
140         System.out.println("GET /api/users/" + id + " - Fetching user by ID");
141         return userService.getUserById(id)
142                 .map(ResponseEntity::ok)
143                 .orElse(ResponseEntity.notFound().build());
144     }
145
146     // POST /api/users - Create new user
147     @PostMapping
148     public ResponseEntity<User> createUser(@RequestBody Map<String, String> userData) {
149         System.out.println("POST /api/users - Creating new user");
150         String name = userData.get("name");
151         String email = userData.get("email");
152         User user = userService.createUser(name, email);
153         return ResponseEntity.ok(user);
154     }
155
156     // PUT /api/users/{id} - Update user
157     @PutMapping("/{id}")
158     public ResponseEntity<User> updateUser(@PathVariable Long id, @RequestBody Map<String, String> userData) {
159         System.out.println("PUT /api/users/" + id + " - Updating user");
160         String name = userData.get("name");
161         String email = userData.get("email");
162         return userService.updateUser(id, name, email)
163                 .map(ResponseEntity::ok)
164                 .orElse(ResponseEntity.notFound().build());
165     }
166
167     // DELETE /api/users/{id} - Delete user
168     @DeleteMapping("/{id}")
169     public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
170         System.out.println("DELETE /api/users/" + id + " - Deleting user");
171         boolean deleted = userService.deleteUser(id);
172         return deleted ? ResponseEntity.ok().build() : ResponseEntity.notFound().build();
173     }
174
175     // GET /api/users/stats - Get user statistics
176     @GetMapping("/stats")
177     public ResponseEntity<Map<String, Object>> getStats() {
178         System.out.println("GET /api/users/stats - Fetching statistics");
179         Map<String, Object> stats = new HashMap<>();
180         stats.put("totalUsers", userService.getUserCount());
181         stats.put("timestamp", new Date());
182         return ResponseEntity.ok(stats);
183     }
184 }
```

**Line 122**: `@RestController` - Combines `@Controller` and `@ResponseBody`
- Methods return data directly, not view names
- Return values automatically serialized to JSON

**Line 123**: `@RequestMapping("/api/users")` - Base path for all endpoints in this controller

**Line 126**: `@Autowired` - Dependency injection of UserService
- Spring automatically injects the UserService instance
- No manual instantiation needed

**Line 130**: `@GetMapping` - Maps HTTP GET requests to this method
**Line 147**: `@PostMapping` - Maps HTTP POST requests
**Line 157**: `@PutMapping` - Maps HTTP PUT requests
**Line 168**: `@DeleteMapping` - Maps HTTP DELETE requests

**Line 139**: `@PathVariable` - Extracts value from URL path (e.g., `/api/users/1`)
**Line 148**: `@RequestBody` - Deserializes JSON request body to Java object

---

### Health Check Controller (Lines 186-200)

```java
186 // Health Check Controller
187 @RestController
188 @RequestMapping("/api")
189 class HealthController {
190
191     @GetMapping("/health")
192     public ResponseEntity<Map<String, String>> health() {
193         System.out.println("GET /api/health - Health check requested");
194         Map<String, String> response = new HashMap<>();
195         response.put("status", "UP");
196         response.put("message", "Spring Boot application is running");
197         return ResponseEntity.ok(response);
198     }
199 }
```

**Lines 186-199**: Simple health check endpoint
- Useful for monitoring and load balancers
- Returns application status

---

## Expected Application Output

### Startup Sequence

```
=== Starting Spring Boot Application ===

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v3.2.0)

2024-11-11T10:15:30.123  INFO 1234 --- [main] MainSpringBoot : Starting MainSpringBoot
2024-11-11T10:15:30.456  INFO 1234 --- [main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 8080 (http)
2024-11-11T10:15:30.789  INFO 1234 --- [main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2024-11-11T10:15:30.901  INFO 1234 --- [main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.15]

Initializing UserService with sample data...                    ← Line 74: @PostConstruct initialization
Created user: User{id=1, name='Alice Johnson', email='alice@example.com'}  ← Line 84: First sample user
Created user: User{id=2, name='Bob Smith', email='bob@example.com'}        ← Line 84: Second sample user
Sample users created successfully                                          ← Line 77: Initialization complete

2024-11-11T10:15:31.234  INFO 1234 --- [main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http)
2024-11-11T10:15:31.345  INFO 1234 --- [main] MainSpringBoot : Started MainSpringBoot in 1.5 seconds
```

**Annotations:**
- Spring Boot's ASCII banner appears automatically
- Embedded Tomcat server initializes on port 8080
- UserService `@PostConstruct` method runs, creating sample users
- Application ready in ~1.5 seconds

---

### Testing the REST API

#### 1. Health Check
```bash
curl http://localhost:8080/api/health
```

**Console Output:**
```
GET /api/health - Health check requested                       ← Line 193: Health endpoint called
```

**HTTP Response:**
```json
{
  "status": "UP",
  "message": "Spring Boot application is running"
}
```
**Lines 194-196**: Health status map created and returned

---

#### 2. Get All Users
```bash
curl http://localhost:8080/api/users
```

**Console Output:**
```
GET /api/users - Fetching all users                           ← Line 132: GET endpoint called
```

**HTTP Response:**
```json
[
  {
    "id": 1,
    "name": "Alice Johnson",
    "email": "alice@example.com",
    "createdAt": "2024-11-11T10:15:30.890Z"
  },
  {
    "id": 2,
    "name": "Bob Smith",
    "email": "bob@example.com",
    "createdAt": "2024-11-11T10:15:30.891Z"
  }
]
```
**Line 133**: UserService.getAllUsers() returns all users
**Line 134**: ResponseEntity.ok() returns 200 status with JSON body

---

#### 3. Get User by ID
```bash
curl http://localhost:8080/api/users/1
```

**Console Output:**
```
GET /api/users/1 - Fetching user by ID                        ← Line 140: GET by ID called
```

**HTTP Response:**
```json
{
  "id": 1,
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "createdAt": "2024-11-11T10:15:30.890Z"
}
```
**Line 141-143**: Optional pattern - returns 200 if found, 404 if not

---

#### 4. Create New User
```bash
curl -X POST http://localhost:8080/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Charlie Davis","email":"charlie@example.com"}'
```

**Console Output:**
```
POST /api/users - Creating new user                           ← Line 149: POST endpoint called
Created user: User{id=3, name='Charlie Davis', email='charlie@example.com'}  ← Line 84: User created in service
```

**HTTP Response:**
```json
{
  "id": 3,
  "name": "Charlie Davis",
  "email": "charlie@example.com",
  "createdAt": "2024-11-11T10:16:45.123Z"
}
```
**Line 148**: `@RequestBody` deserializes JSON to Map
**Line 150-151**: Extract name and email from request data
**Line 152**: Service creates user with auto-generated ID (line 81)

---

#### 5. Update User
```bash
curl -X PUT http://localhost:8080/api/users/3 \
  -H "Content-Type: application/json" \
  -d '{"name":"Charlie Davis Jr.","email":"charlie.jr@example.com"}'
```

**Console Output:**
```
PUT /api/users/3 - Updating user                              ← Line 159: PUT endpoint called
Updated user: User{id=3, name='Charlie Davis Jr.', email='charlie.jr@example.com'}  ← Line 101: Update confirmed
```

**HTTP Response:**
```json
{
  "id": 3,
  "name": "Charlie Davis Jr.",
  "email": "charlie.jr@example.com",
  "createdAt": "2024-11-11T10:16:45.123Z"
}
```
**Line 158**: `@PathVariable` extracts ID from URL
**Line 162-164**: Returns 200 if updated, 404 if user not found

---

#### 6. Get Statistics
```bash
curl http://localhost:8080/api/users/stats
```

**Console Output:**
```
GET /api/users/stats - Fetching statistics                    ← Line 178: Stats endpoint called
```

**HTTP Response:**
```json
{
  "totalUsers": 3,
  "timestamp": "2024-11-11T10:17:30.456Z"
}
```
**Line 180**: getUserCount() returns current user count
**Line 181**: Current timestamp added to response

---

#### 7. Delete User
```bash
curl -X DELETE http://localhost:8080/api/users/3
```

**Console Output:**
```
DELETE /api/users/3 - Deleting user                           ← Line 170: DELETE endpoint called
Deleted user: User{id=3, name='Charlie Davis Jr.', email='charlie.jr@example.com'}  ← Line 110: Deletion confirmed
```

**HTTP Response:**
```
HTTP/1.1 200 OK
```
**Line 171**: deleteUser() removes user from map
**Line 172**: Returns 200 if deleted, 404 if user not found

---

## Key Spring Boot Features Demonstrated

### 1. **Auto-Configuration**
- No XML configuration required
- Embedded Tomcat server configured automatically
- JSON serialization (Jackson) enabled by default
- Component scanning happens automatically

### 2. **Dependency Injection**
- `@Autowired` injects UserService into UserController (line 126)
- Spring manages the lifecycle of all beans
- No manual instantiation needed

### 3. **RESTful API**
- Clean, declarative endpoint mapping with annotations
- Automatic JSON serialization/deserialization
- Built-in HTTP status code handling with ResponseEntity

### 4. **Lifecycle Management**
- `@PostConstruct` for initialization logic (line 71)
- Beans created in correct order
- Automatic resource cleanup on shutdown

### 5. **Thread Safety**
- ConcurrentHashMap for thread-safe operations (line 68)
- AtomicLong for thread-safe ID generation (line 69)
- Spring singleton beans are thread-safe by design

---

## Architecture Pattern: MVC (Model-View-Controller)

```
┌─────────────────┐
│  HTTP Request   │
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│   UserController    │  ← Controller Layer (@RestController)
│   (Lines 121-184)   │    - Handles HTTP requests
└────────┬────────────┘    - Routes to service layer
         │                 - Returns HTTP responses
         ▼
┌─────────────────────┐
│    UserService      │  ← Service Layer (@Service)
│   (Lines 65-119)    │    - Business logic
└────────┬────────────┘    - Data validation
         │                 - Transaction management
         ▼
┌─────────────────────┐
│       User          │  ← Model Layer (POJO)
│   (Lines 31-63)     │    - Data structure
└─────────────────────┘    - Validation rules
```

---

## Production Considerations

**What This Example Shows:**
- ✅ Basic Spring Boot setup
- ✅ RESTful API design
- ✅ Dependency injection
- ✅ In-memory data storage
- ✅ Thread-safe operations

**For Production, Add:**
- Real database (PostgreSQL, MySQL) with JPA/Hibernate
- Security (Spring Security, JWT authentication)
- Validation (Bean Validation, `@Valid`)
- Exception handling (ControllerAdvice)
- Logging (SLF4J, Logback)
- Testing (JUnit, MockMvc)
- API documentation (Swagger/OpenAPI)
- Monitoring (Actuator endpoints, Prometheus)

---

## Summary

This example demonstrates **Spring Boot's philosophy of "convention over configuration"**:
- Minimal code to create a fully functional REST API
- Auto-configuration eliminates boilerplate
- Annotations drive behavior declaratively
- Embedded server means no deployment complexity
- Production-ready features available with minimal effort

The application creates a complete CRUD (Create, Read, Update, Delete) REST API for user management in under 200 lines of code!
