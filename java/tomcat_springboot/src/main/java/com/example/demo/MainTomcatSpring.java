package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Main Spring Boot Application demonstrating:
 * - Embedded Tomcat server
 * - JUnit 5 testing with MockMvc
 * - Database layer mocking
 * - Code coverage with JaCoCo
 */
@SpringBootApplication
public class MainTomcatSpring {

    public static void main(String[] args) {
        SpringApplication.run(MainTomcatSpring.class, args);
    }
}
