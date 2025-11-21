# Font Awesome with Bun and TypeScript

This example demonstrates how to use Font Awesome icons programmatically with Bun and TypeScript, including solid, regular, and brand icons.

## Requirements

- **Bun**: v1.0.0 or higher
- **Font Awesome**: v6.7.2 or higher
- **TypeScript**: Comes with Bun

## Installation

```bash
bun install
```

## Running the Program

```bash
bun run main_font_awesome.ts
```

## Source Code with Annotations

### Lines 26-35: Adding Icons to the Library

```typescript
26: // Line 26: Add icons to the library
27: library.add(
28:   faCoffee,
29:   faHeart,
30:   faUser,
31:   faStar,
32:   faCheckCircle,
33:   faSmile,
34:   faGithub,
35:   faTwitter,
36:   faLinkedin
37: );
```

**Purpose**: Registers all imported icons with Font Awesome's library for easy access throughout the application.

---

### Lines 42-49: Generating Solid Icons

```typescript
42: // Line 42: Generate a solid icon (Coffee)
43: const coffeeIcon = icon({ prefix: 'fas', iconName: 'coffee' });
44: console.log('1. Solid Coffee Icon:');
45: console.log(`   - Icon Name: ${coffeeIcon.iconName}`);
46: console.log(`   - Prefix: ${coffeeIcon.prefix}`);
47: console.log(`   - HTML: ${coffeeIcon.html[0].substring(0, 80)}...`);
48: console.log();
```

**Output (Lines 1-5)**:
```
1. Solid Coffee Icon:
   - Icon Name: mug-saucer
   - Prefix: fas
   - HTML: <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="mug-sauce...
```

**Explanation**:
- The `icon()` function generates an icon object from the library
- Prefix `fas` = Font Awesome Solid
- Note: `coffee` icon is aliased to `mug-saucer` in Font Awesome 6.x
- The icon object contains HTML SVG markup ready for rendering

---

### Lines 50-57: Generating Regular Icons

```typescript
50: // Line 50: Generate a regular icon (Smile)
51: const smileIcon = icon({ prefix: 'far', iconName: 'smile' });
52: console.log('2. Regular Smile Icon:');
53: console.log(`   - Icon Name: ${smileIcon.iconName}`);
54: console.log(`   - Prefix: ${smileIcon.prefix}`);
55: console.log(`   - HTML: ${smileIcon.html[0].substring(0, 80)}...`);
56: console.log();
```

**Output (Lines 7-10)**:
```
2. Regular Smile Icon:
   - Icon Name: face-smile
   - Prefix: far
   - HTML: <svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="face-smil...
```

**Explanation**:
- Prefix `far` = Font Awesome Regular (outlined style)
- Regular icons have a lighter, outlined appearance compared to solid icons
- The `smile` icon is aliased to `face-smile` in Font Awesome 6.x

---

### Lines 58-65: Generating Brand Icons

```typescript
58: // Line 58: Generate brand icons
59: const githubIcon = icon({ prefix: 'fab', iconName: 'github' });
60: console.log('3. Brand GitHub Icon:');
61: console.log(`   - Icon Name: ${githubIcon.iconName}`);
62: console.log(`   - Prefix: ${githubIcon.prefix}`);
63: console.log(`   - SVG ViewBox: ${githubIcon.icon[0]}x${githubIcon.icon[1]}`);
64: console.log();
```

**Output (Lines 12-15)**:
```
3. Brand GitHub Icon:
   - Icon Name: github
   - Prefix: fab
   - SVG ViewBox: 496x512
```

**Explanation**:
- Prefix `fab` = Font Awesome Brands (company/product logos)
- Brand icons represent logos from various companies and services
- The `icon` property contains SVG metadata: `[width, height, ligatures, unicode, svgPathData]`

---

### Lines 66-81: Creating an Icon Collection

```typescript
66: // Line 66: Create a collection of icons
67: const icons = [
68:   { name: 'Heart', icon: icon({ prefix: 'fas', iconName: 'heart' }) },
69:   { name: 'Star', icon: icon({ prefix: 'fas', iconName: 'star' }) },
70:   { name: 'User', icon: icon({ prefix: 'fas', iconName: 'user' }) },
71:   { name: 'Check', icon: icon({ prefix: 'fas', iconName: 'check-circle' }) },
72:   { name: 'Twitter', icon: icon({ prefix: 'fab', iconName: 'twitter' }) },
73:   { name: 'LinkedIn', icon: icon({ prefix: 'fab', iconName: 'linkedin' }) },
74: ];
75:
76: console.log('4. Icon Collection:');
77: icons.forEach((item, index) => {
78:   console.log(`   ${index + 1}. ${item.name} (${item.icon.prefix}:${item.icon.iconName})`);
79: });
80: console.log();
```

**Output (Lines 17-23)**:
```
4. Icon Collection:
   1. Heart (fas:heart)
   2. Star (fas:star)
   3. User (fas:user)
   4. Check (fas:circle-check)
   5. Twitter (fab:twitter)
   6. LinkedIn (fab:linkedin)
```

**Explanation**:
- Demonstrates batch icon processing
- Useful for creating icon sets or navigation menus
- Note: `check-circle` is aliased to `circle-check` in Font Awesome 6.x

---

### Lines 82-188: Generating HTML with Embedded Icons

```typescript
82: // Line 82: Generate HTML page with Font Awesome icons
83: console.log('5. Generating HTML page with icons...');
84:
85: const htmlContent = `<!DOCTYPE html>
86: <html lang="en">
87: <head>
    ...
148:             <div class="icon-item">
149:                 ${icon({ prefix: 'fas', iconName: 'coffee' }).html[0]}
150:                 <div class="icon-name solid">Coffee (Solid)</div>
151:             </div>
    ...
188: // Line 195: Write HTML file
189: writeFileSync('font_awesome_demo.html', htmlContent);
190: console.log('   ✓ HTML file generated: font_awesome_demo.html');
```

**Output (Lines 25-26)**:
```
5. Generating HTML page with icons...
   ✓ HTML file generated: font_awesome_demo.html
```

**Explanation**:
- Generates a complete HTML page with embedded SVG icons
- No external CSS or JavaScript required - icons are self-contained SVG elements
- The `html[0]` property returns the complete SVG markup string
- Icons are directly embedded in the HTML, making the page standalone

---

### Lines 192-198: Displaying Icon Metadata

```typescript
192: // Line 200: Display icon metadata
193: console.log('6. Icon Metadata Example (Star icon):');
194: const starIcon = icon({ prefix: 'fas', iconName: 'star' });
195: console.log(`   - Abstract: ${JSON.stringify(starIcon.abstract[0]).substring(0, 100)}...`);
196: console.log(`   - Icon dimensions: ${starIcon.icon[0]} x ${starIcon.icon[1]}`);
197: console.log(`   - SVG path data length: ${starIcon.icon[4].length} characters`);
```

**Output (Lines 28-31)**:
```
6. Icon Metadata Example (Star icon):
   - Abstract: {"tag":"svg","attributes":{"aria-hidden":"true","focusable":"false","data-prefix":"fas","data-icon":...
   - Icon dimensions: 576 x 512
   - SVG path data length: 334 characters
```

**Explanation**:
- `abstract`: Abstract syntax tree representation of the icon
- `icon[0]` and `icon[1]`: SVG viewBox dimensions (width x height)
- `icon[4]`: SVG path data string that defines the icon's shape
- This metadata is useful for programmatic icon manipulation

---

## Complete Program Output

```
=== Font Awesome Icon Demonstration ===

1. Solid Coffee Icon:
   - Icon Name: mug-saucer
   - Prefix: fas
   - HTML: <svg aria-hidden="true" focusable="false" data-prefix="fas" data-icon="mug-sauce...

2. Regular Smile Icon:
   - Icon Name: face-smile
   - Prefix: far
   - HTML: <svg aria-hidden="true" focusable="false" data-prefix="far" data-icon="face-smil...

3. Brand GitHub Icon:
   - Icon Name: github
   - Prefix: fab
   - SVG ViewBox: 496x512

4. Icon Collection:
   1. Heart (fas:heart)
   2. Star (fas:star)
   3. User (fas:user)
   4. Check (fas:circle-check)
   5. Twitter (fab:twitter)
   6. LinkedIn (fab:linkedin)

5. Generating HTML page with icons...
   ✓ HTML file generated: font_awesome_demo.html

6. Icon Metadata Example (Star icon):
   - Abstract: {"tag":"svg","attributes":{"aria-hidden":"true","focusable":"false","data-prefix":"fas","data-icon":...
   - Icon dimensions: 576 x 512
   - SVG path data length: 334 characters

=== Demo Complete ===
Open font_awesome_demo.html in your browser to see the icons!
```

## Key Concepts Demonstrated

1. **Icon Library Management** (Lines 26-37): Registering icons with Font Awesome's library system
2. **Icon Prefixes**: Understanding `fas` (solid), `far` (regular), and `fab` (brands)
3. **Programmatic Icon Generation** (Lines 42-65): Creating icon objects using the `icon()` function
4. **Icon Collections** (Lines 66-81): Batch processing multiple icons
5. **HTML Generation** (Lines 82-188): Embedding SVG icons directly into HTML
6. **Icon Metadata** (Lines 192-198): Accessing icon properties for advanced usage

## Font Awesome Icon Structure

Each generated icon object contains:
- `iconName`: The canonical name of the icon
- `prefix`: Icon style prefix (fas, far, fab)
- `html`: Array containing SVG markup strings
- `abstract`: Abstract syntax tree for the icon
- `icon`: Array with `[width, height, ligatures, unicode, svgPathData]`

## Version Notes

- **Bun v1.3.2+** is required for TypeScript execution
- **Font Awesome 6.7.2+** includes icon name changes (coffee → mug-saucer, smile → face-smile)
- No additional build step or transpilation needed - Bun runs TypeScript natively
