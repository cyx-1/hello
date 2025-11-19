/**
 * Comprehensive demonstration of the Proxy Pattern in Java
 *
 * The Proxy pattern provides a surrogate or placeholder for another object
 * to control access to it.
 */

import java.util.HashMap;
import java.util.Map;

// Subject interface
interface Image {
    void display();
    String getFilename();
}

// Real Subject - expensive to create
class RealImage implements Image {
    private String filename;

    public RealImage(String filename) {
        this.filename = filename;
        loadFromDisk();
    }

    private void loadFromDisk() {
        System.out.println("  [RealImage] Loading image from disk: " + filename);
        // Simulate expensive operation
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    @Override
    public void display() {
        System.out.println("  [RealImage] Displaying: " + filename);
    }

    @Override
    public String getFilename() {
        return filename;
    }
}

// Virtual Proxy - lazy initialization
class ProxyImage implements Image {
    private RealImage realImage;
    private String filename;

    public ProxyImage(String filename) {
        this.filename = filename;
        System.out.println("  [ProxyImage] Created proxy for: " + filename);
    }

    @Override
    public void display() {
        if (realImage == null) {
            realImage = new RealImage(filename);
        }
        realImage.display();
    }

    @Override
    public String getFilename() {
        return filename;
    }
}

// Protection Proxy example

interface Document {
    void read();
    void write(String content);
    void delete();
}

class RealDocument implements Document {
    private String name;
    private String content;

    public RealDocument(String name) {
        this.name = name;
        this.content = "Original content of " + name;
    }

    @Override
    public void read() {
        System.out.println("  [RealDocument] Reading: " + content);
    }

    @Override
    public void write(String content) {
        this.content = content;
        System.out.println("  [RealDocument] Content updated to: " + content);
    }

    @Override
    public void delete() {
        System.out.println("  [RealDocument] Document deleted: " + name);
    }
}

// Protection Proxy with access control
class ProtectedDocumentProxy implements Document {
    private RealDocument realDocument;
    private String userRole;
    private String documentName;

    public ProtectedDocumentProxy(String documentName, String userRole) {
        this.documentName = documentName;
        this.userRole = userRole;
    }

    private void initDocument() {
        if (realDocument == null) {
            realDocument = new RealDocument(documentName);
        }
    }

    @Override
    public void read() {
        initDocument();
        // Everyone can read
        realDocument.read();
    }

    @Override
    public void write(String content) {
        if (!userRole.equals("admin") && !userRole.equals("editor")) {
            System.out.println("  [ProtectionProxy] Access denied! " + userRole + " cannot write.");
            return;
        }
        initDocument();
        realDocument.write(content);
    }

    @Override
    public void delete() {
        if (!userRole.equals("admin")) {
            System.out.println("  [ProtectionProxy] Access denied! Only admin can delete.");
            return;
        }
        initDocument();
        realDocument.delete();
    }
}

// Caching Proxy example

interface DataService {
    String fetchData(String key);
}

class RealDataService implements DataService {
    @Override
    public String fetchData(String key) {
        System.out.println("  [RealDataService] Fetching data from database for key: " + key);
        // Simulate database call
        try {
            Thread.sleep(50);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return "Data for " + key + " from DB";
    }
}

class CachingProxy implements DataService {
    private RealDataService realService;
    private Map<String, String> cache = new HashMap<>();

    public CachingProxy() {
        this.realService = new RealDataService();
    }

    @Override
    public String fetchData(String key) {
        if (cache.containsKey(key)) {
            System.out.println("  [CachingProxy] Returning cached data for: " + key);
            return cache.get(key);
        }

        String data = realService.fetchData(key);
        cache.put(key, data);
        System.out.println("  [CachingProxy] Data cached for: " + key);
        return data;
    }

    public void clearCache() {
        cache.clear();
        System.out.println("  [CachingProxy] Cache cleared");
    }
}

// Logging Proxy example

interface Calculator {
    int add(int a, int b);
    int subtract(int a, int b);
    int multiply(int a, int b);
    int divide(int a, int b);
}

class RealCalculator implements Calculator {
    @Override
    public int add(int a, int b) { return a + b; }

    @Override
    public int subtract(int a, int b) { return a - b; }

    @Override
    public int multiply(int a, int b) { return a * b; }

    @Override
    public int divide(int a, int b) { return a / b; }
}

class LoggingCalculatorProxy implements Calculator {
    private RealCalculator calculator = new RealCalculator();

    @Override
    public int add(int a, int b) {
        int result = calculator.add(a, b);
        System.out.println("  [Log] add(" + a + ", " + b + ") = " + result);
        return result;
    }

    @Override
    public int subtract(int a, int b) {
        int result = calculator.subtract(a, b);
        System.out.println("  [Log] subtract(" + a + ", " + b + ") = " + result);
        return result;
    }

    @Override
    public int multiply(int a, int b) {
        int result = calculator.multiply(a, b);
        System.out.println("  [Log] multiply(" + a + ", " + b + ") = " + result);
        return result;
    }

    @Override
    public int divide(int a, int b) {
        if (b == 0) {
            System.out.println("  [Log] divide(" + a + ", " + b + ") - Error: Division by zero!");
            throw new ArithmeticException("Division by zero");
        }
        int result = calculator.divide(a, b);
        System.out.println("  [Log] divide(" + a + ", " + b + ") = " + result);
        return result;
    }
}

// Remote Proxy simulation

interface RemoteService {
    String executeQuery(String query);
}

class RemoteServiceProxy implements RemoteService {
    private String serverAddress;

    public RemoteServiceProxy(String serverAddress) {
        this.serverAddress = serverAddress;
    }

    @Override
    public String executeQuery(String query) {
        System.out.println("  [RemoteProxy] Connecting to " + serverAddress);
        System.out.println("  [RemoteProxy] Sending query: " + query);
        // Simulate network call
        System.out.println("  [RemoteProxy] Waiting for response...");
        String result = "Result from " + serverAddress + " for query: " + query;
        System.out.println("  [RemoteProxy] Received response");
        return result;
    }
}

public class MainProxy {
    public static void main(String[] args) {
        System.out.println("=== Proxy Pattern Demonstration ===\n");

        // Virtual Proxy example
        System.out.println("--- 1. Virtual Proxy (Lazy Loading) ---");
        System.out.println("Creating image proxies (no loading yet):\n");

        Image image1 = new ProxyImage("photo1.jpg");
        Image image2 = new ProxyImage("photo2.jpg");
        Image image3 = new ProxyImage("photo3.jpg");

        System.out.println("\nFirst access to image1 (loads from disk):");
        image1.display();

        System.out.println("\nSecond access to image1 (already loaded):");
        image1.display();

        System.out.println("\nFirst access to image2:");
        image2.display();

        System.out.println("\nimage3 never accessed - never loaded!\n");

        // Protection Proxy example
        System.out.println("--- 2. Protection Proxy (Access Control) ---");

        System.out.println("\nAdmin user operations:");
        Document adminDoc = new ProtectedDocumentProxy("secret.txt", "admin");
        adminDoc.read();
        adminDoc.write("New admin content");
        adminDoc.delete();

        System.out.println("\nEditor user operations:");
        Document editorDoc = new ProtectedDocumentProxy("report.txt", "editor");
        editorDoc.read();
        editorDoc.write("Editor's content");
        editorDoc.delete();  // Should be denied

        System.out.println("\nViewer user operations:");
        Document viewerDoc = new ProtectedDocumentProxy("readme.txt", "viewer");
        viewerDoc.read();
        viewerDoc.write("Unauthorized edit");  // Should be denied
        viewerDoc.delete();  // Should be denied
        System.out.println();

        // Caching Proxy example
        System.out.println("--- 3. Caching Proxy ---");
        CachingProxy dataService = new CachingProxy();

        System.out.println("\nFirst fetch (cache miss):");
        String data1 = dataService.fetchData("user_123");
        System.out.println("  Result: " + data1);

        System.out.println("\nSecond fetch same key (cache hit):");
        String data2 = dataService.fetchData("user_123");
        System.out.println("  Result: " + data2);

        System.out.println("\nFetch different key (cache miss):");
        String data3 = dataService.fetchData("user_456");
        System.out.println("  Result: " + data3);
        System.out.println();

        // Logging Proxy example
        System.out.println("--- 4. Logging Proxy ---");
        Calculator calc = new LoggingCalculatorProxy();

        calc.add(10, 5);
        calc.subtract(10, 5);
        calc.multiply(10, 5);
        calc.divide(10, 5);
        System.out.println();

        // Remote Proxy example
        System.out.println("--- 5. Remote Proxy ---");
        RemoteService remoteDb = new RemoteServiceProxy("db.example.com:5432");
        String result = remoteDb.executeQuery("SELECT * FROM users");
        System.out.println("  Result: " + result);

        System.out.println("\n=== Summary ===");
        System.out.println("Proxy pattern types:");
        System.out.println("  - Virtual Proxy: lazy initialization, load on demand");
        System.out.println("  - Protection Proxy: access control based on permissions");
        System.out.println("  - Caching Proxy: cache results of expensive operations");
        System.out.println("  - Logging Proxy: log method calls and parameters");
        System.out.println("  - Remote Proxy: represent objects in different address spaces");
        System.out.println("\nKey benefits:");
        System.out.println("  - Control access to the real object");
        System.out.println("  - Add functionality without changing real object");
        System.out.println("  - Manage lifecycle of real object");
    }
}
