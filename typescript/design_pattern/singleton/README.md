# Singleton Design Pattern in TypeScript

The Singleton pattern ensures a class has only one instance and provides a global point of access to it. This is useful for resources that should be shared across an application, such as database connections, loggers, or configuration managers.

## Requirements

- Node.js 18+
- TypeScript 5.3+

## How to Run

```bash
npm install
npm run start
```

## Source Code

```typescript
1   /**
2    * Singleton Design Pattern in TypeScript
3    *
4    * The Singleton pattern ensures a class has only one instance
5    * and provides a global point of access to it.
6    */
7
8   // Classic Singleton implementation
9   class DatabaseConnection {
10      private static instance: DatabaseConnection | null = null;
11      private connectionId: string;
12      private queryCount: number = 0;
13
14      // Private constructor prevents direct instantiation
15      private constructor() {
16          this.connectionId = `conn_${Math.random().toString(36).substr(2, 9)}`;
17          console.log(`[Line 17] Creating new DatabaseConnection with ID: ${this.connectionId}`);
18      }
19
20      // Static method to get the singleton instance
21      public static getInstance(): DatabaseConnection {
22          if (!DatabaseConnection.instance) {
23              console.log("[Line 22] No instance exists, creating new one...");
24              DatabaseConnection.instance = new DatabaseConnection();
25          } else {
26              console.log("[Line 25] Returning existing instance...");
27          }
28          return DatabaseConnection.instance;
29      }
30
31      public query(sql: string): string {
32          this.queryCount++;
33          const result = `Result from ${this.connectionId} (Query #${this.queryCount}): ${sql}`;
34          console.log(`[Line 33] ${result}`);
35          return result;
36      }
37
38      public getConnectionId(): string {
39          return this.connectionId;
40      }
41
42      public getQueryCount(): number {
43          return this.queryCount;
44      }
45  }
46
47  // Modern TypeScript Singleton using a module pattern
48  class Logger {
49      private static instance: Logger;
50      private logs: string[] = [];
51
52      private constructor() {
53          console.log("[Line 51] Logger singleton initialized");
54      }
55
56      public static getInstance(): Logger {
57          if (!Logger.instance) {
58              Logger.instance = new Logger();
59          }
60          return Logger.instance;
61      }
62
63      public log(message: string): void {
64          const timestamp = new Date().toISOString();
65          const entry = `[${timestamp}] ${message}`;
66          this.logs.push(entry);
67          console.log(`[Line 64] ${entry}`);
68      }
69
70      public getLogs(): string[] {
71          return [...this.logs];
72      }
73
74      public getLogCount(): number {
75          return this.logs.length;
76      }
77  }
78
79  // Demonstration
80  function main(): void {
81      console.log("=== Singleton Pattern Demonstration ===\n");
82
83      // Demo 1: DatabaseConnection Singleton
84      console.log("--- Database Connection Singleton ---");
85
86      const db1 = DatabaseConnection.getInstance();
87      const db2 = DatabaseConnection.getInstance();
88      const db3 = DatabaseConnection.getInstance();
89
90      console.log(`\n[Line 86] db1 connection ID: ${db1.getConnectionId()}`);
91      console.log(`[Line 87] db2 connection ID: ${db2.getConnectionId()}`);
92      console.log(`[Line 88] db3 connection ID: ${db3.getConnectionId()}`);
93      console.log(`[Line 89] Are db1 and db2 the same instance? ${db1 === db2}`);
94      console.log(`[Line 90] Are db2 and db3 the same instance? ${db2 === db3}`);
95
96      // Execute queries through different references
97      db1.query("SELECT * FROM users");
98      db2.query("INSERT INTO orders VALUES (1, 'item')");
99      db3.query("UPDATE products SET price = 100");
100
101     console.log(`\n[Line 97] Total queries executed: ${db1.getQueryCount()}`);
102
103     // Demo 2: Logger Singleton
104     console.log("\n--- Logger Singleton ---");
105
106     const logger1 = Logger.getInstance();
107     const logger2 = Logger.getInstance();
108
109     logger1.log("Application started");
110     logger2.log("User logged in");
111     logger1.log("Processing request");
112
113     console.log(`\n[Line 109] logger1 log count: ${logger1.getLogCount()}`);
114     console.log(`[Line 110] logger2 log count: ${logger2.getLogCount()}`);
115     console.log(`[Line 111] Are logger1 and logger2 the same? ${logger1 === logger2}`);
116
117     console.log("\n=== End of Demonstration ===");
118 }
119
120 main();
```

## Program Output

```
=== Singleton Pattern Demonstration ===

--- Database Connection Singleton ---
[Line 22] No instance exists, creating new one...
[Line 17] Creating new DatabaseConnection with ID: conn_6nx01usgw
[Line 25] Returning existing instance...
[Line 25] Returning existing instance...

[Line 86] db1 connection ID: conn_6nx01usgw
[Line 87] db2 connection ID: conn_6nx01usgw
[Line 88] db3 connection ID: conn_6nx01usgw
[Line 89] Are db1 and db2 the same instance? true
[Line 90] Are db2 and db3 the same instance? true
[Line 33] Result from conn_6nx01usgw (Query #1): SELECT * FROM users
[Line 33] Result from conn_6nx01usgw (Query #2): INSERT INTO orders VALUES (1, 'item')
[Line 33] Result from conn_6nx01usgw (Query #3): UPDATE products SET price = 100

[Line 97] Total queries executed: 3

--- Logger Singleton ---
[Line 51] Logger singleton initialized
[Line 64] [2025-11-19T00:37:47.664Z] Application started
[Line 64] [2025-11-19T00:37:47.665Z] User logged in
[Line 64] [2025-11-19T00:37:47.665Z] Processing request

[Line 109] logger1 log count: 3
[Line 110] logger2 log count: 3
[Line 111] Are logger1 and logger2 the same? true

=== End of Demonstration ===
```

## Code Analysis and Annotations

### Key Implementation Details

#### Private Constructor (Lines 15-18, 52-54)
- The `private constructor()` prevents external instantiation with `new DatabaseConnection()`
- This is the core mechanism that enforces the singleton pattern in TypeScript
- Any attempt to call `new DatabaseConnection()` outside the class results in a compile-time error

#### Static Instance Storage (Lines 10, 49)
- `private static instance` stores the single instance at the class level
- The `static` keyword ensures the instance is shared across all calls to `getInstance()`

#### getInstance() Method (Lines 21-29, 56-61)
- The public static method provides the global access point
- Implements lazy initialization - instance is created only when first needed
- Returns the existing instance on subsequent calls

### Output Correlation

| Output Line | Source Line | Explanation |
|-------------|-------------|-------------|
| `[Line 22] No instance exists...` | Line 86 | First call to `getInstance()` triggers creation |
| `[Line 17] Creating new DatabaseConnection...` | Line 16-17 | Constructor called only once |
| `[Line 25] Returning existing instance...` (x2) | Lines 87-88 | Second and third calls return cached instance |
| All connection IDs are identical | Lines 86-88 | Proves all variables reference same object |
| `Are db1 and db2 the same instance? true` | Line 93 | Identity check confirms singleton |
| `Total queries executed: 3` | Line 101 | Query count persists across all references |
| `logger1 log count: 3` / `logger2 log count: 3` | Lines 113-114 | Both references share the same log array |

### Why Singleton Works

1. **Single Creation**: Output shows `[Line 17]` appears only once, proving the constructor runs just once
2. **Shared State**: All three database references (`db1`, `db2`, `db3`) have the same `connectionId`
3. **Cumulative Operations**: The query count increments to 3 regardless of which reference executes the query
4. **Identity Equality**: `db1 === db2` and `db2 === db3` both return `true`

### Use Cases

- **Database Connections**: Reuse expensive connections (as demonstrated)
- **Loggers**: Centralized logging with shared state
- **Configuration Managers**: Single source of truth for app settings
- **Caches**: Shared in-memory cache across modules
