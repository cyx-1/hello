#!/bin/bash

# Script to run tests and generate code coverage report
# This demonstrates JUnit testing with embedded Tomcat and database mocking

echo "=========================================="
echo "Spring Boot Test & Coverage Demonstration"
echo "=========================================="
echo ""

# Clean previous builds
echo "Step 1: Cleaning previous builds..."
mvn clean

# Run tests with code coverage
echo ""
echo "Step 2: Running tests (unit + integration)..."
echo "  - Unit tests with mocked repository"
echo "  - Integration tests with embedded Tomcat"
echo "  - Code coverage analysis with JaCoCo"
echo ""
mvn test

# Check if tests succeeded
if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✓ All tests passed!"
    echo "=========================================="
    echo ""
    echo "Code coverage report generated at:"
    echo "  target/site/jacoco/index.html"
    echo ""
    echo "To view the report:"
    echo "  open target/site/jacoco/index.html"
    echo ""
else
    echo ""
    echo "=========================================="
    echo "✗ Tests failed. Check output above."
    echo "=========================================="
    exit 1
fi

# Optional: Run the application
read -p "Do you want to start the application? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "Starting Spring Boot application with embedded Tomcat..."
    echo "Access the API at: http://localhost:8080/api/users"
    echo "Press Ctrl+C to stop"
    echo ""
    mvn spring-boot:run
fi
