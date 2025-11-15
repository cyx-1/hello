package com.example.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

/**
 * Service layer containing business logic for User operations.
 * This layer will be tested with mocked repository to demonstrate:
 * - Unit testing with mocks
 * - Code coverage of business logic
 */
@Service
public class UserService {

    private final UserRepository userRepository;

    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    /**
     * Create a new user.
     * Business rule: Email must be unique.
     */
    public User createUser(User user) {
        // Business logic: Check if email already exists
        Optional<User> existingUser = userRepository.findByEmail(user.getEmail());
        if (existingUser.isPresent()) {
            throw new IllegalArgumentException("User with email " + user.getEmail() + " already exists");
        }

        // Business logic: Validate age if provided
        if (user.getAge() != null && user.getAge() < 0) {
            throw new IllegalArgumentException("Age cannot be negative");
        }

        return userRepository.save(user);
    }

    /**
     * Get a user by ID.
     */
    public Optional<User> getUserById(Long id) {
        return userRepository.findById(id);
    }

    /**
     * Get all users.
     */
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    /**
     * Get users older than a specific age.
     * Business rule: Age filtering.
     */
    public List<User> getUsersOlderThan(Integer age) {
        if (age == null || age < 0) {
            throw new IllegalArgumentException("Age must be a positive number");
        }
        return userRepository.findByAgeGreaterThan(age);
    }

    /**
     * Update a user.
     * Business rule: User must exist.
     */
    public User updateUser(Long id, User updatedUser) {
        User existingUser = userRepository.findById(id)
                .orElseThrow(() -> new IllegalArgumentException("User with ID " + id + " not found"));

        // Update fields
        if (updatedUser.getName() != null) {
            existingUser.setName(updatedUser.getName());
        }
        if (updatedUser.getEmail() != null) {
            // Check email uniqueness if changing
            if (!existingUser.getEmail().equals(updatedUser.getEmail())) {
                Optional<User> userWithEmail = userRepository.findByEmail(updatedUser.getEmail());
                if (userWithEmail.isPresent()) {
                    throw new IllegalArgumentException("Email " + updatedUser.getEmail() + " is already in use");
                }
            }
            existingUser.setEmail(updatedUser.getEmail());
        }
        if (updatedUser.getAge() != null) {
            if (updatedUser.getAge() < 0) {
                throw new IllegalArgumentException("Age cannot be negative");
            }
            existingUser.setAge(updatedUser.getAge());
        }

        return userRepository.save(existingUser);
    }

    /**
     * Delete a user by ID.
     */
    public void deleteUser(Long id) {
        if (!userRepository.existsById(id)) {
            throw new IllegalArgumentException("User with ID " + id + " not found");
        }
        userRepository.deleteById(id);
    }

    /**
     * Check if a user exists by email.
     */
    public boolean existsByEmail(String email) {
        return userRepository.findByEmail(email).isPresent();
    }
}
