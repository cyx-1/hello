/**
 * Template Method Design Pattern in TypeScript
 *
 * The Template Method pattern defines the skeleton of an algorithm in an
 * abstract class, allowing subclasses to override specific steps without
 * changing the algorithm's structure. It lets subclasses redefine certain
 * steps while keeping the overall process intact.
 */

// Sample data types
interface DataRecord {
    id: string;
    name: string;
    value: number;
    category: string;
    timestamp: Date;
}

// Abstract class with Template Method
abstract class DataProcessor {
    // Template Method - defines the algorithm skeleton
    public processData(rawData: DataRecord[]): string {
        console.log(`[Line 22] ${this.constructor.name}: Starting data processing...`);

        // Step 1: Validate data (required)
        const validData = this.validateData(rawData);
        console.log(`[Line 26] ${this.constructor.name}: Validated ${validData.length} of ${rawData.length} records`);

        // Step 2: Hook for pre-processing (optional)
        if (this.shouldPreprocess()) {
            console.log(`[Line 30] ${this.constructor.name}: Pre-processing enabled`);
            this.preprocess(validData);
        }

        // Step 3: Transform data (required)
        const transformedData = this.transformData(validData);
        console.log(`[Line 36] ${this.constructor.name}: Transformed ${transformedData.length} records`);

        // Step 4: Analyze data (required)
        const analysis = this.analyzeData(transformedData);
        console.log(`[Line 40] ${this.constructor.name}: Analysis complete`);

        // Step 5: Format output (required)
        const output = this.formatOutput(analysis);
        console.log(`[Line 44] ${this.constructor.name}: Output formatted`);

        // Step 6: Hook for post-processing (optional)
        this.postProcess(output);

        console.log(`[Line 49] ${this.constructor.name}: Data processing complete`);
        return output;
    }

    // Abstract methods - must be implemented by subclasses
    protected abstract validateData(data: DataRecord[]): DataRecord[];
    protected abstract transformData(data: DataRecord[]): DataRecord[];
    protected abstract analyzeData(data: DataRecord[]): Record<string, unknown>;
    protected abstract formatOutput(analysis: Record<string, unknown>): string;

    // Hook methods - can be overridden by subclasses (optional)
    protected shouldPreprocess(): boolean {
        return false; // Default: no pre-processing
    }

    protected preprocess(data: DataRecord[]): void {
        // Default: do nothing
    }

    protected postProcess(output: string): void {
        console.log(`[Line 68] ${this.constructor.name}: Default post-processing (no action)`);
    }
}

// Concrete Implementation 1: CSV Report Generator
class CSVReportGenerator extends DataProcessor {
    protected validateData(data: DataRecord[]): DataRecord[] {
        console.log(`[Line 75] CSVReportGenerator: Validating data for CSV format`);
        return data.filter(record => {
            const isValid = record.id && record.name && record.value !== undefined;
            if (!isValid) {
                console.log(`[Line 79] CSVReportGenerator: Invalid record skipped - ${record.id || 'unknown'}`);
            }
            return isValid;
        });
    }

    protected transformData(data: DataRecord[]): DataRecord[] {
        console.log(`[Line 86] CSVReportGenerator: Transforming data (sanitizing strings)`);
        return data.map(record => ({
            ...record,
            name: record.name.replace(/,/g, ';'), // Escape commas for CSV
        }));
    }

    protected analyzeData(data: DataRecord[]): Record<string, unknown> {
        console.log(`[Line 94] CSVReportGenerator: Analyzing data for summary`);
        const total = data.reduce((sum, r) => sum + r.value, 0);
        const average = data.length > 0 ? total / data.length : 0;

        return {
            recordCount: data.length,
            totalValue: total,
            averageValue: average.toFixed(2),
            records: data,
        };
    }

    protected formatOutput(analysis: Record<string, unknown>): string {
        console.log(`[Line 107] CSVReportGenerator: Formatting as CSV`);
        const records = analysis.records as DataRecord[];
        const header = 'id,name,value,category,timestamp';
        const rows = records.map(r =>
            `${r.id},${r.name},${r.value},${r.category},${r.timestamp.toISOString()}`
        );
        const summary = `# Summary: ${analysis.recordCount} records, Total: ${analysis.totalValue}, Avg: ${analysis.averageValue}`;

        return `${summary}\n${header}\n${rows.join('\n')}`;
    }
}

// Concrete Implementation 2: JSON Analytics Processor
class JSONAnalyticsProcessor extends DataProcessor {
    private categories: Set<string> = new Set();

    protected shouldPreprocess(): boolean {
        return true; // Override hook: enable pre-processing
    }

    protected preprocess(data: DataRecord[]): void {
        console.log(`[Line 127] JSONAnalyticsProcessor: Collecting unique categories`);
        data.forEach(record => this.categories.add(record.category));
        console.log(`[Line 129] JSONAnalyticsProcessor: Found ${this.categories.size} unique categories`);
    }

    protected validateData(data: DataRecord[]): DataRecord[] {
        console.log(`[Line 133] JSONAnalyticsProcessor: Validating data with strict rules`);
        return data.filter(record => {
            const isValid = record.id &&
                            record.name &&
                            record.value > 0 &&
                            record.category &&
                            record.timestamp instanceof Date;
            if (!isValid) {
                console.log(`[Line 141] JSONAnalyticsProcessor: Rejected record - ${record.id || 'unknown'}`);
            }
            return isValid;
        });
    }

    protected transformData(data: DataRecord[]): DataRecord[] {
        console.log(`[Line 148] JSONAnalyticsProcessor: Normalizing values`);
        const maxValue = Math.max(...data.map(r => r.value));
        return data.map(record => ({
            ...record,
            value: Math.round((record.value / maxValue) * 100), // Normalize to 0-100
        }));
    }

    protected analyzeData(data: DataRecord[]): Record<string, unknown> {
        console.log(`[Line 157] JSONAnalyticsProcessor: Performing category analysis`);

        const categoryStats: Record<string, { count: number; totalValue: number }> = {};

        data.forEach(record => {
            if (!categoryStats[record.category]) {
                categoryStats[record.category] = { count: 0, totalValue: 0 };
            }
            categoryStats[record.category].count++;
            categoryStats[record.category].totalValue += record.value;
        });

        return {
            totalRecords: data.length,
            categories: Array.from(this.categories),
            categoryStats,
            processedAt: new Date().toISOString(),
        };
    }

    protected formatOutput(analysis: Record<string, unknown>): string {
        console.log(`[Line 178] JSONAnalyticsProcessor: Formatting as JSON`);
        return JSON.stringify(analysis, null, 2);
    }

    protected postProcess(output: string): void {
        console.log(`[Line 183] JSONAnalyticsProcessor: Post-processing - validating JSON output`);
        try {
            JSON.parse(output);
            console.log(`[Line 186] JSONAnalyticsProcessor: JSON validation passed`);
        } catch (error) {
            console.log(`[Line 188] JSONAnalyticsProcessor: JSON validation failed!`);
        }
    }
}

// Concrete Implementation 3: Summary Report Generator
class SummaryReportGenerator extends DataProcessor {
    protected validateData(data: DataRecord[]): DataRecord[] {
        console.log(`[Line 196] SummaryReportGenerator: Quick validation`);
        return data.filter(record => record.id && record.value !== undefined);
    }

    protected transformData(data: DataRecord[]): DataRecord[] {
        console.log(`[Line 201] SummaryReportGenerator: Sorting by value descending`);
        return [...data].sort((a, b) => b.value - a.value);
    }

    protected analyzeData(data: DataRecord[]): Record<string, unknown> {
        console.log(`[Line 206] SummaryReportGenerator: Generating executive summary`);

        const total = data.reduce((sum, r) => sum + r.value, 0);
        const topPerformers = data.slice(0, 3);
        const categoryBreakdown: Record<string, number> = {};

        data.forEach(record => {
            categoryBreakdown[record.category] = (categoryBreakdown[record.category] || 0) + record.value;
        });

        return {
            totalRecords: data.length,
            totalValue: total,
            topPerformers: topPerformers.map(r => ({ id: r.id, name: r.name, value: r.value })),
            categoryBreakdown,
        };
    }

    protected formatOutput(analysis: Record<string, unknown>): string {
        console.log(`[Line 224] SummaryReportGenerator: Formatting as executive summary`);

        const topPerformers = analysis.topPerformers as Array<{ id: string; name: string; value: number }>;
        const categoryBreakdown = analysis.categoryBreakdown as Record<string, number>;

        let report = '=== EXECUTIVE SUMMARY ===\n';
        report += `Total Records: ${analysis.totalRecords}\n`;
        report += `Total Value: $${analysis.totalValue}\n\n`;
        report += 'Top Performers:\n';
        topPerformers.forEach((p, i) => {
            report += `  ${i + 1}. ${p.name} (${p.id}): $${p.value}\n`;
        });
        report += '\nCategory Breakdown:\n';
        Object.entries(categoryBreakdown).forEach(([category, value]) => {
            report += `  - ${category}: $${value}\n`;
        });

        return report;
    }

    protected postProcess(output: string): void {
        console.log(`[Line 246] SummaryReportGenerator: Post-processing - checking report length`);
        const lines = output.split('\n').length;
        console.log(`[Line 248] SummaryReportGenerator: Report contains ${lines} lines`);
    }
}

// Demonstration
function main(): void {
    console.log('=== Template Method Pattern Demonstration ===\n');

    // Sample data
    const sampleData: DataRecord[] = [
        { id: 'R001', name: 'Product Alpha', value: 1500, category: 'Electronics', timestamp: new Date('2024-01-15') },
        { id: 'R002', name: 'Service Beta', value: 2300, category: 'Services', timestamp: new Date('2024-01-16') },
        { id: 'R003', name: 'Product Gamma', value: 800, category: 'Electronics', timestamp: new Date('2024-01-17') },
        { id: 'R004', name: 'Consulting, Inc', value: 3200, category: 'Services', timestamp: new Date('2024-01-18') },
        { id: 'R005', name: 'Hardware Delta', value: 1100, category: 'Hardware', timestamp: new Date('2024-01-19') },
        { id: '', name: 'Invalid Record', value: 500, category: 'Other', timestamp: new Date('2024-01-20') }, // Invalid
        { id: 'R006', name: 'Software Epsilon', value: 2800, category: 'Software', timestamp: new Date('2024-01-21') },
    ];

    // Demo 1: CSV Report Generator
    console.log('--- Demo 1: CSV Report Generator ---\n');
    const csvGenerator = new CSVReportGenerator();
    const csvOutput = csvGenerator.processData(sampleData);
    console.log('\nGenerated CSV Report:');
    console.log(csvOutput);

    // Demo 2: JSON Analytics Processor
    console.log('\n\n--- Demo 2: JSON Analytics Processor ---\n');
    const jsonProcessor = new JSONAnalyticsProcessor();
    const jsonOutput = jsonProcessor.processData(sampleData);
    console.log('\nGenerated JSON Analytics:');
    console.log(jsonOutput);

    // Demo 3: Summary Report Generator
    console.log('\n\n--- Demo 3: Summary Report Generator ---\n');
    const summaryGenerator = new SummaryReportGenerator();
    const summaryOutput = summaryGenerator.processData(sampleData);
    console.log('\nGenerated Executive Summary:');
    console.log(summaryOutput);

    // Demonstrate polymorphism
    console.log('\n\n--- Polymorphism Demonstration ---\n');
    const processors: DataProcessor[] = [
        new CSVReportGenerator(),
        new JSONAnalyticsProcessor(),
        new SummaryReportGenerator()
    ];

    const miniData: DataRecord[] = [
        { id: 'M001', name: 'Mini Item', value: 100, category: 'Test', timestamp: new Date() },
    ];

    console.log('Processing same data through all processors:\n');
    processors.forEach((processor, index) => {
        console.log(`\n[Processor ${index + 1}: ${processor.constructor.name}]`);
        processor.processData(miniData);
    });

    console.log('\n\n=== End of Demonstration ===');
}

main();
