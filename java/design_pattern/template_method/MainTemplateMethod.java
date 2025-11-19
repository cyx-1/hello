/**
 * Comprehensive demonstration of the Template Method Pattern in Java
 *
 * The Template Method pattern defines the skeleton of an algorithm in a method,
 * deferring some steps to subclasses. It lets subclasses redefine certain steps
 * of an algorithm without changing the algorithm's structure.
 */

// Abstract class with template method
abstract class DataMiner {
    // Template method - defines the algorithm skeleton
    public final void mine(String path) {
        openFile(path);
        extractData();
        parseData();
        analyzeData();
        sendReport();
        closeFile();
    }

    // Common operations
    protected void sendReport() {
        System.out.println("  [DataMiner] Sending analysis report via email");
    }

    // Abstract operations - must be implemented by subclasses
    protected abstract void openFile(String path);
    protected abstract void extractData();
    protected abstract void parseData();
    protected abstract void closeFile();

    // Hook - optional operation with default implementation
    protected void analyzeData() {
        System.out.println("  [DataMiner] Performing standard analysis");
    }
}

// Concrete implementations
class PDFDataMiner extends DataMiner {
    @Override
    protected void openFile(String path) {
        System.out.println("  [PDF] Opening PDF file: " + path);
    }

    @Override
    protected void extractData() {
        System.out.println("  [PDF] Extracting text from PDF pages");
    }

    @Override
    protected void parseData() {
        System.out.println("  [PDF] Parsing PDF data structure");
    }

    @Override
    protected void closeFile() {
        System.out.println("  [PDF] Closing PDF file");
    }
}

class CSVDataMiner extends DataMiner {
    @Override
    protected void openFile(String path) {
        System.out.println("  [CSV] Opening CSV file: " + path);
    }

    @Override
    protected void extractData() {
        System.out.println("  [CSV] Reading CSV rows and columns");
    }

    @Override
    protected void parseData() {
        System.out.println("  [CSV] Parsing comma-separated values");
    }

    @Override
    protected void closeFile() {
        System.out.println("  [CSV] Closing CSV file");
    }

    @Override
    protected void analyzeData() {
        System.out.println("  [CSV] Performing statistical analysis on numeric data");
    }
}

class XMLDataMiner extends DataMiner {
    @Override
    protected void openFile(String path) {
        System.out.println("  [XML] Opening XML file: " + path);
    }

    @Override
    protected void extractData() {
        System.out.println("  [XML] Parsing XML DOM tree");
    }

    @Override
    protected void parseData() {
        System.out.println("  [XML] Extracting data from XML nodes");
    }

    @Override
    protected void closeFile() {
        System.out.println("  [XML] Closing XML file");
    }
}

// Game AI example

abstract class GameAI {
    // Template method
    public final void turn() {
        collectResources();
        buildStructures();
        buildUnits();
        attack();
    }

    // Default implementation
    protected void collectResources() {
        System.out.println("  [AI] Collecting resources from nearby sources");
    }

    // Abstract methods
    protected abstract void buildStructures();
    protected abstract void buildUnits();

    // Hook with default
    protected void attack() {
        System.out.println("  [AI] Sending scouts to find enemy");
    }
}

class AggressiveAI extends GameAI {
    @Override
    protected void buildStructures() {
        System.out.println("  [Aggressive] Building barracks and weapons factories");
    }

    @Override
    protected void buildUnits() {
        System.out.println("  [Aggressive] Training large army of soldiers");
    }

    @Override
    protected void attack() {
        System.out.println("  [Aggressive] Launching full-scale attack on enemy base!");
    }
}

class DefensiveAI extends GameAI {
    @Override
    protected void buildStructures() {
        System.out.println("  [Defensive] Building walls and defensive towers");
    }

    @Override
    protected void buildUnits() {
        System.out.println("  [Defensive] Training defenders and archers");
    }

    @Override
    protected void attack() {
        System.out.println("  [Defensive] Holding position, waiting for enemy");
    }
}

class EconomicAI extends GameAI {
    @Override
    protected void collectResources() {
        System.out.println("  [Economic] Optimizing resource collection with multiple workers");
    }

    @Override
    protected void buildStructures() {
        System.out.println("  [Economic] Building markets and resource storage");
    }

    @Override
    protected void buildUnits() {
        System.out.println("  [Economic] Training workers and traders");
    }
}

// Web page generator example

abstract class PageGenerator {
    // Template method with hooks
    public final String generatePage(String title, String content) {
        StringBuilder html = new StringBuilder();
        html.append(getDocType());
        html.append("<html>\n<head>\n");
        html.append(getStyles());
        html.append("<title>").append(title).append("</title>\n");
        html.append("</head>\n<body>\n");
        html.append(getHeader());
        html.append("<main>\n").append(content).append("\n</main>\n");
        html.append(getFooter());
        html.append("</body>\n</html>");
        return html.toString();
    }

    // Hooks with default implementations
    protected String getDocType() {
        return "<!DOCTYPE html>\n";
    }

    protected String getStyles() {
        return "<style>body { font-family: Arial; }</style>\n";
    }

    // Abstract methods
    protected abstract String getHeader();
    protected abstract String getFooter();
}

class BlogPageGenerator extends PageGenerator {
    @Override
    protected String getHeader() {
        return "<header><h1>My Tech Blog</h1><nav>Home | Posts | About</nav></header>\n";
    }

    @Override
    protected String getFooter() {
        return "<footer>Copyright 2024 Tech Blog</footer>\n";
    }

    @Override
    protected String getStyles() {
        return "<style>body { font-family: Georgia; } header { background: #333; color: white; }</style>\n";
    }
}

class PortfolioPageGenerator extends PageGenerator {
    @Override
    protected String getHeader() {
        return "<header><h1>John's Portfolio</h1></header>\n";
    }

    @Override
    protected String getFooter() {
        return "<footer>Contact: john@example.com</footer>\n";
    }
}

// Beverage preparation example

abstract class Beverage {
    // Template method
    public final void prepare() {
        boilWater();
        brew();
        pourInCup();
        if (customerWantsCondiments()) {
            addCondiments();
        }
    }

    protected void boilWater() {
        System.out.println("  Boiling water");
    }

    protected void pourInCup() {
        System.out.println("  Pouring into cup");
    }

    // Abstract methods
    protected abstract void brew();
    protected abstract void addCondiments();

    // Hook - subclasses can override
    protected boolean customerWantsCondiments() {
        return true;
    }
}

class Coffee extends Beverage {
    @Override
    protected void brew() {
        System.out.println("  [Coffee] Dripping coffee through filter");
    }

    @Override
    protected void addCondiments() {
        System.out.println("  [Coffee] Adding sugar and milk");
    }
}

class Tea extends Beverage {
    @Override
    protected void brew() {
        System.out.println("  [Tea] Steeping the tea bag");
    }

    @Override
    protected void addCondiments() {
        System.out.println("  [Tea] Adding lemon");
    }

    @Override
    protected boolean customerWantsCondiments() {
        return false;  // No condiments for tea
    }
}

public class MainTemplateMethod {
    public static void main(String[] args) {
        System.out.println("=== Template Method Pattern Demonstration ===\n");

        // Data mining example
        System.out.println("--- 1. Data Mining Template ---");

        System.out.println("\nMining PDF file:");
        DataMiner pdfMiner = new PDFDataMiner();
        pdfMiner.mine("report.pdf");

        System.out.println("\nMining CSV file:");
        DataMiner csvMiner = new CSVDataMiner();
        csvMiner.mine("data.csv");

        System.out.println("\nMining XML file:");
        DataMiner xmlMiner = new XMLDataMiner();
        xmlMiner.mine("config.xml");
        System.out.println();

        // Game AI example
        System.out.println("--- 2. Game AI Template ---");

        System.out.println("\nAggressive AI turn:");
        GameAI aggressive = new AggressiveAI();
        aggressive.turn();

        System.out.println("\nDefensive AI turn:");
        GameAI defensive = new DefensiveAI();
        defensive.turn();

        System.out.println("\nEconomic AI turn:");
        GameAI economic = new EconomicAI();
        economic.turn();
        System.out.println();

        // Beverage example
        System.out.println("--- 3. Beverage Preparation Template ---");

        System.out.println("\nPreparing Coffee:");
        Beverage coffee = new Coffee();
        coffee.prepare();

        System.out.println("\nPreparing Tea:");
        Beverage tea = new Tea();
        tea.prepare();

        System.out.println("\n=== Summary ===");
        System.out.println("Template Method pattern benefits:");
        System.out.println("  - Defines algorithm skeleton in base class");
        System.out.println("  - Lets subclasses override specific steps");
        System.out.println("  - Avoids code duplication");
        System.out.println("  - Controls extension points via hooks");
        System.out.println("\nKey elements:");
        System.out.println("  - Template method: final, defines algorithm");
        System.out.println("  - Abstract methods: must be implemented");
        System.out.println("  - Hooks: optional overrides with defaults");
    }
}
