// Simple Bun server to serve the React Router application
// This demonstrates how to serve a React app with Bun

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

console.log(`========================================`);
console.log(`React Router & Hooks Demo Server`);
console.log(`Server running at http://localhost:${server.port}`);
console.log(`Open your browser and navigate to the URL above`);
console.log(`========================================`);
