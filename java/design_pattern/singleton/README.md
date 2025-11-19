# Singleton Pattern in Java

The Singleton pattern is a creational design pattern that ensures a class has only one instance and provides a global point of access to it. This demonstration shows six different approaches to implementing the Singleton pattern in Java.

## Source Code

### MainSingletonPattern.java

```java
1   /**
2    * Comprehensive demonstration of the Singleton Pattern in Java
3    *
4    * The Singleton pattern ensures a class has only one instance and provides
5    * a global point of access to it.
6    */
7
8   // 1. Eager Initialization Singleton
9   class EagerSingleton {
10      // Instance is created at class loading time
11      private static final EagerSingleton instance = new EagerSingleton();
12
13      private EagerSingleton() {
14          System.out.println("EagerSingleton instance created");
15      }
16
17      public static EagerSingleton getInstance() {
18          return instance;
19      }
20
21      public void showMessage() {
22          System.out.println("Hello from EagerSingleton: " + this.hashCode());
23      }
24  }
25
26  // 2. Lazy Initialization Singleton (NOT thread-safe)
27  class LazySingleton {
28      private static LazySingleton instance;
29
30      private LazySingleton() {
31          System.out.println("LazySingleton instance created");
32      }
33
34      // This is not thread-safe - multiple threads could create multiple instances
35      public static LazySingleton getInstance() {
36          if (instance == null) {
37              instance = new LazySingleton();
38          }
39          return instance;
40      }
41
42      public void showMessage() {
43          System.out.println("Hello from LazySingleton: " + this.hashCode());
44      }
45  }
46
47  // 3. Thread-Safe Lazy Initialization (synchronized method)
48  class ThreadSafeSingleton {
49      private static ThreadSafeSingleton instance;
50
51      private ThreadSafeSingleton() {
52          System.out.println("ThreadSafeSingleton instance created");
53      }
54
55      // Synchronized method - thread-safe but performance overhead
56      public static synchronized ThreadSafeSingleton getInstance() {
57          if (instance == null) {
58              instance = new ThreadSafeSingleton();
59          }
60          return instance;
61      }
62
63      public void showMessage() {
64          System.out.println("Hello from ThreadSafeSingleton: " + this.hashCode());
65      }
66  }
67
68  // 4. Double-Checked Locking Singleton
69  class DoubleCheckedSingleton {
70      // volatile keyword ensures visibility of changes across threads
71      private static volatile DoubleCheckedSingleton instance;
72
73      private DoubleCheckedSingleton() {
74          System.out.println("DoubleCheckedSingleton instance created");
75      }
76
77      // Double-checked locking - reduces synchronization overhead
78      public static DoubleCheckedSingleton getInstance() {
79          if (instance == null) {
80              synchronized (DoubleCheckedSingleton.class) {
81                  if (instance == null) {
82                      instance = new DoubleCheckedSingleton();
83                  }
84              }
85          }
86          return instance;
87      }
88
89      public void showMessage() {
90          System.out.println("Hello from DoubleCheckedSingleton: " + this.hashCode());
91      }
92  }
93
94  // 5. Bill Pugh Singleton (using inner static helper class)
95  class BillPughSingleton {
96      private BillPughSingleton() {
97          System.out.println("BillPughSingleton instance created");
98      }
99
100     // Inner static class is loaded only when getInstance() is called
101     private static class SingletonHelper {
102         private static final BillPughSingleton INSTANCE = new BillPughSingleton();
103     }
104
105     public static BillPughSingleton getInstance() {
106         return SingletonHelper.INSTANCE;
107     }
108
109     public void showMessage() {
110         System.out.println("Hello from BillPughSingleton: " + this.hashCode());
111     }
112 }
113
114 // 6. Enum Singleton (most concise and inherently thread-safe)
115 enum EnumSingleton {
116     INSTANCE;
117
118     EnumSingleton() {
119         System.out.println("EnumSingleton instance created");
120     }
121
122     public void showMessage() {
123         System.out.println("Hello from EnumSingleton: " + this.hashCode());
124     }
125 }
126
127 public class MainSingletonPattern {
128     public static void main(String[] args) {
129         System.out.println("=== Singleton Pattern Demonstration ===\n");
130
131         // 1. Eager Singleton
132         System.out.println("--- 1. Eager Initialization Singleton ---");
133         EagerSingleton eager1 = EagerSingleton.getInstance();
134         eager1.showMessage();
135         EagerSingleton eager2 = EagerSingleton.getInstance();
136         eager2.showMessage();
137         System.out.println("Are both instances same? " + (eager1 == eager2));
138         System.out.println();
139
140         // 2. Lazy Singleton
141         System.out.println("--- 2. Lazy Initialization Singleton ---");
142         LazySingleton lazy1 = LazySingleton.getInstance();
143         lazy1.showMessage();
144         LazySingleton lazy2 = LazySingleton.getInstance();
145         lazy2.showMessage();
146         System.out.println("Are both instances same? " + (lazy1 == lazy2));
147         System.out.println();
148
149         // 3. Thread-Safe Singleton
150         System.out.println("--- 3. Thread-Safe Singleton ---");
151         ThreadSafeSingleton ts1 = ThreadSafeSingleton.getInstance();
152         ts1.showMessage();
153         ThreadSafeSingleton ts2 = ThreadSafeSingleton.getInstance();
154         ts2.showMessage();
155         System.out.println("Are both instances same? " + (ts1 == ts2));
156         System.out.println();
157
158         // 4. Double-Checked Locking Singleton
159         System.out.println("--- 4. Double-Checked Locking Singleton ---");
160         DoubleCheckedSingleton dc1 = DoubleCheckedSingleton.getInstance();
161         dc1.showMessage();
162         DoubleCheckedSingleton dc2 = DoubleCheckedSingleton.getInstance();
163         dc2.showMessage();
164         System.out.println("Are both instances same? " + (dc1 == dc2));
165         System.out.println();
166
167         // 5. Bill Pugh Singleton
168         System.out.println("--- 5. Bill Pugh Singleton (Inner Static Helper) ---");
169         BillPughSingleton bp1 = BillPughSingleton.getInstance();
170         bp1.showMessage();
171         BillPughSingleton bp2 = BillPughSingleton.getInstance();
172         bp2.showMessage();
173         System.out.println("Are both instances same? " + (bp1 == bp2));
174         System.out.println();
175
176         // 6. Enum Singleton
177         System.out.println("--- 6. Enum Singleton ---");
178         EnumSingleton enum1 = EnumSingleton.INSTANCE;
179         enum1.showMessage();
180         EnumSingleton enum2 = EnumSingleton.INSTANCE;
181         enum2.showMessage();
182         System.out.println("Are both instances same? " + (enum1 == enum2));
183         System.out.println();
184
185         System.out.println("=== Summary ===");
186         System.out.println("All singleton implementations ensure only one instance exists.");
187         System.out.println("Best practices:");
188         System.out.println("  - Use Enum Singleton for simplicity and thread-safety");
189         System.out.println("  - Use Bill Pugh for lazy initialization without synchronization overhead");
190         System.out.println("  - Use Double-Checked Locking if you need lazy initialization with minimal overhead");
191     }
192 }
```

## Program Output

```
=== Singleton Pattern Demonstration ===

--- 1. Eager Initialization Singleton ---
EagerSingleton instance created
Hello from EagerSingleton: 705927765
Hello from EagerSingleton: 705927765
Are both instances same? true

--- 2. Lazy Initialization Singleton ---
LazySingleton instance created
Hello from LazySingleton: 1554874502
Hello from LazySingleton: 1554874502
Are both instances same? true

--- 3. Thread-Safe Singleton ---
ThreadSafeSingleton instance created
Hello from ThreadSafeSingleton: 1639705018
Hello from ThreadSafeSingleton: 1639705018
Are both instances same? true

--- 4. Double-Checked Locking Singleton ---
DoubleCheckedSingleton instance created
Hello from DoubleCheckedSingleton: 1360875712
Hello from DoubleCheckedSingleton: 1360875712
Are both instances same? true

--- 5. Bill Pugh Singleton (Inner Static Helper) ---
BillPughSingleton instance created
Hello from BillPughSingleton: 491044090
Hello from BillPughSingleton: 491044090
Are both instances same? true

--- 6. Enum Singleton ---
EnumSingleton instance created
Hello from EnumSingleton: 1872034366
Hello from EnumSingleton: 1872034366
Are both instances same? true

=== Summary ===
All singleton implementations ensure only one instance exists.
Best practices:
  - Use Enum Singleton for simplicity and thread-safety
  - Use Bill Pugh for lazy initialization without synchronization overhead
  - Use Double-Checked Locking if you need lazy initialization with minimal overhead
```

## Detailed Annotations

### 1. Eager Initialization Singleton (Lines 9-24)

**Key Features:**
- **Line 11**: The instance is created at class loading time using `static final`
- **Line 13-15**: Private constructor prevents external instantiation
- **Line 17-19**: Public static method provides global access point

**Output Analysis:**
- Notice "EagerSingleton instance created" appears before the first `getInstance()` call
- Both calls to `getInstance()` (lines 133, 135) return the same instance (hash code 705927765)
- The comparison `eager1 == eager2` returns `true`, confirming only one instance exists

**Pros:** Simple, thread-safe (guaranteed by JVM)
**Cons:** Instance created even if never used (not lazy)

---

### 2. Lazy Initialization Singleton (Lines 26-45)

**Key Features:**
- **Line 28**: Instance is `null` initially
- **Line 36-38**: Instance created only when `getInstance()` is first called
- **Line 34**: NOT thread-safe - in multi-threaded environments, multiple instances could be created

**Output Analysis:**
- "LazySingleton instance created" appears only when `getInstance()` is first called (line 142)
- Both instances share the same hash code (1554874502)
- This demonstrates lazy initialization: the instance is created on-demand

**Pros:** Lazy initialization
**Cons:** Not thread-safe

---

### 3. Thread-Safe Singleton (Lines 47-66)

**Key Features:**
- **Line 56**: The `synchronized` keyword makes the entire method thread-safe
- **Line 57-59**: Null check and instance creation protected by synchronization

**Output Analysis:**
- "ThreadSafeSingleton instance created" appears on first call (line 151)
- Both instances have identical hash code (1639705018)
- Thread-safe but slower due to synchronization overhead on every call

**Pros:** Thread-safe, lazy initialization
**Cons:** Performance overhead from synchronization

---

### 4. Double-Checked Locking Singleton (Lines 68-92)

**Key Features:**
- **Line 71**: `volatile` keyword ensures visibility of changes across threads
- **Line 79**: First null check (outside synchronized block) for performance
- **Line 80-84**: Second null check (inside synchronized block) for thread safety

**Output Analysis:**
- "DoubleCheckedSingleton instance created" on first call (line 160)
- Both instances share hash code (1360875712)
- Synchronization only occurs during initialization, reducing performance overhead

**Pros:** Thread-safe, lazy initialization, better performance than fully synchronized
**Cons:** More complex code, requires Java 5+ for proper volatile semantics

---

### 5. Bill Pugh Singleton (Lines 94-112)

**Key Features:**
- **Line 101-103**: Inner static class `SingletonHelper` holds the instance
- **Line 102**: Instance created when `SingletonHelper` is loaded (lazy)
- **Line 105-107**: `getInstance()` triggers loading of `SingletonHelper` class

**Output Analysis:**
- "BillPughSingleton instance created" appears when `getInstance()` is first called (line 169)
- Both instances have the same hash code (491044090)
- JVM's class loading mechanism guarantees thread safety

**Pros:** Lazy initialization, thread-safe without synchronization, clean code
**Cons:** None significant

---

### 6. Enum Singleton (Lines 114-125)

**Key Features:**
- **Line 115-116**: Enum with single constant `INSTANCE`
- **Line 118-120**: Constructor called when enum is loaded
- Inherently serialization-safe and reflection-proof

**Output Analysis:**
- "EnumSingleton instance created" when first accessed (line 178)
- Both references have identical hash code (1872034366)
- Most concise implementation

**Pros:** Thread-safe, serialization-safe, prevents reflection attacks, most concise
**Cons:** Not lazy (though can be modified), less flexible

---

## Comparison Summary

| Approach | Thread-Safe | Lazy Init | Performance | Complexity | Recommended |
|----------|-------------|-----------|-------------|------------|-------------|
| Eager Initialization | ✅ | ❌ | High | Low | For small objects |
| Lazy Initialization | ❌ | ✅ | High | Low | Single-threaded only |
| Thread-Safe (synchronized) | ✅ | ✅ | Low | Low | Avoid if possible |
| Double-Checked Locking | ✅ | ✅ | Medium | High | Legacy codebases |
| Bill Pugh | ✅ | ✅ | High | Medium | ✅ Recommended |
| Enum | ✅ | Partial | High | Low | ✅ Best choice |

## Running the Code

```bash
# Compile
javac MainSingletonPattern.java

# Run
java MainSingletonPattern
```

Or using Maven:

```bash
mvn clean compile exec:java
```

## Version Requirements

- **Java Version**: Java 11 or higher
- **Dependencies**: None (pure Java, no external libraries required)
- **Note**: Double-Checked Locking requires Java 5+ for proper `volatile` semantics

## Key Takeaways

1. **All six approaches guarantee a single instance** - verified by identical hash codes and `==` comparison
2. **Enum Singleton is the modern best practice** - concise, thread-safe, and prevents reflection attacks
3. **Bill Pugh Singleton is ideal for complex initialization** - provides lazy loading without synchronization
4. **Avoid simple lazy initialization in production** - not thread-safe
5. **The `volatile` keyword is crucial** for double-checked locking to work correctly in multi-threaded environments
