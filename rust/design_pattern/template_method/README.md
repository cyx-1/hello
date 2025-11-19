# Template Method Design Pattern in Rust

The Template Method pattern defines the skeleton of an algorithm in a base trait, allowing concrete implementations to override specific steps without changing the algorithm's structure. This pattern promotes code reuse by moving common algorithm steps into a shared trait while letting specific variations be handled by implementing types.

In Rust, this pattern is implemented using traits with:
- **Template method**: A method with a default implementation that calls other trait methods in sequence
- **Abstract methods**: Methods without default implementations that must be provided by implementors
- **Hook methods**: Optional methods with empty or default implementations that can be overridden

## Source Code

```rust
  1  // Template Method Design Pattern in Rust
  2  // Demonstrates data mining with different file formats
  3
  4  /// DataMiner trait defines the template method pattern
  5  /// The template method defines the algorithm skeleton
  6  /// while allowing subclasses to override specific steps
  7  trait DataMiner {
  8      // Template method - defines the algorithm skeleton
  9      // This method is final (not meant to be overridden)
 10      fn mine(&self) {
 11          println!("=== Starting Data Mining Process ===");
 12          self.open_file();
 13          let raw_data = self.extract_data();
 14          let processed_data = self.parse_data(&raw_data);
 15          self.analyze_data(&processed_data);
 16          self.send_report(&processed_data);
 17          self.hook_before_close();
 18          self.close_file();
 19          println!("=== Data Mining Complete ===\n");
 20      }
 21
 22      // Abstract methods - must be implemented by concrete types
 23      fn open_file(&self);
 24      fn extract_data(&self) -> String;
 25      fn parse_data(&self, raw_data: &str) -> Vec<String>;
 26      fn close_file(&self);
 27
 28      // Concrete methods with default implementation
 29      fn analyze_data(&self, data: &[String]) {
 30          println!("  [Analyze] Processing {} records", data.len());
 31          for (i, record) in data.iter().enumerate() {
 32              println!("    - Record {}: {}", i + 1, record);
 33          }
 34      }
 35
 36      fn send_report(&self, data: &[String]) {
 37          println!("  [Report] Sending report with {} items", data.len());
 38      }
 39
 40      // Hook method - empty by default, can be overridden
 41      fn hook_before_close(&self) {
 42          // Default: do nothing
 43      }
 44  }
 45
 46  /// CSV Data Miner - concrete implementation for CSV files
 47  struct CsvDataMiner {
 48      filename: String,
 49  }
 50
 51  impl CsvDataMiner {
 52      fn new(filename: &str) -> Self {
 53          CsvDataMiner {
 54              filename: filename.to_string(),
 55          }
 56      }
 57  }
 58
 59  impl DataMiner for CsvDataMiner {
 60      fn open_file(&self) {
 61          println!("  [Open] Opening CSV file: {}", self.filename);
 62      }
 63
 64      fn extract_data(&self) -> String {
 65          println!("  [Extract] Reading CSV rows...");
 66          // Simulated CSV data
 67          String::from("name,age,city\nAlice,30,NYC\nBob,25,LA\nCharlie,35,Chicago")
 68      }
 69
 70      fn parse_data(&self, raw_data: &str) -> Vec<String> {
 71          println!("  [Parse] Parsing CSV format...");
 72          let lines: Vec<&str> = raw_data.lines().collect();
 73          let header = lines[0];
 74          let fields: Vec<&str> = header.split(',').collect();
 75
 76          lines[1..]
 77              .iter()
 78              .map(|line| {
 79                  let values: Vec<&str> = line.split(',').collect();
 80                  fields
 81                      .iter()
 82                      .zip(values.iter())
 83                      .map(|(k, v)| format!("{}={}", k, v))
 84                      .collect::<Vec<_>>()
 85                      .join(", ")
 86              })
 87              .collect()
 88      }
 89
 90      fn close_file(&self) {
 91          println!("  [Close] Closing CSV file: {}", self.filename);
 92      }
 93
 94      // Override hook to add CSV-specific cleanup
 95      fn hook_before_close(&self) {
 96          println!("  [Hook] CSV cleanup: clearing row buffer");
 97      }
 98  }
 99
100  /// JSON Data Miner - concrete implementation for JSON files
101  struct JsonDataMiner {
102      filename: String,
103      pretty_print: bool,
104  }
105
106  impl JsonDataMiner {
107      fn new(filename: &str, pretty_print: bool) -> Self {
108          JsonDataMiner {
109              filename: filename.to_string(),
110              pretty_print,
111          }
112      }
113  }
114
115  impl DataMiner for JsonDataMiner {
116      fn open_file(&self) {
117          println!("  [Open] Opening JSON file: {}", self.filename);
118          if self.pretty_print {
119              println!("    (Pretty print mode enabled)");
120          }
121      }
122
123      fn extract_data(&self) -> String {
124          println!("  [Extract] Reading JSON content...");
125          // Simulated JSON data
126          String::from(r#"[{"name":"Diana","score":95},{"name":"Eve","score":88}]"#)
127      }
128
129      fn parse_data(&self, raw_data: &str) -> Vec<String> {
130          println!("  [Parse] Parsing JSON format...");
131          // Simple manual JSON parsing for demonstration
132          let mut results = Vec::new();
133          let trimmed = raw_data.trim_start_matches('[').trim_end_matches(']');
134
135          for obj in trimmed.split("},{") {
136              let clean = obj
137                  .trim_start_matches('{')
138                  .trim_end_matches('}')
139                  .replace('"', "");
140
141              let parts: Vec<&str> = clean.split(',').collect();
142              let formatted: Vec<String> = parts
143                  .iter()
144                  .map(|p| p.replace(':', "="))
145                  .collect();
146
147              results.push(formatted.join(", "));
148          }
149          results
150      }
151
152      fn close_file(&self) {
153          println!("  [Close] Closing JSON file: {}", self.filename);
154      }
155
156      // Override the analyze method for JSON-specific analysis
157      fn analyze_data(&self, data: &[String]) {
158          println!("  [Analyze] JSON analysis of {} records:", data.len());
159          for (i, record) in data.iter().enumerate() {
160              if self.pretty_print {
161                  println!("    {{ Record {} }}", i + 1);
162                  for field in record.split(", ") {
163                      println!("      - {}", field);
164                  }
165              } else {
166                  println!("    Record {}: {}", i + 1, record);
167              }
168          }
169      }
170  }
171
172  /// Game AI using Template Method - another example
173  trait GameAI {
174      // Template method for AI turn
175      fn take_turn(&self) {
176          println!("--- AI Turn Started ---");
177          self.collect_resources();
178          self.build_structures();
179          self.build_units();
180          self.attack();
181          println!("--- AI Turn Ended ---\n");
182      }
183
184      // Abstract methods
185      fn build_structures(&self);
186      fn build_units(&self);
187
188      // Methods with default behavior
189      fn collect_resources(&self) {
190          println!("  [Resources] Collecting nearby resources");
191      }
192
193      fn attack(&self) {
194          println!("  [Attack] Sending units to attack enemy");
195      }
196  }
197
198  /// Aggressive Orc AI
199  struct OrcAI;
200
201  impl GameAI for OrcAI {
202      fn build_structures(&self) {
203          println!("  [Build] Constructing War Camp and Barracks");
204      }
205
206      fn build_units(&self) {
207          println!("  [Units] Training Grunts and Wolfriders");
208      }
209
210      fn attack(&self) {
211          println!("  [Attack] WAAAGH! All units charge!");
212      }
213  }
214
215  /// Defensive Human AI
216  struct HumanAI;
217
218  impl GameAI for HumanAI {
219      fn build_structures(&self) {
220          println!("  [Build] Constructing Castle and Towers");
221      }
222
223      fn build_units(&self) {
224          println!("  [Units] Training Knights and Archers");
225      }
226
227      fn collect_resources(&self) {
228          println!("  [Resources] Peasants gathering gold and lumber");
229      }
230  }
231
232  fn main() {
233      println!("========================================");
234      println!(" Template Method Pattern Demonstration");
235      println!("========================================\n");
236
237      // Data Mining Examples
238      println!(">> DATA MINING EXAMPLES <<\n");
239
240      let csv_miner = CsvDataMiner::new("users.csv");
241      csv_miner.mine();
242
243      let json_miner = JsonDataMiner::new("scores.json", true);
244      json_miner.mine();
245
246      // Game AI Examples
247      println!(">> GAME AI EXAMPLES <<\n");
248
249      let orc_ai = OrcAI;
250      orc_ai.take_turn();
251
252      let human_ai = HumanAI;
253      human_ai.take_turn();
254
255      println!("========================================");
256      println!(" Pattern demonstration complete!");
257      println!("========================================");
258  }
```

## Program Output

```
========================================
 Template Method Pattern Demonstration
========================================

>> DATA MINING EXAMPLES <<

=== Starting Data Mining Process ===
  [Open] Opening CSV file: users.csv
  [Extract] Reading CSV rows...
  [Parse] Parsing CSV format...
  [Analyze] Processing 3 records
    - Record 1: name=Alice, age=30, city=NYC
    - Record 2: name=Bob, age=25, city=LA
    - Record 3: name=Charlie, age=35, city=Chicago
  [Report] Sending report with 3 items
  [Hook] CSV cleanup: clearing row buffer
  [Close] Closing CSV file: users.csv
=== Data Mining Complete ===

=== Starting Data Mining Process ===
  [Open] Opening JSON file: scores.json
    (Pretty print mode enabled)
  [Extract] Reading JSON content...
  [Parse] Parsing JSON format...
  [Analyze] JSON analysis of 2 records:
    { Record 1 }
      - name=Diana
      - score=95
    { Record 2 }
      - name=Eve
      - score=88
  [Report] Sending report with 2 items
  [Close] Closing JSON file: scores.json
=== Data Mining Complete ===

>> GAME AI EXAMPLES <<

--- AI Turn Started ---
  [Resources] Collecting nearby resources
  [Build] Constructing War Camp and Barracks
  [Units] Training Grunts and Wolfriders
  [Attack] WAAAGH! All units charge!
--- AI Turn Ended ---

--- AI Turn Started ---
  [Resources] Peasants gathering gold and lumber
  [Build] Constructing Castle and Towers
  [Units] Training Knights and Archers
  [Attack] Sending units to attack enemy
--- AI Turn Ended ---

========================================
 Pattern demonstration complete!
========================================
```

## Code Annotations

### Key Sections Explained

#### DataMiner Trait (Lines 7-44)
- **Lines 10-20**: The `mine()` template method defines the algorithm skeleton. It calls methods in a specific order: open, extract, parse, analyze, report, hook, close. This sequence cannot be changed by implementors.
- **Lines 23-26**: Abstract methods without default implementations. These MUST be implemented by any struct that implements `DataMiner`.
- **Lines 29-38**: Concrete methods with default behavior. Implementors can use these as-is or override them.
- **Lines 41-43**: Hook method `hook_before_close()` - does nothing by default but can be overridden for custom behavior.

#### CsvDataMiner (Lines 46-98)
- **Lines 59-92**: Implements required abstract methods for CSV-specific file handling.
- **Lines 70-88**: Custom parsing logic that transforms CSV rows into key=value format.
- **Lines 95-97**: Overrides the hook method to add CSV-specific cleanup behavior.

#### JsonDataMiner (Lines 100-170)
- **Lines 115-154**: Implements required abstract methods for JSON-specific handling.
- **Lines 157-169**: Overrides `analyze_data()` to provide custom JSON-formatted output with pretty printing support.

#### GameAI Trait (Lines 173-196)
- **Lines 175-182**: Second example of template method pattern with `take_turn()`.
- **Lines 185-186**: Required methods that each AI type must implement.
- **Lines 189-195**: Default behaviors that can be overridden by specific AI types.

#### Concrete AI Implementations (Lines 198-230)
- **OrcAI (Lines 201-213)**: Overrides `attack()` for aggressive behavior.
- **HumanAI (Lines 218-230)**: Overrides `collect_resources()` for custom resource gathering.

### Output to Source Code Correlation

| Output Line | Source Lines | Description |
|-------------|--------------|-------------|
| `=== Starting Data Mining Process ===` | 11 | Template method begins execution |
| `[Open] Opening CSV file: users.csv` | 61 | CsvDataMiner.open_file() called by template (line 12) |
| `[Extract] Reading CSV rows...` | 65 | CsvDataMiner.extract_data() called by template (line 13) |
| `[Parse] Parsing CSV format...` | 71 | CsvDataMiner.parse_data() called by template (line 14) |
| `[Analyze] Processing 3 records` | 30 | Default analyze_data() from trait (line 15) |
| `- Record 1: name=Alice...` | 32 | Default analyze_data() iteration |
| `[Report] Sending report...` | 37 | Default send_report() from trait (line 16) |
| `[Hook] CSV cleanup...` | 96 | Overridden hook_before_close() (line 17) |
| `[Close] Closing CSV file...` | 91 | CsvDataMiner.close_file() called by template (line 18) |
| `[Open] Opening JSON file...` | 117 | JsonDataMiner.open_file() |
| `(Pretty print mode enabled)` | 119 | Conditional output based on struct field |
| `[Analyze] JSON analysis...` | 158 | Overridden analyze_data() in JsonDataMiner |
| `{ Record 1 }` | 161 | Pretty print formatting in overridden method |
| `--- AI Turn Started ---` | 176 | GameAI template method begins |
| `[Resources] Collecting nearby...` | 190 | Default collect_resources() for OrcAI |
| `[Resources] Peasants gathering...` | 228 | Overridden collect_resources() for HumanAI |
| `[Attack] WAAAGH!...` | 211 | Overridden attack() for OrcAI |
| `[Attack] Sending units...` | 194 | Default attack() for HumanAI |

### Key Characteristics of Template Method in Rust

1. **Trait-Based Implementation**: Rust uses traits instead of abstract classes. The template method is a trait method with a default implementation that calls other trait methods.

2. **No True Abstract Methods**: Methods without default implementations serve as "abstract methods" that must be implemented by any type using the trait.

3. **Hook Methods**: Empty default implementations allow optional customization points without requiring override.

4. **Composition over Inheritance**: While Rust doesn't have inheritance, traits provide similar behavioral polymorphism. Each concrete struct can hold its own state (like `filename` or `pretty_print`).

5. **Static Dispatch**: By default, Rust uses monomorphization, meaning each concrete type gets its own specialized version of the template method at compile time - no runtime overhead.

6. **Cannot Prevent Override**: Unlike languages with `final` methods, Rust cannot prevent implementors from overriding the template method itself. Convention and documentation must convey the intent.

7. **Type Safety**: Rust's type system ensures all required methods are implemented at compile time, preventing runtime errors from missing implementations.
