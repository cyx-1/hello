# Visitor Design Pattern - TypeScript Implementation

## Pattern Description

The **Visitor** design pattern is a behavioral pattern that lets you separate algorithms from the objects on which they operate. It allows adding new operations to existing object structures without modifying those structures.

### Key Concepts

- **Double Dispatch**: The operation executed depends on both the type of visitor and the type of element being visited
- **Open/Closed Principle**: Add new operations by creating new visitors without modifying existing element classes
- **Separation of Concerns**: Keep related operations together in visitor classes rather than spreading them across element classes

### Use Cases

- Performing operations on elements of a complex object structure (e.g., AST, document tree)
- When you need many distinct operations on objects and want to avoid "polluting" their classes
- When the object structure rarely changes but you often need to define new operations

## Requirements

- **Node.js**: 18.0 or higher
- **TypeScript**: 5.3 or higher
- **npm**: 9.0 or higher

## How to Run

```bash
# Install dependencies
npm install

# Build and run
npm run start

# Or for development with ts-node (if installed)
npm run dev
```

## Source Code

```typescript
     1	/**
     2	 * Visitor Design Pattern - Document Processing Example
     3	 *
     4	 * Demonstrates:
     5	 * - Double dispatch mechanism
     6	 * - Multiple visitor implementations
     7	 * - Adding new operations without modifying existing structures
     8	 */
     9
    10	// ============================================================================
    11	// Visitor Interface
    12	// ============================================================================
    13
    14	// [Line 14-19] Visitor interface declares visit methods for each concrete element
    15	interface DocumentVisitor {
    16	  visitParagraph(paragraph: Paragraph): void;
    17	  visitImage(image: Image): void;
    18	  visitTable(table: Table): void;
    19	  visitCodeBlock(codeBlock: CodeBlock): void;
    20	}
    21
    22	// ============================================================================
    23	// Element Interface
    24	// ============================================================================
    25
    26	// [Line 26-28] Element interface declares the accept method for double dispatch
    27	interface DocumentElement {
    28	  accept(visitor: DocumentVisitor): void;
    29	}
    30
    31	// ============================================================================
    32	// Concrete Elements
    33	// ============================================================================
    34
    35	// [Line 35-48] Paragraph element with text content
    36	class Paragraph implements DocumentElement {
    37	  constructor(
    38	    public readonly text: string,
    39	    public readonly style: 'normal' | 'heading' | 'quote' = 'normal'
    40	  ) {}
    41
    42	  // [Line 42-44] Accept method enables double dispatch
    43	  accept(visitor: DocumentVisitor): void {
    44	    console.log(`[Line 43] Paragraph.accept() called - dispatching to visitor`);
    45	    visitor.visitParagraph(this);
    46	  }
    47	}
    48
    49	// [Line 50-64] Image element with source and dimensions
    50	class Image implements DocumentElement {
    51	  constructor(
    52	    public readonly src: string,
    53	    public readonly alt: string,
    54	    public readonly width: number,
    55	    public readonly height: number
    56	  ) {}
    57
    58	  // [Line 59-61] Accept method for Image
    59	  accept(visitor: DocumentVisitor): void {
    60	    console.log(`[Line 60] Image.accept() called - dispatching to visitor`);
    61	    visitor.visitImage(this);
    62	  }
    63	}
    64
    65	// [Line 66-81] Table element with headers and rows
    66	class Table implements DocumentElement {
    67	  constructor(
    68	    public readonly headers: string[],
    69	    public readonly rows: string[][]
    70	  ) {}
    71
    72	  // [Line 73-75] Accept method for Table
    73	  accept(visitor: DocumentVisitor): void {
    74	    console.log(`[Line 74] Table.accept() called - dispatching to visitor`);
    75	    visitor.visitTable(this);
    76	  }
    77
    78	  // [Line 78-80] Helper to get total cell count
    79	  getCellCount(): number {
    80	    return this.headers.length + this.rows.reduce((sum, row) => sum + row.length, 0);
    81	  }
    82	}
    83
    84	// [Line 83-97] CodeBlock element with language and code content
    85	class CodeBlock implements DocumentElement {
    86	  constructor(
    87	    public readonly language: string,
    88	    public readonly code: string
    89	  ) {}
    90
    91	  // [Line 91-93] Accept method for CodeBlock
    92	  accept(visitor: DocumentVisitor): void {
    93	    console.log(`[Line 92] CodeBlock.accept() called - dispatching to visitor`);
    94	    visitor.visitCodeBlock(this);
    95	  }
    96	}
    97
    98	// ============================================================================
    99	// Concrete Visitors
   100	// ============================================================================
   101
   102	// [Line 103-145] HTML Export Visitor - converts elements to HTML
   103	class HTMLExportVisitor implements DocumentVisitor {
   104	  private output: string[] = [];
   105
   106	  // [Line 107-119] Visit Paragraph - convert to HTML paragraph/heading/blockquote
   107	  visitParagraph(paragraph: Paragraph): void {
   108	    console.log(`[Line 108] HTMLExportVisitor.visitParagraph() - style: ${paragraph.style}`);
   109	    switch (paragraph.style) {
   110	      case 'heading':
   111	        this.output.push(`<h1>${paragraph.text}</h1>`);
   112	        break;
   113	      case 'quote':
   114	        this.output.push(`<blockquote>${paragraph.text}</blockquote>`);
   115	        break;
   116	      default:
   117	        this.output.push(`<p>${paragraph.text}</p>`);
   118	    }
   119	  }
   120
   121	  // [Line 122-125] Visit Image - convert to HTML img tag
   122	  visitImage(image: Image): void {
   123	    console.log(`[Line 123] HTMLExportVisitor.visitImage() - src: ${image.src}`);
   124	    this.output.push(`<img src="${image.src}" alt="${image.alt}" width="${image.width}" height="${image.height}" />`);
   125	  }
   126
   127	  // [Line 128-136] Visit Table - convert to HTML table
   128	  visitTable(table: Table): void {
   129	    console.log(`[Line 129] HTMLExportVisitor.visitTable() - ${table.headers.length} columns`);
   130	    const headerRow = `<tr>${table.headers.map(h => `<th>${h}</th>`).join('')}</tr>`;
   131	    const bodyRows = table.rows.map(row =>
   132	      `<tr>${row.map(cell => `<td>${cell}</td>`).join('')}</tr>`
   133	    ).join('\n    ');
   134	    this.output.push(`<table>\n  <thead>\n    ${headerRow}\n  </thead>\n  <tbody>\n    ${bodyRows}\n  </tbody>\n</table>`);
   135	  }
   136
   137	  // [Line 139-142] Visit CodeBlock - convert to HTML pre/code
   138	  visitCodeBlock(codeBlock: CodeBlock): void {
   139	    console.log(`[Line 140] HTMLExportVisitor.visitCodeBlock() - language: ${codeBlock.language}`);
   140	    this.output.push(`<pre><code class="language-${codeBlock.language}">${codeBlock.code}</code></pre>`);
   141	  }
   142
   143	  // [Line 145-147] Get the accumulated HTML output
   144	  getOutput(): string {
   145	    return this.output.join('\n');
   146	  }
   147	}
   148
   149	// [Line 151-193] Markdown Export Visitor - converts elements to Markdown
   150	class MarkdownExportVisitor implements DocumentVisitor {
   151	  private output: string[] = [];
   152
   153	  // [Line 155-167] Visit Paragraph - convert to Markdown
   154	  visitParagraph(paragraph: Paragraph): void {
   155	    console.log(`[Line 156] MarkdownExportVisitor.visitParagraph() - style: ${paragraph.style}`);
   156	    switch (paragraph.style) {
   157	      case 'heading':
   158	        this.output.push(`# ${paragraph.text}`);
   159	        break;
   160	      case 'quote':
   161	        this.output.push(`> ${paragraph.text}`);
   162	        break;
   163	      default:
   164	        this.output.push(paragraph.text);
   165	    }
   166	  }
   167
   168	  // [Line 170-173] Visit Image - convert to Markdown image
   169	  visitImage(image: Image): void {
   170	    console.log(`[Line 171] MarkdownExportVisitor.visitImage() - alt: ${image.alt}`);
   171	    this.output.push(`![${image.alt}](${image.src})`);
   172	  }
   173
   174	  // [Line 176-184] Visit Table - convert to Markdown table
   175	  visitTable(table: Table): void {
   176	    console.log(`[Line 177] MarkdownExportVisitor.visitTable() - rows: ${table.rows.length}`);
   177	    const header = `| ${table.headers.join(' | ')} |`;
   178	    const separator = `| ${table.headers.map(() => '---').join(' | ')} |`;
   179	    const rows = table.rows.map(row => `| ${row.join(' | ')} |`).join('\n');
   180	    this.output.push(`${header}\n${separator}\n${rows}`);
   181	  }
   182
   183	  // [Line 187-190] Visit CodeBlock - convert to Markdown code block
   184	  visitCodeBlock(codeBlock: CodeBlock): void {
   185	    console.log(`[Line 188] MarkdownExportVisitor.visitCodeBlock() - ${codeBlock.code.split('\n').length} lines`);
   186	    this.output.push(`\`\`\`${codeBlock.language}\n${codeBlock.code}\n\`\`\``);
   187	  }
   188
   189	  // [Line 193-195] Get the accumulated Markdown output
   190	  getOutput(): string {
   191	    return this.output.join('\n\n');
   192	  }
   193	}
   194
   195	// [Line 199-246] Statistics Visitor - collects document statistics
   196	class StatisticsVisitor implements DocumentVisitor {
   197	  private stats = {
   198	    paragraphs: 0,
   199	    images: 0,
   200	    tables: 0,
   201	    codeBlocks: 0,
   202	    wordCount: 0,
   203	    imageArea: 0,
   204	    tableCells: 0,
   205	    codeLines: 0
   206	  };
   207
   208	  // [Line 212-216] Visit Paragraph - count words
   209	  visitParagraph(paragraph: Paragraph): void {
   210	    this.stats.paragraphs++;
   211	    const words = paragraph.text.split(/\s+/).filter(w => w.length > 0).length;
   212	    this.stats.wordCount += words;
   213	    console.log(`[Line 216] StatisticsVisitor.visitParagraph() - ${words} words found`);
   214	  }
   215
   216	  // [Line 219-223] Visit Image - calculate area
   217	  visitImage(image: Image): void {
   218	    this.stats.images++;
   219	    const area = image.width * image.height;
   220	    this.stats.imageArea += area;
   221	    console.log(`[Line 223] StatisticsVisitor.visitImage() - area: ${area}px`);
   222	  }
   223
   224	  // [Line 226-230] Visit Table - count cells
   225	  visitTable(table: Table): void {
   226	    this.stats.tables++;
   227	    const cells = table.getCellCount();
   228	    this.stats.tableCells += cells;
   229	    console.log(`[Line 230] StatisticsVisitor.visitTable() - ${cells} cells`);
   230	  }
   231
   232	  // [Line 233-237] Visit CodeBlock - count lines
   233	  visitCodeBlock(codeBlock: CodeBlock): void {
   234	    this.stats.codeBlocks++;
   235	    const lines = codeBlock.code.split('\n').length;
   236	    this.stats.codeLines += lines;
   237	    console.log(`[Line 237] StatisticsVisitor.visitCodeBlock() - ${lines} lines of ${codeBlock.language}`);
   238	  }
   239
   240	  // [Line 240-242] Get collected statistics
   241	  getStats() {
   242	    return { ...this.stats };
   243	  }
   244	}
   245
   246	// ============================================================================
   247	// Document Structure (Object Structure)
   248	// ============================================================================
   249
   250	// [Line 250-262] Document class holds collection of elements
   251	class Document {
   252	  private elements: DocumentElement[] = [];
   253
   254	  // [Line 254-256] Add element to document
   255	  addElement(element: DocumentElement): void {
   256	    this.elements.push(element);
   257	  }
   258
   259	  // [Line 259-264] Accept visitor for all elements (traversal)
   260	  accept(visitor: DocumentVisitor): void {
   261	    console.log(`[Line 260] Document.accept() - visiting ${this.elements.length} elements`);
   262	    for (const element of this.elements) {
   263	      element.accept(visitor);
   264	    }
   265	  }
   266	}
```

## Program Output

```
======================================================================
[Line 273] Visitor Design Pattern - Document Processing Example
======================================================================

[Line 277] Creating document with multiple elements...
[Line 299] Document created with 6 elements

----------------------------------------------------------------------
[Line 303] Applying HTMLExportVisitor to document
----------------------------------------------------------------------
[Line 260] Document.accept() - visiting 6 elements
[Line 43] Paragraph.accept() called - dispatching to visitor
[Line 108] HTMLExportVisitor.visitParagraph() - style: heading
[Line 43] Paragraph.accept() called - dispatching to visitor
[Line 108] HTMLExportVisitor.visitParagraph() - style: normal
[Line 43] Paragraph.accept() called - dispatching to visitor
[Line 108] HTMLExportVisitor.visitParagraph() - style: quote
[Line 60] Image.accept() called - dispatching to visitor
[Line 123] HTMLExportVisitor.visitImage() - src: diagram.png
[Line 74] Table.accept() called - dispatching to visitor
[Line 129] HTMLExportVisitor.visitTable() - 3 columns
[Line 92] CodeBlock.accept() called - dispatching to visitor
[Line 140] HTMLExportVisitor.visitCodeBlock() - language: typescript

[Line 309] HTML Output:
<h1>Welcome to the Visitor Pattern</h1>
<p>The Visitor pattern lets you separate algorithms from the objects on which they operate.</p>
<blockquote>Design patterns are reusable solutions to common problems.</blockquote>
<img src="diagram.png" alt="Visitor Pattern UML" width="400" height="300" />
<table>
  <thead>
    <tr><th>Pattern</th><th>Category</th><th>Intent</th></tr>
  </thead>
  <tbody>
    <tr><td>Visitor</td><td>Behavioral</td><td>Separate algorithm from object structure</td></tr>
    <tr><td>Strategy</td><td>Behavioral</td><td>Define family of algorithms</td></tr>
    <tr><td>Observer</td><td>Behavioral</td><td>Define one-to-many dependency</td></tr>
  </tbody>
</table>
<pre><code class="language-typescript">interface Visitor {
  visit(element: Element): void;
}</code></pre>

----------------------------------------------------------------------
[Line 316] Applying MarkdownExportVisitor to document
----------------------------------------------------------------------
[Line 260] Document.accept() - visiting 6 elements
[Line 43] Paragraph.accept() called - dispatching to visitor
[Line 156] MarkdownExportVisitor.visitParagraph() - style: heading
[Line 43] Paragraph.accept() called - dispatching to visitor
[Line 156] MarkdownExportVisitor.visitParagraph() - style: normal
[Line 43] Paragraph.accept() called - dispatching to visitor
[Line 156] MarkdownExportVisitor.visitParagraph() - style: quote
[Line 60] Image.accept() called - dispatching to visitor
[Line 171] MarkdownExportVisitor.visitImage() - alt: Visitor Pattern UML
[Line 74] Table.accept() called - dispatching to visitor
[Line 177] MarkdownExportVisitor.visitTable() - rows: 3
[Line 92] CodeBlock.accept() called - dispatching to visitor
[Line 188] MarkdownExportVisitor.visitCodeBlock() - 3 lines

[Line 322] Markdown Output:
# Welcome to the Visitor Pattern

The Visitor pattern lets you separate algorithms from the objects on which they operate.

> Design patterns are reusable solutions to common problems.

![Visitor Pattern UML](diagram.png)

| Pattern | Category | Intent |
| --- | --- | --- |
| Visitor | Behavioral | Separate algorithm from object structure |
| Strategy | Behavioral | Define family of algorithms |
| Observer | Behavioral | Define one-to-many dependency |

```typescript
interface Visitor {
  visit(element: Element): void;
}
```

----------------------------------------------------------------------
[Line 329] Applying StatisticsVisitor to document
----------------------------------------------------------------------
[Line 260] Document.accept() - visiting 6 elements
[Line 43] Paragraph.accept() called - dispatching to visitor
[Line 216] StatisticsVisitor.visitParagraph() - 5 words found
[Line 43] Paragraph.accept() called - dispatching to visitor
[Line 216] StatisticsVisitor.visitParagraph() - 14 words found
[Line 43] Paragraph.accept() called - dispatching to visitor
[Line 216] StatisticsVisitor.visitParagraph() - 8 words found
[Line 60] Image.accept() called - dispatching to visitor
[Line 223] StatisticsVisitor.visitImage() - area: 120000px
[Line 74] Table.accept() called - dispatching to visitor
[Line 230] StatisticsVisitor.visitTable() - 12 cells
[Line 92] CodeBlock.accept() called - dispatching to visitor
[Line 237] StatisticsVisitor.visitCodeBlock() - 3 lines of typescript

[Line 335] Document Statistics:
  - Paragraphs: 3
  - Images: 1 (total area: 120000px)
  - Tables: 1 (total cells: 12)
  - Code Blocks: 1 (total lines: 3)
  - Total Word Count: 27

----------------------------------------------------------------------
[Line 345] Double Dispatch Demonstration
----------------------------------------------------------------------
[Line 348] Creating a single paragraph and applying both visitors:
[Line 351] Visitor 1 (HTML):
[Line 43] Paragraph.accept() called - dispatching to visitor
[Line 108] HTMLExportVisitor.visitParagraph() - style: normal
  Result: <p>Double dispatch in action!</p>
[Line 356] Visitor 2 (Markdown):
[Line 43] Paragraph.accept() called - dispatching to visitor
[Line 156] MarkdownExportVisitor.visitParagraph() - style: normal
  Result: Double dispatch in action!

======================================================================
[Line 363] Pattern demonstration complete
======================================================================
```

## Code Analysis and Annotations

### Pattern Structure Overview

| Component | Source Lines | Purpose |
|-----------|-------------|---------|
| `DocumentVisitor` | 14-20 | Visitor interface with visit methods for each element type |
| `DocumentElement` | 26-29 | Element interface with accept method for double dispatch |
| `Paragraph` | 35-47 | Concrete element representing text content |
| `Image` | 49-63 | Concrete element representing images |
| `Table` | 65-82 | Concrete element representing tabular data |
| `CodeBlock` | 84-96 | Concrete element representing code snippets |
| `HTMLExportVisitor` | 102-147 | Visitor that converts elements to HTML |
| `MarkdownExportVisitor` | 149-193 | Visitor that converts elements to Markdown |
| `StatisticsVisitor` | 195-244 | Visitor that collects document statistics |
| `Document` | 250-266 | Object structure holding elements |

### Double Dispatch Flow Analysis

The double dispatch mechanism is the core of the Visitor pattern. Here's how it works:

| Step | Output Line | Source Line | Description |
|------|-------------|-------------|-------------|
| 1 | `Document.accept() - visiting 6 elements` | 260 | Document starts traversal |
| 2 | `Paragraph.accept() called - dispatching to visitor` | 43 | First dispatch: element.accept(visitor) |
| 3 | `HTMLExportVisitor.visitParagraph() - style: heading` | 108 | Second dispatch: visitor.visitParagraph(this) |

### HTMLExportVisitor Output Correlation

| Element | Accept (Line) | Visit (Line) | HTML Output |
|---------|--------------|--------------|-------------|
| Paragraph (heading) | 43 | 108 | `<h1>Welcome to the Visitor Pattern</h1>` |
| Paragraph (normal) | 43 | 108 | `<p>The Visitor pattern lets you...</p>` |
| Paragraph (quote) | 43 | 108 | `<blockquote>Design patterns are...</blockquote>` |
| Image | 60 | 123 | `<img src="diagram.png" alt="Visitor Pattern UML".../>` |
| Table | 74 | 129 | `<table>...<tr><th>Pattern</th>...</table>` |
| CodeBlock | 92 | 140 | `<pre><code class="language-typescript">...</code></pre>` |

### MarkdownExportVisitor Output Correlation

| Element | Accept (Line) | Visit (Line) | Markdown Output |
|---------|--------------|--------------|-----------------|
| Paragraph (heading) | 43 | 156 | `# Welcome to the Visitor Pattern` |
| Paragraph (normal) | 43 | 156 | Plain text paragraph |
| Paragraph (quote) | 43 | 156 | `> Design patterns are...` |
| Image | 60 | 171 | `![Visitor Pattern UML](diagram.png)` |
| Table | 74 | 177 | Markdown table with `|` separators |
| CodeBlock | 92 | 188 | Fenced code block with language |

### StatisticsVisitor Calculations

| Element | Accept (Line) | Visit (Line) | Calculation | Result |
|---------|--------------|--------------|-------------|--------|
| Paragraph 1 | 43 | 216 | Word count | 5 words |
| Paragraph 2 | 43 | 216 | Word count | 14 words |
| Paragraph 3 | 43 | 216 | Word count | 8 words |
| Image | 60 | 223 | 400 x 300 | 120000px area |
| Table | 74 | 230 | 3 headers + 9 cells | 12 cells |
| CodeBlock | 92 | 237 | Line count | 3 lines |

### Key Pattern Benefits Demonstrated

| Benefit | How Demonstrated |
|---------|------------------|
| **Open/Closed Principle** | Three different visitors operate on same elements without modifying element classes |
| **Single Responsibility** | Each visitor handles one specific concern (HTML export, Markdown export, statistics) |
| **Double Dispatch** | Lines 43/108 show element dispatching to visitor, then visitor dispatching back with typed method |
| **Easy Extension** | Adding a new visitor (e.g., `PDFExportVisitor`) requires no changes to existing code |

### Adding New Operations

To add a new operation (e.g., PDF export), you only need to:

1. Create a new visitor class implementing `DocumentVisitor`
2. Implement visit methods for each element type
3. No changes required to any existing element classes

### Adding New Elements

To add a new element type (e.g., `Video`):

1. Create the new element class implementing `DocumentElement`
2. Add `visitVideo()` method to `DocumentVisitor` interface
3. Implement `visitVideo()` in all existing visitor classes

This is the trade-off of the Visitor pattern: adding new elements requires modifying all visitors.

## Version Requirements

This implementation uses the following TypeScript features:

| Feature | Minimum Version |
|---------|-----------------|
| `readonly` class properties | TypeScript 2.0+ |
| Strict null checks | TypeScript 2.0+ |
| Union types | TypeScript 1.4+ |
| ES2022 target | Node.js 18+ |

The code is compatible with TypeScript 5.3+ and Node.js 18+ as specified in the requirements.
