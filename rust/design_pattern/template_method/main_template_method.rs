// Template Method Design Pattern in Rust
// Demonstrates data mining with different file formats

/// DataMiner trait defines the template method pattern
/// The template method defines the algorithm skeleton
/// while allowing subclasses to override specific steps
trait DataMiner {
    // Template method - defines the algorithm skeleton
    // This method is final (not meant to be overridden)
    fn mine(&self) {
        println!("=== Starting Data Mining Process ===");
        self.open_file();
        let raw_data = self.extract_data();
        let processed_data = self.parse_data(&raw_data);
        self.analyze_data(&processed_data);
        self.send_report(&processed_data);
        self.hook_before_close();
        self.close_file();
        println!("=== Data Mining Complete ===\n");
    }

    // Abstract methods - must be implemented by concrete types
    fn open_file(&self);
    fn extract_data(&self) -> String;
    fn parse_data(&self, raw_data: &str) -> Vec<String>;
    fn close_file(&self);

    // Concrete methods with default implementation
    fn analyze_data(&self, data: &[String]) {
        println!("  [Analyze] Processing {} records", data.len());
        for (i, record) in data.iter().enumerate() {
            println!("    - Record {}: {}", i + 1, record);
        }
    }

    fn send_report(&self, data: &[String]) {
        println!("  [Report] Sending report with {} items", data.len());
    }

    // Hook method - empty by default, can be overridden
    fn hook_before_close(&self) {
        // Default: do nothing
    }
}

/// CSV Data Miner - concrete implementation for CSV files
struct CsvDataMiner {
    filename: String,
}

impl CsvDataMiner {
    fn new(filename: &str) -> Self {
        CsvDataMiner {
            filename: filename.to_string(),
        }
    }
}

impl DataMiner for CsvDataMiner {
    fn open_file(&self) {
        println!("  [Open] Opening CSV file: {}", self.filename);
    }

    fn extract_data(&self) -> String {
        println!("  [Extract] Reading CSV rows...");
        // Simulated CSV data
        String::from("name,age,city\nAlice,30,NYC\nBob,25,LA\nCharlie,35,Chicago")
    }

    fn parse_data(&self, raw_data: &str) -> Vec<String> {
        println!("  [Parse] Parsing CSV format...");
        let lines: Vec<&str> = raw_data.lines().collect();
        let header = lines[0];
        let fields: Vec<&str> = header.split(',').collect();

        lines[1..]
            .iter()
            .map(|line| {
                let values: Vec<&str> = line.split(',').collect();
                fields
                    .iter()
                    .zip(values.iter())
                    .map(|(k, v)| format!("{}={}", k, v))
                    .collect::<Vec<_>>()
                    .join(", ")
            })
            .collect()
    }

    fn close_file(&self) {
        println!("  [Close] Closing CSV file: {}", self.filename);
    }

    // Override hook to add CSV-specific cleanup
    fn hook_before_close(&self) {
        println!("  [Hook] CSV cleanup: clearing row buffer");
    }
}

/// JSON Data Miner - concrete implementation for JSON files
struct JsonDataMiner {
    filename: String,
    pretty_print: bool,
}

impl JsonDataMiner {
    fn new(filename: &str, pretty_print: bool) -> Self {
        JsonDataMiner {
            filename: filename.to_string(),
            pretty_print,
        }
    }
}

impl DataMiner for JsonDataMiner {
    fn open_file(&self) {
        println!("  [Open] Opening JSON file: {}", self.filename);
        if self.pretty_print {
            println!("    (Pretty print mode enabled)");
        }
    }

    fn extract_data(&self) -> String {
        println!("  [Extract] Reading JSON content...");
        // Simulated JSON data
        String::from(r#"[{"name":"Diana","score":95},{"name":"Eve","score":88}]"#)
    }

    fn parse_data(&self, raw_data: &str) -> Vec<String> {
        println!("  [Parse] Parsing JSON format...");
        // Simple manual JSON parsing for demonstration
        let mut results = Vec::new();
        let trimmed = raw_data.trim_start_matches('[').trim_end_matches(']');

        for obj in trimmed.split("},{") {
            let clean = obj
                .trim_start_matches('{')
                .trim_end_matches('}')
                .replace('"', "");

            let parts: Vec<&str> = clean.split(',').collect();
            let formatted: Vec<String> = parts
                .iter()
                .map(|p| p.replace(':', "="))
                .collect();

            results.push(formatted.join(", "));
        }
        results
    }

    fn close_file(&self) {
        println!("  [Close] Closing JSON file: {}", self.filename);
    }

    // Override the analyze method for JSON-specific analysis
    fn analyze_data(&self, data: &[String]) {
        println!("  [Analyze] JSON analysis of {} records:", data.len());
        for (i, record) in data.iter().enumerate() {
            if self.pretty_print {
                println!("    {{ Record {} }}", i + 1);
                for field in record.split(", ") {
                    println!("      - {}", field);
                }
            } else {
                println!("    Record {}: {}", i + 1, record);
            }
        }
    }
}

/// Game AI using Template Method - another example
trait GameAI {
    // Template method for AI turn
    fn take_turn(&self) {
        println!("--- AI Turn Started ---");
        self.collect_resources();
        self.build_structures();
        self.build_units();
        self.attack();
        println!("--- AI Turn Ended ---\n");
    }

    // Abstract methods
    fn build_structures(&self);
    fn build_units(&self);

    // Methods with default behavior
    fn collect_resources(&self) {
        println!("  [Resources] Collecting nearby resources");
    }

    fn attack(&self) {
        println!("  [Attack] Sending units to attack enemy");
    }
}

/// Aggressive Orc AI
struct OrcAI;

impl GameAI for OrcAI {
    fn build_structures(&self) {
        println!("  [Build] Constructing War Camp and Barracks");
    }

    fn build_units(&self) {
        println!("  [Units] Training Grunts and Wolfriders");
    }

    fn attack(&self) {
        println!("  [Attack] WAAAGH! All units charge!");
    }
}

/// Defensive Human AI
struct HumanAI;

impl GameAI for HumanAI {
    fn build_structures(&self) {
        println!("  [Build] Constructing Castle and Towers");
    }

    fn build_units(&self) {
        println!("  [Units] Training Knights and Archers");
    }

    fn collect_resources(&self) {
        println!("  [Resources] Peasants gathering gold and lumber");
    }
}

fn main() {
    println!("========================================");
    println!(" Template Method Pattern Demonstration");
    println!("========================================\n");

    // Data Mining Examples
    println!(">> DATA MINING EXAMPLES <<\n");

    let csv_miner = CsvDataMiner::new("users.csv");
    csv_miner.mine();

    let json_miner = JsonDataMiner::new("scores.json", true);
    json_miner.mine();

    // Game AI Examples
    println!(">> GAME AI EXAMPLES <<\n");

    let orc_ai = OrcAI;
    orc_ai.take_turn();

    let human_ai = HumanAI;
    human_ai.take_turn();

    println!("========================================");
    println!(" Pattern demonstration complete!");
    println!("========================================");
}
