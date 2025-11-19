/**
 * Observer Design Pattern in TypeScript
 *
 * The Observer pattern defines a one-to-many dependency between objects
 * so that when one object changes state, all its dependents are notified
 * and updated automatically.
 */

// Observer interface - defines the update method that all observers must implement
interface Observer {
    update(stockSymbol: string, price: number): void;
    getName(): string;
}

// Subject interface - defines methods for managing observers
interface Subject {
    attach(observer: Observer): void;
    detach(observer: Observer): void;
    notify(): void;
}

// Concrete Subject - Stock Market that notifies observers of price changes
class StockMarket implements Subject {
    private observers: Observer[] = [];
    private stocks: Map<string, number> = new Map();

    public attach(observer: Observer): void {
        const isExist = this.observers.includes(observer);
        if (isExist) {
            console.log(`[Line 28] StockMarket: ${observer.getName()} is already subscribed.`);
            return;
        }
        this.observers.push(observer);
        console.log(`[Line 32] StockMarket: ${observer.getName()} has been subscribed.`);
    }

    public detach(observer: Observer): void {
        const observerIndex = this.observers.indexOf(observer);
        if (observerIndex === -1) {
            console.log(`[Line 37] StockMarket: ${observer.getName()} was not found.`);
            return;
        }
        this.observers.splice(observerIndex, 1);
        console.log(`[Line 41] StockMarket: ${observer.getName()} has been unsubscribed.`);
    }

    public notify(): void {
        console.log(`[Line 45] StockMarket: Notifying ${this.observers.length} observer(s)...`);
        for (const observer of this.observers) {
            for (const [symbol, price] of this.stocks) {
                observer.update(symbol, price);
            }
        }
    }

    // Business logic method to update stock prices
    public setStockPrice(symbol: string, price: number): void {
        const oldPrice = this.stocks.get(symbol);
        this.stocks.set(symbol, price);

        if (oldPrice !== undefined) {
            const change = ((price - oldPrice) / oldPrice * 100).toFixed(2);
            console.log(`[Line 59] StockMarket: ${symbol} price updated from $${oldPrice.toFixed(2)} to $${price.toFixed(2)} (${change}%)`);
        } else {
            console.log(`[Line 61] StockMarket: ${symbol} added at $${price.toFixed(2)}`);
        }

        this.notify();
    }

    public getObserverCount(): number {
        return this.observers.length;
    }
}

// Concrete Observer 1 - Individual Investor
class IndividualInvestor implements Observer {
    private name: string;
    private portfolio: Map<string, number> = new Map();
    private alertThreshold: number;

    constructor(name: string, alertThreshold: number = 5) {
        this.name = name;
        this.alertThreshold = alertThreshold;
        console.log(`[Line 79] IndividualInvestor: ${name} created with ${alertThreshold}% alert threshold`);
    }

    public update(stockSymbol: string, price: number): void {
        const previousPrice = this.portfolio.get(stockSymbol);

        if (previousPrice !== undefined) {
            const changePercent = ((price - previousPrice) / previousPrice) * 100;
            if (Math.abs(changePercent) >= this.alertThreshold) {
                console.log(`[Line 87] ${this.name}: ALERT! ${stockSymbol} changed by ${changePercent.toFixed(2)}% (now $${price.toFixed(2)})`);
            } else {
                console.log(`[Line 89] ${this.name}: ${stockSymbol} updated to $${price.toFixed(2)} (within threshold)`);
            }
        } else {
            console.log(`[Line 92] ${this.name}: Tracking new stock ${stockSymbol} at $${price.toFixed(2)}`);
        }

        this.portfolio.set(stockSymbol, price);
    }

    public getName(): string {
        return this.name;
    }
}

// Concrete Observer 2 - Institutional Investor
class InstitutionalInvestor implements Observer {
    private name: string;
    private watchlist: string[];
    private priceHistory: Map<string, number[]> = new Map();

    constructor(name: string, watchlist: string[]) {
        this.name = name;
        this.watchlist = watchlist;
        console.log(`[Line 111] InstitutionalInvestor: ${name} created, watching: ${watchlist.join(", ")}`);
    }

    public update(stockSymbol: string, price: number): void {
        if (!this.watchlist.includes(stockSymbol)) {
            console.log(`[Line 116] ${this.name}: Ignoring ${stockSymbol} (not in watchlist)`);
            return;
        }

        const history = this.priceHistory.get(stockSymbol) || [];
        history.push(price);
        this.priceHistory.set(stockSymbol, history);

        const avgPrice = history.reduce((a, b) => a + b, 0) / history.length;
        console.log(`[Line 124] ${this.name}: ${stockSymbol} = $${price.toFixed(2)} | Avg: $${avgPrice.toFixed(2)} | Data points: ${history.length}`);
    }

    public getName(): string {
        return this.name;
    }
}

// Concrete Observer 3 - News Agency
class NewsAgency implements Observer {
    private name: string;
    private significantChangeThreshold: number;
    private lastReportedPrices: Map<string, number> = new Map();

    constructor(name: string, significantChangeThreshold: number = 10) {
        this.name = name;
        this.significantChangeThreshold = significantChangeThreshold;
        console.log(`[Line 140] NewsAgency: ${name} created with ${significantChangeThreshold}% significance threshold`);
    }

    public update(stockSymbol: string, price: number): void {
        const lastPrice = this.lastReportedPrices.get(stockSymbol);

        if (lastPrice !== undefined) {
            const changePercent = ((price - lastPrice) / lastPrice) * 100;
            if (Math.abs(changePercent) >= this.significantChangeThreshold) {
                const direction = changePercent > 0 ? "SURGES" : "PLUMMETS";
                console.log(`[Line 150] ${this.name}: BREAKING NEWS - ${stockSymbol} ${direction} ${Math.abs(changePercent).toFixed(1)}% to $${price.toFixed(2)}!`);
                this.lastReportedPrices.set(stockSymbol, price);
            } else {
                console.log(`[Line 153] ${this.name}: ${stockSymbol} at $${price.toFixed(2)} (no significant news)`);
            }
        } else {
            console.log(`[Line 156] ${this.name}: Initial report - ${stockSymbol} trading at $${price.toFixed(2)}`);
            this.lastReportedPrices.set(stockSymbol, price);
        }
    }

    public getName(): string {
        return this.name;
    }
}

// Demonstration
function main(): void {
    console.log("=== Observer Pattern Demonstration ===");
    console.log("=== Stock Market Monitoring System ===\n");

    // Create the subject (stock market)
    const stockMarket = new StockMarket();
    console.log("[Line 172] Created StockMarket instance\n");

    // Create observers
    console.log("--- Creating Observers ---");
    const alice = new IndividualInvestor("Alice", 5);
    const bob = new IndividualInvestor("Bob", 3);
    const hedgeFund = new InstitutionalInvestor("AlphaCapital", ["AAPL", "GOOGL"]);
    const newsAgency = new NewsAgency("MarketWatch", 8);
    console.log("");

    // Subscribe observers to the stock market
    console.log("--- Subscribing Observers ---");
    stockMarket.attach(alice);
    stockMarket.attach(bob);
    stockMarket.attach(hedgeFund);
    stockMarket.attach(newsAgency);
    console.log(`[Line 187] Total observers: ${stockMarket.getObserverCount()}\n`);

    // Try to subscribe an existing observer
    console.log("--- Attempting Duplicate Subscription ---");
    stockMarket.attach(alice);
    console.log("");

    // Initial stock prices
    console.log("--- Setting Initial Stock Prices ---");
    stockMarket.setStockPrice("AAPL", 150.00);
    console.log("");

    stockMarket.setStockPrice("GOOGL", 2800.00);
    console.log("");

    stockMarket.setStockPrice("TSLA", 250.00);
    console.log("");

    // Update stock prices - small change
    console.log("--- Small Price Update (within thresholds) ---");
    stockMarket.setStockPrice("AAPL", 152.00);
    console.log("");

    // Update stock prices - significant change
    console.log("--- Significant Price Update ---");
    stockMarket.setStockPrice("AAPL", 165.00);
    console.log("");

    // Unsubscribe Bob
    console.log("--- Unsubscribing Bob ---");
    stockMarket.detach(bob);
    console.log(`[Line 217] Remaining observers: ${stockMarket.getObserverCount()}\n`);

    // Another update after Bob unsubscribed
    console.log("--- Price Update After Bob Unsubscribed ---");
    stockMarket.setStockPrice("GOOGL", 3100.00);
    console.log("");

    // Try to unsubscribe non-existent observer
    console.log("--- Attempting to Unsubscribe Non-existent Observer ---");
    const phantom = new IndividualInvestor("Phantom", 1);
    stockMarket.detach(phantom);
    console.log("");

    // Unsubscribe all remaining observers
    console.log("--- Unsubscribing All Remaining Observers ---");
    stockMarket.detach(alice);
    stockMarket.detach(hedgeFund);
    stockMarket.detach(newsAgency);
    console.log(`[Line 235] Final observer count: ${stockMarket.getObserverCount()}\n`);

    // Final update with no observers
    console.log("--- Price Update With No Observers ---");
    stockMarket.setStockPrice("TSLA", 275.00);
    console.log("");

    console.log("=== End of Demonstration ===");
}

main();
