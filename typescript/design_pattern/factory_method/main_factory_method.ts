/**
 * Factory Method Design Pattern in TypeScript
 *
 * The Factory Method pattern defines an interface for creating objects,
 * but lets subclasses decide which classes to instantiate. It promotes
 * loose coupling by eliminating the need to bind application-specific
 * classes into the code.
 */

// Product Interface - defines the interface for objects created by the factory method
interface Transport {
    deliver(): string;
    getCapacity(): number;
    getCost(): number;
}

// Concrete Product 1 - Truck
class Truck implements Transport {
    private capacity: number;
    private costPerUnit: number;

    constructor(capacity: number = 10, costPerUnit: number = 50) {
        this.capacity = capacity;
        this.costPerUnit = costPerUnit;
        console.log(`[Line 24] Truck: Created with capacity ${capacity} tons, cost $${costPerUnit}/unit`);
    }

    deliver(): string {
        const message = `Truck: Delivering cargo by land in a box`;
        console.log(`[Line 29] ${message}`);
        return message;
    }

    getCapacity(): number {
        return this.capacity;
    }

    getCost(): number {
        return this.costPerUnit;
    }
}

// Concrete Product 2 - Ship
class Ship implements Transport {
    private capacity: number;
    private costPerUnit: number;

    constructor(capacity: number = 500, costPerUnit: number = 20) {
        this.capacity = capacity;
        this.costPerUnit = costPerUnit;
        console.log(`[Line 48] Ship: Created with capacity ${capacity} tons, cost $${costPerUnit}/unit`);
    }

    deliver(): string {
        const message = `Ship: Delivering cargo by sea in a container`;
        console.log(`[Line 53] ${message}`);
        return message;
    }

    getCapacity(): number {
        return this.capacity;
    }

    getCost(): number {
        return this.costPerUnit;
    }
}

// Concrete Product 3 - Airplane
class Airplane implements Transport {
    private capacity: number;
    private costPerUnit: number;

    constructor(capacity: number = 50, costPerUnit: number = 200) {
        this.capacity = capacity;
        this.costPerUnit = costPerUnit;
        console.log(`[Line 72] Airplane: Created with capacity ${capacity} tons, cost $${costPerUnit}/unit`);
    }

    deliver(): string {
        const message = `Airplane: Delivering cargo by air in cargo hold`;
        console.log(`[Line 77] ${message}`);
        return message;
    }

    getCapacity(): number {
        return this.capacity;
    }

    getCost(): number {
        return this.costPerUnit;
    }
}

// Abstract Creator - declares the factory method
abstract class LogisticsCompany {
    protected companyName: string;

    constructor(name: string) {
        this.companyName = name;
        console.log(`[Line 94] LogisticsCompany: "${name}" initialized`);
    }

    // Factory Method - to be implemented by subclasses
    abstract createTransport(): Transport;

    // Business logic that uses the factory method
    planDelivery(cargo: number): void {
        console.log(`\n[Line 101] ${this.companyName}: Planning delivery for ${cargo} tons of cargo`);

        // Call factory method to create transport
        const transport = this.createTransport();

        const capacity = transport.getCapacity();
        const cost = transport.getCost();
        const trips = Math.ceil(cargo / capacity);
        const totalCost = trips * cost * capacity;

        console.log(`[Line 110] ${this.companyName}: Transport capacity: ${capacity} tons`);
        console.log(`[Line 111] ${this.companyName}: Number of trips needed: ${trips}`);
        console.log(`[Line 112] ${this.companyName}: Cost per unit: $${cost}`);
        console.log(`[Line 113] ${this.companyName}: Total estimated cost: $${totalCost}`);

        // Perform delivery
        transport.deliver();
    }

    // Another business operation using factory method
    getQuote(cargo: number): number {
        console.log(`[Line 120] ${this.companyName}: Generating quote for ${cargo} tons`);
        const transport = this.createTransport();
        const trips = Math.ceil(cargo / transport.getCapacity());
        const quote = trips * transport.getCost() * transport.getCapacity();
        console.log(`[Line 124] ${this.companyName}: Quote generated: $${quote}`);
        return quote;
    }
}

// Concrete Creator 1 - Road Logistics
class RoadLogistics extends LogisticsCompany {
    constructor() {
        super("RoadLogistics Inc.");
        console.log("[Line 131] RoadLogistics: Specialized in land transportation");
    }

    createTransport(): Transport {
        console.log("[Line 135] RoadLogistics: Factory method creating Truck");
        return new Truck();
    }
}

// Concrete Creator 2 - Sea Logistics
class SeaLogistics extends LogisticsCompany {
    constructor() {
        super("SeaLogistics Corp.");
        console.log("[Line 143] SeaLogistics: Specialized in maritime transportation");
    }

    createTransport(): Transport {
        console.log("[Line 147] SeaLogistics: Factory method creating Ship");
        return new Ship();
    }
}

// Concrete Creator 3 - Air Logistics
class AirLogistics extends LogisticsCompany {
    constructor() {
        super("AirLogistics Ltd.");
        console.log("[Line 155] AirLogistics: Specialized in air freight");
    }

    createTransport(): Transport {
        console.log("[Line 159] AirLogistics: Factory method creating Airplane");
        return new Airplane();
    }
}

// ============================================================
// Second Example: Document Creator Factory
// ============================================================

// Product Interface
interface Document {
    open(): void;
    save(): void;
    getExtension(): string;
}

// Concrete Product - PDF Document
class PDFDocument implements Document {
    private name: string;

    constructor(name: string) {
        this.name = name;
        console.log(`[Line 180] PDFDocument: Created "${name}"`);
    }

    open(): void {
        console.log(`[Line 184] PDFDocument: Opening ${this.name}.pdf in PDF viewer`);
    }

    save(): void {
        console.log(`[Line 188] PDFDocument: Saving ${this.name}.pdf with compression`);
    }

    getExtension(): string {
        return "pdf";
    }
}

// Concrete Product - Word Document
class WordDocument implements Document {
    private name: string;

    constructor(name: string) {
        this.name = name;
        console.log(`[Line 201] WordDocument: Created "${name}"`);
    }

    open(): void {
        console.log(`[Line 205] WordDocument: Opening ${this.name}.docx in Word processor`);
    }

    save(): void {
        console.log(`[Line 209] WordDocument: Saving ${this.name}.docx with formatting`);
    }

    getExtension(): string {
        return "docx";
    }
}

// Concrete Product - Spreadsheet Document
class SpreadsheetDocument implements Document {
    private name: string;

    constructor(name: string) {
        this.name = name;
        console.log(`[Line 222] SpreadsheetDocument: Created "${name}"`);
    }

    open(): void {
        console.log(`[Line 226] SpreadsheetDocument: Opening ${this.name}.xlsx in Spreadsheet app`);
    }

    save(): void {
        console.log(`[Line 230] SpreadsheetDocument: Saving ${this.name}.xlsx with formulas`);
    }

    getExtension(): string {
        return "xlsx";
    }
}

// Abstract Creator
abstract class DocumentCreator {
    abstract createDocument(name: string): Document;

    // Template method using factory method
    newDocument(name: string): Document {
        console.log(`[Line 243] DocumentCreator: Creating new document "${name}"`);
        const doc = this.createDocument(name);
        doc.open();
        return doc;
    }

    // Another operation using factory method
    saveDocument(name: string): void {
        console.log(`[Line 251] DocumentCreator: Preparing to save "${name}"`);
        const doc = this.createDocument(name);
        doc.save();
        console.log(`[Line 254] DocumentCreator: Document saved as ${name}.${doc.getExtension()}`);
    }
}

// Concrete Creator - PDF Creator
class PDFCreator extends DocumentCreator {
    createDocument(name: string): Document {
        console.log(`[Line 260] PDFCreator: Factory method creating PDF document`);
        return new PDFDocument(name);
    }
}

// Concrete Creator - Word Creator
class WordCreator extends DocumentCreator {
    createDocument(name: string): Document {
        console.log(`[Line 268] WordCreator: Factory method creating Word document`);
        return new WordDocument(name);
    }
}

// Concrete Creator - Spreadsheet Creator
class SpreadsheetCreator extends DocumentCreator {
    createDocument(name: string): Document {
        console.log(`[Line 276] SpreadsheetCreator: Factory method creating Spreadsheet`);
        return new SpreadsheetDocument(name);
    }
}

// Client code that works with creators through abstract interface
function processLogistics(company: LogisticsCompany, cargo: number): void {
    console.log(`\n[Line 282] Client: Processing logistics request`);
    company.planDelivery(cargo);
}

function processDocument(creator: DocumentCreator, name: string): void {
    console.log(`\n[Line 287] Client: Processing document request`);
    creator.saveDocument(name);
}

// Demonstration
function main(): void {
    console.log("=== Factory Method Pattern Demonstration ===");

    // Demo 1: Logistics Factory Method
    console.log("\n--- Logistics Factory Method Demo ---");

    // Create different logistics companies
    console.log("\n[Line 297] Creating logistics companies:");
    const roadCompany = new RoadLogistics();
    const seaCompany = new SeaLogistics();
    const airCompany = new AirLogistics();

    // Use them through the abstract interface
    processLogistics(roadCompany, 25);
    processLogistics(seaCompany, 1000);
    processLogistics(airCompany, 100);

    // Get quotes from all companies
    console.log("\n[Line 307] Comparing quotes for 200 tons:");
    const companies: LogisticsCompany[] = [roadCompany, seaCompany, airCompany];
    const quotes: { company: string; quote: number }[] = [];

    companies.forEach(company => {
        const quote = company.getQuote(200);
        quotes.push({ company: company["companyName"], quote });
    });

    console.log("\n[Line 315] Quote Summary:");
    quotes.forEach(q => {
        console.log(`[Line 317] ${q.company}: $${q.quote}`);
    });

    // Find cheapest option
    const cheapest = quotes.reduce((min, q) => q.quote < min.quote ? q : min);
    console.log(`[Line 321] Best value: ${cheapest.company} at $${cheapest.quote}`);

    // Demo 2: Document Creator Factory Method
    console.log("\n\n--- Document Creator Factory Method Demo ---");

    // Create different document creators
    console.log("\n[Line 327] Creating document creators:");
    const pdfCreator = new PDFCreator();
    const wordCreator = new WordCreator();
    const spreadsheetCreator = new SpreadsheetCreator();

    // Create and work with documents
    console.log("\n[Line 333] Creating and saving documents:");
    processDocument(pdfCreator, "annual_report");
    processDocument(wordCreator, "meeting_notes");
    processDocument(spreadsheetCreator, "budget_2024");

    // Demonstrate polymorphism
    console.log("\n[Line 339] Demonstrating polymorphism with document creators:");
    const creators: DocumentCreator[] = [pdfCreator, wordCreator, spreadsheetCreator];
    const docNames = ["summary", "proposal", "data"];

    creators.forEach((creator, index) => {
        const doc = creator.newDocument(docNames[index]);
        console.log(`[Line 345] Created document with extension: .${doc.getExtension()}`);
    });

    console.log("\n=== End of Demonstration ===");
}

main();
