# Template Method Pattern

Defines the skeleton of an algorithm in a method, deferring some steps to subclasses.

## How to Run
```bash
cd java/template_method
mvn compile exec:java
```

## Key Source Code

### Template Method (Lines 9-19)
```java
abstract class DataMiner {
    // Template method - defines algorithm skeleton
    public final void mine(String path) {
        openFile(path);
        extractData();
        parseData();
        analyzeData();
        sendReport();
        closeFile();
    }

    protected abstract void openFile(String path);
    protected abstract void extractData();

    // Hook - optional override
    protected void analyzeData() {
        System.out.println("Performing standard analysis");
    }
}
```

### Concrete Implementation (Lines 38-58)
```java
class CSVDataMiner extends DataMiner {
    @Override
    protected void openFile(String path) {
        System.out.println("Opening CSV file: " + path);
    }

    @Override
    protected void analyzeData() {
        System.out.println("Performing statistical analysis");
    }
}
```

## Program Output
```
--- 1. Data Mining Template ---
Mining PDF file:
  [PDF] Opening PDF file: report.pdf
  [PDF] Extracting text from PDF pages
  [PDF] Parsing PDF data structure
  [DataMiner] Performing standard analysis
  [DataMiner] Sending analysis report via email
  [PDF] Closing PDF file

Mining CSV file:
  [CSV] Opening CSV file: data.csv
  [CSV] Reading CSV rows and columns
  [CSV] Parsing comma-separated values
  [CSV] Performing statistical analysis on numeric data
  [DataMiner] Sending analysis report via email

--- 3. Beverage Preparation Template ---
Preparing Coffee:
  Boiling water
  [Coffee] Dripping coffee through filter
  Pouring into cup
  [Coffee] Adding sugar and milk

Preparing Tea:
  Boiling water
  [Tea] Steeping the tea bag
  Pouring into cup
```

## Pattern Benefits
- Defines algorithm skeleton
- Lets subclasses override specific steps
- Avoids code duplication
- Controls extension via hooks

## Requirements
- Java 17 or higher
- Maven 3.x
