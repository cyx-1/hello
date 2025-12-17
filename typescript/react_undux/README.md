# React Undux TypeScript Demo

A comprehensive demonstration of React with Undux state management and TypeScript, showcasing type-safe state management with minimal boilerplate, effects (side effects), and seamless React integration.

## Requirements

- **Node.js**: 18.x or higher
- **TypeScript**: 5.6.x or higher
- **React**: 18.3.x
- **Undux**: 5.0.x

## Installation and Running

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build
```

## Key TypeScript Features Demonstrated

1. **Typed State Interface** (Lines 12-16): Defining strongly-typed state structure
2. **Type-Safe Store Creation** (Line 32): Creating a connected store with TypeScript support
3. **Type-Safe State Access** (Line 58): Using `store.get('key')` with autocomplete
4. **Type-Safe State Updates** (Line 64): Using `store.set('key')(value)` with type checking
5. **Type-Safe Effects** (Lines 36-49): Subscribing to state changes with type safety

---

## Source Code Walkthrough

### Section 1: State Interface Definition (Lines 12-16)

```typescript
12 | interface AppState {
13 |   count: number;
14 |   username: string;
15 |   todos: string[];
16 | }
```

**Purpose**: Defines the TypeScript interface for our application state. This provides type safety and IntelliSense throughout the application.

**TypeScript Benefit**: Any attempt to access non-existent properties or assign wrong types will be caught at compile time.

---

### Section 2: Initial State (Lines 20-24)

```typescript
20 | const initialState: AppState = {
21 |   count: 0,
22 |   username: 'Guest',
23 |   todos: ['Learn Undux', 'Build awesome apps']
24 | };
```

**Purpose**: Defines the initial state with type annotation ensuring it matches `AppState` interface.

**Output**:
```
[Line 27] Initial State: {
  "count": 0,
  "username": "Guest",
  "todos": ["Learn Undux", "Build awesome apps"]
}
```

---

### Section 3: Store Creation with Effects (Lines 31-51)

```typescript
32 | const StoreContainer = createConnectedStore(initialState, (store: Store<AppState>) => {
33 |   console.log('[Line 33] Undux Store Created');
34 |
35 |   // Effect: Log count changes
36 |   store.on('count').subscribe(count => {
37 |     console.log(`[Line 37] Effect: Count changed to ${count}`);
38 |   });
39 |
40 |   // Effect: Log username changes
41 |   store.on('username').subscribe(username => {
42 |     console.log(`[Line 42] Effect: Username changed to "${username}"`);
43 |   });
44 |
45 |   // Effect: Log todos changes
46 |   store.on('todos').subscribe(todos => {
47 |     console.log(`[Line 47] Effect: Todos updated, count = ${todos.length}`);
48 |   });
49 |
50 |   return store;
51 | });
```

**Key Concepts**:
- **createConnectedStore**: Creates a store with React bindings
- **Effects**: Side effects that run when specific state properties change
- **Type Safety**: `store.on('count')` knows the type is `number`, `store.on('username')` knows it's `string`

**TypeScript Magic**: The `Store<AppState>` generic ensures all state keys are type-checked.

**Output**:
```
[Line 33] Undux Store Created
```

---

### Section 4: Counter Component (Lines 55-95)

```typescript
55 | const Counter: React.FC = () => {
56 |   const store = StoreContainer.useStore();
57 |   const count = store.get('count');
58 |
59 |   console.log(`[Line 60] Counter Component Rendered | Current count: ${count}`);
60 |
61 |   const increment = () => {
62 |     console.log('[Line 63] Button: Increment clicked');
63 |     store.set('count')(count + 1);
64 |   };
```

**TypeScript Features**:
- Line 57: `store.get('count')` returns `number` type
- Line 64: `store.set('count')` expects a `number` value
- TypeScript will error if you try `store.set('count')('invalid')` or `store.get('invalidKey')`

**Undux Pattern**: Simple `get()` and `set()` API—no actions, reducers, or action creators needed!

**User Interaction Output** (Increment Button):
```
[Line 63] Button: Increment clicked
[Line 37] Effect: Count changed to 1
[Line 60] Counter Component Rendered | Current count: 1
```

---

### Section 5: User Profile Component (Lines 99-140)

```typescript
99  | const UserProfile: React.FC = () => {
100 |   const store = StoreContainer.useStore();
101 |   const username = store.get('username');
102 |   const [inputValue, setInputValue] = React.useState(username);
103 |
104 |   console.log(`[Line 105] UserProfile Component Rendered | Username: "${username}"`);
105 |
106 |   const updateUsername = () => {
107 |     console.log(`[Line 108] Button: Update username to "${inputValue}"`);
108 |     store.set('username')(inputValue);
109 |   };
```

**Purpose**: Demonstrates managing string state with Undux and combining it with local React state (`useState`).

**User Interaction Output** (Update Button with "Alice"):
```
[Line 108] Button: Update username to "Alice"
[Line 42] Effect: Username changed to "Alice"
[Line 105] UserProfile Component Rendered | Username: "Alice"
```

---

### Section 6: Todo List Component (Lines 144-202)

```typescript
144 | const TodoList: React.FC = () => {
145 |   const store = StoreContainer.useStore();
146 |   const todos = store.get('todos');
147 |   const [newTodo, setNewTodo] = React.useState('');
148 |
149 |   console.log(`[Line 150] TodoList Component Rendered | Todo count: ${todos.length}`);
150 |
151 |   const addTodo = () => {
152 |     if (newTodo.trim()) {
153 |       console.log(`[Line 154] Button: Add todo "${newTodo}"`);
154 |       store.set('todos')([...todos, newTodo]);
155 |       setNewTodo('');
156 |     }
157 |   };
158 |
159 |   const removeTodo = (index: number) => {
160 |     console.log(`[Line 161] Button: Remove todo at index ${index}`);
161 |     const newTodos = todos.filter((_, i) => i !== index);
162 |     store.set('todos')(newTodos);
163 |   };
```

**TypeScript Safety**:
- Line 146: `todos` is inferred as `string[]`
- Line 154: TypeScript ensures you're setting an array of strings
- Line 161: TypeScript validates the filter operation returns `string[]`

**User Interaction Output** (Add "Write tests"):
```
[Line 154] Button: Add todo "Write tests"
[Line 47] Effect: Todos updated, count = 3
[Line 150] TodoList Component Rendered | Todo count: 3
```

**User Interaction Output** (Remove todo at index 0):
```
[Line 161] Button: Remove todo at index 0
[Line 47] Effect: Todos updated, count = 2
[Line 150] TodoList Component Rendered | Todo count: 2
```

---

### Section 7: Main App Component (Lines 220-243)

```typescript
220 | const App: React.FC = () => {
221 |   console.log('[Line 222] App Component Initialized');
222 |
223 |   return (
224 |     <StoreContainer.Container>
225 |       <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
226 |         <h1 style={{ textAlign: 'center', color: '#1f2937' }}>
227 |           React Undux TypeScript Demo
228 |         </h1>
```

**Purpose**: Main application container that wraps all components with the Undux store provider (`StoreContainer.Container`).

**Pattern**: Similar to Redux's `<Provider>` but automatically created by `createConnectedStore()`.

---

### Section 8: Application Bootstrap (Lines 248-260)

```typescript
250 | console.log('[Line 250] Starting React Application');
251 |
252 | const rootElement = document.getElementById('root');
253 | if (!rootElement) {
254 |   throw new Error('[Line 254] Root element not found');
255 | }
256 |
257 | console.log('[Line 257] Mounting React Application to DOM');
258 | const root = createRoot(rootElement);
259 | root.render(<App />);
260 | console.log('[Line 260] React Application Rendered');
```

**Output**:
```
[Line 250] Starting React Application
[Line 257] Mounting React Application to DOM
[Line 222] App Component Initialized
[Line 60] Counter Component Rendered | Current count: 0
[Line 105] UserProfile Component Rendered | Username: "Guest"
[Line 150] TodoList Component Rendered | Todo count: 2
[Line 260] React Application Rendered
```

---

## Complete Console Output

When the application loads:

```
[Line 27] Initial State: {
  "count": 0,
  "username": "Guest",
  "todos": ["Learn Undux", "Build awesome apps"]
}
[Line 33] Undux Store Created
[Line 250] Starting React Application
[Line 257] Mounting React Application to DOM
[Line 222] App Component Initialized
[Line 60] Counter Component Rendered | Current count: 0
[Line 105] UserProfile Component Rendered | Username: "Guest"
[Line 150] TodoList Component Rendered | Todo count: 2
[Line 260] React Application Rendered

========== Programmatic Store Demonstration ==========
[Line 268] Accessing store programmatically after 1 second...
[Line 273] Programmatically incrementing count...
[Line 277] ✓ React Undux TypeScript demonstration complete!
[Line 278] Key Concepts Illustrated:
  • Type-safe state management with TypeScript
  • Simple API: store.get() and store.set()
  • Effects with store.on() for side effects
  • Multiple components sharing the same store
  • Automatic re-rendering on state changes
  • Less boilerplate compared to Redux
  • No actions, reducers, or action creators needed
  • Perfect for small to medium applications
[Line 287] All components are reactive and type-safe!
```

### User Interaction Examples

**Example 1: Click Increment Button**
```
[Line 63] Button: Increment clicked
[Line 37] Effect: Count changed to 1
[Line 60] Counter Component Rendered | Current count: 1
```

**Example 2: Click "Add 5" Button**
```
[Line 73] Button: Add 5 clicked
[Line 37] Effect: Count changed to 6
[Line 60] Counter Component Rendered | Current count: 6
```

**Example 3: Update Username to "Bob"**
```
[Line 131] Input: Value changed to "B"
[Line 131] Input: Value changed to "Bo"
[Line 131] Input: Value changed to "Bob"
[Line 108] Button: Update username to "Bob"
[Line 42] Effect: Username changed to "Bob"
[Line 105] UserProfile Component Rendered | Username: "Bob"
```

**Example 4: Add New Todo "Deploy app"**
```
[Line 183] Input: New todo value = "D"
[Line 183] Input: New todo value = "De"
...
[Line 183] Input: New todo value = "Deploy app"
[Line 154] Button: Add todo "Deploy app"
[Line 47] Effect: Todos updated, count = 3
[Line 150] TodoList Component Rendered | Todo count: 3
```

**Example 5: Click Reset Button**
```
[Line 78] Button: Reset clicked
[Line 37] Effect: Count changed to 0
[Line 60] Counter Component Rendered | Current count: 0
```

---

## Code-to-Output Correlation

| Source Line | Output Line | Description |
|-------------|-------------|-------------|
| 27 | 27 | Initial state logged |
| 33 | 33 | Store creation logged |
| 250 | 250 | Application start logged |
| 257 | 257 | DOM mounting logged |
| 222 | 222 | App component initialization |
| 60 | 60 (multiple) | Counter renders on every count change |
| 105 | 105 (multiple) | UserProfile renders on username change |
| 150 | 150 (multiple) | TodoList renders on todos change |
| 37 | 37 (on count change) | Effect triggered when count changes |
| 42 | 42 (on username change) | Effect triggered when username changes |
| 47 | 47 (on todos change) | Effect triggered when todos change |
| 63 | 63 (on click) | Increment button click logged |
| 68 | 68 (on click) | Decrement button click logged |
| 73 | 73 (on click) | Add 5 button click logged |
| 78 | 78 (on click) | Reset button click logged |
| 108 | 108 (on click) | Update username button click logged |
| 154 | 154 (on add) | Add todo action logged |
| 161 | 161 (on remove) | Remove todo action logged |

---

## TypeScript Benefits Illustrated

### 1. Compile-Time Type Checking

Undux with TypeScript prevents common errors:

```typescript
// ✅ Valid: TypeScript knows 'count' is a number
const count = store.get('count');
store.set('count')(count + 1);

// ❌ TypeScript Error: Property 'invalidKey' does not exist on type 'AppState'
const value = store.get('invalidKey');

// ❌ TypeScript Error: Argument of type 'string' is not assignable to parameter of type 'number'
store.set('count')("invalid");

// ❌ TypeScript Error: Argument of type 'number' is not assignable to parameter of type 'string[]'
store.set('todos')(123);
```

### 2. IntelliSense and Autocomplete

TypeScript provides intelligent autocomplete:
- When typing `store.get('`, IDE shows: `'count' | 'username' | 'todos'`
- When typing `store.set('count')(`, IDE indicates it expects a `number`
- After `const todos = store.get('todos')`, IDE knows `todos` is `string[]`

### 3. Effect Type Safety

Effects are fully typed:

```typescript
// ✅ TypeScript knows 'count' is number
store.on('count').subscribe((count) => {
  // count is automatically typed as number
  console.log(count.toFixed(2)); // Valid
});

// ✅ TypeScript knows 'todos' is string[]
store.on('todos').subscribe((todos) => {
  // todos is automatically typed as string[]
  console.log(todos.length); // Valid
  console.log(todos.map(t => t.toUpperCase())); // Valid
});
```

### 4. Refactoring Safety

If you rename `count` to `counter` in the `AppState` interface:

```typescript
interface AppState {
  counter: number; // renamed from 'count'
  username: string;
  todos: string[];
}
```

TypeScript will flag **every** location that references `'count'`:
- All `store.get('count')` calls
- All `store.set('count')` calls
- All `store.on('count')` subscriptions

This prevents runtime errors and makes large-scale refactoring safe.

---

## Undux vs Redux: Key Differences

### Undux Advantages

1. **Less Boilerplate**: No action creators, action types, or reducers
2. **Simpler API**: Just `store.get()` and `store.set()`
3. **Built-in Effects**: `store.on()` for side effects (similar to Redux middleware)
4. **TypeScript First**: Designed with TypeScript in mind
5. **Smaller Bundle**: Lighter weight than Redux Toolkit

### When to Use Undux

- Small to medium applications
- Teams that want simplicity over flexibility
- Projects that prioritize TypeScript experience
- Applications without complex state orchestration needs

### When to Use Redux

- Large applications with complex state
- Need for time-travel debugging
- Extensive middleware requirements
- Large ecosystem of Redux libraries needed

---

## Architecture Highlights

### Simple State Flow

```
User Action → store.set('key')(value) → State Updated
                                             ↓
                                    Effects Triggered
                                             ↓
                                 Components Re-render
```

### Type Safety Flow

```
AppState Interface → createConnectedStore → Store<AppState>
                                                ↓
                                    Type-Safe store.get()
                                    Type-Safe store.set()
                                    Type-Safe store.on()
                                                ↓
                                        Compile-Time Safety
```

### Component Integration

```typescript
// 1. Get store instance
const store = StoreContainer.useStore();

// 2. Read state (type-safe)
const count = store.get('count'); // number

// 3. Update state (type-safe)
store.set('count')(count + 1); // ✓ Valid

// 4. Component automatically re-renders
```

---

## UI Features

The application renders a user interface with three main sections:

1. **Counter Component**:
   - Large count display
   - Increment, Decrement, Add 5, and Reset buttons
   - Demonstrates number state management

2. **User Profile Component**:
   - Current username display
   - Text input for username entry
   - Update and Clear buttons
   - Demonstrates string state management

3. **Todo List Component**:
   - Todo counter display
   - Input field for new todos
   - Add and Clear All buttons
   - Individual remove buttons for each todo
   - Demonstrates array state management

---

## Key Takeaways

1. **Type Safety**: Every state operation is type-checked, from reads to writes to effects
2. **Simplicity**: Undux's `get()` and `set()` API is easier to learn than Redux
3. **Less Code**: No actions, reducers, or action creators—just direct state manipulation
4. **Developer Experience**: Excellent IntelliSense, autocomplete, and refactoring support
5. **React Integration**: First-class React hooks with `useStore()`
6. **Effects System**: Built-in side effect handling with `store.on()`
7. **TypeScript First**: Designed for TypeScript from the ground up
8. **Production Ready**: Battle-tested library from Facebook (now Meta)

---

## Version Requirements

This demonstration requires:
- **TypeScript 5.6 or higher** for optimal type inference
- **React 18.3 or higher** for React 18 features (createRoot)
- **Undux 5.0 or higher** for latest TypeScript support

---

**Last Updated**: December 17, 2025
