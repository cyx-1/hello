#!/usr/bin/env swift
// main_basic.swift - Demonstrates fundamental Swift language features

import Foundation

// MARK: - 1. Variables and Constants
print("=== 1. Variables and Constants ===")
let constant = "I cannot be changed"      // Line 9: immutable with 'let'
var variable = "I can be changed"          // Line 10: mutable with 'var'
variable = "See, I changed!"
print("Constant: \(constant)")             // Line 12: string interpolation
print("Variable: \(variable)")

// MARK: - 2. Basic Types
print("\n=== 2. Basic Types ===")
let integer: Int = 42                      // Line 17: explicit type annotation
let double: Double = 3.14159
let boolean: Bool = true
let character: Character = "A"
let string: String = "Hello, Swift!"
print("Int: \(integer), Double: \(double), Bool: \(boolean), Char: \(character)")
print("String: \(string)")

// MARK: - 3. Type Inference
print("\n=== 3. Type Inference ===")
let inferredInt = 100                      // Line 26: Swift infers Int
let inferredDouble = 2.718                 // Line 27: Swift infers Double
let inferredString = "Inferred!"           // Line 28: Swift infers String
print("Inferred types - Int: \(inferredInt), Double: \(inferredDouble), String: \(inferredString)")

// MARK: - 4. Collections
print("\n=== 4. Collections ===")

// Arrays
var fruits = ["Apple", "Banana", "Cherry"] // Line 34: Array literal
fruits.append("Date")                       // Line 35: Append element
print("Fruits array: \(fruits)")
print("First fruit: \(fruits[0])")          // Line 37: Subscript access

// Dictionaries
var ages: [String: Int] = [                 // Line 40: Dictionary with type
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35
]
ages["Diana"] = 28                          // Line 45: Add new key-value
print("Ages dictionary: \(ages)")
print("Alice's age: \(ages["Alice"] ?? 0)") // Line 47: Optional unwrapping with ??

// Sets
var uniqueNumbers: Set<Int> = [1, 2, 3, 2, 1] // Line 50: Set removes duplicates
uniqueNumbers.insert(4)
print("Unique numbers set: \(uniqueNumbers)")

// MARK: - 5. Optionals
print("\n=== 5. Optionals ===")
var optionalName: String? = nil            // Line 56: Optional can be nil
print("Optional is nil: \(optionalName == nil)")

optionalName = "Swift Developer"
if let name = optionalName {                // Line 60: Optional binding
    print("Unwrapped name: \(name)")
}

let forcedName = optionalName!              // Line 64: Force unwrap (use carefully!)
print("Force unwrapped: \(forcedName)")

let defaultName = optionalName ?? "Unknown" // Line 67: Nil coalescing
print("With default: \(defaultName)")

// MARK: - 6. Control Flow
print("\n=== 6. Control Flow ===")

// If-else
let score = 85
if score >= 90 {                            // Line 74: If statement
    print("Grade: A")
} else if score >= 80 {
    print("Grade: B")
} else {
    print("Grade: C or below")
}

// Switch (must be exhaustive)
let dayNumber = 3
switch dayNumber {                          // Line 84: Switch statement
case 1: print("Monday")
case 2: print("Tuesday")
case 3: print("Wednesday")
case 4: print("Thursday")
case 5: print("Friday")
case 6, 7: print("Weekend")                 // Line 90: Multiple cases
default: print("Invalid day")               // Line 91: Default required
}

// MARK: - 7. Loops
print("\n=== 7. Loops ===")

// For-in loop
print("For-in loop:")
for fruit in fruits {                       // Line 98: Iterate over array
    print("  - \(fruit)")
}

// Range loop
print("Range loop (1...5):")
for i in 1...5 {                            // Line 104: Closed range
    print("  \(i)", terminator: " ")
}
print()

// While loop
print("While loop:")
var count = 3
while count > 0 {                           // Line 112: While condition
    print("  Countdown: \(count)")
    count -= 1
}

// MARK: - 8. Functions
print("\n=== 8. Functions ===")

func greet(person: String) -> String {      // Line 120: Function with parameter and return
    return "Hello, \(person)!"
}
print(greet(person: "World"))

func add(_ a: Int, _ b: Int) -> Int {       // Line 125: Omit argument labels with _
    return a + b
}
print("5 + 3 = \(add(5, 3))")

func greetWithDefault(name: String = "Guest") -> String {  // Line 130: Default parameter
    return "Welcome, \(name)!"
}
print(greetWithDefault())
print(greetWithDefault(name: "Alice"))

// Function returning tuple
func minMax(array: [Int]) -> (min: Int, max: Int)? {  // Line 137: Return optional tuple
    guard !array.isEmpty else { return nil }           // Line 138: Guard statement
    return (array.min()!, array.max()!)
}
if let result = minMax(array: [3, 1, 4, 1, 5, 9, 2, 6]) {
    print("Min: \(result.min), Max: \(result.max)")
}

// MARK: - 9. Closures
print("\n=== 9. Closures ===")

let numbers = [5, 2, 8, 1, 9]
let sorted = numbers.sorted { $0 < $1 }     // Line 148: Closure shorthand syntax
print("Sorted numbers: \(sorted)")

let doubled = numbers.map { $0 * 2 }        // Line 151: Map with closure
print("Doubled: \(doubled)")

let evens = numbers.filter { $0 % 2 == 0 }  // Line 154: Filter with closure
print("Even numbers: \(evens)")

let sum = numbers.reduce(0, +)              // Line 157: Reduce with operator
print("Sum: \(sum)")

// MARK: - 10. Structs
print("\n=== 10. Structs ===")

struct Point {                              // Line 163: Struct definition
    var x: Double
    var y: Double

    func distance(to other: Point) -> Double {  // Line 167: Method
        let dx = x - other.x
        let dy = y - other.y
        return (dx*dx + dy*dy).squareRoot()
    }

    mutating func moveBy(dx: Double, dy: Double) {  // Line 173: Mutating method
        x += dx
        y += dy
    }
}

var point1 = Point(x: 0, y: 0)              // Line 179: Memberwise initializer
let point2 = Point(x: 3, y: 4)
print("Point1: (\(point1.x), \(point1.y))")
print("Point2: (\(point2.x), \(point2.y))")
print("Distance: \(point1.distance(to: point2))")

point1.moveBy(dx: 1, dy: 1)                 // Line 185: Call mutating method
print("Point1 after move: (\(point1.x), \(point1.y))")

// MARK: - 11. Classes
print("\n=== 11. Classes ===")

class Animal {                              // Line 191: Class definition
    var name: String

    init(name: String) {                    // Line 194: Initializer
        self.name = name
    }

    func speak() -> String {                // Line 198: Method to override
        return "\(name) makes a sound"
    }
}

class Dog: Animal {                         // Line 203: Inheritance
    var breed: String

    init(name: String, breed: String) {
        self.breed = breed
        super.init(name: name)              // Line 208: Call superclass init
    }

    override func speak() -> String {       // Line 211: Override method
        return "\(name) the \(breed) barks: Woof!"
    }
}

let dog = Dog(name: "Buddy", breed: "Golden Retriever")
print(dog.speak())

// MARK: - 12. Protocols
print("\n=== 12. Protocols ===")

protocol Describable {                      // Line 221: Protocol definition
    var description: String { get }
    func describe() -> String
}

struct Book: Describable {                  // Line 226: Conform to protocol
    var title: String
    var author: String

    var description: String {               // Line 230: Computed property
        return "\"\(title)\" by \(author)"
    }

    func describe() -> String {
        return "Book: \(description)"
    }
}

let book = Book(title: "1984", author: "George Orwell")
print(book.describe())

// MARK: - 13. Extensions
print("\n=== 13. Extensions ===")

extension Int {                             // Line 244: Extend existing type
    var squared: Int {
        return self * self
    }

    func times(_ action: () -> Void) {      // Line 249: Method extension
        for _ in 0..<self {
            action()
        }
    }
}

print("5 squared = \(5.squared)")
print("Repeat 3 times:")
3.times { print("  Hello!") }               // Line 258: Use extension method

// MARK: - 14. Enums
print("\n=== 14. Enums ===")

enum Direction: String {                    // Line 263: Enum with raw value
    case north = "N"
    case south = "S"
    case east = "E"
    case west = "W"
}

let direction = Direction.north
print("Direction: \(direction), Raw: \(direction.rawValue)")

enum Result<T> {                            // Line 273: Generic enum (like Swift's Result)
    case success(T)
    case failure(String)
}

let result: Result<Int> = .success(42)
switch result {
case .success(let value):                   // Line 280: Pattern matching with associated value
    print("Success with value: \(value)")
case .failure(let error):
    print("Failed with error: \(error)")
}

// MARK: - 15. Error Handling
print("\n=== 15. Error Handling ===")

enum ValidationError: Error {               // Line 289: Custom error type
    case tooShort
    case tooLong
    case invalidCharacter(Character)
}

func validatePassword(_ password: String) throws -> Bool {  // Line 295: Throwing function
    guard password.count >= 8 else {
        throw ValidationError.tooShort
    }
    guard password.count <= 20 else {
        throw ValidationError.tooLong
    }
    return true
}

do {
    let isValid = try validatePassword("short")  // Line 306: Try in do-catch
    print("Password valid: \(isValid)")
} catch ValidationError.tooShort {
    print("Error: Password too short (min 8 chars)")
} catch ValidationError.tooLong {
    print("Error: Password too long (max 20 chars)")
} catch {
    print("Error: \(error)")
}

// Using try? for optional result
let result2 = try? validatePassword("validPassword123")  // Line 317: try? returns optional
print("Valid password check: \(result2 ?? false)")

// MARK: - 16. Guard Statement
print("\n=== 16. Guard Statement ===")

func processUser(name: String?, age: Int?) {
    guard let userName = name, let userAge = age else {  // Line 324: Guard for early exit
        print("Invalid user data")
        return
    }
    guard userAge >= 18 else {
        print("\(userName) is too young")
        return
    }
    print("Welcome, \(userName)! Age: \(userAge)")
}

processUser(name: nil, age: 25)
processUser(name: "Alice", age: 16)
processUser(name: "Bob", age: 30)

// MARK: - 17. Defer
print("\n=== 17. Defer ===")

func demoDefer() {
    print("  Start of function")
    defer { print("  First defer (executes last)") }   // Line 342: Defer executes on exit
    defer { print("  Second defer (executes first)") } // Line 343: LIFO order
    print("  End of function body")
}
print("Calling demoDefer:")
demoDefer()

print("\n=== Program Complete ===")
