# Adapter Pattern

The Adapter pattern converts the interface of a class into another interface that clients expect. It lets classes work together that couldn't otherwise because of incompatible interfaces.

**Requires: Python 3.10+** (uses union types with `|` syntax)

## Key Components

- **Target**: The interface that clients use (`DataAnalyzer`)
- **Adaptee**: The existing interface that needs adapting (e.g., `LegacyXMLDataSystem`)
- **Adapter**: Converts the Adaptee interface to Target interface (e.g., `XMLDataAdapter`)
- **Client**: Collaborates with objects conforming to Target interface

## Source Code

### Target Interface (Lines 26-39)

```python:main_adapter.py startLine=26 endLine=39
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
```

### Adaptee Example - Legacy XML System (Lines 43-70)

```python:main_adapter.py startLine=43 endLine=70
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
```

### Adapter - XML to DataAnalyzer (Lines 128-164)

```python:main_adapter.py startLine=128 endLine=164
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
```

### Client Code (Lines 245-249)

```python:main_adapter.py startLine=245 endLine=249
def analyze_data(analyzer: DataAnalyzer, data: dict[str, Any]) -> None:
    """Client function that works with any DataAnalyzer."""
    analyzer.load_data(data)
    print(f"\nSummary: {json.dumps(analyzer.get_summary(), indent=2)}")
    print(f"Records: {json.dumps(analyzer.get_records(), indent=2)}")
```

## Program Output

```
============================================================
Adapter Pattern - Data Integration Demo
============================================================

Sample data to process:
{
  "records": [
    {
      "id": 1,
      "name": "Alice",
      "score": 95
    },
    {
      "id": 2,
      "name": "Bob",
      "score": 87
    },
    {
      "id": 3,
      "name": "Charlie",
      "score": 92
    }
  ]
}

--- Using XML Data Adapter ---

Summary: {
  "source": "XMLDataAdapter",
  "total_records": 3,
  "adapter_type": "Legacy XML System"
}
Records: [
  {
    "id": 1,
    "name": "Alice",
    "score": 95
  },
  {
    "id": 2,
    "name": "Bob",
    "score": 87
  },
  {
    "id": 3,
    "name": "Charlie",
    "score": 92
  }
]

--- Using CSV Data Adapter ---

Summary: {
  "source": "CSVDataAdapter",
  "total_records": 3,
  "columns": [
    "id",
    "name",
    "score"
  ],
  "adapter_type": "Third-party CSV Processor"
}
Records: [
  {
    "id": 1,
    "name": "Alice",
    "score": 95
  },
  {
    "id": 2,
    "name": "Bob",
    "score": 87
  },
  {
    "id": 3,
    "name": "Charlie",
    "score": 92
  }
]

--- Using API Data Adapter ---

Summary: {
  "source": "APIDataAdapter",
  "total_records": 3,
  "status": "success",
  "adapter_type": "External API Client"
}
Records: [
  {
    "id": 1,
    "name": "Alice",
    "score": 95
  },
  {
    "id": 2,
    "name": "Bob",
    "score": 87
  },
  {
    "id": 3,
    "name": "Charlie",
    "score": 92
  }
]

============================================================
Benefits of Adapter Pattern:
============================================================
1. Single Responsibility: separate interface conversion logic
2. Open/Closed: add new adapters without changing client
3. Reuse existing classes with incompatible interfaces
4. Flexibility to use multiple adaptees interchangeably
```

## Annotations

### How It Works

1. **Target Interface (Lines 26-39)**: The `DataAnalyzer` abstract class defines the interface that all our client code expects - `load_data()`, `get_records()`, and `get_summary()`.

2. **Adaptee Classes (Lines 43-124)**: Three legacy/third-party systems exist with incompatible interfaces:
   - `LegacyXMLDataSystem` uses `parse_xml()` and `get_xml_elements()`
   - `ThirdPartyCSVProcessor` uses `import_csv_data()` and `fetch_all_rows()`
   - `ExternalAPIClient` uses `set_response()` and `get_items()`

3. **Adapter Classes (Lines 128-241)**: Each adapter wraps an adaptee and implements the `DataAnalyzer` interface:
   - `XMLDataAdapter.load_data()` (Lines 134-144) converts the input dict to XML format before calling `parse_xml()`
   - `XMLDataAdapter.get_records()` (Lines 146-156) converts XML elements back to dicts
   - The same pattern applies for `CSVDataAdapter` and `APIDataAdapter`

4. **Client Code (Lines 245-249)**: The `analyze_data()` function accepts any `DataAnalyzer` and uses the uniform interface. It doesn't need to know about the underlying XML, CSV, or API implementations.

5. **Output Consistency**: All three adapters produce identical record output despite using completely different internal systems. The summary shows metadata specific to each adapter type while maintaining a consistent structure.

### Key Insight

The client code on lines 269-285 creates different adaptees and adapters but calls the same `analyze_data()` function for all. This demonstrates how the Adapter pattern enables incompatible interfaces to work together through a common target interface.
