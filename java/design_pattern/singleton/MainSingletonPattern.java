/**
 * Comprehensive demonstration of the Singleton Pattern in Java
 *
 * The Singleton pattern ensures a class has only one instance and provides
 * a global point of access to it.
 */

// 1. Eager Initialization Singleton
class EagerSingleton {
    // Instance is created at class loading time
    private static final EagerSingleton instance = new EagerSingleton();

    private EagerSingleton() {
        System.out.println("EagerSingleton instance created");
    }

    public static EagerSingleton getInstance() {
        return instance;
    }

    public void showMessage() {
        System.out.println("Hello from EagerSingleton: " + this.hashCode());
    }
}

// 2. Lazy Initialization Singleton (NOT thread-safe)
class LazySingleton {
    private static LazySingleton instance;

    private LazySingleton() {
        System.out.println("LazySingleton instance created");
    }

    // This is not thread-safe - multiple threads could create multiple instances
    public static LazySingleton getInstance() {
        if (instance == null) {
            instance = new LazySingleton();
        }
        return instance;
    }

    public void showMessage() {
        System.out.println("Hello from LazySingleton: " + this.hashCode());
    }
}

// 3. Thread-Safe Lazy Initialization (synchronized method)
class ThreadSafeSingleton {
    private static ThreadSafeSingleton instance;

    private ThreadSafeSingleton() {
        System.out.println("ThreadSafeSingleton instance created");
    }

    // Synchronized method - thread-safe but performance overhead
    public static synchronized ThreadSafeSingleton getInstance() {
        if (instance == null) {
            instance = new ThreadSafeSingleton();
        }
        return instance;
    }

    public void showMessage() {
        System.out.println("Hello from ThreadSafeSingleton: " + this.hashCode());
    }
}

// 4. Double-Checked Locking Singleton
class DoubleCheckedSingleton {
    // volatile keyword ensures visibility of changes across threads
    private static volatile DoubleCheckedSingleton instance;

    private DoubleCheckedSingleton() {
        System.out.println("DoubleCheckedSingleton instance created");
    }

    // Double-checked locking - reduces synchronization overhead
    public static DoubleCheckedSingleton getInstance() {
        if (instance == null) {
            synchronized (DoubleCheckedSingleton.class) {
                if (instance == null) {
                    instance = new DoubleCheckedSingleton();
                }
            }
        }
        return instance;
    }

    public void showMessage() {
        System.out.println("Hello from DoubleCheckedSingleton: " + this.hashCode());
    }
}

// 5. Bill Pugh Singleton (using inner static helper class)
class BillPughSingleton {
    private BillPughSingleton() {
        System.out.println("BillPughSingleton instance created");
    }

    // Inner static class is loaded only when getInstance() is called
    private static class SingletonHelper {
        private static final BillPughSingleton INSTANCE = new BillPughSingleton();
    }

    public static BillPughSingleton getInstance() {
        return SingletonHelper.INSTANCE;
    }

    public void showMessage() {
        System.out.println("Hello from BillPughSingleton: " + this.hashCode());
    }
}

// 6. Enum Singleton (most concise and inherently thread-safe)
enum EnumSingleton {
    INSTANCE;

    EnumSingleton() {
        System.out.println("EnumSingleton instance created");
    }

    public void showMessage() {
        System.out.println("Hello from EnumSingleton: " + this.hashCode());
    }
}

public class MainSingletonPattern {
    public static void main(String[] args) {
        System.out.println("=== Singleton Pattern Demonstration ===\n");

        // 1. Eager Singleton
        System.out.println("--- 1. Eager Initialization Singleton ---");
        EagerSingleton eager1 = EagerSingleton.getInstance();
        eager1.showMessage();
        EagerSingleton eager2 = EagerSingleton.getInstance();
        eager2.showMessage();
        System.out.println("Are both instances same? " + (eager1 == eager2));
        System.out.println();

        // 2. Lazy Singleton
        System.out.println("--- 2. Lazy Initialization Singleton ---");
        LazySingleton lazy1 = LazySingleton.getInstance();
        lazy1.showMessage();
        LazySingleton lazy2 = LazySingleton.getInstance();
        lazy2.showMessage();
        System.out.println("Are both instances same? " + (lazy1 == lazy2));
        System.out.println();

        // 3. Thread-Safe Singleton
        System.out.println("--- 3. Thread-Safe Singleton ---");
        ThreadSafeSingleton ts1 = ThreadSafeSingleton.getInstance();
        ts1.showMessage();
        ThreadSafeSingleton ts2 = ThreadSafeSingleton.getInstance();
        ts2.showMessage();
        System.out.println("Are both instances same? " + (ts1 == ts2));
        System.out.println();

        // 4. Double-Checked Locking Singleton
        System.out.println("--- 4. Double-Checked Locking Singleton ---");
        DoubleCheckedSingleton dc1 = DoubleCheckedSingleton.getInstance();
        dc1.showMessage();
        DoubleCheckedSingleton dc2 = DoubleCheckedSingleton.getInstance();
        dc2.showMessage();
        System.out.println("Are both instances same? " + (dc1 == dc2));
        System.out.println();

        // 5. Bill Pugh Singleton
        System.out.println("--- 5. Bill Pugh Singleton (Inner Static Helper) ---");
        BillPughSingleton bp1 = BillPughSingleton.getInstance();
        bp1.showMessage();
        BillPughSingleton bp2 = BillPughSingleton.getInstance();
        bp2.showMessage();
        System.out.println("Are both instances same? " + (bp1 == bp2));
        System.out.println();

        // 6. Enum Singleton
        System.out.println("--- 6. Enum Singleton ---");
        EnumSingleton enum1 = EnumSingleton.INSTANCE;
        enum1.showMessage();
        EnumSingleton enum2 = EnumSingleton.INSTANCE;
        enum2.showMessage();
        System.out.println("Are both instances same? " + (enum1 == enum2));
        System.out.println();

        System.out.println("=== Summary ===");
        System.out.println("All singleton implementations ensure only one instance exists.");
        System.out.println("Best practices:");
        System.out.println("  - Use Enum Singleton for simplicity and thread-safety");
        System.out.println("  - Use Bill Pugh for lazy initialization without synchronization overhead");
        System.out.println("  - Use Double-Checked Locking if you need lazy initialization with minimal overhead");
    }
}
