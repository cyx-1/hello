#!/usr/bin/env bun

/**
 * Font Awesome with Bun and TypeScript
 * Demonstrates using Font Awesome icons programmatically
 */

import { icon, library } from '@fortawesome/fontawesome-svg-core';
import {
  faCoffee,
  faHeart,
  faUser,
  faStar,
  faCheckCircle
} from '@fortawesome/free-solid-svg-icons';
import {
  faSmile
} from '@fortawesome/free-regular-svg-icons';
import {
  faGithub,
  faTwitter,
  faLinkedin
} from '@fortawesome/free-brands-svg-icons';
import { writeFileSync } from 'fs';

// Line 26: Add icons to the library
library.add(
  faCoffee,
  faHeart,
  faUser,
  faStar,
  faCheckCircle,
  faSmile,
  faGithub,
  faTwitter,
  faLinkedin
);

console.log('=== Font Awesome Icon Demonstration ===\n');

// Line 42: Generate a solid icon (Coffee)
const coffeeIcon = icon({ prefix: 'fas', iconName: 'coffee' });
console.log('1. Solid Coffee Icon:');
console.log(`   - Icon Name: ${coffeeIcon.iconName}`);
console.log(`   - Prefix: ${coffeeIcon.prefix}`);
console.log(`   - HTML: ${coffeeIcon.html[0].substring(0, 80)}...`);
console.log();

// Line 50: Generate a regular icon (Smile)
const smileIcon = icon({ prefix: 'far', iconName: 'smile' });
console.log('2. Regular Smile Icon:');
console.log(`   - Icon Name: ${smileIcon.iconName}`);
console.log(`   - Prefix: ${smileIcon.prefix}`);
console.log(`   - HTML: ${smileIcon.html[0].substring(0, 80)}...`);
console.log();

// Line 58: Generate brand icons
const githubIcon = icon({ prefix: 'fab', iconName: 'github' });
console.log('3. Brand GitHub Icon:');
console.log(`   - Icon Name: ${githubIcon.iconName}`);
console.log(`   - Prefix: ${githubIcon.prefix}`);
console.log(`   - SVG ViewBox: ${githubIcon.icon[0]}x${githubIcon.icon[1]}`);
console.log();

// Line 66: Create a collection of icons
const icons = [
  { name: 'Heart', icon: icon({ prefix: 'fas', iconName: 'heart' }) },
  { name: 'Star', icon: icon({ prefix: 'fas', iconName: 'star' }) },
  { name: 'User', icon: icon({ prefix: 'fas', iconName: 'user' }) },
  { name: 'Check', icon: icon({ prefix: 'fas', iconName: 'check-circle' }) },
  { name: 'Twitter', icon: icon({ prefix: 'fab', iconName: 'twitter' }) },
  { name: 'LinkedIn', icon: icon({ prefix: 'fab', iconName: 'linkedin' }) },
];

console.log('4. Icon Collection:');
icons.forEach((item, index) => {
  console.log(`   ${index + 1}. ${item.name} (${item.icon.prefix}:${item.icon.iconName})`);
});
console.log();

// Line 82: Generate HTML page with Font Awesome icons
console.log('5. Generating HTML page with icons...');

const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Font Awesome Icons - Bun + TypeScript</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            border-bottom: 3px solid #228ae6;
            padding-bottom: 10px;
        }
        .icon-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .icon-item {
            text-align: center;
            padding: 20px;
            border: 1px solid #e0e0e0;
            border-radius: 5px;
            transition: transform 0.2s;
        }
        .icon-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .icon-item svg {
            width: 48px;
            height: 48px;
            margin-bottom: 10px;
        }
        .icon-name {
            font-size: 14px;
            color: #666;
        }
        .solid { color: #228ae6; }
        .regular { color: #fa5252; }
        .brand { color: #40c057; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎨 Font Awesome Icons Demo</h1>
        <p>Generated using Bun and TypeScript with @fortawesome packages</p>

        <div class="icon-grid">
            <div class="icon-item">
                ${icon({ prefix: 'fas', iconName: 'coffee' }).html[0]}
                <div class="icon-name solid">Coffee (Solid)</div>
            </div>
            <div class="icon-item">
                ${icon({ prefix: 'fas', iconName: 'heart' }).html[0]}
                <div class="icon-name solid">Heart (Solid)</div>
            </div>
            <div class="icon-item">
                ${icon({ prefix: 'fas', iconName: 'star' }).html[0]}
                <div class="icon-name solid">Star (Solid)</div>
            </div>
            <div class="icon-item">
                ${icon({ prefix: 'fas', iconName: 'user' }).html[0]}
                <div class="icon-name solid">User (Solid)</div>
            </div>
            <div class="icon-item">
                ${icon({ prefix: 'fas', iconName: 'check-circle' }).html[0]}
                <div class="icon-name solid">Check (Solid)</div>
            </div>
            <div class="icon-item">
                ${icon({ prefix: 'far', iconName: 'smile' }).html[0]}
                <div class="icon-name regular">Smile (Regular)</div>
            </div>
            <div class="icon-item">
                ${icon({ prefix: 'fab', iconName: 'github' }).html[0]}
                <div class="icon-name brand">GitHub (Brand)</div>
            </div>
            <div class="icon-item">
                ${icon({ prefix: 'fab', iconName: 'twitter' }).html[0]}
                <div class="icon-name brand">Twitter (Brand)</div>
            </div>
            <div class="icon-item">
                ${icon({ prefix: 'fab', iconName: 'linkedin' }).html[0]}
                <div class="icon-name brand">LinkedIn (Brand)</div>
            </div>
        </div>
    </div>
</body>
</html>`;

// Line 195: Write HTML file
writeFileSync('font_awesome_demo.html', htmlContent);
console.log('   ✓ HTML file generated: font_awesome_demo.html');
console.log();

// Line 200: Display icon metadata
console.log('6. Icon Metadata Example (Star icon):');
const starIcon = icon({ prefix: 'fas', iconName: 'star' });
console.log(`   - Abstract: ${JSON.stringify(starIcon.abstract[0]).substring(0, 100)}...`);
console.log(`   - Icon dimensions: ${starIcon.icon[0]} x ${starIcon.icon[1]}`);
console.log(`   - SVG path data length: ${starIcon.icon[4].length} characters`);
console.log();

console.log('=== Demo Complete ===');
console.log('Open font_awesome_demo.html in your browser to see the icons!');
