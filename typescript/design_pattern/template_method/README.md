# Template Method Design Pattern in TypeScript

The Template Method pattern defines the skeleton of an algorithm in an abstract class, allowing subclasses to override specific steps without changing the algorithm's structure. It promotes code reuse by encapsulating the invariant parts of an algorithm while letting subclasses implement the variant parts.

This example demonstrates a data processing framework where the template method defines the overall workflow (validate, transform, analyze, format), while concrete implementations provide specific behavior for CSV reports, JSON analytics, and executive summaries.

## Requirements

- Node.js 18+
- TypeScript 5.3+

## How to Run

```bash
npm install
npm run start
```

## Source Code

```typescript
1   /**
2    * Template Method Design Pattern in TypeScript
3    *
4    * The Template Method pattern defines the skeleton of an algorithm in an
5    * abstract class, allowing subclasses to override specific steps without
6    * changing the algorithm's structure. It lets subclasses redefine certain
7    * steps while keeping the overall process intact.
8    */
9
10  // Sample data types
11  interface DataRecord {
12      id: string;
13      name: string;
14      value: number;
15      category: string;
16      timestamp: Date;
17  }
18
19  // Abstract class with Template Method
20  abstract class DataProcessor {
21      // Template Method - defines the algorithm skeleton
22      public processData(rawData: DataRecord[]): string {
23          console.log(`[Line 22] ${this.constructor.name}: Starting data processing...`);
24
25          // Step 1: Validate data (required)
26          const validData = this.validateData(rawData);
27          console.log(`[Line 26] ${this.constructor.name}: Validated ${validData.length} of ${rawData.length} records`);
28
29          // Step 2: Hook for pre-processing (optional)
30          if (this.shouldPreprocess()) {
31              console.log(`[Line 30] ${this.constructor.name}: Pre-processing enabled`);
32              this.preprocess(validData);
33          }
34
35          // Step 3: Transform data (required)
36          const transformedData = this.transformData(validData);
37          console.log(`[Line 36] ${this.constructor.name}: Transformed ${transformedData.length} records`);
38
39          // Step 4: Analyze data (required)
40          const analysis = this.analyzeData(transformedData);
41          console.log(`[Line 40] ${this.constructor.name}: Analysis complete`);
42
43          // Step 5: Format output (required)
44          const output = this.formatOutput(analysis);
45          console.log(`[Line 44] ${this.constructor.name}: Output formatted`);
46
47          // Step 6: Hook for post-processing (optional)
48          this.postProcess(output);
49
50          console.log(`[Line 49] ${this.constructor.name}: Data processing complete`);
51          return output;
52      }
53
54      // Abstract methods - must be implemented by subclasses
55      protected abstract validateData(data: DataRecord[]): DataRecord[];
56      protected abstract transformData(data: DataRecord[]): DataRecord[];
57      protected abstract analyzeData(data: DataRecord[]): Record<string, unknown>;
58      protected abstract formatOutput(analysis: Record<string, unknown>): string;
59
60      // Hook methods - can be overridden by subclasses (optional)
61      protected shouldPreprocess(): boolean {
62          return false; // Default: no pre-processing
63      }
64
65      protected preprocess(data: DataRecord[]): void {
66          // Default: do nothing
67      }
68
69      protected postProcess(output: string): void {
70          console.log(`[Line 68] ${this.constructor.name}: Default post-processing (no action)`);
71      }
72  }
73
74  // Concrete Implementation 1: CSV Report Generator
75  class CSVReportGenerator extends DataProcessor {
76      protected validateData(data: DataRecord[]): DataRecord[] {
77          console.log(`[Line 75] CSVReportGenerator: Validating data for CSV format`);
78          return data.filter(record => {
79              const isValid = record.id && record.name && record.value !== undefined;
80              if (!isValid) {
81                  console.log(`[Line 79] CSVReportGenerator: Invalid record skipped - ${record.id || 'unknown'}`);
82              }
83              return isValid;
84          });
85      }
86
87      protected transformData(data: DataRecord[]): DataRecord[] {
88          console.log(`[Line 86] CSVReportGenerator: Transforming data (sanitizing strings)`);
89          return data.map(record => ({
90              ...record,
91              name: record.name.replace(/,/g, ';'), // Escape commas for CSV
92          }));
93      }
94
95      protected analyzeData(data: DataRecord[]): Record<string, unknown> {
96          console.log(`[Line 94] CSVReportGenerator: Analyzing data for summary`);
97          const total = data.reduce((sum, r) => sum + r.value, 0);
98          const average = data.length > 0 ? total / data.length : 0;
99
100         return {
101             recordCount: data.length,
102             totalValue: total,
103             averageValue: average.toFixed(2),
104             records: data,
105         };
106     }
107
108     protected formatOutput(analysis: Record<string, unknown>): string {
109         console.log(`[Line 107] CSVReportGenerator: Formatting as CSV`);
110         const records = analysis.records as DataRecord[];
111         const header = 'id,name,value,category,timestamp';
112         const rows = records.map(r =>
113             `${r.id},${r.name},${r.value},${r.category},${r.timestamp.toISOString()}`
114         );
115         const summary = `# Summary: ${analysis.recordCount} records, Total: ${analysis.totalValue}, Avg: ${analysis.averageValue}`;
116
117         return `${summary}\n${header}\n${rows.join('\n')}`;
118     }
119 }
120
121 // Concrete Implementation 2: JSON Analytics Processor
122 class JSONAnalyticsProcessor extends DataProcessor {
123     private categories: Set<string> = new Set();
124
125     protected shouldPreprocess(): boolean {
126         return true; // Override hook: enable pre-processing
127     }
128
129     protected preprocess(data: DataRecord[]): void {
130         console.log(`[Line 127] JSONAnalyticsProcessor: Collecting unique categories`);
131         data.forEach(record => this.categories.add(record.category));
132         console.log(`[Line 129] JSONAnalyticsProcessor: Found ${this.categories.size} unique categories`);
133     }
134
135     protected validateData(data: DataRecord[]): DataRecord[] {
136         console.log(`[Line 133] JSONAnalyticsProcessor: Validating data with strict rules`);
137         return data.filter(record => {
138             const isValid = record.id &&
139                             record.name &&
140                             record.value > 0 &&
141                             record.category &&
142                             record.timestamp instanceof Date;
143             if (!isValid) {
144                 console.log(`[Line 141] JSONAnalyticsProcessor: Rejected record - ${record.id || 'unknown'}`);
145             }
146             return isValid;
147         });
148     }
149
150     protected transformData(data: DataRecord[]): DataRecord[] {
151         console.log(`[Line 148] JSONAnalyticsProcessor: Normalizing values`);
152         const maxValue = Math.max(...data.map(r => r.value));
153         return data.map(record => ({
154             ...record,
155             value: Math.round((record.value / maxValue) * 100), // Normalize to 0-100
156         }));
157     }
158
159     protected analyzeData(data: DataRecord[]): Record<string, unknown> {
160         console.log(`[Line 157] JSONAnalyticsProcessor: Performing category analysis`);
161
162         const categoryStats: Record<string, { count: number; totalValue: number }> = {};
163
164         data.forEach(record => {
165             if (!categoryStats[record.category]) {
166                 categoryStats[record.category] = { count: 0, totalValue: 0 };
167             }
168             categoryStats[record.category].count++;
169             categoryStats[record.category].totalValue += record.value;
170         });
171
172         return {
173             totalRecords: data.length,
174             categories: Array.from(this.categories),
175             categoryStats,
176             processedAt: new Date().toISOString(),
177         };
178     }
179
180     protected formatOutput(analysis: Record<string, unknown>): string {
181         console.log(`[Line 178] JSONAnalyticsProcessor: Formatting as JSON`);
182         return JSON.stringify(analysis, null, 2);
183     }
184
185     protected postProcess(output: string): void {
186         console.log(`[Line 183] JSONAnalyticsProcessor: Post-processing - validating JSON output`);
187         try {
188             JSON.parse(output);
189             console.log(`[Line 186] JSONAnalyticsProcessor: JSON validation passed`);
190         } catch (error) {
191             console.log(`[Line 188] JSONAnalyticsProcessor: JSON validation failed!`);
192         }
193     }
194 }
195
196 // Concrete Implementation 3: Summary Report Generator
197 class SummaryReportGenerator extends DataProcessor {
198     protected validateData(data: DataRecord[]): DataRecord[] {
199         console.log(`[Line 196] SummaryReportGenerator: Quick validation`);
200         return data.filter(record => record.id && record.value !== undefined);
201     }
202
203     protected transformData(data: DataRecord[]): DataRecord[] {
204         console.log(`[Line 201] SummaryReportGenerator: Sorting by value descending`);
205         return [...data].sort((a, b) => b.value - a.value);
206     }
207
208     protected analyzeData(data: DataRecord[]): Record<string, unknown> {
209         console.log(`[Line 206] SummaryReportGenerator: Generating executive summary`);
210
211         const total = data.reduce((sum, r) => sum + r.value, 0);
212         const topPerformers = data.slice(0, 3);
213         const categoryBreakdown: Record<string, number> = {};
214
215         data.forEach(record => {
216             categoryBreakdown[record.category] = (categoryBreakdown[record.category] || 0) + record.value;
217         });
218
219         return {
220             totalRecords: data.length,
221             totalValue: total,
222             topPerformers: topPerformers.map(r => ({ id: r.id, name: r.name, value: r.value })),
223             categoryBreakdown,
224         };
225     }
226
227     protected formatOutput(analysis: Record<string, unknown>): string {
228         console.log(`[Line 224] SummaryReportGenerator: Formatting as executive summary`);
229
230         const topPerformers = analysis.topPerformers as Array<{ id: string; name: string; value: number }>;
231         const categoryBreakdown = analysis.categoryBreakdown as Record<string, number>;
232
233         let report = '=== EXECUTIVE SUMMARY ===\n';
234         report += `Total Records: ${analysis.totalRecords}\n`;
235         report += `Total Value: $${analysis.totalValue}\n\n`;
236         report += 'Top Performers:\n';
237         topPerformers.forEach((p, i) => {
238             report += `  ${i + 1}. ${p.name} (${p.id}): $${p.value}\n`;
239         });
240         report += '\nCategory Breakdown:\n';
241         Object.entries(categoryBreakdown).forEach(([category, value]) => {
242             report += `  - ${category}: $${value}\n`;
243         });
244
245         return report;
246     }
247
248     protected postProcess(output: string): void {
249         console.log(`[Line 246] SummaryReportGenerator: Post-processing - checking report length`);
250         const lines = output.split('\n').length;
251         console.log(`[Line 248] SummaryReportGenerator: Report contains ${lines} lines`);
252     }
253 }
```

## Program Output

```
=== Template Method Pattern Demonstration ===

--- Demo 1: CSV Report Generator ---

[Line 22] CSVReportGenerator: Starting data processing...
[Line 75] CSVReportGenerator: Validating data for CSV format
[Line 79] CSVReportGenerator: Invalid record skipped - unknown
[Line 26] CSVReportGenerator: Validated 6 of 7 records
[Line 86] CSVReportGenerator: Transforming data (sanitizing strings)
[Line 36] CSVReportGenerator: Transformed 6 records
[Line 94] CSVReportGenerator: Analyzing data for summary
[Line 40] CSVReportGenerator: Analysis complete
[Line 107] CSVReportGenerator: Formatting as CSV
[Line 44] CSVReportGenerator: Output formatted
[Line 68] CSVReportGenerator: Default post-processing (no action)
[Line 49] CSVReportGenerator: Data processing complete

Generated CSV Report:
# Summary: 6 records, Total: 11700, Avg: 1950.00
id,name,value,category,timestamp
R001,Product Alpha,1500,Electronics,2024-01-15T00:00:00.000Z
R002,Service Beta,2300,Services,2024-01-16T00:00:00.000Z
R003,Product Gamma,800,Electronics,2024-01-17T00:00:00.000Z
R004,Consulting; Inc,3200,Services,2024-01-18T00:00:00.000Z
R005,Hardware Delta,1100,Hardware,2024-01-19T00:00:00.000Z
R006,Software Epsilon,2800,Software,2024-01-21T00:00:00.000Z


--- Demo 2: JSON Analytics Processor ---

[Line 22] JSONAnalyticsProcessor: Starting data processing...
[Line 133] JSONAnalyticsProcessor: Validating data with strict rules
[Line 141] JSONAnalyticsProcessor: Rejected record - unknown
[Line 26] JSONAnalyticsProcessor: Validated 6 of 7 records
[Line 30] JSONAnalyticsProcessor: Pre-processing enabled
[Line 127] JSONAnalyticsProcessor: Collecting unique categories
[Line 129] JSONAnalyticsProcessor: Found 4 unique categories
[Line 148] JSONAnalyticsProcessor: Normalizing values
[Line 36] JSONAnalyticsProcessor: Transformed 6 records
[Line 157] JSONAnalyticsProcessor: Performing category analysis
[Line 40] JSONAnalyticsProcessor: Analysis complete
[Line 178] JSONAnalyticsProcessor: Formatting as JSON
[Line 44] JSONAnalyticsProcessor: Output formatted
[Line 183] JSONAnalyticsProcessor: Post-processing - validating JSON output
[Line 186] JSONAnalyticsProcessor: JSON validation passed
[Line 49] JSONAnalyticsProcessor: Data processing complete

Generated JSON Analytics:
{
  "totalRecords": 6,
  "categories": [
    "Electronics",
    "Services",
    "Hardware",
    "Software"
  ],
  "categoryStats": {
    "Electronics": {
      "count": 2,
      "totalValue": 72
    },
    "Services": {
      "count": 2,
      "totalValue": 172
    },
    "Hardware": {
      "count": 1,
      "totalValue": 34
    },
    "Software": {
      "count": 1,
      "totalValue": 88
    }
  },
  "processedAt": "2025-11-19T01:03:27.213Z"
}


--- Demo 3: Summary Report Generator ---

[Line 22] SummaryReportGenerator: Starting data processing...
[Line 196] SummaryReportGenerator: Quick validation
[Line 26] SummaryReportGenerator: Validated 6 of 7 records
[Line 201] SummaryReportGenerator: Sorting by value descending
[Line 36] SummaryReportGenerator: Transformed 6 records
[Line 206] SummaryReportGenerator: Generating executive summary
[Line 40] SummaryReportGenerator: Analysis complete
[Line 224] SummaryReportGenerator: Formatting as executive summary
[Line 44] SummaryReportGenerator: Output formatted
[Line 246] SummaryReportGenerator: Post-processing - checking report length
[Line 248] SummaryReportGenerator: Report contains 15 lines
[Line 49] SummaryReportGenerator: Data processing complete

Generated Executive Summary:
=== EXECUTIVE SUMMARY ===
Total Records: 6
Total Value: $11700

Top Performers:
  1. Consulting, Inc (R004): $3200
  2. Software Epsilon (R006): $2800
  3. Service Beta (R002): $2300

Category Breakdown:
  - Services: $5500
  - Software: $2800
  - Electronics: $2300
  - Hardware: $1100
```

## Code Analysis and Annotations

### Pattern Components

#### Abstract Class (Lines 20-72)
The `DataProcessor` class defines the template method and provides the algorithm skeleton:
- **Template Method** (`processData`): Defines the fixed sequence of steps
- **Abstract Methods**: Required operations that subclasses must implement
- **Hook Methods**: Optional operations with default implementations

#### Template Method (Lines 22-52)
The `processData` method defines the algorithm skeleton with six steps:
1. Validate data (required)
2. Pre-process data (optional hook)
3. Transform data (required)
4. Analyze data (required)
5. Format output (required)
6. Post-process output (optional hook)

#### Concrete Implementations (Lines 75-253)
Three implementations demonstrate different behaviors while following the same workflow:
- `CSVReportGenerator`: Produces comma-separated value reports
- `JSONAnalyticsProcessor`: Creates JSON analytics with category breakdown
- `SummaryReportGenerator`: Generates executive summaries with top performers

### Output Correlation Table - CSV Report Generator

| Output | Source Line | Explanation |
|--------|-------------|-------------|
| `CSVReportGenerator: Starting data processing...` | Line 22 | Template method begins execution |
| `Validating data for CSV format` | Line 75 | Abstract method `validateData` called |
| `Invalid record skipped - unknown` | Line 79 | Record without ID filtered out |
| `Validated 6 of 7 records` | Line 26 | Template method reports validation result |
| `Transforming data (sanitizing strings)` | Line 86 | Abstract method `transformData` called |
| `Transformed 6 records` | Line 36 | Template method reports transformation result |
| `Analyzing data for summary` | Line 94 | Abstract method `analyzeData` called |
| `Formatting as CSV` | Line 107 | Abstract method `formatOutput` called |
| `Default post-processing (no action)` | Line 68 | Default hook implementation executes |

### Output Correlation Table - JSON Analytics Processor

| Output | Source Line | Explanation |
|--------|-------------|-------------|
| `Starting data processing...` | Line 22 | Template method begins |
| `Validating data with strict rules` | Line 133 | Stricter validation than CSV |
| `Pre-processing enabled` | Line 30 | Hook method `shouldPreprocess()` returns true |
| `Collecting unique categories` | Line 127 | Custom pre-processing step |
| `Found 4 unique categories` | Line 129 | Categories collected for analysis |
| `Normalizing values` | Line 148 | Values normalized to 0-100 scale |
| `Performing category analysis` | Line 157 | Category-wise statistics calculated |
| `Formatting as JSON` | Line 178 | Output formatted as JSON |
| `Post-processing - validating JSON output` | Line 183 | Custom post-processing validates JSON |
| `JSON validation passed` | Line 186 | Validation successful |

### Output Correlation Table - Summary Report Generator

| Output | Source Line | Explanation |
|--------|-------------|-------------|
| `Quick validation` | Line 196 | Minimal validation requirements |
| `Sorting by value descending` | Line 201 | Transform sorts for top performers |
| `Generating executive summary` | Line 206 | Analysis focuses on summary metrics |
| `Formatting as executive summary` | Line 224 | Human-readable report format |
| `Post-processing - checking report length` | Line 246 | Custom post-processing counts lines |
| `Report contains 15 lines` | Line 248 | Reports line count |

### Hook Methods Comparison

| Hook Method | CSVReportGenerator | JSONAnalyticsProcessor | SummaryReportGenerator |
|-------------|-------------------|----------------------|----------------------|
| `shouldPreprocess()` | false (default) | **true** (overridden) | false (default) |
| `preprocess()` | Not called | Collects categories | Not called |
| `postProcess()` | Default (no action) | Validates JSON | Counts lines |

### Key Pattern Characteristics

#### 1. Algorithm Invariance
The template method (`processData`) guarantees the same sequence of operations across all implementations:
- Validation always happens before transformation
- Analysis always uses transformed data
- Formatting always uses analysis results

#### 2. Selective Override
Each subclass only overrides the methods relevant to its purpose:
- All override the four abstract methods (required)
- Only `JSONAnalyticsProcessor` enables pre-processing
- `CSVReportGenerator` uses default post-processing

#### 3. Code Reuse
The abstract class handles:
- Logging the workflow progress
- Calling hooks at appropriate times
- Managing the data flow between steps

### Transformation Examples

#### CSV Report Generator
```
Input:  { name: "Consulting, Inc" }
Output: { name: "Consulting; Inc" }  // Comma escaped
```

#### JSON Analytics Processor
```
Input values:  [1500, 2300, 800, 3200, 1100, 2800]
Max value:     3200
Output values: [47, 72, 25, 100, 34, 88]  // Normalized to 0-100
```

#### Summary Report Generator
```
Input order:  [R001, R002, R003, R004, R005, R006]
Output order: [R004, R006, R002, R001, R005, R003]  // Sorted by value desc
```

### Use Cases for Template Method Pattern

- **Report Generation**: Different formats (PDF, CSV, Excel) with same data processing
- **Data Import/Export**: Various file formats with consistent validation
- **Build Systems**: Different platforms with same build steps
- **Test Frameworks**: Setup, execute, teardown with custom test logic
- **Game AI**: Different characters with same decision-making flow
- **ETL Pipelines**: Extract, Transform, Load with varying implementations

### Benefits Demonstrated

1. **Eliminates Code Duplication**: Common algorithm logic is in one place (base class)
2. **Easy Extension**: New report types only need to implement abstract methods
3. **Consistent Behavior**: All processors follow the same workflow
4. **Controlled Flexibility**: Hooks allow optional customization at specific points
5. **Polymorphism**: All processors can be used interchangeably through base class interface
