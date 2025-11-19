# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Template Method Pattern

The Template Method pattern defines the skeleton of an algorithm in the
superclass but lets subclasses override specific steps of the algorithm
without changing its structure.

Key Components:
- AbstractClass: Defines template method and abstract operations
- ConcreteClass: Implements the abstract operations
"""

from abc import ABC, abstractmethod
from datetime import datetime


# Abstract Class with Template Method
class DataMiner(ABC):
    """
    Abstract class that defines the template method for data mining.
    The template method defines the algorithm's skeleton.
    """

    def mine(self, path: str) -> dict:
        """
        Template method - defines the algorithm skeleton.
        Subclasses cannot override this method.
        """
        # Fixed sequence of steps
        raw_data = self.extract_data(path)
        parsed_data = self.parse_data(raw_data)
        analyzed_data = self.analyze_data(parsed_data)
        report = self.generate_report(analyzed_data)

        # Hook methods - optional extensions
        self.send_notifications(report)

        return report

    @abstractmethod
    def extract_data(self, path: str) -> str:
        """Extract data from source - must be implemented by subclasses."""
        pass

    @abstractmethod
    def parse_data(self, raw_data: str) -> list[dict]:
        """Parse raw data into structured format - must be implemented."""
        pass

    def analyze_data(self, data: list[dict]) -> dict:
        """
        Analyze data - default implementation, can be overridden.
        """
        return {
            "record_count": len(data),
            "data": data,
        }

    def generate_report(self, analysis: dict) -> dict:
        """Generate report - default implementation, can be overridden."""
        return {
            "timestamp": datetime.now().isoformat(),
            "source_type": self.__class__.__name__,
            "analysis": analysis,
        }

    def send_notifications(self, report: dict) -> None:
        """Hook method - empty by default, can be overridden."""
        pass


# Concrete Classes
class CSVDataMiner(DataMiner):
    """Concrete class for mining CSV data."""

    def extract_data(self, path: str) -> str:
        print(f"  [CSVMiner] Extracting data from {path}")
        # Simulate reading CSV file
        return """name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago"""

    def parse_data(self, raw_data: str) -> list[dict]:
        print("  [CSVMiner] Parsing CSV data")
        lines = raw_data.strip().split("\n")
        headers = lines[0].split(",")
        result = []

        for line in lines[1:]:
            values = line.split(",")
            record = dict(zip(headers, values))
            result.append(record)

        return result

    def analyze_data(self, data: list[dict]) -> dict:
        print("  [CSVMiner] Analyzing CSV data")
        analysis = super().analyze_data(data)

        # Add CSV-specific analysis
        if data:
            ages = [int(d.get("age", 0)) for d in data if d.get("age", "").isdigit()]
            if ages:
                analysis["average_age"] = sum(ages) / len(ages)

        return analysis


class JSONDataMiner(DataMiner):
    """Concrete class for mining JSON data."""

    def extract_data(self, path: str) -> str:
        print(f"  [JSONMiner] Extracting data from {path}")
        # Simulate reading JSON file
        return '''[
            {"name": "Alice", "age": 30, "city": "New York"},
            {"name": "Bob", "age": 25, "city": "Los Angeles"},
            {"name": "Charlie", "age": 35, "city": "Chicago"}
        ]'''

    def parse_data(self, raw_data: str) -> list[dict]:
        print("  [JSONMiner] Parsing JSON data")
        import json

        return json.loads(raw_data)

    def send_notifications(self, report: dict) -> None:
        """Override hook to send notifications for JSON mining."""
        print("  [JSONMiner] Sending webhook notification")


class XMLDataMiner(DataMiner):
    """Concrete class for mining XML data."""

    def extract_data(self, path: str) -> str:
        print(f"  [XMLMiner] Extracting data from {path}")
        return """<people>
    <person><name>Alice</name><age>30</age><city>New York</city></person>
    <person><name>Bob</name><age>25</age><city>Los Angeles</city></person>
    <person><name>Charlie</name><age>35</age><city>Chicago</city></person>
</people>"""

    def parse_data(self, raw_data: str) -> list[dict]:
        print("  [XMLMiner] Parsing XML data")
        import xml.etree.ElementTree as ET

        root = ET.fromstring(raw_data)
        result = []

        for person in root.findall("person"):
            record = {}
            for child in person:
                record[child.tag] = child.text
            result.append(record)

        return result


class DatabaseMiner(DataMiner):
    """Concrete class for mining database data."""

    def extract_data(self, path: str) -> str:
        print(f"  [DBMiner] Connecting to database: {path}")
        # Simulate database query result
        return "Alice|30|New York\nBob|25|Los Angeles\nCharlie|35|Chicago"

    def parse_data(self, raw_data: str) -> list[dict]:
        print("  [DBMiner] Parsing query results")
        result = []
        for line in raw_data.strip().split("\n"):
            parts = line.split("|")
            result.append(
                {"name": parts[0], "age": parts[1], "city": parts[2]}
            )
        return result

    def analyze_data(self, data: list[dict]) -> dict:
        print("  [DBMiner] Running database-specific analysis")
        analysis = super().analyze_data(data)

        # Group by city
        cities: dict[str, int] = {}
        for record in data:
            city = record.get("city", "Unknown")
            cities[city] = cities.get(city, 0) + 1

        analysis["by_city"] = cities
        return analysis


# Report Generator example
class ReportGenerator(ABC):
    """Abstract class for generating reports."""

    def generate(self, title: str, data: list[dict]) -> str:
        """Template method for report generation."""
        report = []
        report.append(self.create_header(title))
        report.append(self.create_body(data))
        report.append(self.create_footer())
        return "\n".join(report)

    @abstractmethod
    def create_header(self, title: str) -> str:
        pass

    @abstractmethod
    def create_body(self, data: list[dict]) -> str:
        pass

    def create_footer(self) -> str:
        """Default footer - can be overridden."""
        return f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}"


class TextReport(ReportGenerator):
    """Generate plain text reports."""

    def create_header(self, title: str) -> str:
        return f"{'=' * 40}\n{title.upper()}\n{'=' * 40}"

    def create_body(self, data: list[dict]) -> str:
        if not data:
            return "No data available"

        lines = []
        for i, record in enumerate(data, 1):
            items = [f"{k}: {v}" for k, v in record.items()]
            lines.append(f"{i}. {', '.join(items)}")
        return "\n".join(lines)


class HTMLReport(ReportGenerator):
    """Generate HTML reports."""

    def create_header(self, title: str) -> str:
        return f"<html><head><title>{title}</title></head><body><h1>{title}</h1>"

    def create_body(self, data: list[dict]) -> str:
        if not data:
            return "<p>No data available</p>"

        html = ["<table border='1'>"]

        # Header row
        html.append("<tr>")
        for key in data[0].keys():
            html.append(f"<th>{key}</th>")
        html.append("</tr>")

        # Data rows
        for record in data:
            html.append("<tr>")
            for value in record.values():
                html.append(f"<td>{value}</td>")
            html.append("</tr>")

        html.append("</table>")
        return "".join(html)

    def create_footer(self) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        return f"<footer>Generated on {timestamp}</footer></body></html>"


class MarkdownReport(ReportGenerator):
    """Generate Markdown reports."""

    def create_header(self, title: str) -> str:
        return f"# {title}\n"

    def create_body(self, data: list[dict]) -> str:
        if not data:
            return "*No data available*"

        md = []

        # Header row
        headers = list(data[0].keys())
        md.append("| " + " | ".join(headers) + " |")
        md.append("| " + " | ".join(["---"] * len(headers)) + " |")

        # Data rows
        for record in data:
            values = [str(v) for v in record.values()]
            md.append("| " + " | ".join(values) + " |")

        return "\n".join(md)


def main() -> None:
    print("=" * 60)
    print("Template Method Pattern - Data Mining Demo")
    print("=" * 60)

    # Demo 1: Different data miners using same template
    print("\n--- CSV Data Mining ---")
    csv_miner = CSVDataMiner()
    result = csv_miner.mine("data/users.csv")
    print(f"Result: {result['analysis']['record_count']} records")
    if "average_age" in result["analysis"]:
        print(f"Average age: {result['analysis']['average_age']:.1f}")

    print("\n--- JSON Data Mining ---")
    json_miner = JSONDataMiner()
    result = json_miner.mine("data/users.json")
    print(f"Result: {result['analysis']['record_count']} records")

    print("\n--- XML Data Mining ---")
    xml_miner = XMLDataMiner()
    result = xml_miner.mine("data/users.xml")
    print(f"Result: {result['analysis']['record_count']} records")

    print("\n--- Database Mining ---")
    db_miner = DatabaseMiner()
    result = db_miner.mine("postgresql://localhost/users")
    print(f"Result: {result['analysis']['record_count']} records")
    print(f"By city: {result['analysis']['by_city']}")

    # Demo 2: Report generators
    print("\n" + "=" * 60)
    print("Template Method Pattern - Report Generation Demo")
    print("=" * 60)

    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"},
    ]

    print("\n--- Text Report ---")
    text_gen = TextReport()
    print(text_gen.generate("User Report", sample_data))

    print("\n--- HTML Report ---")
    html_gen = HTMLReport()
    print(html_gen.generate("User Report", sample_data))

    print("\n--- Markdown Report ---")
    md_gen = MarkdownReport()
    print(md_gen.generate("User Report", sample_data))

    print("\n" + "=" * 60)
    print("Benefits of Template Method Pattern:")
    print("=" * 60)
    print("1. Defines algorithm skeleton in one place")
    print("2. Subclasses can override specific steps")
    print("3. Promotes code reuse")
    print("4. Controls extension points via hooks")
    print("5. Follows Hollywood Principle: 'Don't call us, we'll call you'")


if __name__ == "__main__":
    main()
