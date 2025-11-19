# Template Method Pattern

The Template Method pattern defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

## Key Components

- **AbstractClass**: Defines template method and abstract operations
- **ConcreteClass**: Implements the abstract operations

## Key Source Code

### Abstract Class with Template Method

```python:main_template_method.py startLine=22 endLine=74
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
```

### Concrete Implementation (CSVDataMiner)

```python:main_template_method.py startLine=77 endLine=112
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
```

### Hook Method Override (JSONDataMiner)

```python:main_template_method.py startLine=114 endLine=135
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
```

## Program Output

```
============================================================
Template Method Pattern - Data Mining Demo
============================================================

--- CSV Data Mining ---
  [CSVMiner] Extracting data from data/users.csv
  [CSVMiner] Parsing CSV data
  [CSVMiner] Analyzing CSV data
Result: 3 records
Average age: 30.0

--- JSON Data Mining ---
  [JSONMiner] Extracting data from data/users.json
  [JSONMiner] Parsing JSON data
  [JSONMiner] Sending webhook notification
Result: 3 records

--- XML Data Mining ---
  [XMLMiner] Extracting data from data/users.xml
  [XMLMiner] Parsing XML data
Result: 3 records

--- Database Mining ---
  [DBMiner] Connecting to database: postgresql://localhost/users
  [DBMiner] Parsing query results
  [DBMiner] Running database-specific analysis
Result: 3 records
By city: {'New York': 1, 'Los Angeles': 1, 'Chicago': 1}

============================================================
Template Method Pattern - Report Generation Demo
============================================================

--- Text Report ---
========================================
USER REPORT
========================================
1. name: Alice, age: 30, city: New York
2. name: Bob, age: 25, city: Los Angeles
3. name: Charlie, age: 35, city: Chicago
Generated on 2025-11-18 23:52

--- HTML Report ---
<html><head><title>User Report</title></head><body><h1>User Report</h1>
<table border='1'><tr><th>name</th><th>age</th><th>city</th></tr><tr><td>Alice</td><td>30</td><td>New York</td></tr><tr><td>Bob</td><td>25</td><td>Los Angeles</td></tr><tr><td>Charlie</td><td>35</td><td>Chicago</td></tr></table>
<footer>Generated on 2025-11-18 23:52</footer></body></html>

--- Markdown Report ---
# User Report

| name | age | city |
| --- | --- | --- |
| Alice | 30 | New York |
| Bob | 25 | Los Angeles |
| Charlie | 35 | Chicago |
Generated on 2025-11-18 23:52

============================================================
Benefits of Template Method Pattern:
============================================================
1. Defines algorithm skeleton in one place
2. Subclasses can override specific steps
3. Promotes code reuse
4. Controls extension points via hooks
5. Follows Hollywood Principle: 'Don't call us, we'll call you'
```

## Output Annotations

- **Lines 5-10**: CSV mining follows template method `mine()` (lines 28-42) - extract, parse, analyze steps. CSVMiner overrides `analyze_data()` (lines 101-111) to add average_age calculation
- **Lines 12-16**: JSON mining uses same template but different implementations. Note "Sending webhook notification" - JSONMiner overrides hook method `send_notifications()` (lines 132-134)
- **Lines 18-21**: XML mining shows minimal implementation - only required abstract methods, uses default analyze and no notifications
- **Lines 23-27**: Database mining overrides `analyze_data()` (lines 182-193) to add city grouping, demonstrating how subclasses can extend default behavior
- **Lines 31-38**: Text report uses `TextReport.create_header()` (lines 224-225) for uppercase title with borders and `create_body()` (lines 227-235) for numbered list format
- **Lines 40-43**: HTML report generates table structure via `HTMLReport.create_body()` (lines 244-264) and custom footer (lines 266-268)
- **Lines 45-52**: Markdown report creates table with `|` separators and `---` header dividers (lines 277-293)

## Requirements

- Python 3.10+ (uses type hints with `dict[str, dict]`)

## Running the Example

```bash
uv run python main_template_method.py
```
