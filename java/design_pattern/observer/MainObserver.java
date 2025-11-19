/**
 * Comprehensive demonstration of the Observer Pattern in Java
 *
 * The Observer pattern defines a one-to-many dependency between objects so that
 * when one object changes state, all its dependents are notified and updated
 * automatically.
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// Observer interface
interface Observer {
    void update(String event, Object data);
}

// Subject interface
interface Subject {
    void attach(Observer observer);
    void detach(Observer observer);
    void notifyObservers(String event, Object data);
}

// Concrete Subject - News Agency
class NewsAgency implements Subject {
    private List<Observer> observers = new ArrayList<>();
    private String latestNews;

    @Override
    public void attach(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void detach(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers(String event, Object data) {
        for (Observer observer : observers) {
            observer.update(event, data);
        }
    }

    public void publishNews(String news) {
        this.latestNews = news;
        System.out.println("  [NewsAgency] Publishing: " + news);
        notifyObservers("NEWS", news);
    }
}

// Concrete Observers
class NewsChannel implements Observer {
    private String name;

    public NewsChannel(String name) {
        this.name = name;
    }

    @Override
    public void update(String event, Object data) {
        System.out.println("  [" + name + "] Breaking news: " + data);
    }
}

class NewsWebsite implements Observer {
    private String name;

    public NewsWebsite(String name) {
        this.name = name;
    }

    @Override
    public void update(String event, Object data) {
        System.out.println("  [" + name + "] Website updated with: " + data);
    }
}

class MobileApp implements Observer {
    private String name;

    public MobileApp(String name) {
        this.name = name;
    }

    @Override
    public void update(String event, Object data) {
        System.out.println("  [" + name + "] Push notification: " + data);
    }
}

// Event-based Observer with multiple event types

interface EventListener {
    void onEvent(String eventType, Map<String, Object> data);
}

class EventManager {
    private Map<String, List<EventListener>> listeners = new HashMap<>();

    public EventManager(String... eventTypes) {
        for (String type : eventTypes) {
            listeners.put(type, new ArrayList<>());
        }
    }

    public void subscribe(String eventType, EventListener listener) {
        listeners.get(eventType).add(listener);
    }

    public void unsubscribe(String eventType, EventListener listener) {
        listeners.get(eventType).remove(listener);
    }

    public void notify(String eventType, Map<String, Object> data) {
        for (EventListener listener : listeners.get(eventType)) {
            listener.onEvent(eventType, data);
        }
    }
}

class FileEditor {
    private EventManager events;
    private String filename;

    public FileEditor() {
        events = new EventManager("open", "save", "close");
    }

    public EventManager getEvents() {
        return events;
    }

    public void openFile(String filename) {
        this.filename = filename;
        Map<String, Object> data = new HashMap<>();
        data.put("filename", filename);
        System.out.println("  [FileEditor] Opened: " + filename);
        events.notify("open", data);
    }

    public void saveFile() {
        Map<String, Object> data = new HashMap<>();
        data.put("filename", filename);
        System.out.println("  [FileEditor] Saved: " + filename);
        events.notify("save", data);
    }

    public void closeFile() {
        Map<String, Object> data = new HashMap<>();
        data.put("filename", filename);
        System.out.println("  [FileEditor] Closed: " + filename);
        events.notify("close", data);
        filename = null;
    }
}

class LoggingListener implements EventListener {
    private String logFile;

    public LoggingListener(String logFile) {
        this.logFile = logFile;
    }

    @Override
    public void onEvent(String eventType, Map<String, Object> data) {
        System.out.println("  [Logger] Writing to " + logFile + ": " +
                          eventType + " - " + data.get("filename"));
    }
}

class EmailListener implements EventListener {
    private String email;

    public EmailListener(String email) {
        this.email = email;
    }

    @Override
    public void onEvent(String eventType, Map<String, Object> data) {
        System.out.println("  [Email] Sending to " + email + ": File " +
                          data.get("filename") + " was " + eventType + "ed");
    }
}

// Stock market example

class Stock implements Subject {
    private String symbol;
    private double price;
    private List<Observer> investors = new ArrayList<>();

    public Stock(String symbol, double initialPrice) {
        this.symbol = symbol;
        this.price = initialPrice;
    }

    @Override
    public void attach(Observer observer) {
        investors.add(observer);
    }

    @Override
    public void detach(Observer observer) {
        investors.remove(observer);
    }

    @Override
    public void notifyObservers(String event, Object data) {
        for (Observer observer : investors) {
            observer.update(event, data);
        }
    }

    public void setPrice(double newPrice) {
        double oldPrice = this.price;
        this.price = newPrice;
        String direction = newPrice > oldPrice ? "UP" : "DOWN";
        double change = Math.abs(newPrice - oldPrice);

        System.out.println("  [" + symbol + "] Price changed: $" +
                          String.format("%.2f", oldPrice) + " -> $" +
                          String.format("%.2f", newPrice));

        Map<String, Object> data = new HashMap<>();
        data.put("symbol", symbol);
        data.put("oldPrice", oldPrice);
        data.put("newPrice", newPrice);
        data.put("change", change);
        data.put("direction", direction);

        notifyObservers("PRICE_CHANGE", data);
    }

    public String getSymbol() { return symbol; }
    public double getPrice() { return price; }
}

class Investor implements Observer {
    private String name;

    public Investor(String name) {
        this.name = name;
    }

    @Override
    @SuppressWarnings("unchecked")
    public void update(String event, Object data) {
        Map<String, Object> stockData = (Map<String, Object>) data;
        String symbol = (String) stockData.get("symbol");
        double newPrice = (Double) stockData.get("newPrice");
        String direction = (String) stockData.get("direction");

        System.out.println("  [Investor " + name + "] " + symbol + " is " +
                          direction + "! New price: $" + String.format("%.2f", newPrice));
    }
}

public class MainObserver {
    public static void main(String[] args) {
        System.out.println("=== Observer Pattern Demonstration ===\n");

        // News agency example
        System.out.println("--- 1. News Agency with Multiple Channels ---");

        NewsAgency agency = new NewsAgency();

        NewsChannel cnn = new NewsChannel("CNN");
        NewsWebsite bbc = new NewsWebsite("BBC.com");
        MobileApp newsApp = new MobileApp("NewsApp");

        agency.attach(cnn);
        agency.attach(bbc);
        agency.attach(newsApp);

        agency.publishNews("Breaking: Major tech announcement today!");
        System.out.println();

        agency.detach(cnn);
        agency.publishNews("Update: More details emerging...");
        System.out.println();

        // Event-based system
        System.out.println("--- 2. File Editor with Event System ---");

        FileEditor editor = new FileEditor();

        LoggingListener logger = new LoggingListener("activity.log");
        EmailListener emailer = new EmailListener("admin@example.com");

        editor.getEvents().subscribe("open", logger);
        editor.getEvents().subscribe("save", logger);
        editor.getEvents().subscribe("save", emailer);

        editor.openFile("document.txt");
        editor.saveFile();
        editor.closeFile();
        System.out.println();

        // Stock market example
        System.out.println("--- 3. Stock Market Observers ---");

        Stock apple = new Stock("AAPL", 150.00);
        Stock google = new Stock("GOOGL", 2800.00);

        Investor john = new Investor("John");
        Investor jane = new Investor("Jane");

        apple.attach(john);
        apple.attach(jane);
        google.attach(jane);

        System.out.println();
        apple.setPrice(155.50);
        System.out.println();
        google.setPrice(2750.00);
        System.out.println();
        apple.setPrice(152.30);

        System.out.println("\n=== Summary ===");
        System.out.println("Observer pattern benefits:");
        System.out.println("  - Loose coupling between subject and observers");
        System.out.println("  - Support for broadcast communication");
        System.out.println("  - Dynamic relationships at runtime");
        System.out.println("\nVariations:");
        System.out.println("  - Push model: subject sends data with notification");
        System.out.println("  - Pull model: observers query subject for data");
        System.out.println("  - Event-based: multiple event types");
    }
}
