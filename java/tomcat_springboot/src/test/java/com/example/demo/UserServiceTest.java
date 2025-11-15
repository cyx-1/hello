package com.example.demo;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

/**
 * Unit tests for UserService with mocked repository.
 * Demonstrates:
 * - Mockito for mocking database layer
 * - Testing business logic in isolation
 * - Code coverage of service methods
 */
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserService userService;

    private User testUser;

    @BeforeEach
    void setUp() {
        testUser = new User("John Doe", "john@example.com", 30);
        testUser.setId(1L);
    }

    @Test
    void createUser_Success() {
        // Arrange: Mock repository behavior
        when(userRepository.findByEmail(testUser.getEmail())).thenReturn(Optional.empty());
        when(userRepository.save(any(User.class))).thenReturn(testUser);

        // Act: Call service method
        User createdUser = userService.createUser(testUser);

        // Assert: Verify results
        assertNotNull(createdUser);
        assertEquals("John Doe", createdUser.getName());
        assertEquals("john@example.com", createdUser.getEmail());

        // Verify mock interactions
        verify(userRepository, times(1)).findByEmail(testUser.getEmail());
        verify(userRepository, times(1)).save(any(User.class));
    }

    @Test
    void createUser_DuplicateEmail_ThrowsException() {
        // Arrange: Mock existing user with same email
        when(userRepository.findByEmail(testUser.getEmail())).thenReturn(Optional.of(testUser));

        // Act & Assert: Verify exception is thrown
        IllegalArgumentException exception = assertThrows(
                IllegalArgumentException.class,
                () -> userService.createUser(testUser)
        );

        assertTrue(exception.getMessage().contains("already exists"));
        verify(userRepository, times(1)).findByEmail(testUser.getEmail());
        verify(userRepository, never()).save(any(User.class));
    }

    @Test
    void createUser_NegativeAge_ThrowsException() {
        // Arrange: User with negative age
        User invalidUser = new User("Jane Doe", "jane@example.com", -5);
        when(userRepository.findByEmail(invalidUser.getEmail())).thenReturn(Optional.empty());

        // Act & Assert
        IllegalArgumentException exception = assertThrows(
                IllegalArgumentException.class,
                () -> userService.createUser(invalidUser)
        );

        assertTrue(exception.getMessage().contains("Age cannot be negative"));
        verify(userRepository, never()).save(any(User.class));
    }

    @Test
    void getUserById_Found() {
        // Arrange
        when(userRepository.findById(1L)).thenReturn(Optional.of(testUser));

        // Act
        Optional<User> foundUser = userService.getUserById(1L);

        // Assert
        assertTrue(foundUser.isPresent());
        assertEquals("John Doe", foundUser.get().getName());
        verify(userRepository, times(1)).findById(1L);
    }

    @Test
    void getUserById_NotFound() {
        // Arrange
        when(userRepository.findById(999L)).thenReturn(Optional.empty());

        // Act
        Optional<User> foundUser = userService.getUserById(999L);

        // Assert
        assertFalse(foundUser.isPresent());
        verify(userRepository, times(1)).findById(999L);
    }

    @Test
    void getAllUsers_ReturnsMultiple() {
        // Arrange
        User user2 = new User("Jane Smith", "jane@example.com", 25);
        user2.setId(2L);
        List<User> users = Arrays.asList(testUser, user2);
        when(userRepository.findAll()).thenReturn(users);

        // Act
        List<User> allUsers = userService.getAllUsers();

        // Assert
        assertEquals(2, allUsers.size());
        verify(userRepository, times(1)).findAll();
    }

    @Test
    void getUsersOlderThan_Success() {
        // Arrange
        List<User> olderUsers = Arrays.asList(testUser);
        when(userRepository.findByAgeGreaterThan(25)).thenReturn(olderUsers);

        // Act
        List<User> result = userService.getUsersOlderThan(25);

        // Assert
        assertEquals(1, result.size());
        assertEquals(30, result.get(0).getAge());
        verify(userRepository, times(1)).findByAgeGreaterThan(25);
    }

    @Test
    void getUsersOlderThan_NegativeAge_ThrowsException() {
        // Act & Assert
        assertThrows(IllegalArgumentException.class, () -> userService.getUsersOlderThan(-5));
        verify(userRepository, never()).findByAgeGreaterThan(anyInt());
    }

    @Test
    void updateUser_Success() {
        // Arrange
        User updatedData = new User("John Updated", "john.updated@example.com", 31);
        when(userRepository.findById(1L)).thenReturn(Optional.of(testUser));
        when(userRepository.findByEmail("john.updated@example.com")).thenReturn(Optional.empty());
        when(userRepository.save(any(User.class))).thenReturn(testUser);

        // Act
        User result = userService.updateUser(1L, updatedData);

        // Assert
        assertNotNull(result);
        verify(userRepository, times(1)).save(any(User.class));
    }

    @Test
    void updateUser_NotFound_ThrowsException() {
        // Arrange
        when(userRepository.findById(999L)).thenReturn(Optional.empty());

        // Act & Assert
        assertThrows(IllegalArgumentException.class,
                () -> userService.updateUser(999L, new User()));
        verify(userRepository, never()).save(any(User.class));
    }

    @Test
    void updateUser_DuplicateEmail_ThrowsException() {
        // Arrange
        User anotherUser = new User("Another User", "another@example.com", 28);
        anotherUser.setId(2L);

        User updateData = new User();
        updateData.setEmail("another@example.com");

        when(userRepository.findById(1L)).thenReturn(Optional.of(testUser));
        when(userRepository.findByEmail("another@example.com")).thenReturn(Optional.of(anotherUser));

        // Act & Assert
        assertThrows(IllegalArgumentException.class,
                () -> userService.updateUser(1L, updateData));
        verify(userRepository, never()).save(any(User.class));
    }

    @Test
    void deleteUser_Success() {
        // Arrange
        when(userRepository.existsById(1L)).thenReturn(true);
        doNothing().when(userRepository).deleteById(1L);

        // Act
        userService.deleteUser(1L);

        // Assert
        verify(userRepository, times(1)).existsById(1L);
        verify(userRepository, times(1)).deleteById(1L);
    }

    @Test
    void deleteUser_NotFound_ThrowsException() {
        // Arrange
        when(userRepository.existsById(999L)).thenReturn(false);

        // Act & Assert
        assertThrows(IllegalArgumentException.class, () -> userService.deleteUser(999L));
        verify(userRepository, never()).deleteById(anyLong());
    }

    @Test
    void existsByEmail_True() {
        // Arrange
        when(userRepository.findByEmail("john@example.com")).thenReturn(Optional.of(testUser));

        // Act
        boolean exists = userService.existsByEmail("john@example.com");

        // Assert
        assertTrue(exists);
        verify(userRepository, times(1)).findByEmail("john@example.com");
    }

    @Test
    void existsByEmail_False() {
        // Arrange
        when(userRepository.findByEmail("nonexistent@example.com")).thenReturn(Optional.empty());

        // Act
        boolean exists = userService.existsByEmail("nonexistent@example.com");

        // Assert
        assertFalse(exists);
        verify(userRepository, times(1)).findByEmail("nonexistent@example.com");
    }
}
