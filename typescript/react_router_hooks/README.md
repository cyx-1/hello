# React Router and Hooks with Bun and TypeScript

This example demonstrates React Router v6 with various React hooks including `useState`, `useEffect`, `useParams`, `useNavigate`, `useLocation`, and routing features like `NavLink`, `Link`, and `Navigate`.

## Requirements

- **Bun**: v1.0.0 or higher
- **React**: v18.2.0 or higher
- **React Router DOM**: v6.20.0 or higher
- **TypeScript**: v5.3.0 or higher

## Installation

```bash
bun install
```

## Running the Application

```bash
bun run dev
# or
bun run serve
```

The server will start at `http://localhost:3000`. Open your browser and navigate to this URL.

## Features Demonstrated

### 1. React Router Setup (Lines 313-342)

The application uses `BrowserRouter` to provide routing context:

```tsx
// Line 313: BrowserRouter provides routing context to entire app
<BrowserRouter>
  <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
    <Navigation />

    <main>
      {/* Line 320: Routes component wraps all Route definitions */}
      <Routes>
        {/* Line 322: Route with exact path match */}
        <Route path="/" element={<Home />} />

        {/* Line 325: Route for About page */}
        <Route path="/about" element={<About />} />

        {/* Line 328: Route with URL parameter using :userId syntax */}
        <Route path="/users/:userId" element={<UserProfile />} />

        {/* Line 331: Route for products list */}
        <Route path="/products" element={<Products />} />

        {/* Line 334: Nested route for product details */}
        <Route path="/products/:productId" element={<ProductDetail />} />

        {/* Line 337: Redirect from /home to / */}
        <Route path="/home" element={<Navigate to="/" replace />} />

        {/* Line 340: Catch-all route for 404 Not Found */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </main>
  </div>
</BrowserRouter>
```

**Console Output:**
```
[Line 361] Initializing React application...
[Line 306] ========================================
[Line 307] React Router & Hooks App Started
[Line 308] Start Time: 10:30:45 AM
[Line 309] ========================================
[Line 371] React application rendered successfully
```

### 2. useState Hook (Lines 30-31)

The `useState` hook manages component state:

```tsx
// Line 30: useState hook for managing visit count
const [visitCount, setVisitCount] = useState<number>(0);
```

**Console Output:**
```
[Line 36] Home component mounted
```

When you visit the Home page, the visit count increments and displays in the UI.

### 3. useEffect Hook (Lines 35-40)

The `useEffect` hook handles side effects and lifecycle events:

```tsx
// Line 35: useEffect hook runs on component mount
useEffect(() => {
  console.log('[Line 36] Home component mounted');
  setVisitCount(prev => prev + 1);
  return () => console.log('[Line 39] Home component unmounting');
}, []);
```

**Console Output:**
```
[Line 36] Home component mounted
[Line 39] Home component unmounting  // When navigating away
```

### 4. useParams Hook (Lines 85-107)

The `useParams` hook extracts URL parameters from dynamic routes:

```tsx
// Line 85: useParams hook to extract URL parameters
const { userId } = useParams<{ userId: string }>();
const [user, setUser] = useState<User | null>(null);
const [loading, setLoading] = useState<boolean>(true);

// Line 90: useEffect to simulate fetching user data
useEffect(() => {
  console.log(`[Line 92] Fetching user with ID: ${userId}`);
  setLoading(true);

  // Simulate API call with setTimeout
  const timer = setTimeout(() => {
    const mockUser: User = {
      id: parseInt(userId || '0'),
      name: `User ${userId}`,
      email: `user${userId}@example.com`
    };
    setUser(mockUser);
    setLoading(false);
    console.log(`[Line 104] User data loaded:`, mockUser);
  }, 500);

  return () => clearTimeout(timer);
}, [userId]);
```

**Console Output when navigating to `/users/123`:**
```
[Line 92] Fetching user with ID: 123
[Line 104] User data loaded: { id: 123, name: 'User 123', email: 'user123@example.com' }
```

**UI Display:**
```
User Profile
ID: 123
Name: User 123
Email: user123@example.com
URL Parameter (userId): 123
```

### 5. useNavigate Hook (Lines 43-47)

The `useNavigate` hook enables programmatic navigation:

```tsx
// Line 43: Programmatic navigation using useNavigate hook
const handleNavigateToAbout = () => {
  console.log('[Line 45] Navigating to About page programmatically');
  navigate('/about');
};
```

**Console Output when clicking "Go to About (programmatic)" button:**
```
[Line 45] Navigating to About page programmatically
[Line 67] About page loaded at path: /about
[Line 68] Search params:
```

### 6. useLocation Hook (Lines 61-71)

The `useLocation` hook provides access to the current location object:

```tsx
// Line 61: useLocation hook to access current location
const location = useLocation();
const [renderCount, setRenderCount] = useState<number>(0);

// Line 65: useEffect to track location changes
useEffect(() => {
  console.log(`[Line 67] About page loaded at path: ${location.pathname}`);
  console.log(`[Line 68] Search params: ${location.search}`);
  setRenderCount(prev => prev + 1);
}, [location]);
```

**Console Output:**
```
[Line 67] About page loaded at path: /about
[Line 68] Search params:
```

### 7. NavLink with Active Styling (Lines 244-258)

`NavLink` automatically applies active styling to the current route:

```tsx
{/* Line 244: NavLink automatically adds 'active' class to current route */}
<NavLink
  to="/"
  style={({ isActive }) => ({
    padding: '8px 12px',
    backgroundColor: isActive ? '#007bff' : '#fff',
    color: isActive ? '#fff' : '#007bff',
    textDecoration: 'none',
    borderRadius: '4px',
    border: '1px solid #007bff'
  })}
>
  Home
</NavLink>
```

When on the home page (`/`), the Home link will have a blue background. Other links will have white backgrounds.

### 8. Dynamic Product List (Lines 135-174)

Demonstrates list rendering with navigation:

```tsx
// Line 135: useState to manage products list
const [products, setProducts] = useState<Product[]>([]);
const navigate = useNavigate();

// Line 139: useEffect to load products on mount
useEffect(() => {
  console.log('[Line 141] Loading products...');
  const mockProducts: Product[] = [
    { id: 1, name: 'Laptop', price: 999 },
    { id: 2, name: 'Mouse', price: 29 },
    { id: 3, name: 'Keyboard', price: 79 },
  ];
  setProducts(mockProducts);
  console.log('[Line 148] Products loaded:', mockProducts.length);
}, []);

const handleProductClick = (productId: number) => {
  console.log(`[Line 152] Navigating to product ${productId}`);
  navigate(`/products/${productId}`);
};
```

**Console Output when navigating to `/products`:**
```
[Line 141] Loading products...
[Line 148] Products loaded: 3
```

**Console Output when clicking "View Details" for product 1:**
```
[Line 152] Navigating to product 1
[Line 184] Loading product details for ID: 1
[Line 196] Product found: { id: 1, name: 'Laptop', price: 999 }
```

### 9. 404 Not Found Route (Lines 215-230)

Catch-all route for non-existent pages:

```tsx
const NotFound: React.FC = () => {
  const location = useLocation();

  useEffect(() => {
    console.log(`[Line 219] 404 - Page not found: ${location.pathname}`);
  }, [location]);

  return (
    <div>
      <h2>404 - Page Not Found</h2>
      <p>The page '{location.pathname}' does not exist.</p>
      <Link to="/">Go back to Home</Link>
    </div>
  );
};
```

**Console Output when navigating to `/non-existent-page`:**
```
[Line 219] 404 - Page not found: /non-existent-page
```

### 10. Server Implementation

The `server.ts` file demonstrates Bun's built-in server capabilities:

```typescript
const server = Bun.serve({
  port: 3000,
  async fetch(req) {
    const url = new URL(req.url);
    console.log(`[Server] ${req.method} ${url.pathname}`);

    // Serve the main HTML file for all routes (SPA routing)
    if (url.pathname === '/' || !url.pathname.includes('.')) {
      return new Response(Bun.file('./index.html'), {
        headers: { 'Content-Type': 'text/html' }
      });
    }

    // Serve static files (JS, CSS, etc.)
    const filePath = `.${url.pathname}`;
    const file = Bun.file(filePath);

    if (await file.exists()) {
      return new Response(file);
    }

    // 404 for missing files
    return new Response('Not Found', { status: 404 });
  },
});
```

**Server Console Output:**
```
========================================
React Router & Hooks Demo Server
Server running at http://localhost:3000
Open your browser and navigate to the URL above
========================================
[Server] GET /
[Server] GET /main_react_router_hooks.tsx
```

## Complete User Flow Example

1. **Start Server:**
   ```
   ========================================
   React Router & Hooks Demo Server
   Server running at http://localhost:3000
   ========================================
   ```

2. **Navigate to Home (`/`):**
   ```
   [Line 361] Initializing React application...
   [Line 306] ========================================
   [Line 307] React Router & Hooks App Started
   [Line 308] Start Time: 10:30:45 AM
   [Line 309] ========================================
   [Line 36] Home component mounted
   [Line 371] React application rendered successfully
   ```

3. **Click "Go to About (programmatic)":**
   ```
   [Line 45] Navigating to About page programmatically
   [Line 39] Home component unmounting
   [Line 67] About page loaded at path: /about
   [Line 68] Search params:
   ```

4. **Navigate to User Profile (`/users/123`):**
   ```
   [Line 92] Fetching user with ID: 123
   [Line 104] User data loaded: { id: 123, name: 'User 123', email: 'user123@example.com' }
   ```

5. **Navigate to Products (`/products`):**
   ```
   [Line 141] Loading products...
   [Line 148] Products loaded: 3
   ```

6. **Click product details:**
   ```
   [Line 152] Navigating to product 1
   [Line 184] Loading product details for ID: 1
   [Line 196] Product found: { id: 1, name: 'Laptop', price: 999 }
   ```

## Key React Hooks Demonstrated

| Hook | Purpose | Line Reference |
|------|---------|----------------|
| `useState` | Manage component state | Line 30, 135, 301 |
| `useEffect` | Handle side effects and lifecycle | Line 35, 65, 90, 139, 304 |
| `useParams` | Extract URL parameters | Line 85, 179 |
| `useNavigate` | Programmatic navigation | Line 33, 43-47, 137, 152 |
| `useLocation` | Access current location | Line 61, 216 |

## React Router Features Demonstrated

| Feature | Purpose | Line Reference |
|---------|---------|----------------|
| `BrowserRouter` | Provides routing context | Line 313 |
| `Routes` | Container for all routes | Line 320 |
| `Route` | Define individual routes | Lines 322-340 |
| `Link` | Declarative navigation | Line 228 |
| `NavLink` | Navigation with active state | Lines 244-294 |
| `Navigate` | Redirect component | Line 337 |

## Type Safety

This example demonstrates TypeScript type safety:

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

interface Product {
  id: number;
  name: string;
  price: number;
}

const { userId } = useParams<{ userId: string }>();
```

All hooks and components are fully typed for compile-time safety.

## Project Structure

```
typescript/react_router_hooks/
├── main_react_router_hooks.tsx  # Main React application
├── server.ts                     # Bun server
├── index.html                    # HTML entry point
├── package.json                  # Dependencies and scripts
├── tsconfig.json                 # TypeScript configuration
└── README.md                     # This file
```

## Browser Console Output

When running the application in a browser, open Developer Tools (F12) to see the console logs that correspond to the line numbers referenced above. This helps you understand the flow of the application and when each hook is triggered.

---

**Last Updated:** 2025-11-21
