/**
 * Visitor Design Pattern - Document Processing Example
 *
 * Demonstrates:
 * - Double dispatch mechanism
 * - Multiple visitor implementations
 * - Adding new operations without modifying existing structures
 */

// ============================================================================
// Visitor Interface
// ============================================================================

// [Line 14-19] Visitor interface declares visit methods for each concrete element
interface DocumentVisitor {
  visitParagraph(paragraph: Paragraph): void;
  visitImage(image: Image): void;
  visitTable(table: Table): void;
  visitCodeBlock(codeBlock: CodeBlock): void;
}

// ============================================================================
// Element Interface
// ============================================================================

// [Line 26-28] Element interface declares the accept method for double dispatch
interface DocumentElement {
  accept(visitor: DocumentVisitor): void;
}

// ============================================================================
// Concrete Elements
// ============================================================================

// [Line 35-48] Paragraph element with text content
class Paragraph implements DocumentElement {
  constructor(
    public readonly text: string,
    public readonly style: 'normal' | 'heading' | 'quote' = 'normal'
  ) {}

  // [Line 42-44] Accept method enables double dispatch
  accept(visitor: DocumentVisitor): void {
    console.log(`[Line 43] Paragraph.accept() called - dispatching to visitor`);
    visitor.visitParagraph(this);
  }
}

// [Line 50-64] Image element with source and dimensions
class Image implements DocumentElement {
  constructor(
    public readonly src: string,
    public readonly alt: string,
    public readonly width: number,
    public readonly height: number
  ) {}

  // [Line 59-61] Accept method for Image
  accept(visitor: DocumentVisitor): void {
    console.log(`[Line 60] Image.accept() called - dispatching to visitor`);
    visitor.visitImage(this);
  }
}

// [Line 66-81] Table element with headers and rows
class Table implements DocumentElement {
  constructor(
    public readonly headers: string[],
    public readonly rows: string[][]
  ) {}

  // [Line 73-75] Accept method for Table
  accept(visitor: DocumentVisitor): void {
    console.log(`[Line 74] Table.accept() called - dispatching to visitor`);
    visitor.visitTable(this);
  }

  // [Line 78-80] Helper to get total cell count
  getCellCount(): number {
    return this.headers.length + this.rows.reduce((sum, row) => sum + row.length, 0);
  }
}

// [Line 83-97] CodeBlock element with language and code content
class CodeBlock implements DocumentElement {
  constructor(
    public readonly language: string,
    public readonly code: string
  ) {}

  // [Line 91-93] Accept method for CodeBlock
  accept(visitor: DocumentVisitor): void {
    console.log(`[Line 92] CodeBlock.accept() called - dispatching to visitor`);
    visitor.visitCodeBlock(this);
  }
}

// ============================================================================
// Concrete Visitors
// ============================================================================

// [Line 103-145] HTML Export Visitor - converts elements to HTML
class HTMLExportVisitor implements DocumentVisitor {
  private output: string[] = [];

  // [Line 107-119] Visit Paragraph - convert to HTML paragraph/heading/blockquote
  visitParagraph(paragraph: Paragraph): void {
    console.log(`[Line 108] HTMLExportVisitor.visitParagraph() - style: ${paragraph.style}`);
    switch (paragraph.style) {
      case 'heading':
        this.output.push(`<h1>${paragraph.text}</h1>`);
        break;
      case 'quote':
        this.output.push(`<blockquote>${paragraph.text}</blockquote>`);
        break;
      default:
        this.output.push(`<p>${paragraph.text}</p>`);
    }
  }

  // [Line 122-125] Visit Image - convert to HTML img tag
  visitImage(image: Image): void {
    console.log(`[Line 123] HTMLExportVisitor.visitImage() - src: ${image.src}`);
    this.output.push(`<img src="${image.src}" alt="${image.alt}" width="${image.width}" height="${image.height}" />`);
  }

  // [Line 128-136] Visit Table - convert to HTML table
  visitTable(table: Table): void {
    console.log(`[Line 129] HTMLExportVisitor.visitTable() - ${table.headers.length} columns`);
    const headerRow = `<tr>${table.headers.map(h => `<th>${h}</th>`).join('')}</tr>`;
    const bodyRows = table.rows.map(row =>
      `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`
    ).join('\n    ');
    this.output.push(`<table>\n  <thead>\n    ${headerRow}\n  </thead>\n  <tbody>\n    ${bodyRows}\n  </tbody>\n</table>`);
  }

  // [Line 139-142] Visit CodeBlock - convert to HTML pre/code
  visitCodeBlock(codeBlock: CodeBlock): void {
    console.log(`[Line 140] HTMLExportVisitor.visitCodeBlock() - language: ${codeBlock.language}`);
    this.output.push(`<pre><code class="language-${codeBlock.language}">${codeBlock.code}</code></pre>`);
  }

  // [Line 145-147] Get the accumulated HTML output
  getOutput(): string {
    return this.output.join('\n');
  }
}

// [Line 151-193] Markdown Export Visitor - converts elements to Markdown
class MarkdownExportVisitor implements DocumentVisitor {
  private output: string[] = [];

  // [Line 155-167] Visit Paragraph - convert to Markdown
  visitParagraph(paragraph: Paragraph): void {
    console.log(`[Line 156] MarkdownExportVisitor.visitParagraph() - style: ${paragraph.style}`);
    switch (paragraph.style) {
      case 'heading':
        this.output.push(`# ${paragraph.text}`);
        break;
      case 'quote':
        this.output.push(`> ${paragraph.text}`);
        break;
      default:
        this.output.push(paragraph.text);
    }
  }

  // [Line 170-173] Visit Image - convert to Markdown image
  visitImage(image: Image): void {
    console.log(`[Line 171] MarkdownExportVisitor.visitImage() - alt: ${image.alt}`);
    this.output.push(`![${image.alt}](${image.src})`);
  }

  // [Line 176-184] Visit Table - convert to Markdown table
  visitTable(table: Table): void {
    console.log(`[Line 177] MarkdownExportVisitor.visitTable() - rows: ${table.rows.length}`);
    const header = `| ${table.headers.join(' | ')} |`;
    const separator = `| ${table.headers.map(() => '---').join(' | ')} |`;
    const rows = table.rows.map(row => `| ${row.join(' | ')} |`).join('\n');
    this.output.push(`${header}\n${separator}\n${rows}`);
  }

  // [Line 187-190] Visit CodeBlock - convert to Markdown code block
  visitCodeBlock(codeBlock: CodeBlock): void {
    console.log(`[Line 188] MarkdownExportVisitor.visitCodeBlock() - ${codeBlock.code.split('\n').length} lines`);
    this.output.push(`\`\`\`${codeBlock.language}\n${codeBlock.code}\n\`\`\``);
  }

  // [Line 193-195] Get the accumulated Markdown output
  getOutput(): string {
    return this.output.join('\n\n');
  }
}

// [Line 199-246] Statistics Visitor - collects document statistics
class StatisticsVisitor implements DocumentVisitor {
  private stats = {
    paragraphs: 0,
    images: 0,
    tables: 0,
    codeBlocks: 0,
    wordCount: 0,
    imageArea: 0,
    tableCells: 0,
    codeLines: 0
  };

  // [Line 212-216] Visit Paragraph - count words
  visitParagraph(paragraph: Paragraph): void {
    this.stats.paragraphs++;
    const words = paragraph.text.split(/\s+/).filter(w => w.length > 0).length;
    this.stats.wordCount += words;
    console.log(`[Line 216] StatisticsVisitor.visitParagraph() - ${words} words found`);
  }

  // [Line 219-223] Visit Image - calculate area
  visitImage(image: Image): void {
    this.stats.images++;
    const area = image.width * image.height;
    this.stats.imageArea += area;
    console.log(`[Line 223] StatisticsVisitor.visitImage() - area: ${area}px`);
  }

  // [Line 226-230] Visit Table - count cells
  visitTable(table: Table): void {
    this.stats.tables++;
    const cells = table.getCellCount();
    this.stats.tableCells += cells;
    console.log(`[Line 230] StatisticsVisitor.visitTable() - ${cells} cells`);
  }

  // [Line 233-237] Visit CodeBlock - count lines
  visitCodeBlock(codeBlock: CodeBlock): void {
    this.stats.codeBlocks++;
    const lines = codeBlock.code.split('\n').length;
    this.stats.codeLines += lines;
    console.log(`[Line 237] StatisticsVisitor.visitCodeBlock() - ${lines} lines of ${codeBlock.language}`);
  }

  // [Line 240-242] Get collected statistics
  getStats() {
    return { ...this.stats };
  }
}

// ============================================================================
// Document Structure (Object Structure)
// ============================================================================

// [Line 250-262] Document class holds collection of elements
class Document {
  private elements: DocumentElement[] = [];

  // [Line 254-256] Add element to document
  addElement(element: DocumentElement): void {
    this.elements.push(element);
  }

  // [Line 259-264] Accept visitor for all elements (traversal)
  accept(visitor: DocumentVisitor): void {
    console.log(`[Line 260] Document.accept() - visiting ${this.elements.length} elements`);
    for (const element of this.elements) {
      element.accept(visitor);
    }
  }
}

// ============================================================================
// Main Demonstration
// ============================================================================

function main(): void {
  console.log('='.repeat(70));
  console.log('[Line 273] Visitor Design Pattern - Document Processing Example');
  console.log('='.repeat(70));
  console.log();

  // [Line 277-297] Create a document with various elements
  console.log('[Line 277] Creating document with multiple elements...');
  const doc = new Document();

  doc.addElement(new Paragraph('Welcome to the Visitor Pattern', 'heading'));
  doc.addElement(new Paragraph(
    'The Visitor pattern lets you separate algorithms from the objects on which they operate.',
    'normal'
  ));
  doc.addElement(new Paragraph(
    'Design patterns are reusable solutions to common problems.',
    'quote'
  ));
  doc.addElement(new Image('diagram.png', 'Visitor Pattern UML', 400, 300));
  doc.addElement(new Table(
    ['Pattern', 'Category', 'Intent'],
    [
      ['Visitor', 'Behavioral', 'Separate algorithm from object structure'],
      ['Strategy', 'Behavioral', 'Define family of algorithms'],
      ['Observer', 'Behavioral', 'Define one-to-many dependency']
    ]
  ));
  doc.addElement(new CodeBlock('typescript',
`interface Visitor {
  visit(element: Element): void;
}`));

  console.log('[Line 299] Document created with 6 elements');
  console.log();

  // [Line 302-312] Demonstrate HTML Export Visitor
  console.log('-'.repeat(70));
  console.log('[Line 303] Applying HTMLExportVisitor to document');
  console.log('-'.repeat(70));
  const htmlVisitor = new HTMLExportVisitor();
  doc.accept(htmlVisitor);
  console.log();
  console.log('[Line 309] HTML Output:');
  console.log(htmlVisitor.getOutput());
  console.log();

  // [Line 315-325] Demonstrate Markdown Export Visitor
  console.log('-'.repeat(70));
  console.log('[Line 316] Applying MarkdownExportVisitor to document');
  console.log('-'.repeat(70));
  const markdownVisitor = new MarkdownExportVisitor();
  doc.accept(markdownVisitor);
  console.log();
  console.log('[Line 322] Markdown Output:');
  console.log(markdownVisitor.getOutput());
  console.log();

  // [Line 328-341] Demonstrate Statistics Visitor
  console.log('-'.repeat(70));
  console.log('[Line 329] Applying StatisticsVisitor to document');
  console.log('-'.repeat(70));
  const statsVisitor = new StatisticsVisitor();
  doc.accept(statsVisitor);
  console.log();
  console.log('[Line 335] Document Statistics:');
  const stats = statsVisitor.getStats();
  console.log(`  - Paragraphs: ${stats.paragraphs}`);
  console.log(`  - Images: ${stats.images} (total area: ${stats.imageArea}px)`);
  console.log(`  - Tables: ${stats.tables} (total cells: ${stats.tableCells})`);
  console.log(`  - Code Blocks: ${stats.codeBlocks} (total lines: ${stats.codeLines})`);
  console.log(`  - Total Word Count: ${stats.wordCount}`);
  console.log();

  // [Line 344-356] Demonstrate double dispatch with single element
  console.log('-'.repeat(70));
  console.log('[Line 345] Double Dispatch Demonstration');
  console.log('-'.repeat(70));
  console.log('[Line 348] Creating a single paragraph and applying both visitors:');
  const singleParagraph = new Paragraph('Double dispatch in action!', 'normal');

  console.log('[Line 351] Visitor 1 (HTML):');
  const htmlVisitor2 = new HTMLExportVisitor();
  singleParagraph.accept(htmlVisitor2);
  console.log(`  Result: ${htmlVisitor2.getOutput()}`);

  console.log('[Line 356] Visitor 2 (Markdown):');
  const markdownVisitor2 = new MarkdownExportVisitor();
  singleParagraph.accept(markdownVisitor2);
  console.log(`  Result: ${markdownVisitor2.getOutput()}`);
  console.log();

  console.log('='.repeat(70));
  console.log('[Line 363] Pattern demonstration complete');
  console.log('='.repeat(70));
}

// Run the demonstration
main();
