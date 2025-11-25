import React, { useState } from 'react';
import { createRoot } from 'react-dom/client';

// Line 4: React Functional Component with TypeScript
const HelloWorld: React.FC = () => {
  // Line 6: State using useState hook
  const [message] = useState<string>('Hello from React with TypeScript!');
  const [count, setCount] = useState<number>(0);

  // Line 10: Method to increment counter
  const increment = () => {
    setCount(prevCount => {
      const newCount = prevCount + 1;
      console.log(`Count incremented to: ${newCount}`);
      return newCount;
    });
  };

  // Line 19: JSX return statement
  return (
    <div className="container">
      <h1>{message}</h1>
      <p>You clicked {count} times</p>
      <button onClick={increment}>Click me</button>
    </div>
  );
};

// Line 29: Render React app
const container = document.getElementById('app');
if (container) {
  const root = createRoot(container);
  root.render(<HelloWorld />);
  console.log('React app rendered successfully!');
}
