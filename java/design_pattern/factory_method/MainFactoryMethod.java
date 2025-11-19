/**
 * Comprehensive demonstration of the Factory Method Pattern in Java
 *
 * The Factory Method pattern defines an interface for creating an object,
 * but lets subclasses decide which class to instantiate. It lets a class
 * defer instantiation to subclasses.
 */

import java.util.HashMap;
import java.util.Map;

// Product interface
interface Document {
    void open();
    void save();
    void close();
    String getType();
}

// Concrete Products
class PDFDocument implements Document {
    private String name;

    public PDFDocument(String name) {
        this.name = name;
        System.out.println("  [PDFDocument] Created PDF document: " + name);
    }

    @Override
    public void open() {
        System.out.println("  [PDFDocument] Opening PDF: " + name);
    }

    @Override
    public void save() {
        System.out.println("  [PDFDocument] Saving PDF with compression: " + name);
    }

    @Override
    public void close() {
        System.out.println("  [PDFDocument] Closing PDF: " + name);
    }

    @Override
    public String getType() {
        return "PDF";
    }
}

class WordDocument implements Document {
    private String name;

    public WordDocument(String name) {
        this.name = name;
        System.out.println("  [WordDocument] Created Word document: " + name);
    }

    @Override
    public void open() {
        System.out.println("  [WordDocument] Opening Word doc: " + name);
    }

    @Override
    public void save() {
        System.out.println("  [WordDocument] Saving Word doc with formatting: " + name);
    }

    @Override
    public void close() {
        System.out.println("  [WordDocument] Closing Word doc: " + name);
    }

    @Override
    public String getType() {
        return "Word";
    }
}

class ExcelDocument implements Document {
    private String name;

    public ExcelDocument(String name) {
        this.name = name;
        System.out.println("  [ExcelDocument] Created Excel spreadsheet: " + name);
    }

    @Override
    public void open() {
        System.out.println("  [ExcelDocument] Opening Excel: " + name);
    }

    @Override
    public void save() {
        System.out.println("  [ExcelDocument] Saving Excel with formulas: " + name);
    }

    @Override
    public void close() {
        System.out.println("  [ExcelDocument] Closing Excel: " + name);
    }

    @Override
    public String getType() {
        return "Excel";
    }
}

class TextDocument implements Document {
    private String name;

    public TextDocument(String name) {
        this.name = name;
        System.out.println("  [TextDocument] Created text file: " + name);
    }

    @Override
    public void open() {
        System.out.println("  [TextDocument] Opening text file: " + name);
    }

    @Override
    public void save() {
        System.out.println("  [TextDocument] Saving plain text: " + name);
    }

    @Override
    public void close() {
        System.out.println("  [TextDocument] Closing text file: " + name);
    }

    @Override
    public String getType() {
        return "Text";
    }
}

// Creator (Abstract class with factory method)
abstract class Application {
    // Factory method - subclasses must implement
    public abstract Document createDocument(String name);

    // Template method that uses the factory method
    public void newDocument(String name) {
        Document doc = createDocument(name);
        doc.open();
        System.out.println("  Document ready for editing...");
    }

    public void saveAndClose(String name) {
        Document doc = createDocument(name);
        doc.save();
        doc.close();
    }
}

// Concrete Creators
class PDFApplication extends Application {
    @Override
    public Document createDocument(String name) {
        return new PDFDocument(name);
    }
}

class WordApplication extends Application {
    @Override
    public Document createDocument(String name) {
        return new WordDocument(name);
    }
}

class ExcelApplication extends Application {
    @Override
    public Document createDocument(String name) {
        return new ExcelDocument(name);
    }
}

class TextEditorApplication extends Application {
    @Override
    public Document createDocument(String name) {
        return new TextDocument(name);
    }
}

// Parameterized Factory Method example
class DocumentFactory {
    public Document createDocument(String type, String name) {
        switch (type.toLowerCase()) {
            case "pdf":
                return new PDFDocument(name);
            case "word":
                return new WordDocument(name);
            case "excel":
                return new ExcelDocument(name);
            case "text":
                return new TextDocument(name);
            default:
                throw new IllegalArgumentException("Unknown document type: " + type);
        }
    }
}

// Registry-based Factory example
class DocumentRegistry {
    private Map<String, Class<? extends Document>> registry = new HashMap<>();

    public void registerDocument(String type, Class<? extends Document> documentClass) {
        registry.put(type.toLowerCase(), documentClass);
    }

    public Document createDocument(String type, String name) {
        Class<? extends Document> documentClass = registry.get(type.toLowerCase());
        if (documentClass == null) {
            throw new IllegalArgumentException("Unknown document type: " + type);
        }

        try {
            return documentClass.getConstructor(String.class).newInstance(name);
        } catch (Exception e) {
            throw new RuntimeException("Failed to create document", e);
        }
    }
}

// Another example: Notification Factory
interface Notification {
    void send(String message);
}

class EmailNotification implements Notification {
    @Override
    public void send(String message) {
        System.out.println("  [Email] Sending email: " + message);
    }
}

class SMSNotification implements Notification {
    @Override
    public void send(String message) {
        System.out.println("  [SMS] Sending SMS: " + message);
    }
}

class PushNotification implements Notification {
    @Override
    public void send(String message) {
        System.out.println("  [Push] Sending push notification: " + message);
    }
}

class SlackNotification implements Notification {
    @Override
    public void send(String message) {
        System.out.println("  [Slack] Sending Slack message: " + message);
    }
}

abstract class NotificationService {
    public abstract Notification createNotification();

    public void notifyUser(String message) {
        Notification notification = createNotification();
        notification.send(message);
    }
}

class EmailService extends NotificationService {
    @Override
    public Notification createNotification() {
        return new EmailNotification();
    }
}

class SMSService extends NotificationService {
    @Override
    public Notification createNotification() {
        return new SMSNotification();
    }
}

class PushService extends NotificationService {
    @Override
    public Notification createNotification() {
        return new PushNotification();
    }
}

class SlackService extends NotificationService {
    @Override
    public Notification createNotification() {
        return new SlackNotification();
    }
}

public class MainFactoryMethod {
    public static void main(String[] args) {
        System.out.println("=== Factory Method Pattern Demonstration ===\n");

        // Using concrete creators
        System.out.println("--- 1. Using Concrete Creator Classes ---");

        System.out.println("\nPDF Application:");
        Application pdfApp = new PDFApplication();
        pdfApp.newDocument("report.pdf");

        System.out.println("\nWord Application:");
        Application wordApp = new WordApplication();
        wordApp.newDocument("letter.docx");

        System.out.println("\nExcel Application:");
        Application excelApp = new ExcelApplication();
        excelApp.newDocument("budget.xlsx");

        System.out.println("\nText Editor:");
        Application textApp = new TextEditorApplication();
        textApp.newDocument("notes.txt");

        // Using parameterized factory
        System.out.println("\n--- 2. Parameterized Factory Method ---");
        DocumentFactory factory = new DocumentFactory();

        Document doc1 = factory.createDocument("pdf", "invoice.pdf");
        doc1.open();
        doc1.save();
        doc1.close();

        System.out.println();

        Document doc2 = factory.createDocument("excel", "data.xlsx");
        doc2.open();
        doc2.save();
        doc2.close();

        // Using registry-based factory
        System.out.println("\n--- 3. Registry-Based Factory ---");
        DocumentRegistry registry = new DocumentRegistry();
        registry.registerDocument("pdf", PDFDocument.class);
        registry.registerDocument("word", WordDocument.class);
        registry.registerDocument("excel", ExcelDocument.class);
        registry.registerDocument("text", TextDocument.class);

        Document regDoc = registry.createDocument("word", "contract.docx");
        regDoc.open();
        regDoc.save();
        regDoc.close();

        // Notification example
        System.out.println("\n--- 4. Notification Factory Example ---");

        NotificationService emailService = new EmailService();
        emailService.notifyUser("Your order has been shipped!");

        NotificationService smsService = new SMSService();
        smsService.notifyUser("Verification code: 123456");

        NotificationService pushService = new PushService();
        pushService.notifyUser("New message received");

        NotificationService slackService = new SlackService();
        slackService.notifyUser("Build completed successfully");

        System.out.println("\n=== Summary ===");
        System.out.println("Factory Method pattern benefits:");
        System.out.println("  - Avoids tight coupling between creator and concrete products");
        System.out.println("  - Single Responsibility: product creation code in one place");
        System.out.println("  - Open/Closed: introduce new products without breaking existing code");
        System.out.println("  - Provides hooks for subclasses to extend");
    }
}
