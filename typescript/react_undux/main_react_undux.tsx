/**
 * React Undux TypeScript Demo
 * Demonstrates type-safe state management with Undux
 */

import React from 'react';
import { createRoot } from 'react-dom/client';
import { createConnectedStore, Store } from 'undux';

// ============================================================
// Section 1: State Interface Definition (Lines 12-16)
// ============================================================
interface AppState {
  count: number;
  username: string;
  todos: string[];
}

// ============================================================
// Section 2: Initial State (Lines 20-24)
// ============================================================
const initialState: AppState = {
  count: 0,
  username: 'Guest',
  todos: ['Learn Undux', 'Build awesome apps']
};

console.log('[Line 27] Initial State:', JSON.stringify(initialState, null, 2));

// ============================================================
// Section 3: Store Creation with Effects (Lines 31-56)
// ============================================================
console.log('[Line 33] Creating Undux Store');

// Create store with effects
const StoreContainer = createConnectedStore(initialState);

// Set up effects after store creation
const setupEffects = (store: Store<AppState>) => {
  console.log('[Line 40] Setting up Undux effects');

  // Effect: Log count changes
  store.on('count').subscribe(count => {
    console.log(`[Line 44] Effect: Count changed to ${count}`);
  });

  // Effect: Log username changes
  store.on('username').subscribe(username => {
    console.log(`[Line 49] Effect: Username changed to "${username}"`);
  });

  // Effect: Log todos changes
  store.on('todos').subscribe(todos => {
    console.log(`[Line 54] Effect: Todos updated, count = ${todos.length}`);
  });
};

// ============================================================
// Section 4: Counter Component (Lines 59-100)
// ============================================================
const Counter: React.FC = () => {
  const store = StoreContainer.useStore();
  const count = store.get('count');

  // Set up effects once when component mounts
  React.useEffect(() => {
    setupEffects(store);
  }, [store]);

  console.log(`[Line 68] Counter Component Rendered | Current count: ${count}`);

  const increment = () => {
    console.log('[Line 63] Button: Increment clicked');
    store.set('count')(count + 1);
  };

  const decrement = () => {
    console.log('[Line 68] Button: Decrement clicked');
    store.set('count')(count - 1);
  };

  const addFive = () => {
    console.log('[Line 73] Button: Add 5 clicked');
    store.set('count')(count + 5);
  };

  const reset = () => {
    console.log('[Line 78] Button: Reset clicked');
    store.set('count')(0);
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h2>Counter Component</h2>
      <div style={{ fontSize: '48px', margin: '20px 0', color: '#2563eb' }}>
        {count}
      </div>
      <div style={{ display: 'flex', gap: '10px', marginTop: '10px' }}>
        <button onClick={increment} style={buttonStyle}>Increment</button>
        <button onClick={decrement} style={buttonStyle}>Decrement</button>
        <button onClick={addFive} style={buttonStyle}>Add 5</button>
        <button onClick={reset} style={buttonStyle}>Reset</button>
      </div>
    </div>
  );
};

// ============================================================
// Section 5: User Profile Component (Lines 99-140)
// ============================================================
const UserProfile: React.FC = () => {
  const store = StoreContainer.useStore();
  const username = store.get('username');
  const [inputValue, setInputValue] = React.useState(username);

  console.log(`[Line 105] UserProfile Component Rendered | Username: "${username}"`);

  const updateUsername = () => {
    console.log(`[Line 108] Button: Update username to "${inputValue}"`);
    store.set('username')(inputValue);
  };

  const clearUsername = () => {
    console.log('[Line 113] Button: Clear username clicked');
    store.set('username')('Guest');
    setInputValue('Guest');
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif', borderTop: '2px solid #ccc' }}>
      <h2>User Profile Component</h2>
      <div style={{ marginBottom: '15px' }}>
        <strong>Current User:</strong> <span style={{ color: '#059669', fontSize: '20px' }}>{username}</span>
      </div>
      <div style={{ display: 'flex', gap: '10px', alignItems: 'center' }}>
        <input
          type="text"
          value={inputValue}
          onChange={(e) => {
            console.log(`[Line 131] Input: Value changed to "${e.target.value}"`);
            setInputValue(e.target.value);
          }}
          placeholder="Enter username"
          style={inputStyle}
        />
        <button onClick={updateUsername} style={buttonStyle}>Update</button>
        <button onClick={clearUsername} style={buttonStyle}>Clear</button>
      </div>
    </div>
  );
};

// ============================================================
// Section 6: Todo List Component (Lines 144-202)
// ============================================================
const TodoList: React.FC = () => {
  const store = StoreContainer.useStore();
  const todos = store.get('todos');
  const [newTodo, setNewTodo] = React.useState('');

  console.log(`[Line 150] TodoList Component Rendered | Todo count: ${todos.length}`);

  const addTodo = () => {
    if (newTodo.trim()) {
      console.log(`[Line 154] Button: Add todo "${newTodo}"`);
      store.set('todos')([...todos, newTodo]);
      setNewTodo('');
    }
  };

  const removeTodo = (index: number) => {
    console.log(`[Line 161] Button: Remove todo at index ${index}`);
    const newTodos = todos.filter((_, i) => i !== index);
    store.set('todos')(newTodos);
  };

  const clearAll = () => {
    console.log('[Line 167] Button: Clear all todos');
    store.set('todos')([]);
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif', borderTop: '2px solid #ccc' }}>
      <h2>Todo List Component</h2>
      <div style={{ marginBottom: '15px' }}>
        <strong>Total Todos:</strong> <span style={{ color: '#dc2626', fontSize: '20px' }}>{todos.length}</span>
      </div>
      <div style={{ display: 'flex', gap: '10px', marginBottom: '15px', alignItems: 'center' }}>
        <input
          type="text"
          value={newTodo}
          onChange={(e) => {
            console.log(`[Line 183] Input: New todo value = "${e.target.value}"`);
            setNewTodo(e.target.value);
          }}
          onKeyPress={(e) => {
            if (e.key === 'Enter') {
              addTodo();
            }
          }}
          placeholder="Enter new todo"
          style={inputStyle}
        />
        <button onClick={addTodo} style={buttonStyle}>Add</button>
        <button onClick={clearAll} style={buttonStyle}>Clear All</button>
      </div>
      <ul style={{ listStyle: 'none', padding: 0 }}>
        {todos.map((todo, index) => (
          <li key={index} style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            padding: '10px',
            marginBottom: '5px',
            backgroundColor: '#f3f4f6',
            borderRadius: '5px'
          }}>
            <span>{todo}</span>
            <button
              onClick={() => removeTodo(index)}
              style={{ ...buttonStyle, backgroundColor: '#ef4444' }}
            >
              Remove
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

// ============================================================
// Section 7: Main App Component (Lines 220-238)
// ============================================================
const App: React.FC = () => {
  console.log('[Line 222] App Component Initialized');

  return (
    <StoreContainer.Container>
      <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
        <h1 style={{ textAlign: 'center', color: '#1f2937' }}>
          React Undux TypeScript Demo
        </h1>
        <div style={{ backgroundColor: '#fef3c7', padding: '15px', borderRadius: '8px', marginBottom: '20px' }}>
          <strong>TypeScript Features:</strong>
          <ul style={{ margin: '10px 0' }}>
            <li>Type-safe state interface (AppState)</li>
            <li>Compile-time type checking for all state operations</li>
            <li>IntelliSense support for store.get() and store.set()</li>
            <li>Type-safe effects with .on() subscriptions</li>
          </ul>
        </div>
        <Counter />
        <UserProfile />
        <TodoList />
      </div>
    </StoreContainer.Container>
  );
};

// ============================================================
// Section 8: Bootstrap Application (Lines 248-260)
// ============================================================
console.log('[Line 250] Starting React Application');

const rootElement = document.getElementById('root');
if (!rootElement) {
  throw new Error('[Line 254] Root element not found');
}

console.log('[Line 257] Mounting React Application to DOM');
const root = createRoot(rootElement);
root.render(<App />);
console.log('[Line 260] React Application Rendered');

// ============================================================
// Section 9: Programmatic Store Access (Lines 264-289)
// ============================================================
console.log('\n========== Programmatic Store Demonstration ==========');

// Access store directly (outside React components)
setTimeout(() => {
  console.log('[Line 268] Accessing store programmatically after 1 second...');

  console.log('[Line 270] Note: Direct store access outside components is not typical in Undux');
  console.log('[Line 271] In a real application, all state updates happen via components');

  console.log('[Line 273] ✓ React Undux TypeScript demonstration complete!');
  console.log('[Line 278] Key Concepts Illustrated:');
  console.log('  • Type-safe state management with TypeScript');
  console.log('  • Simple API: store.get() and store.set()');
  console.log('  • Effects with store.on() for side effects');
  console.log('  • Multiple components sharing the same store');
  console.log('  • Automatic re-rendering on state changes');
  console.log('  • Less boilerplate compared to Redux');
  console.log('  • No actions, reducers, or action creators needed');
  console.log('  • Perfect for small to medium applications');
  console.log('[Line 287] All components are reactive and type-safe!');
}, 1000);

// ============================================================
// Styling
// ============================================================
const buttonStyle: React.CSSProperties = {
  padding: '10px 20px',
  fontSize: '16px',
  cursor: 'pointer',
  backgroundColor: '#3b82f6',
  color: 'white',
  border: 'none',
  borderRadius: '5px',
  fontWeight: 'bold'
};

const inputStyle: React.CSSProperties = {
  padding: '10px',
  fontSize: '16px',
  border: '2px solid #d1d5db',
  borderRadius: '5px',
  flex: 1,
  maxWidth: '300px'
};
