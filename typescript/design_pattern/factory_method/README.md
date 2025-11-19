# Factory Method Design Pattern in TypeScript

The Factory Method pattern defines an interface for creating objects, but lets subclasses decide which classes to instantiate. It promotes loose coupling by eliminating the need to bind application-specific classes into the code. This pattern is particularly useful when a class cannot anticipate the type of objects it needs to create.

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
2    * Factory Method Design Pattern in TypeScript
3    *
4    * The Factory Method pattern defines an interface for creating objects,
5    * but lets subclasses decide which classes to instantiate. It promotes
6    * loose coupling by eliminating the need to bind application-specific
7    * classes into the code.
8    */
9
10  // Product Interface - defines the interface for objects created by the factory method
11  interface Transport {
12      deliver(): string;
13      getCapacity(): number;
14      getCost(): number;
15  }
16
17  // Concrete Product 1 - Truck
18  class Truck implements Transport {
19      private capacity: number;
20      private costPerUnit: number;
21
22      constructor(capacity: number = 10, costPerUnit: number = 50) {
23          this.capacity = capacity;
24          this.costPerUnit = costPerUnit;
25          console.log(`[Line 24] Truck: Created with capacity ${capacity} tons, cost $${costPerUnit}/unit`);
26      }
27
28      deliver(): string {
29          const message = `Truck: Delivering cargo by land in a box`;
30          console.log(`[Line 29] ${message}`);
31          return message;
32      }
33
34      getCapacity(): number {
35          return this.capacity;
36      }
37
38      getCost(): number {
39          return this.costPerUnit;
40      }
41  }
42
43  // Concrete Product 2 - Ship
44  class Ship implements Transport {
45      private capacity: number;
46      private costPerUnit: number;
47
48      constructor(capacity: number = 500, costPerUnit: number = 20) {
49          this.capacity = capacity;
50          this.costPerUnit = costPerUnit;
51          console.log(`[Line 48] Ship: Created with capacity ${capacity} tons, cost $${costPerUnit}/unit`);
52      }
53
54      deliver(): string {
55          const message = `Ship: Delivering cargo by sea in a container`;
56          console.log(`[Line 53] ${message}`);
57          return message;
58      }
59
60      getCapacity(): number {
61          return this.capacity;
62      }
63
64      getCost(): number {
65          return this.costPerUnit;
66      }
67  }
68
69  // Concrete Product 3 - Airplane
70  class Airplane implements Transport {
71      private capacity: number;
72      private costPerUnit: number;
73
74      constructor(capacity: number = 50, costPerUnit: number = 200) {
75          this.capacity = capacity;
76          this.costPerUnit = costPerUnit;
77          console.log(`[Line 72] Airplane: Created with capacity ${capacity} tons, cost $${costPerUnit}/unit`);
78      }
79
80      deliver(): string {
81          const message = `Airplane: Delivering cargo by air in cargo hold`;
82          console.log(`[Line 77] ${message}`);
83          return message;
84      }
85
86      getCapacity(): number {
87          return this.capacity;
88      }
89
90      getCost(): number {
91          return this.costPerUnit;
92      }
93  }
94
95  // Abstract Creator - declares the factory method
96  abstract class LogisticsCompany {
97      protected companyName: string;
98
99      constructor(name: string) {
100         this.companyName = name;
101         console.log(`[Line 94] LogisticsCompany: "${name}" initialized`);
102     }
103
104     // Factory Method - to be implemented by subclasses
105     abstract createTransport(): Transport;
106
107     // Business logic that uses the factory method
108     planDelivery(cargo: number): void {
109         console.log(`\n[Line 101] ${this.companyName}: Planning delivery for ${cargo} tons of cargo`);
110
111         // Call factory method to create transport
112         const transport = this.createTransport();
113
114         const capacity = transport.getCapacity();
115         const cost = transport.getCost();
116         const trips = Math.ceil(cargo / capacity);
117         const totalCost = trips * cost * capacity;
118
119         console.log(`[Line 110] ${this.companyName}: Transport capacity: ${capacity} tons`);
120         console.log(`[Line 111] ${this.companyName}: Number of trips needed: ${trips}`);
121         console.log(`[Line 112] ${this.companyName}: Cost per unit: $${cost}`);
122         console.log(`[Line 113] ${this.companyName}: Total estimated cost: $${totalCost}`);
123
124         // Perform delivery
125         transport.deliver();
126     }
127
128     // Another business operation using factory method
129     getQuote(cargo: number): number {
130         console.log(`[Line 120] ${this.companyName}: Generating quote for ${cargo} tons`);
131         const transport = this.createTransport();
132         const trips = Math.ceil(cargo / transport.getCapacity());
133         const quote = trips * transport.getCost() * transport.getCapacity();
134         console.log(`[Line 124] ${this.companyName}: Quote generated: $${quote}`);
135         return quote;
136     }
137 }
138
139 // Concrete Creator 1 - Road Logistics
140 class RoadLogistics extends LogisticsCompany {
141     constructor() {
142         super("RoadLogistics Inc.");
143         console.log("[Line 131] RoadLogistics: Specialized in land transportation");
144     }
145
146     createTransport(): Transport {
147         console.log("[Line 135] RoadLogistics: Factory method creating Truck");
148         return new Truck();
149     }
150 }
151
152 // Concrete Creator 2 - Sea Logistics
153 class SeaLogistics extends LogisticsCompany {
154     constructor() {
155         super("SeaLogistics Corp.");
156         console.log("[Line 143] SeaLogistics: Specialized in maritime transportation");
157     }
158
159     createTransport(): Transport {
160         console.log("[Line 147] SeaLogistics: Factory method creating Ship");
161         return new Ship();
162     }
163 }
164
165 // Concrete Creator 3 - Air Logistics
166 class AirLogistics extends LogisticsCompany {
167     constructor() {
168         super("AirLogistics Ltd.");
169         console.log("[Line 155] AirLogistics: Specialized in air freight");
170     }
171
172     createTransport(): Transport {
173         console.log("[Line 159] AirLogistics: Factory method creating Airplane");
174         return new Airplane();
175     }
176 }
177
178 // ============================================================
179 // Second Example: Document Creator Factory
180 // ============================================================
181
182 // Product Interface
183 interface Document {
184     open(): void;
185     save(): void;
186     getExtension(): string;
187 }
188
189 // Concrete Product - PDF Document
190 class PDFDocument implements Document {
191     private name: string;
192
193     constructor(name: string) {
194         this.name = name;
195         console.log(`[Line 180] PDFDocument: Created "${name}"`);
196     }
197
198     open(): void {
199         console.log(`[Line 184] PDFDocument: Opening ${this.name}.pdf in PDF viewer`);
200     }
201
202     save(): void {
203         console.log(`[Line 188] PDFDocument: Saving ${this.name}.pdf with compression`);
204     }
205
206     getExtension(): string {
207         return "pdf";
208     }
209 }
210
211 // Concrete Product - Word Document
212 class WordDocument implements Document {
213     private name: string;
214
215     constructor(name: string) {
216         this.name = name;
217         console.log(`[Line 201] WordDocument: Created "${name}"`);
218     }
219
220     open(): void {
221         console.log(`[Line 205] WordDocument: Opening ${this.name}.docx in Word processor`);
222     }
223
224     save(): void {
225         console.log(`[Line 209] WordDocument: Saving ${this.name}.docx with formatting`);
226     }
227
228     getExtension(): string {
229         return "docx";
230     }
231 }
232
233 // Concrete Product - Spreadsheet Document
234 class SpreadsheetDocument implements Document {
235     private name: string;
236
237     constructor(name: string) {
238         this.name = name;
239         console.log(`[Line 222] SpreadsheetDocument: Created "${name}"`);
240     }
241
242     open(): void {
243         console.log(`[Line 226] SpreadsheetDocument: Opening ${this.name}.xlsx in Spreadsheet app`);
244     }
245
246     save(): void {
247         console.log(`[Line 230] SpreadsheetDocument: Saving ${this.name}.xlsx with formulas`);
248     }
249
250     getExtension(): string {
251         return "xlsx";
252     }
253 }
254
255 // Abstract Creator
256 abstract class DocumentCreator {
257     abstract createDocument(name: string): Document;
258
259     // Template method using factory method
260     newDocument(name: string): Document {
261         console.log(`[Line 243] DocumentCreator: Creating new document "${name}"`);
262         const doc = this.createDocument(name);
263         doc.open();
264         return doc;
265     }
266
267     // Another operation using factory method
268     saveDocument(name: string): void {
269         console.log(`[Line 251] DocumentCreator: Preparing to save "${name}"`);
270         const doc = this.createDocument(name);
271         doc.save();
272         console.log(`[Line 254] DocumentCreator: Document saved as ${name}.${doc.getExtension()}`);
273     }
274 }
275
276 // Concrete Creator - PDF Creator
277 class PDFCreator extends DocumentCreator {
278     createDocument(name: string): Document {
279         console.log(`[Line 260] PDFCreator: Factory method creating PDF document`);
280         return new PDFDocument(name);
281     }
282 }
283
284 // Concrete Creator - Word Creator
285 class WordCreator extends DocumentCreator {
286     createDocument(name: string): Document {
287         console.log(`[Line 268] WordCreator: Factory method creating Word document`);
288         return new WordDocument(name);
289     }
290 }
291
292 // Concrete Creator - Spreadsheet Creator
293 class SpreadsheetCreator extends DocumentCreator {
294     createDocument(name: string): Document {
295         console.log(`[Line 276] SpreadsheetCreator: Factory method creating Spreadsheet`);
296         return new SpreadsheetDocument(name);
297     }
298 }
```

## Program Output

```
=== Factory Method Pattern Demonstration ===

--- Logistics Factory Method Demo ---

[Line 297] Creating logistics companies:
[Line 94] LogisticsCompany: "RoadLogistics Inc." initialized
[Line 131] RoadLogistics: Specialized in land transportation
[Line 94] LogisticsCompany: "SeaLogistics Corp." initialized
[Line 143] SeaLogistics: Specialized in maritime transportation
[Line 94] LogisticsCompany: "AirLogistics Ltd." initialized
[Line 155] AirLogistics: Specialized in air freight

[Line 282] Client: Processing logistics request

[Line 101] RoadLogistics Inc.: Planning delivery for 25 tons of cargo
[Line 135] RoadLogistics: Factory method creating Truck
[Line 24] Truck: Created with capacity 10 tons, cost $50/unit
[Line 110] RoadLogistics Inc.: Transport capacity: 10 tons
[Line 111] RoadLogistics Inc.: Number of trips needed: 3
[Line 112] RoadLogistics Inc.: Cost per unit: $50
[Line 113] RoadLogistics Inc.: Total estimated cost: $1500
[Line 29] Truck: Delivering cargo by land in a box

[Line 282] Client: Processing logistics request

[Line 101] SeaLogistics Corp.: Planning delivery for 1000 tons of cargo
[Line 147] SeaLogistics: Factory method creating Ship
[Line 48] Ship: Created with capacity 500 tons, cost $20/unit
[Line 110] SeaLogistics Corp.: Transport capacity: 500 tons
[Line 111] SeaLogistics Corp.: Number of trips needed: 2
[Line 112] SeaLogistics Corp.: Cost per unit: $20
[Line 113] SeaLogistics Corp.: Total estimated cost: $20000
[Line 53] Ship: Delivering cargo by sea in a container

[Line 282] Client: Processing logistics request

[Line 101] AirLogistics Ltd.: Planning delivery for 100 tons of cargo
[Line 159] AirLogistics: Factory method creating Airplane
[Line 72] Airplane: Created with capacity 50 tons, cost $200/unit
[Line 110] AirLogistics Ltd.: Transport capacity: 50 tons
[Line 111] AirLogistics Ltd.: Number of trips needed: 2
[Line 112] AirLogistics Ltd.: Cost per unit: $200
[Line 113] AirLogistics Ltd.: Total estimated cost: $20000
[Line 77] Airplane: Delivering cargo by air in cargo hold

[Line 307] Comparing quotes for 200 tons:
[Line 120] RoadLogistics Inc.: Generating quote for 200 tons
[Line 135] RoadLogistics: Factory method creating Truck
[Line 24] Truck: Created with capacity 10 tons, cost $50/unit
[Line 124] RoadLogistics Inc.: Quote generated: $10000
[Line 120] SeaLogistics Corp.: Generating quote for 200 tons
[Line 147] SeaLogistics: Factory method creating Ship
[Line 48] Ship: Created with capacity 500 tons, cost $20/unit
[Line 124] SeaLogistics Corp.: Quote generated: $10000
[Line 120] AirLogistics Ltd.: Generating quote for 200 tons
[Line 159] AirLogistics: Factory method creating Airplane
[Line 72] Airplane: Created with capacity 50 tons, cost $200/unit
[Line 124] AirLogistics Ltd.: Quote generated: $40000

[Line 315] Quote Summary:
[Line 317] RoadLogistics Inc.: $10000
[Line 317] SeaLogistics Corp.: $10000
[Line 317] AirLogistics Ltd.: $40000
[Line 321] Best value: RoadLogistics Inc. at $10000


--- Document Creator Factory Method Demo ---

[Line 327] Creating document creators:

[Line 333] Creating and saving documents:

[Line 287] Client: Processing document request
[Line 251] DocumentCreator: Preparing to save "annual_report"
[Line 260] PDFCreator: Factory method creating PDF document
[Line 180] PDFDocument: Created "annual_report"
[Line 188] PDFDocument: Saving annual_report.pdf with compression
[Line 254] DocumentCreator: Document saved as annual_report.pdf

[Line 287] Client: Processing document request
[Line 251] DocumentCreator: Preparing to save "meeting_notes"
[Line 268] WordCreator: Factory method creating Word document
[Line 201] WordDocument: Created "meeting_notes"
[Line 209] WordDocument: Saving meeting_notes.docx with formatting
[Line 254] DocumentCreator: Document saved as meeting_notes.docx

[Line 287] Client: Processing document request
[Line 251] DocumentCreator: Preparing to save "budget_2024"
[Line 276] SpreadsheetCreator: Factory method creating Spreadsheet
[Line 222] SpreadsheetDocument: Created "budget_2024"
[Line 230] SpreadsheetDocument: Saving budget_2024.xlsx with formulas
[Line 254] DocumentCreator: Document saved as budget_2024.xlsx

[Line 339] Demonstrating polymorphism with document creators:
[Line 243] DocumentCreator: Creating new document "summary"
[Line 260] PDFCreator: Factory method creating PDF document
[Line 180] PDFDocument: Created "summary"
[Line 184] PDFDocument: Opening summary.pdf in PDF viewer
[Line 345] Created document with extension: .pdf
[Line 243] DocumentCreator: Creating new document "proposal"
[Line 268] WordCreator: Factory method creating Word document
[Line 201] WordDocument: Created "proposal"
[Line 205] WordDocument: Opening proposal.docx in Word processor
[Line 345] Created document with extension: .docx
[Line 243] DocumentCreator: Creating new document "data"
[Line 276] SpreadsheetCreator: Factory method creating Spreadsheet
[Line 222] SpreadsheetDocument: Created "data"
[Line 226] SpreadsheetDocument: Opening data.xlsx in Spreadsheet app
[Line 345] Created document with extension: .xlsx

=== End of Demonstration ===
```

## Code Analysis and Annotations

### Pattern Components

#### Product Interface (Lines 11-15, 183-187)
- Defines the interface for objects created by the factory method
- `Transport` declares methods: `deliver()`, `getCapacity()`, `getCost()`
- `Document` declares methods: `open()`, `save()`, `getExtension()`

#### Concrete Products (Lines 18-93, 190-253)
- Implement the Product interface with specific behavior
- `Truck`, `Ship`, `Airplane` - different transport types with varying costs and capacities
- `PDFDocument`, `WordDocument`, `SpreadsheetDocument` - different document types with specific handling

#### Abstract Creator (Lines 96-137, 256-274)
- Declares the factory method that returns Product objects
- Contains business logic that works with products through the Product interface
- `LogisticsCompany` with abstract `createTransport()` method
- `DocumentCreator` with abstract `createDocument()` method

#### Concrete Creators (Lines 140-176, 277-298)
- Override the factory method to return specific Product instances
- `RoadLogistics` creates `Truck` instances
- `SeaLogistics` creates `Ship` instances
- `AirLogistics` creates `Airplane` instances
- `PDFCreator`, `WordCreator`, `SpreadsheetCreator` create respective document types

### Output Correlation

| Output Line | Source Line | Explanation |
|-------------|-------------|-------------|
| `LogisticsCompany: "RoadLogistics Inc." initialized` | Line 101 | Base class constructor called via super() |
| `RoadLogistics: Specialized in land transportation` | Line 143 | Concrete creator initialization complete |
| `RoadLogistics: Factory method creating Truck` | Line 147 | Factory method invoked by planDelivery() |
| `Truck: Created with capacity 10 tons` | Line 25 | Concrete product instantiated |
| `RoadLogistics Inc.: Transport capacity: 10 tons` | Line 119 | Business logic uses product via interface |
| `Truck: Delivering cargo by land in a box` | Line 30 | Product performs its operation |
| `PDFCreator: Factory method creating PDF document` | Line 279 | Document factory method invoked |
| `PDFDocument: Saving annual_report.pdf` | Line 203 | Document product saves itself |

### Key Pattern Benefits Demonstrated

#### 1. Loose Coupling (Lines 282-284, 287-289)
Client code `processLogistics()` and `processDocument()` work with abstract types:
```typescript
function processLogistics(company: LogisticsCompany, cargo: number): void {
    company.planDelivery(cargo);  // Works with any LogisticsCompany subclass
}
```

#### 2. Open/Closed Principle
- Adding new transport types (e.g., `DroneLogistics`) requires no changes to existing code
- Just create a new concrete creator and product class

#### 3. Single Responsibility
- Each concrete creator is responsible for creating one type of product
- Business logic is separated from object creation

#### 4. Polymorphism (Lines 307-321, 339-346)
Multiple creators stored in arrays and processed uniformly:
```typescript
const companies: LogisticsCompany[] = [roadCompany, seaCompany, airCompany];
companies.forEach(company => {
    const quote = company.getQuote(200);  // Same interface, different implementations
});
```

### Factory Method Flow

| Step | Code Location | Description |
|------|---------------|-------------|
| 1 | Line 282 | Client calls business method on abstract creator |
| 2 | Line 108-109 | Creator's business method begins execution |
| 3 | Line 112 | Business method calls factory method (`createTransport()`) |
| 4 | Line 147-148 | Concrete creator's factory method creates specific product |
| 5 | Line 24-25 | Concrete product is instantiated |
| 6 | Line 114-117 | Business method uses product through interface |
| 7 | Line 125 | Product performs its operation |

### When to Use Factory Method

1. **Unknown product types at compile time**: When code needs to work with various product families
2. **Framework/library design**: Allow users to extend internal components
3. **Resource reuse**: Reuse existing objects instead of creating new ones
4. **Decoupling**: Separate product construction code from code that uses the product

### Comparison: Factory Method vs Simple Factory

| Aspect | Factory Method | Simple Factory |
|--------|---------------|----------------|
| Structure | Uses inheritance (abstract creator) | Uses a single factory class |
| Flexibility | Subclasses decide product type | Single factory decides |
| Extensibility | Add new creators without modifying existing | Modify factory for new products |
| Use case | When product family varies by subclass | When centralized creation is enough |

### Real-World Applications

- **UI Frameworks**: Creating platform-specific UI elements (buttons, dialogs)
- **Database Connections**: Creating connections for different database vendors
- **Serialization**: Creating different formatters (JSON, XML, CSV)
- **Game Development**: Creating different enemy types, weapons, or power-ups
- **Payment Processing**: Creating processors for different payment methods
