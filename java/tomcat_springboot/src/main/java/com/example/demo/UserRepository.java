package com.example.demo;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

/**
 * Repository interface for User entity.
 * Spring Data JPA will provide the implementation automatically.
 * This will be mocked in our JUnit tests to avoid actual database operations.
 */
@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    /**
     * Find a user by email address.
     * @param email the email to search for
     * @return Optional containing the user if found
     */
    Optional<User> findByEmail(String email);

    /**
     * Find all users older than a specific age.
     * @param age the minimum age
     * @return list of users
     */
    List<User> findByAgeGreaterThan(Integer age);
}
