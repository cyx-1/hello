# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Factory Method Pattern

The Factory Method pattern defines an interface for creating an object, but lets
subclasses decide which class to instantiate. It lets a class defer instantiation
to subclasses.

Key Components:
- Product: Defines the interface of objects the factory method creates
- ConcreteProduct: Implements the Product interface
- Creator: Declares the factory method that returns a Product object
- ConcreteCreator: Overrides factory method to return a ConcreteProduct instance
"""

from abc import ABC, abstractmethod
from datetime import datetime


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


class MarkdownDocument(Document):
    """Concrete product for Markdown documents."""

    def get_type(self) -> str:
        return "Markdown Document"

    def get_extension(self) -> str:
        return ".md"

    def render(self) -> str:
        return f"# Document\n\n{self.get_content()}"


class PlainTextDocument(Document):
    """Concrete product for plain text documents."""

    def get_type(self) -> str:
        return "Plain Text Document"

    def get_extension(self) -> str:
        return ".txt"

    def render(self) -> str:
        return self.get_content()


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


def main() -> None:
    print("=" * 60)
    print("Factory Method Pattern - Document Creation Demo")
    print("=" * 60)

    # Demo 1: Using concrete creators
    print("\n--- Using Concrete Creators ---")
    creators: list[DocumentCreator] = [
        PDFCreator(),
        HTMLCreator(),
        MarkdownCreator(),
        PlainTextCreator(),
    ]

    for creator in creators:
        doc = creator.new_document("Hello, Factory Method!")
        print(f"\n{doc.get_type()} ({doc.get_extension()}):")
        print("-" * 40)
        print(doc.render()[:200] + "..." if len(doc.render()) > 200 else doc.render())

    # Demo 2: Using factory to generate reports
    print("\n\n--- Generating Reports ---")
    html_creator = HTMLCreator()
    report = html_creator.generate_report(
        "Quarterly Sales",
        ["Revenue increased by 15%", "New customers: 250", "Retention rate: 92%"],
    )
    print(f"\n{report.get_type()} Report:")
    print(report.render())

    # Demo 3: Using parameterized factory
    print("\n--- Using Parameterized Factory ---")
    for doc_type in ["pdf", "html", "markdown", "text"]:
        doc = DocumentFactory.create(doc_type)
        doc.add_content("Created via parameterized factory")
        print(f"Created: {doc.get_type()}")

    # Demo 4: Registering custom document type
    print("\n--- Registering Custom Document Type ---")

    class XMLDocument(Document):
        def get_type(self) -> str:
            return "XML Document"

        def get_extension(self) -> str:
            return ".xml"

        def render(self) -> str:
            return f'<?xml version="1.0"?>\n<document>{self.get_content()}</document>'

    DocumentFactory.register("xml", XMLDocument)
    xml_doc = DocumentFactory.create("xml")
    xml_doc.add_content("Custom XML content")
    print(f"Created: {xml_doc.get_type()}")
    print(xml_doc.render())

    print("\n" + "=" * 60)
    print("Benefits of Factory Method Pattern:")
    print("=" * 60)
    print("1. Decouples client code from concrete product classes")
    print("2. Single Responsibility: creation code in one place")
    print("3. Open/Closed: add new products without modifying client")
    print("4. Provides hooks for subclasses to extend")


if __name__ == "__main__":
    main()
