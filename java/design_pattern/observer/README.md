# Observer Pattern

Defines a one-to-many dependency so that when one object changes state, all dependents are notified automatically.

## How to Run
```bash
cd java/observer
mvn compile exec:java
```

## Key Source Code

### Observer Interface (Lines 15-17)
```java
interface Observer {
    void update(String event, Object data);
}
```

### Subject Interface (Lines 20-24)
```java
interface Subject {
    void attach(Observer observer);
    void detach(Observer observer);
    void notifyObservers(String event, Object data);
}
```

### Concrete Subject (Lines 27-45)
```java
class NewsAgency implements Subject {
    private List<Observer> observers = new ArrayList<>();

    public void publishNews(String news) {
        this.latestNews = news;
        notifyObservers("NEWS", news);
    }
}
```

## Program Output
```
--- 1. News Agency with Multiple Channels ---
  [NewsAgency] Publishing: Breaking: Major tech announcement today!
  [CNN] Breaking news: Breaking: Major tech announcement today!
  [BBC.com] Website updated with: Breaking: Major tech announcement today!
  [NewsApp] Push notification: Breaking: Major tech announcement today!

--- 3. Stock Market Observers ---
  [AAPL] Price changed: $150.00 -> $155.50
  [Investor John] AAPL is UP! New price: $155.50
  [Investor Jane] AAPL is UP! New price: $155.50

  [GOOGL] Price changed: $2800.00 -> $2750.00
  [Investor Jane] GOOGL is DOWN! New price: $2750.00
```

## Pattern Benefits
- Loose coupling between subject and observers
- Support for broadcast communication
- Dynamic relationships at runtime

## Requirements
- Java 17 or higher
- Maven 3.x
