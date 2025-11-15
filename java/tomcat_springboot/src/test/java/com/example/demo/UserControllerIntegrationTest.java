package com.example.demo;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.transaction.annotation.Transactional;

import static org.hamcrest.Matchers.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

/**
 * Integration tests for UserController.
 * Demonstrates:
 * - @SpringBootTest to launch embedded Tomcat server
 * - MockMvc to test REST endpoints
 * - Real database interactions with H2 in-memory database
 * - End-to-end testing of the application
 * - Code coverage across all layers
 */
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
@ActiveProfiles("test")
@Transactional
class UserControllerIntegrationTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @Autowired
    private UserRepository userRepository;

    @Test
    void createUser_Success() throws Exception {
        // Arrange
        User newUser = new User("Alice Johnson", "alice@example.com", 28);

        // Act & Assert: POST request to create user
        mockMvc.perform(post("/api/users")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(newUser)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.id").exists())
                .andExpect(jsonPath("$.name").value("Alice Johnson"))
                .andExpect(jsonPath("$.email").value("alice@example.com"))
                .andExpect(jsonPath("$.age").value(28));
    }

    @Test
    void createUser_DuplicateEmail_ReturnsBadRequest() throws Exception {
        // Arrange: Create first user
        User user1 = new User("Bob Smith", "bob@example.com", 35);
        userRepository.save(user1);

        // Try to create another user with same email
        User user2 = new User("Bob Different", "bob@example.com", 40);

        // Act & Assert
        mockMvc.perform(post("/api/users")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(user2)))
                .andExpect(status().isBadRequest())
                .andExpect(content().string(containsString("already exists")));
    }

    @Test
    void createUser_InvalidEmail_ReturnsBadRequest() throws Exception {
        // Arrange: User with invalid email
        User invalidUser = new User("Charlie", "invalid-email", 25);

        // Act & Assert
        mockMvc.perform(post("/api/users")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(invalidUser)))
                .andExpect(status().isBadRequest());
    }

    @Test
    void getAllUsers_ReturnsEmptyList() throws Exception {
        // Act & Assert
        mockMvc.perform(get("/api/users"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$", hasSize(0)));
    }

    @Test
    void getAllUsers_ReturnsMultipleUsers() throws Exception {
        // Arrange: Create multiple users
        userRepository.save(new User("User 1", "user1@example.com", 20));
        userRepository.save(new User("User 2", "user2@example.com", 30));
        userRepository.save(new User("User 3", "user3@example.com", 40));

        // Act & Assert
        mockMvc.perform(get("/api/users"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$", hasSize(3)))
                .andExpect(jsonPath("$[0].name").value("User 1"))
                .andExpect(jsonPath("$[1].name").value("User 2"))
                .andExpect(jsonPath("$[2].name").value("User 3"));
    }

    @Test
    void getUserById_Found() throws Exception {
        // Arrange
        User user = userRepository.save(new User("David Lee", "david@example.com", 32));

        // Act & Assert
        mockMvc.perform(get("/api/users/" + user.getId()))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.name").value("David Lee"))
                .andExpect(jsonPath("$.email").value("david@example.com"))
                .andExpect(jsonPath("$.age").value(32));
    }

    @Test
    void getUserById_NotFound() throws Exception {
        // Act & Assert
        mockMvc.perform(get("/api/users/999"))
                .andExpect(status().isNotFound());
    }

    @Test
    void getUsersOlderThan_ReturnsFilteredUsers() throws Exception {
        // Arrange
        userRepository.save(new User("Young User", "young@example.com", 20));
        userRepository.save(new User("Middle User", "middle@example.com", 30));
        userRepository.save(new User("Old User", "old@example.com", 40));

        // Act & Assert: Get users older than 25
        mockMvc.perform(get("/api/users/age/25"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$", hasSize(2)))
                .andExpect(jsonPath("$[*].age", everyItem(greaterThan(25))));
    }

    @Test
    void getUsersOlderThan_InvalidAge_ReturnsBadRequest() throws Exception {
        // Act & Assert
        mockMvc.perform(get("/api/users/age/-5"))
                .andExpect(status().isBadRequest());
    }

    @Test
    void updateUser_Success() throws Exception {
        // Arrange: Create initial user
        User user = userRepository.save(new User("Emma Wilson", "emma@example.com", 27));

        // Update data
        User updateData = new User("Emma Wilson-Updated", "emma.new@example.com", 28);

        // Act & Assert
        mockMvc.perform(put("/api/users/" + user.getId())
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(updateData)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.name").value("Emma Wilson-Updated"))
                .andExpect(jsonPath("$.email").value("emma.new@example.com"))
                .andExpect(jsonPath("$.age").value(28));
    }

    @Test
    void updateUser_NotFound_ReturnsBadRequest() throws Exception {
        // Arrange
        User updateData = new User("Nobody", "nobody@example.com", 99);

        // Act & Assert
        mockMvc.perform(put("/api/users/999")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(updateData)))
                .andExpect(status().isBadRequest());
    }

    @Test
    void deleteUser_Success() throws Exception {
        // Arrange
        User user = userRepository.save(new User("Frank Brown", "frank@example.com", 45));

        // Act & Assert: Delete user
        mockMvc.perform(delete("/api/users/" + user.getId()))
                .andExpect(status().isNoContent());

        // Verify user is deleted
        mockMvc.perform(get("/api/users/" + user.getId()))
                .andExpect(status().isNotFound());
    }

    @Test
    void deleteUser_NotFound_ReturnsNotFound() throws Exception {
        // Act & Assert
        mockMvc.perform(delete("/api/users/999"))
                .andExpect(status().isNotFound());
    }

    @Test
    void existsByEmail_True() throws Exception {
        // Arrange
        userRepository.save(new User("Grace Taylor", "grace@example.com", 29));

        // Act & Assert
        mockMvc.perform(get("/api/users/exists/grace@example.com"))
                .andExpect(status().isOk())
                .andExpect(content().string("true"));
    }

    @Test
    void existsByEmail_False() throws Exception {
        // Act & Assert
        mockMvc.perform(get("/api/users/exists/nonexistent@example.com"))
                .andExpect(status().isOk())
                .andExpect(content().string("false"));
    }

    @Test
    void fullWorkflow_CreateUpdateDelete() throws Exception {
        // Step 1: Create user
        User newUser = new User("Harry Potter", "harry@hogwarts.com", 17);

        String response = mockMvc.perform(post("/api/users")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(newUser)))
                .andExpect(status().isCreated())
                .andReturn()
                .getResponse()
                .getContentAsString();

        User createdUser = objectMapper.readValue(response, User.class);
        Long userId = createdUser.getId();

        // Step 2: Verify user exists
        mockMvc.perform(get("/api/users/" + userId))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.name").value("Harry Potter"));

        // Step 3: Update user
        User updateData = new User("Harry Potter-Updated", "harry.new@hogwarts.com", 18);
        mockMvc.perform(put("/api/users/" + userId)
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(updateData)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.age").value(18));

        // Step 4: Delete user
        mockMvc.perform(delete("/api/users/" + userId))
                .andExpect(status().isNoContent());

        // Step 5: Verify deletion
        mockMvc.perform(get("/api/users/" + userId))
                .andExpect(status().isNotFound());
    }
}
