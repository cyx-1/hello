# Hibernate JPA with H2 Database Demo

This example demonstrates how to use Hibernate JPA (Java Persistence API) with an in-memory H2 database to perform CRUD operations.

## Requirements

- **Java Version**: Java 17 or higher
- **Hibernate Version**: 6.4.4.Final (uses Jakarta EE 9+ with `jakarta.persistence.*` packages)
- **H2 Database Version**: 2.2.224

## Project Structure

```
hibernate-jpa-h2/
├── pom.xml
├── src/
│   └── main/
│       ├── java/
│       │   └── MainHibernateJpaH2.java
│       └── resources/
│           └── META-INF/
│               └── persistence.xml
└── README.md
```

## How to Run

```bash
cd java/hibernate-jpa-h2
mvn clean compile exec:java
```

## Key Source Code Components

### Entity Definition (Lines 8-69)

```java
8   @Entity
9   @Table(name = "users")
10  class User {
11      @Id
12      @GeneratedValue(strategy = GenerationType.IDENTITY)
13      private Long id;
14
15      @Column(nullable = false, length = 100)
16      private String name;
17
18      @Column(unique = true, nullable = false)
19      private String email;
20
21      @Column
22      private Integer age;
```

**Annotations Explained:**
- **Line 8** (`@Entity`): Marks this class as a JPA entity that maps to a database table
- **Line 9** (`@Table`): Specifies the table name as "users"
- **Line 11** (`@Id`): Designates the primary key field
- **Line 12** (`@GeneratedValue`): Auto-generates ID values using database identity column
- **Lines 15-22**: Column constraints like nullable, unique, and length

### EntityManagerFactory Initialization (Lines 82-83)

```java
82      System.out.println("=== Initializing Hibernate JPA with H2 Database ===");
83      emf = Persistence.createEntityManagerFactory("hibernate-h2-demo");
```

**What happens here:**
- Creates the EntityManagerFactory from `persistence.xml` configuration
- Connects to H2 in-memory database
- Creates the `users` table automatically (due to `hibernate.hbm2ddl.auto=create-drop`)

### CREATE Operation (Lines 86-88)

```java
86      System.out.println("\n=== Creating Users ===");
87      createUser("Alice Johnson", "alice@example.com", 28);
88      createUser("Bob Smith", "bob@example.com", 35);
89      createUser("Carol White", "carol@example.com", 42);
```

**Implementation (Lines 134-152):**
```java
134  private static void createUser(String name, String email, Integer age) {
135      EntityManager em = emf.createEntityManager();
136      EntityTransaction tx = null;
137      try {
138          tx = em.getTransaction();
139          tx.begin();
140
141          User user = new User(name, email, age);
142          em.persist(user);  // Persist the entity
143
144          tx.commit();  // Commit transaction
145          System.out.println("Created: " + user);
146      } catch (Exception e) {
147          if (tx != null && tx.isActive()) {
148              tx.rollback();  // Rollback on error
149          }
150          e.printStackTrace();
151      } finally {
152          em.close();  // Always close EntityManager
153      }
154  }
```

### READ Operations (Lines 92-106)

```java
92      System.out.println("\n=== Reading All Users ===");
93      List<User> allUsers = findAllUsers();
94      allUsers.forEach(System.out::println);
...
103     System.out.println("\n=== Finding Users Over Age 30 ===");
104     List<User> usersOver30 = findUsersByAgeGreaterThan(30);
105     usersOver30.forEach(System.out::println);
```

**JPQL Query Example (Lines 157-165):**
```java
157  private static List<User> findAllUsers() {
158      EntityManager em = emf.createEntityManager();
159      try {
160          TypedQuery<User> query = em.createQuery("SELECT u FROM User u", User.class);
161          return query.getResultList();
162      } finally {
163          em.close();
164      }
165  }
```

**Parameterized Query (Lines 168-177):**
```java
168  private static List<User> findUsersByAgeGreaterThan(int age) {
169      EntityManager em = emf.createEntityManager();
170      try {
171          TypedQuery<User> query = em.createQuery(
172              "SELECT u FROM User u WHERE u.age > :age ORDER BY u.age", User.class);
173          query.setParameter("age", age);  // Bind parameter
174          return query.getResultList();
175      } finally {
176          em.close();
177      }
178  }
```

### UPDATE Operation (Lines 97-100)

```java
97      System.out.println("\n=== Updating User ===");
98      if (!allUsers.isEmpty()) {
99          updateUser(allUsers.get(0).getId(), "Alice Johnson-Updated", 29);
100     }
```

**Implementation (Lines 181-200):**
```java
181  private static void updateUser(Long id, String newName, Integer newAge) {
182      EntityManager em = emf.createEntityManager();
183      EntityTransaction tx = null;
184      try {
185          tx = em.getTransaction();
186          tx.begin();
187
188          User user = em.find(User.class, id);  // Find entity by ID
189          if (user != null) {
190              user.setName(newName);  // Modify entity
191              user.setAge(newAge);
192              // No em.merge() needed - entity is managed
193              System.out.println("Updated: " + user);
194          }
195
196          tx.commit();  // Changes automatically persisted
197      } catch (Exception e) {
198          if (tx != null && tx.isActive()) {
199              tx.rollback();
200          }
```

**Important Note (Line 192):** Managed entities are automatically synchronized with the database when the transaction commits, so explicit `em.merge()` is not needed.

### DELETE Operation (Lines 108-111)

```java
108     System.out.println("\n=== Deleting User ===");
109     if (allUsers.size() > 1) {
110         deleteUser(allUsers.get(1).getId());
111     }
```

**Implementation (Lines 207-225):**
```java
207  private static void deleteUser(Long id) {
208      EntityManager em = emf.createEntityManager();
209      EntityTransaction tx = null;
210      try {
211          tx = em.getTransaction();
212          tx.begin();
213
214          User user = em.find(User.class, id);
215          if (user != null) {
216              em.remove(user);  // Remove entity
217              System.out.println("Deleted user with ID: " + id);
218          }
219
220          tx.commit();
221      } catch (Exception e) {
222          if (tx != null && tx.isActive()) {
223              tx.rollback();
224          }
```

### JPQL Aggregate Functions (Lines 119-120)

```java
119     System.out.println("\n=== Using JPQL Query ===");
120     demonstrateJPQLQuery();
```

**Implementation (Lines 230-245):**
```java
230  private static void demonstrateJPQLQuery() {
231      EntityManager em = emf.createEntityManager();
232      try {
233          // Count total users
234          TypedQuery<Long> countQuery = em.createQuery(
235              "SELECT COUNT(u) FROM User u", Long.class);
236          Long count = countQuery.getSingleResult();
237          System.out.println("Total users: " + count);
238
239          // Get average age
240          TypedQuery<Double> avgQuery = em.createQuery(
241              "SELECT AVG(u.age) FROM User u", Double.class);
242          Double avgAge = avgQuery.getSingleResult();
243          System.out.println("Average age: " + avgAge);
244      } finally {
245          em.close();
246      }
247  }
```

## Expected Output

```
=== Initializing Hibernate JPA with H2 Database ===

=== Creating Users ===
Created: User{id=1, name='Alice Johnson', email='alice@example.com', age=28}
Created: User{id=2, name='Bob Smith', email='bob@example.com', age=35}
Created: User{id=3, name='Carol White', email='carol@example.com', age=42}

=== Reading All Users ===
User{id=1, name='Alice Johnson', email='alice@example.com', age=28}
User{id=2, name='Bob Smith', email='bob@example.com', age=35}
User{id=3, name='Carol White', email='carol@example.com', age=42}

=== Updating User ===
Updated: User{id=1, name='Alice Johnson-Updated', email='alice@example.com', age=29}

=== Finding Users Over Age 30 ===
User{id=2, name='Bob Smith', email='bob@example.com', age=35}
User{id=3, name='Carol White', email='carol@example.com', age=42}

=== Deleting User ===
Deleted user with ID: 2

=== Final User List ===
User{id=1, name='Alice Johnson-Updated', email='alice@example.com', age=29}
User{id=3, name='Carol White', email='carol@example.com', age=42}

=== Using JPQL Query ===
Total users: 2
Average age: 35.5

=== EntityManagerFactory closed ===
```

## Output Annotations

### Initialization Section
The initialization output confirms that Hibernate successfully:
1. Connects to the H2 in-memory database
2. Creates the `users` table based on the `User` entity definition
3. Sets up the EntityManagerFactory for managing database operations

### CREATE Section (Output Lines 3-5)
- Shows three users being inserted into the database
- Each user is assigned an auto-generated ID (1, 2, 3)
- The ID generation corresponds to `@GeneratedValue(strategy = GenerationType.IDENTITY)` on line 12

### READ Section (Output Lines 7-9)
- Displays all users retrieved using JPQL query: `SELECT u FROM User u`
- Demonstrates that all three users were successfully persisted
- Correlates with source code lines 92-94

### UPDATE Section (Output Line 11)
- Shows Alice's record being modified (name and age changed)
- ID remains 1, but name now includes "-Updated" suffix and age is 29
- Demonstrates JPA's automatic dirty checking (source line 192 comment)

### Filtered READ Section (Output Lines 13-14)
- Shows only users where age > 30 (Bob: 35, Carol: 42)
- Results are ordered by age (ascending)
- Demonstrates parameterized JPQL query from source lines 171-173

### DELETE Section (Output Line 16)
- Bob (ID: 2) is removed from the database
- Corresponds to source code lines 108-111

### Final State Section (Output Lines 18-19)
- Shows remaining users after all operations
- Only Alice (updated) and Carol remain
- Bob was successfully deleted

### JPQL Aggregates Section (Output Lines 21-22)
- **Total users: 2** - COUNT aggregate function (source line 234-236)
- **Average age: 35.5** - AVG aggregate function calculates (29 + 42) / 2 = 35.5 (source line 240-242)

## Key JPA Concepts Demonstrated

1. **Entity Mapping**: `@Entity`, `@Table`, `@Column` annotations
2. **Primary Key Generation**: `@Id` with `@GeneratedValue`
3. **EntityManager Lifecycle**: Creating, using, and closing EntityManager instances
4. **Transaction Management**: Begin, commit, and rollback
5. **CRUD Operations**: persist(), find(), merge(), remove()
6. **JPQL Queries**: TypedQuery with parameterized and aggregate queries
7. **Automatic Schema Generation**: `hibernate.hbm2ddl.auto=create-drop`
8. **Managed Entities**: Automatic synchronization without explicit merge()

## Configuration Notes

### persistence.xml
The `persistence.xml` file configures:
- **Database URL**: `jdbc:h2:mem:testdb` (in-memory database)
- **Hibernate Dialect**: `H2Dialect`
- **Schema Management**: `create-drop` (creates on startup, drops on shutdown)
- **SQL Logging**: Disabled for cleaner output (`hibernate.show_sql=false`)

### H2 Database
- **In-Memory**: Data exists only during application runtime
- **DB_CLOSE_DELAY=-1**: Keeps database open for entire JVM lifetime
- **No persistence**: All data is lost when application terminates

## Dependencies

From `pom.xml`:

```xml
<!-- Hibernate ORM 6.4.4.Final -->
<dependency>
    <groupId>org.hibernate.orm</groupId>
    <artifactId>hibernate-core</artifactId>
</dependency>

<!-- H2 Database 2.2.224 -->
<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
</dependency>

<!-- Jakarta Persistence API 3.1.0 -->
<dependency>
    <groupId>jakarta.persistence</groupId>
    <artifactId>jakarta.persistence-api</artifactId>
</dependency>
```

**Important**: This example requires Hibernate 6.x which uses the `jakarta.persistence.*` package namespace (not the older `javax.persistence.*`). This is part of the transition from Java EE to Jakarta EE.
