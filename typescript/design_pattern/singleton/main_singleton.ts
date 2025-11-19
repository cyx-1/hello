/**
 * Singleton Design Pattern in TypeScript
 *
 * The Singleton pattern ensures a class has only one instance
 * and provides a global point of access to it.
 */

// Classic Singleton implementation
class DatabaseConnection {
    private static instance: DatabaseConnection | null = null;
    private connectionId: string;
    private queryCount: number = 0;

    // Private constructor prevents direct instantiation
    private constructor() {
        this.connectionId = `conn_${Math.random().toString(36).substr(2, 9)}`;
        console.log(`[Line 17] Creating new DatabaseConnection with ID: ${this.connectionId}`);
    }

    // Static method to get the singleton instance
    public static getInstance(): DatabaseConnection {
        if (!DatabaseConnection.instance) {
            console.log("[Line 22] No instance exists, creating new one...");
            DatabaseConnection.instance = new DatabaseConnection();
        } else {
            console.log("[Line 25] Returning existing instance...");
        }
        return DatabaseConnection.instance;
    }

    public query(sql: string): string {
        this.queryCount++;
        const result = `Result from ${this.connectionId} (Query #${this.queryCount}): ${sql}`;
        console.log(`[Line 33] ${result}`);
        return result;
    }

    public getConnectionId(): string {
        return this.connectionId;
    }

    public getQueryCount(): number {
        return this.queryCount;
    }
}

// Modern TypeScript Singleton using a module pattern
class Logger {
    private static instance: Logger;
    private logs: string[] = [];

    private constructor() {
        console.log("[Line 51] Logger singleton initialized");
    }

    public static getInstance(): Logger {
        if (!Logger.instance) {
            Logger.instance = new Logger();
        }
        return Logger.instance;
    }

    public log(message: string): void {
        const timestamp = new Date().toISOString();
        const entry = `[${timestamp}] ${message}`;
        this.logs.push(entry);
        console.log(`[Line 64] ${entry}`);
    }

    public getLogs(): string[] {
        return [...this.logs];
    }

    public getLogCount(): number {
        return this.logs.length;
    }
}

// Demonstration
function main(): void {
    console.log("=== Singleton Pattern Demonstration ===\n");

    // Demo 1: DatabaseConnection Singleton
    console.log("--- Database Connection Singleton ---");

    const db1 = DatabaseConnection.getInstance();
    const db2 = DatabaseConnection.getInstance();
    const db3 = DatabaseConnection.getInstance();

    console.log(`\n[Line 86] db1 connection ID: ${db1.getConnectionId()}`);
    console.log(`[Line 87] db2 connection ID: ${db2.getConnectionId()}`);
    console.log(`[Line 88] db3 connection ID: ${db3.getConnectionId()}`);
    console.log(`[Line 89] Are db1 and db2 the same instance? ${db1 === db2}`);
    console.log(`[Line 90] Are db2 and db3 the same instance? ${db2 === db3}`);

    // Execute queries through different references
    db1.query("SELECT * FROM users");
    db2.query("INSERT INTO orders VALUES (1, 'item')");
    db3.query("UPDATE products SET price = 100");

    console.log(`\n[Line 97] Total queries executed: ${db1.getQueryCount()}`);

    // Demo 2: Logger Singleton
    console.log("\n--- Logger Singleton ---");

    const logger1 = Logger.getInstance();
    const logger2 = Logger.getInstance();

    logger1.log("Application started");
    logger2.log("User logged in");
    logger1.log("Processing request");

    console.log(`\n[Line 109] logger1 log count: ${logger1.getLogCount()}`);
    console.log(`[Line 110] logger2 log count: ${logger2.getLogCount()}`);
    console.log(`[Line 111] Are logger1 and logger2 the same? ${logger1 === logger2}`);

    console.log("\n=== End of Demonstration ===");
}

main();
