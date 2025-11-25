# Vue vs React TypeScript Hello World Comparison

This example demonstrates a simple counter application implemented in both Vue 3 and React 18 with TypeScript, highlighting the key differences in their approaches.

## Running the Examples

```bash
# Install dependencies
npm install

# Run Vue example
npm run dev:vue

# Run React example (in a different terminal)
npm run dev:react
```

## Vue TypeScript Example (main_vue_hello.ts)

### Source Code with Line Numbers

```typescript
1   import { createApp, ref } from 'vue';
2
3   // Vue Component using Composition API
4   const HelloWorld = {
5     setup() {
6       // Line 6: Reactive state using ref()
7       const message = ref('Hello from Vue with TypeScript!');
8       const count = ref(0);
9
10      // Line 10: Method to increment counter
11      const increment = () => {
12        count.value++;
13        console.log(`Count incremented to: ${count.value}`);
14      };
15
16      // Line 16: Expose reactive data and methods to template
17      return {
18        message,
19        count,
20        increment
21      };
22    },
23    // Line 23: Template definition
24    template: `
25      <div class="container">
26        <h1>{{ message }}</h1>
27        <p>You clicked {{ count }} times</p>
28        <button @click="increment">Click me</button>
29      </div>
30    `
31  };
32
33  // Line 33: Create and mount Vue app
34  const app = createApp(HelloWorld);
35  app.mount('#app');
36
37  console.log('Vue app mounted successfully!');
```

### Console Output

```
Vue app mounted successfully!
Count incremented to: 1
Count incremented to: 2
Count incremented to: 3
```

### Key Vue Concepts

**Line 1**: Import Vue's core functions
- `createApp`: Factory function to create Vue application instance
- `ref`: Creates reactive references that automatically trigger re-renders

**Lines 6-8**: Reactive State with `ref()`
- Vue uses `ref()` to wrap primitive values in reactive containers
- Accessing the value requires `.value` syntax (line 12)
- This enables Vue's reactivity system to track dependencies

**Lines 16-21**: Return Statement
- The `setup()` function must return an object exposing data and methods
- Everything returned becomes available to the template
- This is the "contract" between logic and template in Composition API

**Lines 24-30**: Template Syntax
- Uses Vue's template syntax with double curly braces `{{ }}` for interpolation
- `@click` is shorthand for `v-on:click` directive
- Templates are parsed and compiled by Vue

**Lines 34-35**: App Initialization
- Vue apps are created then explicitly mounted to a DOM element
- Two-step process: create → mount

---

## React TypeScript Example (main_react_hello.tsx)

### Source Code with Line Numbers

```typescript
1   import React, { useState } from 'react';
2   import { createRoot } from 'react-dom/client';
3
4   // Line 4: React Functional Component with TypeScript
5   const HelloWorld: React.FC = () => {
6     // Line 6: State using useState hook
7     const [message] = useState<string>('Hello from React with TypeScript!');
8     const [count, setCount] = useState<number>(0);
9
10    // Line 10: Method to increment counter
11    const increment = () => {
12      setCount(prevCount => {
13        const newCount = prevCount + 1;
14        console.log(`Count incremented to: ${newCount}`);
15        return newCount;
16      });
17    };
18
19    // Line 19: JSX return statement
20    return (
21      <div className="container">
22        <h1>{message}</h1>
23        <p>You clicked {count} times</p>
24        <button onClick={increment}>Click me</button>
25      </div>
26    );
27  };
28
29  // Line 29: Render React app
30  const container = document.getElementById('app');
31  if (container) {
32    const root = createRoot(container);
33    root.render(<HelloWorld />);
34    console.log('React app rendered successfully!');
35  }
```

### Console Output

```
React app rendered successfully!
Count incremented to: 1
Count incremented to: 2
Count incremented to: 3
```

### Key React Concepts

**Line 1-2**: Import React and ReactDOM
- `useState`: Hook for adding state to functional components
- `createRoot`: Modern React 18 API for rendering (replaces ReactDOM.render)

**Lines 7-8**: State with `useState()`
- Returns a tuple: `[currentValue, setterFunction]`
- Direct value access without `.value` syntax
- TypeScript generics `<string>` and `<number>` provide type safety

**Lines 11-17**: State Updates
- State is immutable - you must use setter functions
- Updater function form `prevCount => newCount` ensures correct updates
- React batches state updates for performance

**Lines 20-26**: JSX Return
- JSX looks like HTML but is JavaScript
- Single curly braces `{}` for JavaScript expressions
- `className` instead of `class` (reserved word in JS)
- Direct function reference in `onClick` prop

**Lines 32-33**: App Rendering
- React 18's `createRoot` creates a root, then renders into it
- Entire component tree is rendered in one call

---

## Side-by-Side Comparison

| Aspect | Vue 3 | React 18 |
|--------|-------|----------|
| **State Declaration** | `ref('value')` | `useState('value')` |
| **State Access** | `count.value` | `count` (direct) |
| **State Update** | `count.value++` | `setCount(count + 1)` |
| **Template Syntax** | HTML-like template strings | JSX (JavaScript XML) |
| **Reactivity Model** | Proxy-based reactivity | Virtual DOM diffing |
| **Event Binding** | `@click="handler"` | `onClick={handler}` |
| **Interpolation** | `{{ variable }}` | `{variable}` |
| **File Extension** | `.ts` | `.tsx` (for JSX) |
| **Component Style** | Composition API (setup) | Functional Component |
| **Mounting** | `app.mount('#app')` | `root.render(<App />)` |

## Key Philosophical Differences

### Vue Approach
- **Separation of Concerns**: Template, logic, and styles can be separate
- **Explicit Reactivity**: You explicitly mark reactive state with `ref()` or `reactive()`
- **Template-Based**: HTML-centric approach with directives
- **Gentle Learning Curve**: Familiar HTML syntax for beginners
- **Opinionated**: Provides official solutions (Vue Router, Pinia)

### React Approach
- **All JavaScript**: JSX is JavaScript, component is JavaScript
- **Immutable Updates**: State is immutable, you create new state
- **Functional Paradigm**: Heavy use of hooks and functional concepts
- **Explicit Control**: You control rendering flow
- **Unopinionated**: Community provides solutions (React Router, Redux, Zustand)

## Common Ground

Both frameworks:
- Support TypeScript with excellent type inference
- Use virtual DOM for efficient updates
- Provide reactive state management
- Support component composition
- Have large ecosystems and communities
- Use modern JavaScript features (ES6+)
- Offer developer tools for debugging

## Version Requirements

- **Vue**: Requires Vue 3.4+ for Composition API features shown
- **React**: Requires React 18.2+ for `createRoot` API
- **TypeScript**: 5.3+ recommended for both
- **Node.js**: 18+ recommended

## When to Choose Which?

**Choose Vue if:**
- You prefer template-based syntax
- You want an opinionated, batteries-included framework
- You're building a progressive web app that can scale gradually
- You prefer explicit reactivity
- Your team has strong HTML/CSS background

**Choose React if:**
- You prefer JavaScript-centric approach
- You want maximum flexibility in architecture
- You have a large ecosystem of third-party libraries
- You prefer functional programming patterns
- Your team has strong JavaScript background
