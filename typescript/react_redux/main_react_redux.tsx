import React from 'react';
import { createRoot } from 'react-dom/client';
import { configureStore, createSlice, PayloadAction } from '@reduxjs/toolkit';
import { Provider, useSelector, useDispatch } from 'react-redux';

// ============================================================================
// 1. Define State Interface
// ============================================================================
interface CounterState {
  value: number;
  history: string[];
}

// ============================================================================
// 2. Create Redux Slice with TypeScript
// ============================================================================
const counterSlice = createSlice({
  name: 'counter',
  initialState: {
    value: 0,
    history: ['Initialized with value: 0']
  } as CounterState,
  reducers: {
    increment: (state) => {
      state.value += 1;
      state.history.push(`Incremented to: ${state.value}`);
      console.log(`[Line 27] Action: INCREMENT | New value: ${state.value}`);
    },
    decrement: (state) => {
      state.value -= 1;
      state.history.push(`Decremented to: ${state.value}`);
      console.log(`[Line 32] Action: DECREMENT | New value: ${state.value}`);
    },
    incrementByAmount: (state, action: PayloadAction<number>) => {
      state.value += action.payload;
      state.history.push(`Added ${action.payload}, new value: ${state.value}`);
      console.log(`[Line 37] Action: INCREMENT_BY_AMOUNT | Added: ${action.payload} | New value: ${state.value}`);
    },
    reset: (state) => {
      state.value = 0;
      state.history.push('Reset to: 0');
      console.log(`[Line 43] Action: RESET | Value: ${state.value}`);
    }
  }
});

// ============================================================================
// 3. Export Actions
// ============================================================================
export const { increment, decrement, incrementByAmount, reset } = counterSlice.actions;

// ============================================================================
// 4. Configure Store
// ============================================================================
const store = configureStore({
  reducer: {
    counter: counterSlice.reducer
  }
});

// ============================================================================
// 5. Define RootState and AppDispatch Types
// ============================================================================
export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

console.log('[Line 68] Redux Store Configured');
console.log('[Line 69] Initial State:', store.getState());

// ============================================================================
// 6. Counter Component with TypeScript
// ============================================================================
const Counter: React.FC = () => {
  // Type-safe hooks
  const count = useSelector((state: RootState) => state.counter.value);
  const history = useSelector((state: RootState) => state.counter.history);
  const dispatch = useDispatch<AppDispatch>();

  console.log('[Line 81] Counter Component Rendered | Current count:', count);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>React Redux TypeScript Demo</h1>

      <div style={{
        fontSize: '48px',
        margin: '20px 0',
        padding: '20px',
        backgroundColor: '#f0f0f0',
        borderRadius: '8px',
        textAlign: 'center'
      }}>
        Count: {count}
      </div>

      <div style={{ display: 'flex', gap: '10px', marginBottom: '20px' }}>
        <button
          onClick={() => {
            console.log('[Line 102] Button: Increment clicked');
            dispatch(increment());
          }}
          style={{ padding: '10px 20px', fontSize: '16px', cursor: 'pointer' }}
        >
          Increment (+1)
        </button>

        <button
          onClick={() => {
            console.log('[Line 112] Button: Decrement clicked');
            dispatch(decrement());
          }}
          style={{ padding: '10px 20px', fontSize: '16px', cursor: 'pointer' }}
        >
          Decrement (-1)
        </button>

        <button
          onClick={() => {
            console.log('[Line 122] Button: Add 5 clicked');
            dispatch(incrementByAmount(5));
          }}
          style={{ padding: '10px 20px', fontSize: '16px', cursor: 'pointer' }}
        >
          Add 5
        </button>

        <button
          onClick={() => {
            console.log('[Line 132] Button: Reset clicked');
            dispatch(reset());
          }}
          style={{ padding: '10px 20px', fontSize: '16px', cursor: 'pointer', backgroundColor: '#ff6b6b', color: 'white', border: 'none' }}
        >
          Reset
        </button>
      </div>

      <div style={{
        marginTop: '30px',
        padding: '15px',
        backgroundColor: '#e8f4f8',
        borderRadius: '8px'
      }}>
        <h3>Action History:</h3>
        <ul style={{ maxHeight: '200px', overflowY: 'auto' }}>
          {history.map((entry, index) => (
            <li key={index}>{entry}</li>
          ))}
        </ul>
      </div>

      <div style={{
        marginTop: '30px',
        padding: '15px',
        backgroundColor: '#fff3cd',
        borderRadius: '8px'
      }}>
        <h3>TypeScript Features Demonstrated:</h3>
        <ul>
          <li><strong>Typed State:</strong> CounterState interface (Lines 9-12)</li>
          <li><strong>Typed Actions:</strong> PayloadAction&lt;number&gt; (Line 34)</li>
          <li><strong>Typed Selectors:</strong> useSelector with RootState (Lines 77-78)</li>
          <li><strong>Typed Dispatch:</strong> useDispatch&lt;AppDispatch&gt; (Line 79)</li>
          <li><strong>Type Inference:</strong> ReturnType utility (Line 66)</li>
        </ul>
      </div>
    </div>
  );
};

// ============================================================================
// 7. App Component with Redux Provider
// ============================================================================
const App: React.FC = () => {
  console.log('[Line 183] App Component Initialized');

  return (
    <Provider store={store}>
      <Counter />
    </Provider>
  );
};

// ============================================================================
// 8. Render Application
// ============================================================================
console.log('[Line 195] Starting React Application');
const container = document.getElementById('root');
if (container) {
  const root = createRoot(container);
  root.render(<App />);
  console.log('[Line 200] React Application Rendered to DOM');
} else {
  console.error('[Line 202] Root element not found!');
}

// ============================================================================
// 9. Demonstrate Programmatic Store Access (for educational purposes)
// ============================================================================
console.log('\n========== Programmatic Store Demonstration ==========');
console.log('[Line 209] Dispatching increment action programmatically...');
store.dispatch(increment());

console.log('[Line 212] Dispatching incrementByAmount(10) action programmatically...');
store.dispatch(incrementByAmount(10));

console.log('[Line 215] Current state after programmatic actions:');
console.log(store.getState());

console.log('\n[Line 218] ✓ React Redux TypeScript demonstration complete!');
console.log('[Line 219] Key Concepts Illustrated:');
console.log('  • Redux Toolkit with createSlice (modern Redux)');
console.log('  • TypeScript interfaces for state and actions');
console.log('  • Type-safe hooks (useSelector, useDispatch)');
console.log('  • Redux DevTools compatible store configuration');
console.log('  • Immer-powered immutable updates (built into Redux Toolkit)');
