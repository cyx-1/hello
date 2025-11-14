import jakarta.persistence.*;
import java.util.List;

/**
 * Hibernate JPA with H2 Database demonstration
 * This example shows CRUD operations using JPA and an in-memory H2 database
 */

// Entity class representing a User table
@Entity
@Table(name = "users")
class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name;

    @Column(unique = true, nullable = false)
    private String email;

    @Column
    private Integer age;

    // Default constructor required by JPA
    public User() {
    }

    public User(String name, String email, Integer age) {
        this.name = name;
        this.email = email;
        this.age = age;
    }

    // Getters and setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                ", age=" + age +
                '}';
    }
}

public class MainHibernateJpaH2 {

    private static EntityManagerFactory emf;

    public static void main(String[] args) {
        try {
            // Line 82-83: Initialize EntityManagerFactory with persistence unit
            System.out.println("=== Initializing Hibernate JPA with H2 Database ===");
            emf = Persistence.createEntityManagerFactory("hibernate-h2-demo");

            // Line 86-87: CREATE - Insert new users
            System.out.println("\n=== Creating Users ===");
            createUser("Alice Johnson", "alice@example.com", 28);
            createUser("Bob Smith", "bob@example.com", 35);
            createUser("Carol White", "carol@example.com", 42);

            // Line 92-93: READ - Query all users
            System.out.println("\n=== Reading All Users ===");
            List<User> allUsers = findAllUsers();
            allUsers.forEach(System.out::println);

            // Line 97-99: UPDATE - Modify a user
            System.out.println("\n=== Updating User ===");
            if (!allUsers.isEmpty()) {
                updateUser(allUsers.get(0).getId(), "Alice Johnson-Updated", 29);
            }

            // Line 103-104: Query users by criteria
            System.out.println("\n=== Finding Users Over Age 30 ===");
            List<User> usersOver30 = findUsersByAgeGreaterThan(30);
            usersOver30.forEach(System.out::println);

            // Line 108-111: DELETE - Remove a user
            System.out.println("\n=== Deleting User ===");
            if (allUsers.size() > 1) {
                deleteUser(allUsers.get(1).getId());
            }

            // Line 114-116: Final state
            System.out.println("\n=== Final User List ===");
            List<User> finalUsers = findAllUsers();
            finalUsers.forEach(System.out::println);

            // Line 119-120: Named query example
            System.out.println("\n=== Using JPQL Query ===");
            demonstrateJPQLQuery();

        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            // Line 126-127: Clean up resources
            if (emf != null) {
                emf.close();
            }
            System.out.println("\n=== EntityManagerFactory closed ===");
        }
    }

    // CREATE operation
    private static void createUser(String name, String email, Integer age) {
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = null;
        try {
            tx = em.getTransaction();
            tx.begin();

            User user = new User(name, email, age);
            em.persist(user);

            tx.commit();
            System.out.println("Created: " + user);
        } catch (Exception e) {
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            e.printStackTrace();
        } finally {
            em.close();
        }
    }

    // READ operation - Find all users
    private static List<User> findAllUsers() {
        EntityManager em = emf.createEntityManager();
        try {
            TypedQuery<User> query = em.createQuery("SELECT u FROM User u", User.class);
            return query.getResultList();
        } finally {
            em.close();
        }
    }

    // READ operation - Find users by criteria
    private static List<User> findUsersByAgeGreaterThan(int age) {
        EntityManager em = emf.createEntityManager();
        try {
            TypedQuery<User> query = em.createQuery(
                    "SELECT u FROM User u WHERE u.age > :age ORDER BY u.age", User.class);
            query.setParameter("age", age);
            return query.getResultList();
        } finally {
            em.close();
        }
    }

    // UPDATE operation
    private static void updateUser(Long id, String newName, Integer newAge) {
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = null;
        try {
            tx = em.getTransaction();
            tx.begin();

            User user = em.find(User.class, id);
            if (user != null) {
                user.setName(newName);
                user.setAge(newAge);
                // em.merge() not needed - user is managed
                System.out.println("Updated: " + user);
            }

            tx.commit();
        } catch (Exception e) {
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            e.printStackTrace();
        } finally {
            em.close();
        }
    }

    // DELETE operation
    private static void deleteUser(Long id) {
        EntityManager em = emf.createEntityManager();
        EntityTransaction tx = null;
        try {
            tx = em.getTransaction();
            tx.begin();

            User user = em.find(User.class, id);
            if (user != null) {
                em.remove(user);
                System.out.println("Deleted user with ID: " + id);
            }

            tx.commit();
        } catch (Exception e) {
            if (tx != null && tx.isActive()) {
                tx.rollback();
            }
            e.printStackTrace();
        } finally {
            em.close();
        }
    }

    // Demonstrate JPQL query with aggregate function
    private static void demonstrateJPQLQuery() {
        EntityManager em = emf.createEntityManager();
        try {
            // Count total users
            TypedQuery<Long> countQuery = em.createQuery(
                    "SELECT COUNT(u) FROM User u", Long.class);
            Long count = countQuery.getSingleResult();
            System.out.println("Total users: " + count);

            // Get average age
            TypedQuery<Double> avgQuery = em.createQuery(
                    "SELECT AVG(u.age) FROM User u", Double.class);
            Double avgAge = avgQuery.getSingleResult();
            System.out.println("Average age: " + avgAge);
        } finally {
            em.close();
        }
    }
}
