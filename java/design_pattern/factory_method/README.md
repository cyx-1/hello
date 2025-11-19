# Factory Method Pattern

The Factory Method pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate.

## How to Run

```bash
cd java/factory_method
mvn compile exec:java
```

## Key Source Code

### Product Interface (Lines 13-18)
```java
interface Document {
    void open();
    void save();
    void close();
    String getType();
}
```

### Concrete Products (Lines 21-83)
```java
class PDFDocument implements Document {
    private String name;

    public PDFDocument(String name) {
        this.name = name;
        System.out.println("  [PDFDocument] Created PDF document: " + name);
    }

    @Override
    public void save() {
        System.out.println("  [PDFDocument] Saving PDF with compression: " + name);
    }
    // ...
}
```

### Abstract Creator with Factory Method (Lines 119-133)
```java
abstract class Application {
    // Factory method - subclasses must implement
    public abstract Document createDocument(String name);

    // Template method that uses the factory method
    public void newDocument(String name) {
        Document doc = createDocument(name);
        doc.open();
        System.out.println("  Document ready for editing...");
    }
}
```

### Concrete Creators (Lines 136-157)
```java
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
```

### Parameterized Factory (Lines 160-176)
```java
class DocumentFactory {
    public Document createDocument(String type, String name) {
        switch (type.toLowerCase()) {
            case "pdf":
                return new PDFDocument(name);
            case "word":
                return new WordDocument(name);
            // ...
        }
    }
}
```

## Program Output

```
=== Factory Method Pattern Demonstration ===

--- 1. Using Concrete Creator Classes ---

PDF Application:
  [PDFDocument] Created PDF document: report.pdf
  [PDFDocument] Opening PDF: report.pdf
  Document ready for editing...

Word Application:
  [WordDocument] Created Word document: letter.docx
  [WordDocument] Opening Word doc: letter.docx
  Document ready for editing...

Excel Application:
  [ExcelDocument] Created Excel spreadsheet: budget.xlsx
  [ExcelDocument] Opening Excel: budget.xlsx
  Document ready for editing...

Text Editor:
  [TextDocument] Created text file: notes.txt
  [TextDocument] Opening text file: notes.txt
  Document ready for editing...

--- 2. Parameterized Factory Method ---
  [PDFDocument] Created PDF document: invoice.pdf
  [PDFDocument] Opening PDF: invoice.pdf
  [PDFDocument] Saving PDF with compression: invoice.pdf
  [PDFDocument] Closing PDF: invoice.pdf

  [ExcelDocument] Created Excel spreadsheet: data.xlsx
  [ExcelDocument] Opening Excel: data.xlsx
  [ExcelDocument] Saving Excel with formulas: data.xlsx
  [ExcelDocument] Closing Excel: data.xlsx

--- 3. Registry-Based Factory ---
  [WordDocument] Created Word document: contract.docx
  [WordDocument] Opening Word doc: contract.docx
  [WordDocument] Saving Word doc with formatting: contract.docx
  [WordDocument] Closing Word doc: contract.docx

--- 4. Notification Factory Example ---
  [Email] Sending email: Your order has been shipped!
  [SMS] Sending SMS: Verification code: 123456
  [Push] Sending push notification: New message received
  [Slack] Sending Slack message: Build completed successfully

=== Summary ===
Factory Method pattern benefits:
  - Avoids tight coupling between creator and concrete products
  - Single Responsibility: product creation code in one place
  - Open/Closed: introduce new products without breaking existing code
  - Provides hooks for subclasses to extend
```

## Output Analysis

| Output Section | Source Code Reference | Explanation |
|----------------|----------------------|-------------|
| PDF Application | Lines 136-140 | PDFApplication overrides createDocument() |
| Document ready for editing | Line 128 | Template method uses factory-created document |
| Parameterized Factory | Lines 160-176 | Switch statement selects concrete class |
| Registry-Based Factory | Lines 179-195 | Reflection-based dynamic instantiation |
| Notification Factory | Lines 232-257 | Alternative example showing pattern versatility |

## Pattern Benefits

1. **Loose Coupling**: Creator doesn't need to know concrete product classes
2. **Single Responsibility**: Product creation logic isolated in factory
3. **Open/Closed Principle**: Add new products without changing existing code
4. **Polymorphism**: Different creators produce different products

## Factory Method vs Abstract Factory

| Aspect | Factory Method | Abstract Factory |
|--------|---------------|------------------|
| Purpose | Create one product | Create families of products |
| Implementation | Inheritance | Composition |
| Flexibility | Subclass per product | One factory per family |

## Requirements

- Java 17 or higher
- Maven 3.x
