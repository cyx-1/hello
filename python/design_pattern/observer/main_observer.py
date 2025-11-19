# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Observer Pattern

The Observer pattern defines a one-to-many dependency between objects so that
when one object changes state, all its dependents are notified and updated
automatically.

Key Components:
- Subject: Knows its observers and provides interface to attach/detach
- Observer: Interface for objects that should be notified of changes
- ConcreteSubject: Stores state and sends notifications
- ConcreteObserver: Implements Observer to keep state consistent with Subject
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any


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

    def get_stats(self) -> dict[str, float]:
        return {
            "symbol": self._symbol,
            "price": self._price,
            "open": self._open,
            "high": self._high,
            "low": self._low,
        }


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


class PriceLogger(Observer):
    """Observer that logs all price changes."""

    def __init__(self):
        self._log: list[dict[str, Any]] = []

    def update(self, subject: Subject, *args: Any, **kwargs: Any) -> None:
        if isinstance(subject, Stock):
            entry = {
                "timestamp": datetime.now(),
                "symbol": subject.symbol,
                "price": subject.price,
                "change": kwargs.get("change", 0),
            }
            self._log.append(entry)

    def get_log(self) -> list[dict[str, Any]]:
        return self._log.copy()


# Weather Station example
class WeatherStation(Subject):
    """Concrete subject for weather data."""

    def __init__(self, location: str):
        super().__init__()
        self._location = location
        self._temperature = 0.0
        self._humidity = 0.0
        self._pressure = 0.0

    @property
    def location(self) -> str:
        return self._location

    def set_measurements(
        self, temperature: float, humidity: float, pressure: float
    ) -> None:
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify(
            temperature=temperature, humidity=humidity, pressure=pressure
        )

    def get_measurements(self) -> dict[str, float]:
        return {
            "temperature": self._temperature,
            "humidity": self._humidity,
            "pressure": self._pressure,
        }


class CurrentConditionsDisplay(Observer):
    """Displays current weather conditions."""

    def update(self, subject: Subject, *args: Any, **kwargs: Any) -> None:
        if isinstance(subject, WeatherStation):
            temp = kwargs.get("temperature", 0)
            humidity = kwargs.get("humidity", 0)
            print(
                f"  [CurrentConditions] {subject.location}: "
                f"{temp}°F, {humidity}% humidity"
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


def main() -> None:
    print("=" * 60)
    print("Observer Pattern - Stock Market Demo")
    print("=" * 60)

    # Demo 1: Stock market observers
    print("\n--- Setting Up Stock Observers ---")

    # Create subject
    apple = Stock("AAPL", 150.00)

    # Create observers
    display = StockDisplay("Main Display")
    alert = PriceAlert("AAPL", low_threshold=145.00, high_threshold=160.00)
    bot = TradeBot("AutoTrader", buy_threshold=2.0, sell_threshold=3.0)
    logger = PriceLogger()

    # Attach observers
    apple.attach(display)
    apple.attach(alert)
    apple.attach(bot)
    apple.attach(logger)

    # Simulate price changes
    print("\n--- Price Changes ---")
    price_changes = [152.50, 158.00, 161.00, 155.00, 148.00, 144.00, 150.00]

    for price in price_changes:
        print(f"\nAAPL price update to ${price:.2f}:")
        apple.price = price

    # Show stats
    print(f"\nStock stats: {apple.get_stats()}")
    print(f"Price log entries: {len(logger.get_log())}")

    # Demo 2: Detaching observer
    print("\n--- Detaching Observer ---")
    apple.detach(alert)
    print("\nPrice update after detaching alert:")
    apple.price = 165.00

    # Demo 3: Weather station
    print("\n" + "=" * 60)
    print("Observer Pattern - Weather Station Demo")
    print("=" * 60)

    # Create weather station
    print("\n--- Setting Up Weather Observers ---")
    station = WeatherStation("New York")

    # Create and attach observers
    current = CurrentConditionsDisplay()
    forecast = ForecastDisplay()
    stats = StatisticsDisplay()

    station.attach(current)
    station.attach(forecast)
    station.attach(stats)

    # Simulate weather changes
    print("\n--- Weather Updates ---")
    measurements = [
        (80, 65, 30.4),
        (82, 70, 29.2),
        (78, 90, 29.2),
        (72, 85, 30.0),
    ]

    for temp, humidity, pressure in measurements:
        print(f"\nNew measurement: {temp}°F, {humidity}%, {pressure} in")
        station.set_measurements(temp, humidity, pressure)

    print("\n" + "=" * 60)
    print("Benefits of Observer Pattern:")
    print("=" * 60)
    print("1. Loose coupling between Subject and Observers")
    print("2. Support for broadcast communication")
    print("3. Easy to add/remove observers at runtime")
    print("4. Subject doesn't need to know observer details")
    print("5. Follows Open/Closed Principle")


if __name__ == "__main__":
    main()
