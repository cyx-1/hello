# Observer Pattern

The Observer pattern defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

**Key Components:**
- **Subject**: Knows its observers and provides interface to attach/detach
- **Observer**: Interface for objects that should be notified of changes
- **ConcreteSubject**: Stores state and sends notifications
- **ConcreteObserver**: Implements Observer to keep state consistent with Subject

**Requires**: Python 3.10+ (uses union types with `|` syntax, type hints)

## Key Source Code

### Observer and Subject Interfaces

```python:main_observer.py startLine=24 endLine=55
# Observer interface
class Observer(ABC):
    """Abstract observer interface."""

    @abstractmethod
    def update(self, subject: "Subject", *args: Any, **kwargs: Any) -> None:
        pass


# Subject interface
class Subject(ABC):
    """Abstract subject interface."""

    def __init__(self):
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        """Attach an observer."""
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"  [Subject] Attached {observer.__class__.__name__}")

    def detach(self, observer: Observer) -> None:
        """Detach an observer."""
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"  [Subject] Detached {observer.__class__.__name__}")

    def notify(self, *args: Any, **kwargs: Any) -> None:
        """Notify all observers."""
        for observer in self._observers:
            observer.update(self, *args, **kwargs)
```

### Concrete Subject - Stock

```python:main_observer.py startLine=58 endLine=106
# Concrete Subject: Stock Market
class Stock(Subject):
    """Concrete subject representing a stock."""

    def __init__(self, symbol: str, price: float):
        super().__init__()
        self._symbol = symbol
        self._price = price
        self._high = price
        self._low = price
        self._open = price

    @property
    def symbol(self) -> str:
        return self._symbol

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        old_price = self._price
        self._price = value

        # Update high/low
        if value > self._high:
            self._high = value
        if value < self._low:
            self._low = value

        # Notify observers of price change
        change = value - old_price
        change_percent = (change / old_price) * 100 if old_price > 0 else 0
        self.notify(
            old_price=old_price,
            new_price=value,
            change=change,
            change_percent=change_percent,
        )
```

### Concrete Observers

```python:main_observer.py startLine=109 endLine=177
# Concrete Observers
class StockDisplay(Observer):
    """Observer that displays stock information."""

    def __init__(self, name: str):
        self._name = name

    def update(self, subject: Subject, *args: Any, **kwargs: Any) -> None:
        if isinstance(subject, Stock):
            change = kwargs.get("change", 0)
            change_str = f"+{change:.2f}" if change >= 0 else f"{change:.2f}"
            print(
                f"  [{self._name}] {subject.symbol}: ${subject.price:.2f} ({change_str})"
            )


class PriceAlert(Observer):
    """Observer that alerts on price thresholds."""

    def __init__(self, symbol: str, low_threshold: float, high_threshold: float):
        self._symbol = symbol
        self._low_threshold = low_threshold
        self._high_threshold = high_threshold

    def update(self, subject: Subject, *args: Any, **kwargs: Any) -> None:
        if isinstance(subject, Stock) and subject.symbol == self._symbol:
            if subject.price <= self._low_threshold:
                print(
                    f"  [ALERT] {subject.symbol} dropped to ${subject.price:.2f} "
                    f"(below ${self._low_threshold:.2f})"
                )
            elif subject.price >= self._high_threshold:
                print(
                    f"  [ALERT] {subject.symbol} rose to ${subject.price:.2f} "
                    f"(above ${self._high_threshold:.2f})"
                )


class TradeBot(Observer):
    """Observer that automatically trades based on conditions."""

    def __init__(self, name: str, buy_threshold: float, sell_threshold: float):
        self._name = name
        self._buy_threshold = buy_threshold
        self._sell_threshold = sell_threshold
        self._holdings: dict[str, int] = {}

    def update(self, subject: Subject, *args: Any, **kwargs: Any) -> None:
        if isinstance(subject, Stock):
            change_percent = kwargs.get("change_percent", 0)

            if change_percent <= -self._buy_threshold:
                # Buy on dip
                shares = self._holdings.get(subject.symbol, 0)
                self._holdings[subject.symbol] = shares + 10
                print(
                    f"  [{self._name}] BUY 10 {subject.symbol} at ${subject.price:.2f} "
                    f"({change_percent:.1f}% drop)"
                )
            elif change_percent >= self._sell_threshold:
                # Sell on rise
                shares = self._holdings.get(subject.symbol, 0)
                if shares > 0:
                    sell_amount = min(shares, 10)
                    self._holdings[subject.symbol] = shares - sell_amount
                    print(
                        f"  [{self._name}] SELL {sell_amount} {subject.symbol} "
                        f"at ${subject.price:.2f} ({change_percent:.1f}% rise)"
                    )
```

### Weather Station Example

```python:main_observer.py startLine=200 endLine=282
# Weather Station example
class WeatherStation(Subject):
    """Concrete subject for weather data."""

    def __init__(self, location: str):
        super().__init__()
        self._location = location
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

    def set_measurements(
        self, temperature: float, humidity: float, pressure: float
    ) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify(
            temperature=temperature, humidity=humidity, pressure=pressure
        )


class ForecastDisplay(Observer):
    """Displays weather forecast based on pressure changes."""

    def __init__(self):
        self._last_pressure = 0.0

    def update(self, subject: Subject, *args: Any, **kwargs: Any) -> None:
        if isinstance(subject, WeatherStation):
            pressure = kwargs.get("pressure", 0)
            if pressure > self._last_pressure:
                forecast = "Improving weather on the way!"
            elif pressure < self._last_pressure:
                forecast = "Watch out for cooler, rainy weather"
            else:
                forecast = "More of the same"
            print(f"  [Forecast] {forecast}")
            self._last_pressure = pressure


class StatisticsDisplay(Observer):
    """Displays weather statistics."""

    def __init__(self):
        self._temperatures: list[float] = []

    def update(self, subject: Subject, *args: Any, **kwargs: Any) -> None:
        if isinstance(subject, WeatherStation):
            temp = kwargs.get("temperature", 0)
            self._temperatures.append(temp)

            avg = sum(self._temperatures) / len(self._temperatures)
            max_temp = max(self._temperatures)
            min_temp = min(self._temperatures)

            print(
                f"  [Statistics] Avg/Max/Min: {avg:.1f}/{max_temp:.1f}/{min_temp:.1f}°F"
            )
```

## Program Output

```
============================================================
Observer Pattern - Stock Market Demo
============================================================

--- Setting Up Stock Observers ---
  [Subject] Attached StockDisplay
  [Subject] Attached PriceAlert
  [Subject] Attached TradeBot
  [Subject] Attached PriceLogger

--- Price Changes ---

AAPL price update to $152.50:
  [Main Display] AAPL: $152.50 (+2.50)

AAPL price update to $158.00:
  [Main Display] AAPL: $158.00 (+5.50)

AAPL price update to $161.00:
  [Main Display] AAPL: $161.00 (+3.00)
  [ALERT] AAPL rose to $161.00 (above $160.00)

AAPL price update to $155.00:
  [Main Display] AAPL: $155.00 (-6.00)
  [AutoTrader] BUY 10 AAPL at $155.00 (-3.7% drop)

AAPL price update to $148.00:
  [Main Display] AAPL: $148.00 (-7.00)
  [AutoTrader] BUY 10 AAPL at $148.00 (-4.5% drop)

AAPL price update to $144.00:
  [Main Display] AAPL: $144.00 (-4.00)
  [ALERT] AAPL dropped to $144.00 (below $145.00)
  [AutoTrader] BUY 10 AAPL at $144.00 (-2.7% drop)

AAPL price update to $150.00:
  [Main Display] AAPL: $150.00 (+6.00)
  [AutoTrader] SELL 10 AAPL at $150.00 (4.2% rise)

Stock stats: {'symbol': 'AAPL', 'price': 150.0, 'open': 150.0, 'high': 161.0, 'low': 144.0}
Price log entries: 7

--- Detaching Observer ---
  [Subject] Detached PriceAlert

Price update after detaching alert:
  [Main Display] AAPL: $165.00 (+15.00)
  [AutoTrader] SELL 10 AAPL at $165.00 (10.0% rise)

============================================================
Observer Pattern - Weather Station Demo
============================================================

--- Setting Up Weather Observers ---
  [Subject] Attached CurrentConditionsDisplay
  [Subject] Attached ForecastDisplay
  [Subject] Attached StatisticsDisplay

--- Weather Updates ---

New measurement: 80°F, 65%, 30.4 in
  [CurrentConditions] New York: 80°F, 65% humidity
  [Forecast] Improving weather on the way!
  [Statistics] Avg/Max/Min: 80.0/80.0/80.0°F

New measurement: 82°F, 70%, 29.2 in
  [CurrentConditions] New York: 82°F, 70% humidity
  [Forecast] Watch out for cooler, rainy weather
  [Statistics] Avg/Max/Min: 81.0/82.0/80.0°F

New measurement: 78°F, 90%, 29.2 in
  [CurrentConditions] New York: 78°F, 90% humidity
  [Forecast] More of the same
  [Statistics] Avg/Max/Min: 80.0/82.0/78.0°F

New measurement: 72°F, 85%, 30.0 in
  [CurrentConditions] New York: 72°F, 85% humidity
  [Forecast] Improving weather on the way!
  [Statistics] Avg/Max/Min: 78.0/82.0/72.0°F

============================================================
Benefits of Observer Pattern:
============================================================
1. Loose coupling between Subject and Observers
2. Support for broadcast communication
3. Easy to add/remove observers at runtime
4. Subject doesn't need to know observer details
5. Follows Open/Closed Principle
```

## Output Annotations

### Stock Market Demo

- **Lines 40-44 (attach)**: When observers are attached, they're added to the subject's `_observers` list. The subject prints which observer class was attached. Four different observers with different behaviors are registered.

- **Lines 78-97 (price setter)**: When `apple.price = 152.50` is assigned (line 314), the setter calculates change and change_percent, then calls `notify()`. This triggers all observers' `update()` methods (lines 52-55).

- **Lines 116-122 (StockDisplay)**: Every price update triggers the display observer to print the current price and change amount. This is why every price update shows the Main Display output.

- **Lines 125-144 (PriceAlert)**: The alert only prints when thresholds are crossed. At $161, it exceeds the $160 high threshold. At $144, it drops below the $145 low threshold. Updates to $152.50, $158, $155, $148, and $150 don't trigger alerts.

- **Lines 147-177 (TradeBot)**: The bot has buy_threshold=2.0 and sell_threshold=3.0 (percentages). At $155 (3.7% drop from $161), it buys. It accumulates shares on drops and sells when the price rises 4.2% from $144 to $150.

- **Lines 46-50 (detach)**: After detaching PriceAlert, the $165 update triggers only StockDisplay and TradeBot. No alert is printed even though $165 exceeds the $160 threshold, demonstrating dynamic observer management.

### Weather Station Demo

- **Lines 215-223 (set_measurements)**: Each call to `set_measurements()` updates internal state and calls `notify()` with the new values as kwargs.

- **Lines 233-243 (CurrentConditionsDisplay)**: Simply displays the current temperature and humidity from kwargs.

- **Lines 246-262 (ForecastDisplay)**: Maintains `_last_pressure` state between updates. First update (30.4 in) shows "Improving" because any value > 0 is an increase. Second update (29.2 in) shows "Watch out for cooler, rainy weather" because pressure dropped. Third (29.2 in) shows "More of the same".

- **Lines 265-282 (StatisticsDisplay)**: Accumulates temperatures in a list and calculates running statistics. After four measurements, average is (80+82+78+72)/4 = 78.0, max is 82, min is 72.

- **Lines 52-55 (notify)**: The notify method iterates through all observers and calls their `update()`. Each observer decides how to respond based on its own logic, demonstrating polymorphism.

## Running the Demo

```bash
uv run python main_observer.py
```
