# Factory Method Pattern

The Factory Method pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. It lets a class defer instantiation to subclasses, promoting loose coupling between client code and concrete product classes.

**Requires: Python 3.10+** (for `list[str]` type hints, `dict[str, type]` syntax, and modern ABC features)

## Key Components

- **Product** (`Document`): Defines the interface of objects the factory method creates
- **ConcreteProduct** (`PDFDocument`, `HTMLDocument`, `MarkdownDocument`, `PlainTextDocument`): Implements the Product interface
- **Creator** (`DocumentCreator`): Declares the factory method that returns a Product object
- **ConcreteCreator** (`PDFCreator`, `HTMLCreator`, etc.): Overrides factory method to return a ConcreteProduct instance

## Source Code Highlights

### Abstract Product - Document Interface

```python:main_factory_method.py startLine=23 endLine=47
# Product interface
class Document(ABC):
    """Abstract product representing a document."""

    def __init__(self):
        self.content: list[str] = []
        self.created_at = datetime.now()

    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def get_extension(self) -> str:
        pass

    def add_content(self, text: str) -> None:
        self.content.append(text)

    def get_content(self) -> str:
        return "\n".join(self.content)

    @abstractmethod
    def render(self) -> str:
        pass
```

### Concrete Products - Document Implementations

```python:main_factory_method.py startLine=50 endLine=84
# Concrete Products
class PDFDocument(Document):
    """Concrete product for PDF documents."""

    def get_type(self) -> str:
        return "PDF Document"

    def get_extension(self) -> str:
        return ".pdf"

    def render(self) -> str:
        header = "%PDF-1.4\n"
        body = self.get_content()
        return f"{header}[PDF Binary Content]\n{body}\n%%EOF"


class HTMLDocument(Document):
    """Concrete product for HTML documents."""

    def get_type(self) -> str:
        return "HTML Document"

    def get_extension(self) -> str:
        return ".html"

    def render(self) -> str:
        content = self.get_content().replace("\n", "<br>\n")
        return f"""<!DOCTYPE html>
<html>
<head><title>Document</title></head>
<body>
{content}
</body>
</html>"""
```

### Abstract Creator - Declares Factory Method

```python:main_factory_method.py startLine=112 endLine=136
# Creator (abstract class with factory method)
class DocumentCreator(ABC):
    """Abstract creator that declares the factory method."""

    @abstractmethod
    def create_document(self) -> Document:
        """Factory method - subclasses must implement this."""
        pass

    def new_document(self, content: str) -> Document:
        """Template method that uses the factory method."""
        doc = self.create_document()
        doc.add_content(content)
        return doc

    def generate_report(self, title: str, sections: list[str]) -> Document:
        """Higher-level operation using the factory method."""
        doc = self.create_document()
        doc.add_content(f"Report: {title}")
        doc.add_content("-" * 40)
        for i, section in enumerate(sections, 1):
            doc.add_content(f"{i}. {section}")
        doc.add_content("-" * 40)
        doc.add_content(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return doc
```

### Concrete Creators - Implement Factory Method

```python:main_factory_method.py startLine=139 endLine=165
# Concrete Creators
class PDFCreator(DocumentCreator):
    """Concrete creator for PDF documents."""

    def create_document(self) -> Document:
        return PDFDocument()


class HTMLCreator(DocumentCreator):
    """Concrete creator for HTML documents."""

    def create_document(self) -> Document:
        return HTMLDocument()


class MarkdownCreator(DocumentCreator):
    """Concrete creator for Markdown documents."""

    def create_document(self) -> Document:
        return MarkdownDocument()


class PlainTextCreator(DocumentCreator):
    """Concrete creator for plain text documents."""

    def create_document(self) -> Document:
        return PlainTextDocument()
```

### Parameterized Factory - Alternative Approach

```python:main_factory_method.py startLine=168 endLine=190
# Parameterized Factory Method (alternative approach)
class DocumentFactory:
    """A parameterized factory that creates documents based on type."""

    _creators: dict[str, type[Document]] = {
        "pdf": PDFDocument,
        "html": HTMLDocument,
        "markdown": MarkdownDocument,
        "text": PlainTextDocument,
    }

    @classmethod
    def register(cls, doc_type: str, creator: type[Document]) -> None:
        """Register a new document type."""
        cls._creators[doc_type.lower()] = creator

    @classmethod
    def create(cls, doc_type: str) -> Document:
        """Create a document of the specified type."""
        creator = cls._creators.get(doc_type.lower())
        if creator is None:
            raise ValueError(f"Unknown document type: {doc_type}")
        return creator()
```

## Program Output

```
============================================================
Factory Method Pattern - Document Creation Demo
============================================================

--- Using Concrete Creators ---

PDF Document (.pdf):
----------------------------------------
%PDF-1.4
[PDF Binary Content]
Hello, Factory Method!
%%EOF

HTML Document (.html):
----------------------------------------
<!DOCTYPE html>
<html>
<head><title>Document</title></head>
<body>
Hello, Factory Method!
</body>
</html>

Markdown Document (.md):
----------------------------------------
# Document

Hello, Factory Method!

Plain Text Document (.txt):
----------------------------------------
Hello, Factory Method!


--- Generating Reports ---

HTML Document Report:
<!DOCTYPE html>
<html>
<head><title>Document</title></head>
<body>
Report: Quarterly Sales<br>
----------------------------------------<br>
1. Revenue increased by 15%<br>
2. New customers: 250<br>
3. Retention rate: 92%<br>
----------------------------------------<br>
Generated: 2025-11-18 23:52:16
</body>
</html>

--- Using Parameterized Factory ---
Created: PDF Document
Created: HTML Document
Created: Markdown Document
Created: Plain Text Document

--- Registering Custom Document Type ---
Created: XML Document
<?xml version="1.0"?>
<document>Custom XML content</document>

============================================================
Benefits of Factory Method Pattern:
============================================================
1. Decouples client code from concrete product classes
2. Single Responsibility: creation code in one place
3. Open/Closed: add new products without modifying client
4. Provides hooks for subclasses to extend
```

## Output Annotations

1. **Lines 200-211** - Demo 1 creates a list of concrete creators and calls `new_document()` on each. The `new_document()` template method (lines 121-125) internally calls the abstract `create_document()` factory method, which each concrete creator overrides to return the appropriate document type.

2. **Lines 60-63** - The PDF output shows the `render()` implementation: `%PDF-1.4` header, `[PDF Binary Content]` placeholder, content, and `%%EOF` marker.

3. **Lines 75-83** - The HTML output shows the full HTML structure with `<!DOCTYPE html>`, tags, and content wrapped in the body.

4. **Lines 127-136** - The `generate_report()` method demonstrates how the factory method enables higher-level operations. It creates a document (via the factory method), then adds structured content including title, sections, and timestamp.

5. **Lines 215-221** - The report generation uses `HTMLCreator`, so all the report content gets formatted as HTML with `<br>` tags (see line 76 where `\n` is replaced).

6. **Lines 224-228** - Demo 3 shows the parameterized factory approach using `DocumentFactory.create()` (lines 184-190), which uses a dictionary to map type strings to concrete classes.

7. **Lines 233-247** - Demo 4 shows runtime extensibility: a new `XMLDocument` class is defined and registered with `DocumentFactory.register()` (line 180), then immediately usable via the factory.

## Design Insights

- **Template Method Integration**: The `new_document()` and `generate_report()` methods are template methods that rely on the factory method `create_document()`. This shows how Factory Method often works with Template Method.

- **Two Approaches**: The code demonstrates both the classic inheritance-based factory method (concrete creators) and a simpler parameterized factory (dictionary-based). Choose based on whether you need polymorphic behavior in the creator.

- **Open/Closed Principle**: Adding new document types (like XMLDocument) doesn't require modifying existing code - just create a new class and register it.

## Running the Code

```bash
uv run python main_factory_method.py
```
