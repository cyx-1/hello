// React Router and Hooks Example with Bun and TypeScript
// This example demonstrates React Router v6 with various React hooks

import React, { useState, useEffect } from 'react';
import { createRoot } from 'react-dom/client';
import {
  BrowserRouter,
  Routes,
  Route,
  Link,
  NavLink,
  useParams,
  useNavigate,
  useLocation,
  Navigate
} from 'react-router-dom';

// Type definitions
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

// Home Component - demonstrates useState and basic routing
const Home: React.FC = () => {
  // Line 30: useState hook for managing visit count
  const [visitCount, setVisitCount] = useState<number>(0);
  const navigate = useNavigate();

  // Line 35: useEffect hook runs on component mount
  useEffect(() => {
    console.log('[Line 36] Home component mounted');
    setVisitCount(prev => prev + 1);
    return () => console.log('[Line 39] Home component unmounting');
  }, []);

  // Line 43: Programmatic navigation using useNavigate hook
  const handleNavigateToAbout = () => {
    console.log('[Line 45] Navigating to About page programmatically');
    navigate('/about');
  };

  return (
    <div>
      <h2>Home Page</h2>
      <p>Welcome! You've visited this page {visitCount} time(s)</p>
      <button onClick={handleNavigateToAbout}>Go to About (programmatic)</button>
    </div>
  );
};

// About Component - demonstrates useLocation hook
const About: React.FC = () => {
  // Line 61: useLocation hook to access current location
  const location = useLocation();
  const [renderCount, setRenderCount] = useState<number>(0);

  // Line 65: useEffect to track location changes
  useEffect(() => {
    console.log(`[Line 67] About page loaded at path: ${location.pathname}`);
    console.log(`[Line 68] Search params: ${location.search}`);
    setRenderCount(prev => prev + 1);
  }, [location]);

  return (
    <div>
      <h2>About Page</h2>
      <p>Current path: {location.pathname}</p>
      <p>Render count: {renderCount}</p>
      <p>This page demonstrates the useLocation hook</p>
    </div>
  );
};

// User Profile Component - demonstrates useParams hook
const UserProfile: React.FC = () => {
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

  if (loading) {
    return <div>Loading user profile...</div>;
  }

  return (
    <div>
      <h2>User Profile</h2>
      {user && (
        <div>
          <p><strong>ID:</strong> {user.id}</p>
          <p><strong>Name:</strong> {user.name}</p>
          <p><strong>Email:</strong> {user.email}</p>
        </div>
      )}
      <p style={{ marginTop: '20px', fontSize: '12px', color: '#666' }}>
        URL Parameter (userId): {userId}
      </p>
    </div>
  );
};

// Products Component - demonstrates list rendering with navigation
const Products: React.FC = () => {
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

  return (
    <div>
      <h2>Products</h2>
      <ul>
        {products.map(product => (
          <li key={product.id} style={{ marginBottom: '10px' }}>
            {product.name} - ${product.price}
            <button
              onClick={() => handleProductClick(product.id)}
              style={{ marginLeft: '10px' }}
            >
              View Details
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

// Product Detail Component - demonstrates nested routing
const ProductDetail: React.FC = () => {
  const { productId } = useParams<{ productId: string }>();
  const [product, setProduct] = useState<Product | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    console.log(`[Line 184] Loading product details for ID: ${productId}`);

    // Simulate fetching product details
    const mockProducts: Product[] = [
      { id: 1, name: 'Laptop', price: 999 },
      { id: 2, name: 'Mouse', price: 29 },
      { id: 3, name: 'Keyboard', price: 79 },
    ];

    const foundProduct = mockProducts.find(p => p.id === parseInt(productId || '0'));
    setProduct(foundProduct || null);
    console.log('[Line 196] Product found:', foundProduct);
  }, [productId]);

  if (!product) {
    return <div>Product not found</div>;
  }

  return (
    <div>
      <h2>Product Details</h2>
      <p><strong>Name:</strong> {product.name}</p>
      <p><strong>Price:</strong> ${product.price}</p>
      <button onClick={() => navigate('/products')}>Back to Products</button>
    </div>
  );
};

// Not Found Component
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

// Navigation Component - demonstrates NavLink with active styling
const Navigation: React.FC = () => {
  return (
    <nav style={{
      padding: '20px',
      backgroundColor: '#f0f0f0',
      marginBottom: '20px'
    }}>
      <h1 style={{ margin: '0 0 15px 0' }}>React Router & Hooks Demo</h1>
      <div style={{ display: 'flex', gap: '15px', flexWrap: 'wrap' }}>
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
        <NavLink
          to="/about"
          style={({ isActive }) => ({
            padding: '8px 12px',
            backgroundColor: isActive ? '#007bff' : '#fff',
            color: isActive ? '#fff' : '#007bff',
            textDecoration: 'none',
            borderRadius: '4px',
            border: '1px solid #007bff'
          })}
        >
          About
        </NavLink>
        <NavLink
          to="/users/123"
          style={({ isActive }) => ({
            padding: '8px 12px',
            backgroundColor: isActive ? '#007bff' : '#fff',
            color: isActive ? '#fff' : '#007bff',
            textDecoration: 'none',
            borderRadius: '4px',
            border: '1px solid #007bff'
          })}
        >
          User 123
        </NavLink>
        <NavLink
          to="/products"
          style={({ isActive }) => ({
            padding: '8px 12px',
            backgroundColor: isActive ? '#007bff' : '#fff',
            color: isActive ? '#fff' : '#007bff',
            textDecoration: 'none',
            borderRadius: '4px',
            border: '1px solid #007bff'
          })}
        >
          Products
        </NavLink>
      </div>
    </nav>
  );
};

// Main App Component
const App: React.FC = () => {
  // Line 301: useState hook for app-level state
  const [appStartTime] = useState<Date>(new Date());

  // Line 304: useEffect runs once when app mounts
  useEffect(() => {
    console.log('[Line 306] ========================================');
    console.log('[Line 307] React Router & Hooks App Started');
    console.log('[Line 308] Start Time:', appStartTime.toLocaleTimeString());
    console.log('[Line 309] ========================================');
  }, [appStartTime]);

  return (
    // Line 313: BrowserRouter provides routing context to entire app
    <BrowserRouter>
      <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
        <Navigation />

        <main style={{ padding: '20px', backgroundColor: '#fff', borderRadius: '8px', boxShadow: '0 2px 4px rgba(0,0,0,0.1)' }}>
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

        <footer style={{
          marginTop: '40px',
          padding: '20px',
          textAlign: 'center',
          fontSize: '12px',
          color: '#666'
        }}>
          <p>App started at: {appStartTime.toLocaleTimeString()}</p>
        </footer>
      </div>
    </BrowserRouter>
  );
};

// Line 360: Application entry point
console.log('[Line 361] Initializing React application...');

const container = document.getElementById('root');
if (!container) {
  throw new Error('Root element not found');
}

const root = createRoot(container);
root.render(<App />);

console.log('[Line 371] React application rendered successfully');

export default App;
