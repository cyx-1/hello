# Observer Design Pattern in TypeScript

The Observer pattern defines a one-to-many dependency between objects so that when one object (the subject) changes state, all its dependents (observers) are notified and updated automatically. This pattern is fundamental for implementing distributed event handling systems, where an object needs to notify other objects without making assumptions about what those objects are.

This implementation demonstrates a Stock Market Monitoring System where multiple investors and news agencies subscribe to receive real-time stock price updates.

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
2    * Observer Design Pattern in TypeScript
3    *
4    * The Observer pattern defines a one-to-many dependency between objects
5    * so that when one object changes state, all its dependents are notified
6    * and updated automatically.
7    */
8
9   // Observer interface - defines the update method that all observers must implement
10  interface Observer {
11      update(stockSymbol: string, price: number): void;
12      getName(): string;
13  }
14
15  // Subject interface - defines methods for managing observers
16  interface Subject {
17      attach(observer: Observer): void;
18      detach(observer: Observer): void;
19      notify(): void;
20  }
21
22  // Concrete Subject - Stock Market that notifies observers of price changes
23  class StockMarket implements Subject {
24      private observers: Observer[] = [];
25      private stocks: Map<string, number> = new Map();
26
27      public attach(observer: Observer): void {
28          const isExist = this.observers.includes(observer);
29          if (isExist) {
30              console.log(`[Line 28] StockMarket: ${observer.getName()} is already subscribed.`);
31              return;
32          }
33          this.observers.push(observer);
34          console.log(`[Line 32] StockMarket: ${observer.getName()} has been subscribed.`);
35      }
36
37      public detach(observer: Observer): void {
38          const observerIndex = this.observers.indexOf(observer);
39          if (observerIndex === -1) {
40              console.log(`[Line 37] StockMarket: ${observer.getName()} was not found.`);
41              return;
42          }
43          this.observers.splice(observerIndex, 1);
44          console.log(`[Line 41] StockMarket: ${observer.getName()} has been unsubscribed.`);
45      }
46
47      public notify(): void {
48          console.log(`[Line 45] StockMarket: Notifying ${this.observers.length} observer(s)...`);
49          for (const observer of this.observers) {
50              for (const [symbol, price] of this.stocks) {
51                  observer.update(symbol, price);
52              }
53          }
54      }
55
56      // Business logic method to update stock prices
57      public setStockPrice(symbol: string, price: number): void {
58          const oldPrice = this.stocks.get(symbol);
59          this.stocks.set(symbol, price);
60
61          if (oldPrice !== undefined) {
62              const change = ((price - oldPrice) / oldPrice * 100).toFixed(2);
63              console.log(`[Line 59] StockMarket: ${symbol} price updated from $${oldPrice.toFixed(2)} to $${price.toFixed(2)} (${change}%)`);
64          } else {
65              console.log(`[Line 61] StockMarket: ${symbol} added at $${price.toFixed(2)}`);
66          }
67
68          this.notify();
69      }
70
71      public getObserverCount(): number {
72          return this.observers.length;
73      }
74  }
75
76  // Concrete Observer 1 - Individual Investor
77  class IndividualInvestor implements Observer {
78      private name: string;
79      private portfolio: Map<string, number> = new Map();
80      private alertThreshold: number;
81
82      constructor(name: string, alertThreshold: number = 5) {
83          this.name = name;
84          this.alertThreshold = alertThreshold;
85          console.log(`[Line 79] IndividualInvestor: ${name} created with ${alertThreshold}% alert threshold`);
86      }
87
88      public update(stockSymbol: string, price: number): void {
89          const previousPrice = this.portfolio.get(stockSymbol);
90
91          if (previousPrice !== undefined) {
92              const changePercent = ((price - previousPrice) / previousPrice) * 100;
93              if (Math.abs(changePercent) >= this.alertThreshold) {
94                  console.log(`[Line 87] ${this.name}: ALERT! ${stockSymbol} changed by ${changePercent.toFixed(2)}% (now $${price.toFixed(2)})`);
95              } else {
96                  console.log(`[Line 89] ${this.name}: ${stockSymbol} updated to $${price.toFixed(2)} (within threshold)`);
97              }
98          } else {
99              console.log(`[Line 92] ${this.name}: Tracking new stock ${stockSymbol} at $${price.toFixed(2)}`);
100         }
101
102         this.portfolio.set(stockSymbol, price);
103     }
104
105     public getName(): string {
106         return this.name;
107     }
108 }
109
110 // Concrete Observer 2 - Institutional Investor
111 class InstitutionalInvestor implements Observer {
112     private name: string;
113     private watchlist: string[];
114     private priceHistory: Map<string, number[]> = new Map();
115
116     constructor(name: string, watchlist: string[]) {
117         this.name = name;
118         this.watchlist = watchlist;
119         console.log(`[Line 111] InstitutionalInvestor: ${name} created, watching: ${watchlist.join(", ")}`);
120     }
121
122     public update(stockSymbol: string, price: number): void {
123         if (!this.watchlist.includes(stockSymbol)) {
124             console.log(`[Line 116] ${this.name}: Ignoring ${stockSymbol} (not in watchlist)`);
125             return;
126         }
127
128         const history = this.priceHistory.get(stockSymbol) || [];
129         history.push(price);
130         this.priceHistory.set(stockSymbol, history);
131
132         const avgPrice = history.reduce((a, b) => a + b, 0) / history.length;
133         console.log(`[Line 124] ${this.name}: ${stockSymbol} = $${price.toFixed(2)} | Avg: $${avgPrice.toFixed(2)} | Data points: ${history.length}`);
134     }
135
136     public getName(): string {
137         return this.name;
138     }
139 }
140
141 // Concrete Observer 3 - News Agency
142 class NewsAgency implements Observer {
143     private name: string;
144     private significantChangeThreshold: number;
145     private lastReportedPrices: Map<string, number> = new Map();
146
147     constructor(name: string, significantChangeThreshold: number = 10) {
148         this.name = name;
149         this.significantChangeThreshold = significantChangeThreshold;
150         console.log(`[Line 140] NewsAgency: ${name} created with ${significantChangeThreshold}% significance threshold`);
151     }
152
153     public update(stockSymbol: string, price: number): void {
154         const lastPrice = this.lastReportedPrices.get(stockSymbol);
155
156         if (lastPrice !== undefined) {
157             const changePercent = ((price - lastPrice) / lastPrice) * 100;
158             if (Math.abs(changePercent) >= this.significantChangeThreshold) {
159                 const direction = changePercent > 0 ? "SURGES" : "PLUMMETS";
160                 console.log(`[Line 150] ${this.name}: BREAKING NEWS - ${stockSymbol} ${direction} ${Math.abs(changePercent).toFixed(1)}% to $${price.toFixed(2)}!`);
161                 this.lastReportedPrices.set(stockSymbol, price);
162             } else {
163                 console.log(`[Line 153] ${this.name}: ${stockSymbol} at $${price.toFixed(2)} (no significant news)`);
164             }
165         } else {
166             console.log(`[Line 156] ${this.name}: Initial report - ${stockSymbol} trading at $${price.toFixed(2)}`);
167             this.lastReportedPrices.set(stockSymbol, price);
168         }
169     }
170
171     public getName(): string {
172         return this.name;
173     }
174 }
175
176 // Demonstration
177 function main(): void {
178     console.log("=== Observer Pattern Demonstration ===");
179     console.log("=== Stock Market Monitoring System ===\n");
180
181     // Create the subject (stock market)
182     const stockMarket = new StockMarket();
183     console.log("[Line 172] Created StockMarket instance\n");
184
185     // Create observers
186     console.log("--- Creating Observers ---");
187     const alice = new IndividualInvestor("Alice", 5);
188     const bob = new IndividualInvestor("Bob", 3);
189     const hedgeFund = new InstitutionalInvestor("AlphaCapital", ["AAPL", "GOOGL"]);
190     const newsAgency = new NewsAgency("MarketWatch", 8);
191     console.log("");
192
193     // Subscribe observers to the stock market
194     console.log("--- Subscribing Observers ---");
195     stockMarket.attach(alice);
196     stockMarket.attach(bob);
197     stockMarket.attach(hedgeFund);
198     stockMarket.attach(newsAgency);
199     console.log(`[Line 187] Total observers: ${stockMarket.getObserverCount()}\n`);
200
201     // Try to subscribe an existing observer
202     console.log("--- Attempting Duplicate Subscription ---");
203     stockMarket.attach(alice);
204     console.log("");
205
206     // Initial stock prices
207     console.log("--- Setting Initial Stock Prices ---");
208     stockMarket.setStockPrice("AAPL", 150.00);
209     console.log("");
210
211     stockMarket.setStockPrice("GOOGL", 2800.00);
212     console.log("");
213
214     stockMarket.setStockPrice("TSLA", 250.00);
215     console.log("");
216
217     // Update stock prices - small change
218     console.log("--- Small Price Update (within thresholds) ---");
219     stockMarket.setStockPrice("AAPL", 152.00);
220     console.log("");
221
222     // Update stock prices - significant change
223     console.log("--- Significant Price Update ---");
224     stockMarket.setStockPrice("AAPL", 165.00);
225     console.log("");
226
227     // Unsubscribe Bob
228     console.log("--- Unsubscribing Bob ---");
229     stockMarket.detach(bob);
230     console.log(`[Line 217] Remaining observers: ${stockMarket.getObserverCount()}\n`);
231
232     // Another update after Bob unsubscribed
233     console.log("--- Price Update After Bob Unsubscribed ---");
234     stockMarket.setStockPrice("GOOGL", 3100.00);
235     console.log("");
236
237     // Try to unsubscribe non-existent observer
238     console.log("--- Attempting to Unsubscribe Non-existent Observer ---");
239     const phantom = new IndividualInvestor("Phantom", 1);
240     stockMarket.detach(phantom);
241     console.log("");
242
243     // Unsubscribe all remaining observers
244     console.log("--- Unsubscribing All Remaining Observers ---");
245     stockMarket.detach(alice);
246     stockMarket.detach(hedgeFund);
247     stockMarket.detach(newsAgency);
248     console.log(`[Line 235] Final observer count: ${stockMarket.getObserverCount()}\n`);
249
250     // Final update with no observers
251     console.log("--- Price Update With No Observers ---");
252     stockMarket.setStockPrice("TSLA", 275.00);
253     console.log("");
254
255     console.log("=== End of Demonstration ===");
256 }
257
258 main();
```

## Program Output

```
=== Observer Pattern Demonstration ===
=== Stock Market Monitoring System ===

[Line 172] Created StockMarket instance

--- Creating Observers ---
[Line 79] IndividualInvestor: Alice created with 5% alert threshold
[Line 79] IndividualInvestor: Bob created with 3% alert threshold
[Line 111] InstitutionalInvestor: AlphaCapital created, watching: AAPL, GOOGL
[Line 140] NewsAgency: MarketWatch created with 8% significance threshold

--- Subscribing Observers ---
[Line 32] StockMarket: Alice has been subscribed.
[Line 32] StockMarket: Bob has been subscribed.
[Line 32] StockMarket: AlphaCapital has been subscribed.
[Line 32] StockMarket: MarketWatch has been subscribed.
[Line 187] Total observers: 4

--- Attempting Duplicate Subscription ---
[Line 28] StockMarket: Alice is already subscribed.

--- Setting Initial Stock Prices ---
[Line 61] StockMarket: AAPL added at $150.00
[Line 45] StockMarket: Notifying 4 observer(s)...
[Line 92] Alice: Tracking new stock AAPL at $150.00
[Line 92] Bob: Tracking new stock AAPL at $150.00
[Line 124] AlphaCapital: AAPL = $150.00 | Avg: $150.00 | Data points: 1
[Line 156] MarketWatch: Initial report - AAPL trading at $150.00

[Line 61] StockMarket: GOOGL added at $2800.00
[Line 45] StockMarket: Notifying 4 observer(s)...
[Line 89] Alice: AAPL updated to $150.00 (within threshold)
[Line 92] Alice: Tracking new stock GOOGL at $2800.00
[Line 89] Bob: AAPL updated to $150.00 (within threshold)
[Line 92] Bob: Tracking new stock GOOGL at $2800.00
[Line 124] AlphaCapital: AAPL = $150.00 | Avg: $150.00 | Data points: 2
[Line 124] AlphaCapital: GOOGL = $2800.00 | Avg: $2800.00 | Data points: 1
[Line 153] MarketWatch: AAPL at $150.00 (no significant news)
[Line 156] MarketWatch: Initial report - GOOGL trading at $2800.00

[Line 61] StockMarket: TSLA added at $250.00
[Line 45] StockMarket: Notifying 4 observer(s)...
[Line 89] Alice: AAPL updated to $150.00 (within threshold)
[Line 89] Alice: GOOGL updated to $2800.00 (within threshold)
[Line 92] Alice: Tracking new stock TSLA at $250.00
[Line 89] Bob: AAPL updated to $150.00 (within threshold)
[Line 89] Bob: GOOGL updated to $2800.00 (within threshold)
[Line 92] Bob: Tracking new stock TSLA at $250.00
[Line 124] AlphaCapital: AAPL = $150.00 | Avg: $150.00 | Data points: 3
[Line 124] AlphaCapital: GOOGL = $2800.00 | Avg: $2800.00 | Data points: 2
[Line 116] AlphaCapital: Ignoring TSLA (not in watchlist)
[Line 153] MarketWatch: AAPL at $150.00 (no significant news)
[Line 153] MarketWatch: GOOGL at $2800.00 (no significant news)
[Line 156] MarketWatch: Initial report - TSLA trading at $250.00

--- Small Price Update (within thresholds) ---
[Line 59] StockMarket: AAPL price updated from $150.00 to $152.00 (1.33%)
[Line 45] StockMarket: Notifying 4 observer(s)...
[Line 89] Alice: AAPL updated to $152.00 (within threshold)
[Line 89] Alice: GOOGL updated to $2800.00 (within threshold)
[Line 89] Alice: TSLA updated to $250.00 (within threshold)
[Line 89] Bob: AAPL updated to $152.00 (within threshold)
[Line 89] Bob: GOOGL updated to $2800.00 (within threshold)
[Line 89] Bob: TSLA updated to $250.00 (within threshold)
[Line 124] AlphaCapital: AAPL = $152.00 | Avg: $150.50 | Data points: 4
[Line 124] AlphaCapital: GOOGL = $2800.00 | Avg: $2800.00 | Data points: 3
[Line 116] AlphaCapital: Ignoring TSLA (not in watchlist)
[Line 153] MarketWatch: AAPL at $152.00 (no significant news)
[Line 153] MarketWatch: GOOGL at $2800.00 (no significant news)
[Line 153] MarketWatch: TSLA at $250.00 (no significant news)

--- Significant Price Update ---
[Line 59] StockMarket: AAPL price updated from $152.00 to $165.00 (8.55%)
[Line 45] StockMarket: Notifying 4 observer(s)...
[Line 87] Alice: ALERT! AAPL changed by 8.55% (now $165.00)
[Line 89] Alice: GOOGL updated to $2800.00 (within threshold)
[Line 89] Alice: TSLA updated to $250.00 (within threshold)
[Line 87] Bob: ALERT! AAPL changed by 8.55% (now $165.00)
[Line 89] Bob: GOOGL updated to $2800.00 (within threshold)
[Line 89] Bob: TSLA updated to $250.00 (within threshold)
[Line 124] AlphaCapital: AAPL = $165.00 | Avg: $153.40 | Data points: 5
[Line 124] AlphaCapital: GOOGL = $2800.00 | Avg: $2800.00 | Data points: 4
[Line 116] AlphaCapital: Ignoring TSLA (not in watchlist)
[Line 150] MarketWatch: BREAKING NEWS - AAPL SURGES 10.0% to $165.00!
[Line 153] MarketWatch: GOOGL at $2800.00 (no significant news)
[Line 153] MarketWatch: TSLA at $250.00 (no significant news)

--- Unsubscribing Bob ---
[Line 41] StockMarket: Bob has been unsubscribed.
[Line 217] Remaining observers: 3

--- Price Update After Bob Unsubscribed ---
[Line 59] StockMarket: GOOGL price updated from $2800.00 to $3100.00 (10.71%)
[Line 45] StockMarket: Notifying 3 observer(s)...
[Line 89] Alice: AAPL updated to $165.00 (within threshold)
[Line 87] Alice: ALERT! GOOGL changed by 10.71% (now $3100.00)
[Line 89] Alice: TSLA updated to $250.00 (within threshold)
[Line 124] AlphaCapital: AAPL = $165.00 | Avg: $155.33 | Data points: 6
[Line 124] AlphaCapital: GOOGL = $3100.00 | Avg: $2860.00 | Data points: 5
[Line 116] AlphaCapital: Ignoring TSLA (not in watchlist)
[Line 153] MarketWatch: AAPL at $165.00 (no significant news)
[Line 150] MarketWatch: BREAKING NEWS - GOOGL SURGES 10.7% to $3100.00!
[Line 153] MarketWatch: TSLA at $250.00 (no significant news)

--- Attempting to Unsubscribe Non-existent Observer ---
[Line 79] IndividualInvestor: Phantom created with 1% alert threshold
[Line 37] StockMarket: Phantom was not found.

--- Unsubscribing All Remaining Observers ---
[Line 41] StockMarket: Alice has been unsubscribed.
[Line 41] StockMarket: AlphaCapital has been unsubscribed.
[Line 41] StockMarket: MarketWatch has been unsubscribed.
[Line 235] Final observer count: 0

--- Price Update With No Observers ---
[Line 59] StockMarket: TSLA price updated from $250.00 to $275.00 (10.00%)
[Line 45] StockMarket: Notifying 0 observer(s)...

=== End of Demonstration ===
```

## Code Analysis and Annotations

### Key Implementation Details

#### Observer Interface (Lines 10-13)
- Defines the contract that all observers must implement
- `update()` method receives stock symbol and price data from the subject
- `getName()` provides identification for logging purposes

#### Subject Interface (Lines 16-20)
- Defines the contract for managing observers
- `attach()` subscribes an observer to notifications
- `detach()` unsubscribes an observer
- `notify()` broadcasts updates to all observers

#### StockMarket (Concrete Subject, Lines 23-74)
- Maintains a list of observers in `observers[]` array
- Stores current stock prices in a `Map<string, number>`
- Prevents duplicate subscriptions (Line 28-31)
- Handles non-existent observer removal gracefully (Line 37-41)
- Automatically notifies observers when prices change (Line 68)

#### Three Types of Concrete Observers

| Observer Type | Behavior | Key Feature |
|--------------|----------|-------------|
| IndividualInvestor (Lines 77-108) | Tracks all stocks, alerts on threshold breach | Personal alert threshold (%) |
| InstitutionalInvestor (Lines 111-139) | Only watches specific stocks, tracks history | Selective watchlist + running average |
| NewsAgency (Lines 142-174) | Reports only significant changes | Higher significance threshold for "breaking news" |

### Output Correlation

| Output Pattern | Source Line | Explanation |
|---------------|-------------|-------------|
| `[Line 32] StockMarket: X has been subscribed` | Lines 195-198 | Four observers attach to the subject |
| `[Line 28] StockMarket: Alice is already subscribed` | Line 203 | Duplicate subscription prevention |
| `[Line 61] StockMarket: X added at $Y` | Lines 208, 211, 214 | Initial stock price registration |
| `[Line 45] StockMarket: Notifying N observer(s)` | Line 68 | Broadcast triggered on each price change |
| `[Line 92] X: Tracking new stock...` | Lines 98-99 | First time an observer sees a stock |
| `[Line 89] X: Y updated to $Z (within threshold)` | Lines 95-96 | Price change below alert threshold |
| `[Line 87] X: ALERT! Y changed by Z%` | Lines 93-94 | Price change exceeds alert threshold |
| `[Line 116] AlphaCapital: Ignoring TSLA` | Lines 123-125 | InstitutionalInvestor filters by watchlist |
| `[Line 150] MarketWatch: BREAKING NEWS` | Lines 158-160 | NewsAgency reports significant change (>8%) |
| `[Line 153] MarketWatch: X at $Y (no significant news)` | Lines 162-163 | Change below news threshold |
| `[Line 41] StockMarket: X has been unsubscribed` | Lines 229, 245-247 | Observer removal from notification list |
| `[Line 37] StockMarket: Phantom was not found` | Line 240 | Attempt to remove non-subscribed observer |

### Observer Behavior Comparison

| Scenario | Alice (5%) | Bob (3%) | AlphaCapital | MarketWatch (8%) |
|----------|------------|----------|--------------|------------------|
| AAPL $150 -> $152 (1.33%) | Within threshold | Within threshold | Records data point 4 | No significant news |
| AAPL $152 -> $165 (8.55%) | ALERT triggered | ALERT triggered | Records data point 5, Avg=$153.40 | BREAKING NEWS |
| GOOGL $2800 -> $3100 (10.71%) | ALERT triggered | Unsubscribed | Records data point 5, Avg=$2860 | BREAKING NEWS |
| TSLA updates | Tracks normally | Tracks normally | Ignores (not in watchlist) | Reports normally |

### Pattern Benefits Demonstrated

1. **Loose Coupling**: The StockMarket doesn't know specific observer implementations
2. **Dynamic Subscription**: Observers can be added/removed at runtime (Bob unsubscribes mid-session)
3. **Custom Reactions**: Each observer type processes updates differently based on its needs
4. **Scalability**: Easy to add new observer types without modifying the subject

### Use Cases

- **Event Systems**: GUI frameworks, DOM events, game engines
- **Publish/Subscribe**: Message queues, notification services
- **Data Binding**: MVC/MVVM frameworks, reactive programming
- **Monitoring**: Stock tickers, sensor networks, system health dashboards
- **Real-time Updates**: Chat applications, collaborative editing, live feeds
