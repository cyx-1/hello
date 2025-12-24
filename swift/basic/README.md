# Swift Basics

This program demonstrates fundamental Swift language features including variables, types, collections, optionals, control flow, functions, closures, structs, classes, protocols, extensions, enums, and error handling.

## Requirements

- **Swift 5.0+** (tested with Swift 5.9)
- macOS, Linux with Swift installed, or Windows with Swift toolchain

## Running the Program

```bash
swift main_basic.swift
```

Or compile and run:
```bash
swiftc main_basic.swift -o main_basic
./main_basic
```

## Source Code with Line References

### 1. Variables and Constants (Lines 9-13)
```swift
9  let constant = "I cannot be changed"      // immutable with 'let'
10 var variable = "I can be changed"          // mutable with 'var'
11 variable = "See, I changed!"
12 print("Constant: \(constant)")             // string interpolation
13 print("Variable: \(variable)")
```

### 2. Basic Types (Lines 17-23)
```swift
17 let integer: Int = 42                      // explicit type annotation
18 let double: Double = 3.14159
19 let boolean: Bool = true
20 let character: Character = "A"
21 let string: String = "Hello, Swift!"
22 print("Int: \(integer), Double: \(double), Bool: \(boolean), Char: \(character)")
23 print("String: \(string)")
```

### 3. Collections - Arrays (Lines 34-37)
```swift
34 var fruits = ["Apple", "Banana", "Cherry"] // Array literal
35 fruits.append("Date")                       // Append element
36 print("Fruits array: \(fruits)")
37 print("First fruit: \(fruits[0])")          // Subscript access
```

### 4. Collections - Dictionaries (Lines 40-47)
```swift
40 var ages: [String: Int] = [                 // Dictionary with type
41     "Alice": 30,
42     "Bob": 25,
43     "Charlie": 35
44 ]
45 ages["Diana"] = 28                          // Add new key-value
46 print("Ages dictionary: \(ages)")
47 print("Alice's age: \(ages["Alice"] ?? 0)") // Optional unwrapping with ??
```

### 5. Optionals (Lines 56-67)
```swift
56 var optionalName: String? = nil            // Optional can be nil
60 if let name = optionalName {                // Optional binding
61     print("Unwrapped name: \(name)")
62 }
64 let forcedName = optionalName!              // Force unwrap (use carefully!)
67 let defaultName = optionalName ?? "Unknown" // Nil coalescing
```

### 6. Control Flow - Switch (Lines 84-91)
```swift
84 switch dayNumber {                          // Switch statement
85 case 1: print("Monday")
86 case 2: print("Tuesday")
87 case 3: print("Wednesday")
88 case 4: print("Thursday")
89 case 5: print("Friday")
90 case 6, 7: print("Weekend")                 // Multiple cases
91 default: print("Invalid day")               // Default required
92 }
```

### 7. Functions (Lines 120-142)
```swift
120 func greet(person: String) -> String {      // Function with parameter and return
121     return "Hello, \(person)!"
122 }

125 func add(_ a: Int, _ b: Int) -> Int {       // Omit argument labels with _
126     return a + b
127 }

130 func greetWithDefault(name: String = "Guest") -> String {  // Default parameter
131     return "Welcome, \(name)!"
132 }

137 func minMax(array: [Int]) -> (min: Int, max: Int)? {  // Return optional tuple
138     guard !array.isEmpty else { return nil }           // Guard statement
139     return (array.min()!, array.max()!)
140 }
```

### 8. Closures (Lines 148-157)
```swift
148 let sorted = numbers.sorted { $0 < $1 }     // Closure shorthand syntax
151 let doubled = numbers.map { $0 * 2 }        // Map with closure
154 let evens = numbers.filter { $0 % 2 == 0 }  // Filter with closure
157 let sum = numbers.reduce(0, +)              // Reduce with operator
```

### 9. Structs (Lines 163-186)
```swift
163 struct Point {                              // Struct definition
164     var x: Double
165     var y: Double
167     func distance(to other: Point) -> Double {  // Method
173     mutating func moveBy(dx: Double, dy: Double) {  // Mutating method
179 var point1 = Point(x: 0, y: 0)              // Memberwise initializer
```

### 10. Classes with Inheritance (Lines 191-216)
```swift
191 class Animal {                              // Class definition
194     init(name: String) {                    // Initializer
198     func speak() -> String {                // Method to override

203 class Dog: Animal {                         // Inheritance
208         super.init(name: name)              // Call superclass init
211     override func speak() -> String {       // Override method
```

### 11. Protocols (Lines 221-239)
```swift
221 protocol Describable {                      // Protocol definition
222     var description: String { get }
223     func describe() -> String
224 }

226 struct Book: Describable {                  // Conform to protocol
230     var description: String {               // Computed property
```

### 12. Extensions (Lines 244-258)
```swift
244 extension Int {                             // Extend existing type
245     var squared: Int {
246         return self * self
247     }
249     func times(_ action: () -> Void) {      // Method extension
258 3.times { print("  Hello!") }               // Use extension method
```

### 13. Enums (Lines 263-283)
```swift
263 enum Direction: String {                    // Enum with raw value
264     case north = "N"
273 enum Result<T> {                            // Generic enum
274     case success(T)
275     case failure(String)
280 case .success(let value):                   // Pattern matching with associated value
```

### 14. Error Handling (Lines 289-317)
```swift
289 enum ValidationError: Error {               // Custom error type
290     case tooShort
295 func validatePassword(_ password: String) throws -> Bool {  // Throwing function
306     let isValid = try validatePassword("short")  // Try in do-catch
317 let result2 = try? validatePassword("validPassword123")  // try? returns optional
```

### 15. Guard Statement (Lines 324-335)
```swift
324     guard let userName = name, let userAge = age else {  // Guard for early exit
325         print("Invalid user data")
326         return
327     }
```

### 16. Defer (Lines 342-346)
```swift
342     defer { print("  First defer (executes last)") }   // Defer executes on exit
343     defer { print("  Second defer (executes first)") } // LIFO order
```

## Expected Output

```
=== 1. Variables and Constants ===
Constant: I cannot be changed
Variable: See, I changed!

=== 2. Basic Types ===
Int: 42, Double: 3.14159, Bool: true, Char: A
String: Hello, Swift!

=== 3. Type Inference ===
Inferred types - Int: 100, Double: 2.718, String: Inferred!

=== 4. Collections ===
Fruits array: ["Apple", "Banana", "Cherry", "Date"]
First fruit: Apple
Ages dictionary: ["Alice": 30, "Bob": 25, "Charlie": 35, "Diana": 28]
Alice's age: 30
Unique numbers set: [1, 2, 3, 4]

=== 5. Optionals ===
Optional is nil: true
Unwrapped name: Swift Developer
Force unwrapped: Swift Developer
With default: Swift Developer

=== 6. Control Flow ===
Grade: B
Wednesday

=== 7. Loops ===
For-in loop:
  - Apple
  - Banana
  - Cherry
  - Date
Range loop (1...5):
  1 2 3 4 5
While loop:
  Countdown: 3
  Countdown: 2
  Countdown: 1

=== 8. Functions ===
Hello, World!
5 + 3 = 8
Welcome, Guest!
Welcome, Alice!
Min: 1, Max: 9

=== 9. Closures ===
Sorted numbers: [1, 2, 5, 8, 9]
Doubled: [10, 4, 16, 2, 18]
Even numbers: [2, 8]
Sum: 25

=== 10. Structs ===
Point1: (0.0, 0.0)
Point2: (3.0, 4.0)
Distance: 5.0
Point1 after move: (1.0, 1.0)

=== 11. Classes ===
Buddy the Golden Retriever barks: Woof!

=== 12. Protocols ===
Book: "1984" by George Orwell

=== 13. Extensions ===
5 squared = 25
Repeat 3 times:
  Hello!
  Hello!
  Hello!

=== 14. Enums ===
Direction: north, Raw: N
Success with value: 42

=== 15. Error Handling ===
Error: Password too short (min 8 chars)
Valid password check: true

=== 16. Guard Statement ===
Invalid user data
Alice is too young
Welcome, Bob! Age: 30

=== 17. Defer ===
Calling demoDefer:
  Start of function
  End of function body
  Second defer (executes first)
  First defer (executes last)

=== Program Complete ===
```

## Output Annotations

| Output Section | Source Lines | Key Concept |
|----------------|--------------|-------------|
| Variables and Constants | 9-13 | `let` for immutables, `var` for mutables, string interpolation with `\()` |
| Basic Types | 17-23 | Explicit type annotations with `: Type` |
| Type Inference | 26-29 | Swift infers types from literal values |
| Collections - Array | 34-37 | Array literals `[]`, `.append()`, subscript `[0]` |
| Collections - Dictionary | 40-47 | Key-value pairs `[K: V]`, optional access with `??` |
| Collections - Set | 50-52 | Unique elements, automatic deduplication |
| Optionals | 56-67 | `?` for optional, `if let` binding, `!` force unwrap, `??` nil coalescing |
| Control Flow | 74-91 | `if-else`, exhaustive `switch` with `default` |
| Loops | 98-115 | `for-in`, closed range `...`, `while` |
| Functions | 120-142 | Named parameters, `_` to omit labels, default values, tuple returns, `guard` |
| Closures | 148-157 | `$0`, `$1` shorthand, `map`, `filter`, `reduce` |
| Structs | 163-186 | Value types, memberwise init, `mutating` for state changes |
| Classes | 191-216 | Reference types, inheritance with `:`, `override`, `super.init` |
| Protocols | 221-239 | Contracts, computed properties, conformance |
| Extensions | 244-258 | Add functionality to existing types |
| Enums | 263-283 | Raw values, associated values, pattern matching |
| Error Handling | 289-317 | `Error` protocol, `throws`, `do-catch`, `try?` |
| Guard | 324-335 | Early exit pattern, multiple conditions |
| Defer | 342-346 | Cleanup code, LIFO execution order |

## Key Swift Concepts Summary

1. **Value vs Reference Types**: Structs are value types (copied), Classes are reference types (shared)
2. **Optionals**: Swift's null-safety mechanism - variables must explicitly allow nil
3. **Protocol-Oriented Programming**: Swift favors protocols over inheritance for code reuse
4. **Type Safety**: Swift is strongly typed with powerful type inference
5. **Memory Safety**: ARC (Automatic Reference Counting) manages memory automatically
6. **Error Handling**: Explicit error handling with `throws`, `try`, `do-catch`
