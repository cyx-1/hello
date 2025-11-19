# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Adapter Pattern

The Adapter pattern converts the interface of a class into another interface
that clients expect. It lets classes work together that couldn't otherwise
because of incompatible interfaces.

Key Components:
- Target: The interface that clients use
- Adaptee: The existing interface that needs adapting
- Adapter: Converts the Adaptee interface to Target interface
- Client: Collaborates with objects conforming to Target interface
"""

from abc import ABC, abstractmethod
import json
import xml.etree.ElementTree as ET
from typing import Any


# Target interface - what our application expects
class DataAnalyzer(ABC):
    """Target interface for data analysis."""

    @abstractmethod
    def load_data(self, data: dict[str, Any]) -> None:
        pass

    @abstractmethod
    def get_records(self) -> list[dict[str, Any]]:
        pass

    @abstractmethod
    def get_summary(self) -> dict[str, Any]:
        pass


# Adaptee 1: Legacy XML data system
class LegacyXMLDataSystem:
    """Legacy system that only works with XML data."""

    def __init__(self):
        self._xml_data: str = ""
        self._root: ET.Element | None = None

    def parse_xml(self, xml_string: str) -> None:
        """Parse XML data."""
        self._xml_data = xml_string
        self._root = ET.fromstring(xml_string)

    def get_xml_elements(self) -> list[ET.Element]:
        """Get all record elements."""
        if self._root is None:
            return []
        return list(self._root.findall(".//record"))

    def count_elements(self) -> int:
        """Count total elements."""
        return len(self.get_xml_elements())

    def get_element_attributes(self, element: ET.Element) -> dict[str, str]:
        """Get attributes of an element."""
        result = dict(element.attrib)
        for child in element:
            result[child.tag] = child.text or ""
        return result


# Adaptee 2: Third-party CSV processor
class ThirdPartyCSVProcessor:
    """Third-party library for CSV processing."""

    def __init__(self):
        self._headers: list[str] = []
        self._rows: list[list[str]] = []

    def import_csv_data(self, headers: list[str], rows: list[list[str]]) -> None:
        """Import CSV data."""
        self._headers = headers
        self._rows = rows

    def fetch_row(self, index: int) -> list[str]:
        """Fetch a specific row."""
        return self._rows[index] if 0 <= index < len(self._rows) else []

    def fetch_all_rows(self) -> list[list[str]]:
        """Fetch all rows."""
        return self._rows.copy()

    def get_column_names(self) -> list[str]:
        """Get column names."""
        return self._headers.copy()

    def row_count(self) -> int:
        """Get row count."""
        return len(self._rows)


# Adaptee 3: External API client
class ExternalAPIClient:
    """External API that returns data in a specific format."""

    def __init__(self):
        self._response: dict[str, Any] = {}

    def set_response(self, response: dict[str, Any]) -> None:
        """Simulate API response."""
        self._response = response

    def fetch_paginated_results(self) -> dict[str, Any]:
        """Fetch results with pagination info."""
        return self._response

    def get_metadata(self) -> dict[str, Any]:
        """Get response metadata."""
        return self._response.get("meta", {})

    def get_items(self) -> list[dict[str, Any]]:
        """Get data items."""
        return self._response.get("data", {}).get("items", [])


# Adapter 1: XML to DataAnalyzer
class XMLDataAdapter(DataAnalyzer):
    """Adapter that makes LegacyXMLDataSystem work with DataAnalyzer interface."""

    def __init__(self, xml_system: LegacyXMLDataSystem):
        self._xml_system = xml_system

    def load_data(self, data: dict[str, Any]) -> None:
        """Convert dict to XML and load into legacy system."""
        # Convert dict to XML format
        root = ET.Element("data")
        for record in data.get("records", []):
            record_elem = ET.SubElement(root, "record")
            for key, value in record.items():
                child = ET.SubElement(record_elem, key)
                child.text = str(value)
        xml_string = ET.tostring(root, encoding="unicode")
        self._xml_system.parse_xml(xml_string)

    def get_records(self) -> list[dict[str, Any]]:
        """Convert XML elements to list of dicts."""
        records = []
        for element in self._xml_system.get_xml_elements():
            record = self._xml_system.get_element_attributes(element)
            # Convert numeric strings back to numbers
            for key, value in record.items():
                if value.isdigit():
                    record[key] = int(value)
            records.append(record)
        return records

    def get_summary(self) -> dict[str, Any]:
        """Generate summary from XML data."""
        return {
            "source": "XMLDataAdapter",
            "total_records": self._xml_system.count_elements(),
            "adapter_type": "Legacy XML System",
        }


# Adapter 2: CSV to DataAnalyzer
class CSVDataAdapter(DataAnalyzer):
    """Adapter that makes ThirdPartyCSVProcessor work with DataAnalyzer interface."""

    def __init__(self, csv_processor: ThirdPartyCSVProcessor):
        self._csv_processor = csv_processor

    def load_data(self, data: dict[str, Any]) -> None:
        """Convert dict to CSV format and load."""
        records = data.get("records", [])
        if not records:
            self._csv_processor.import_csv_data([], [])
            return

        headers = list(records[0].keys())
        rows = [[str(record.get(h, "")) for h in headers] for record in records]
        self._csv_processor.import_csv_data(headers, rows)

    def get_records(self) -> list[dict[str, Any]]:
        """Convert CSV rows to list of dicts."""
        headers = self._csv_processor.get_column_names()
        records = []
        for row in self._csv_processor.fetch_all_rows():
            record: dict[str, Any] = {}
            for i, header in enumerate(headers):
                value = row[i] if i < len(row) else ""
                # Convert numeric strings back to numbers
                if value.isdigit():
                    record[header] = int(value)
                else:
                    record[header] = value
            records.append(record)
        return records

    def get_summary(self) -> dict[str, Any]:
        """Generate summary from CSV data."""
        return {
            "source": "CSVDataAdapter",
            "total_records": self._csv_processor.row_count(),
            "columns": self._csv_processor.get_column_names(),
            "adapter_type": "Third-party CSV Processor",
        }


# Adapter 3: API to DataAnalyzer
class APIDataAdapter(DataAnalyzer):
    """Adapter that makes ExternalAPIClient work with DataAnalyzer interface."""

    def __init__(self, api_client: ExternalAPIClient):
        self._api_client = api_client

    def load_data(self, data: dict[str, Any]) -> None:
        """Convert dict to API response format and set."""
        api_response = {
            "meta": {
                "status": "success",
                "count": len(data.get("records", [])),
            },
            "data": {"items": data.get("records", [])},
        }
        self._api_client.set_response(api_response)

    def get_records(self) -> list[dict[str, Any]]:
        """Get records from API response."""
        return self._api_client.get_items()

    def get_summary(self) -> dict[str, Any]:
        """Generate summary from API response."""
        metadata = self._api_client.get_metadata()
        return {
            "source": "APIDataAdapter",
            "total_records": metadata.get("count", 0),
            "status": metadata.get("status", "unknown"),
            "adapter_type": "External API Client",
        }


# Client code
def analyze_data(analyzer: DataAnalyzer, data: dict[str, Any]) -> None:
    """Client function that works with any DataAnalyzer."""
    analyzer.load_data(data)
    print(f"\nSummary: {json.dumps(analyzer.get_summary(), indent=2)}")
    print(f"Records: {json.dumps(analyzer.get_records(), indent=2)}")


def main() -> None:
    print("=" * 60)
    print("Adapter Pattern - Data Integration Demo")
    print("=" * 60)

    # Sample data to process
    sample_data = {
        "records": [
            {"id": 1, "name": "Alice", "score": 95},
            {"id": 2, "name": "Bob", "score": 87},
            {"id": 3, "name": "Charlie", "score": 92},
        ]
    }

    print("\nSample data to process:")
    print(json.dumps(sample_data, indent=2))

    # Demo 1: Using XML adapter
    print("\n--- Using XML Data Adapter ---")
    xml_system = LegacyXMLDataSystem()
    xml_adapter = XMLDataAdapter(xml_system)
    analyze_data(xml_adapter, sample_data)

    # Demo 2: Using CSV adapter
    print("\n--- Using CSV Data Adapter ---")
    csv_processor = ThirdPartyCSVProcessor()
    csv_adapter = CSVDataAdapter(csv_processor)
    analyze_data(csv_adapter, sample_data)

    # Demo 3: Using API adapter
    print("\n--- Using API Data Adapter ---")
    api_client = ExternalAPIClient()
    api_adapter = APIDataAdapter(api_client)
    analyze_data(api_adapter, sample_data)

    print("\n" + "=" * 60)
    print("Benefits of Adapter Pattern:")
    print("=" * 60)
    print("1. Single Responsibility: separate interface conversion logic")
    print("2. Open/Closed: add new adapters without changing client")
    print("3. Reuse existing classes with incompatible interfaces")
    print("4. Flexibility to use multiple adaptees interchangeably")


if __name__ == "__main__":
    main()
