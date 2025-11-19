// Observer Design Pattern in Rust - Weather Station Example
// Demonstrates subject managing observers and broadcasting notifications

use std::cell::RefCell;
use std::rc::Rc;

// Observer trait - defines the interface for all observers
trait Observer {
    fn update(&self, temperature: f32, humidity: f32, pressure: f32);
    fn get_name(&self) -> &str;
}

// Subject trait - defines the interface for the subject
trait Subject {
    fn register_observer(&mut self, observer: Rc<dyn Observer>);
    fn remove_observer(&mut self, observer_name: &str);
    fn notify_observers(&self);
}

// WeatherStation - the concrete subject
struct WeatherStation {
    observers: Vec<Rc<dyn Observer>>,
    temperature: f32,
    humidity: f32,
    pressure: f32,
}

impl WeatherStation {
    fn new() -> Self {
        println!("[WeatherStation] Created new weather station");
        WeatherStation {
            observers: Vec::new(),
            temperature: 0.0,
            humidity: 0.0,
            pressure: 0.0,
        }
    }

    fn set_measurements(&mut self, temperature: f32, humidity: f32, pressure: f32) {
        println!("\n[WeatherStation] New measurements received:");
        println!("  Temperature: {:.1}F, Humidity: {:.1}%, Pressure: {:.1} hPa",
                 temperature, humidity, pressure);

        self.temperature = temperature;
        self.humidity = humidity;
        self.pressure = pressure;

        println!("[WeatherStation] Notifying all observers...");
        self.notify_observers();
    }
}

impl Subject for WeatherStation {
    fn register_observer(&mut self, observer: Rc<dyn Observer>) {
        println!("[WeatherStation] Registering observer: {}", observer.get_name());
        self.observers.push(observer);
    }

    fn remove_observer(&mut self, observer_name: &str) {
        println!("[WeatherStation] Removing observer: {}", observer_name);
        self.observers.retain(|obs| obs.get_name() != observer_name);
    }

    fn notify_observers(&self) {
        for observer in &self.observers {
            observer.update(self.temperature, self.humidity, self.pressure);
        }
    }
}

// CurrentConditionsDisplay - displays current weather conditions
struct CurrentConditionsDisplay {
    name: String,
    temperature: RefCell<f32>,
    humidity: RefCell<f32>,
}

impl CurrentConditionsDisplay {
    fn new(name: &str) -> Self {
        println!("[{}] Display created", name);
        CurrentConditionsDisplay {
            name: name.to_string(),
            temperature: RefCell::new(0.0),
            humidity: RefCell::new(0.0),
        }
    }

    fn display(&self) {
        println!("  [{}] Current conditions: {:.1}F and {:.1}% humidity",
                 self.name, self.temperature.borrow(), self.humidity.borrow());
    }
}

impl Observer for CurrentConditionsDisplay {
    fn update(&self, temperature: f32, humidity: f32, _pressure: f32) {
        *self.temperature.borrow_mut() = temperature;
        *self.humidity.borrow_mut() = humidity;
        self.display();
    }

    fn get_name(&self) -> &str {
        &self.name
    }
}

// StatisticsDisplay - displays weather statistics
struct StatisticsDisplay {
    name: String,
    temperatures: RefCell<Vec<f32>>,
}

impl StatisticsDisplay {
    fn new(name: &str) -> Self {
        println!("[{}] Display created", name);
        StatisticsDisplay {
            name: name.to_string(),
            temperatures: RefCell::new(Vec::new()),
        }
    }

    fn display(&self) {
        let temps = self.temperatures.borrow();
        if temps.is_empty() {
            return;
        }

        let sum: f32 = temps.iter().sum();
        let avg = sum / temps.len() as f32;
        let min = temps.iter().cloned().fold(f32::INFINITY, f32::min);
        let max = temps.iter().cloned().fold(f32::NEG_INFINITY, f32::max);

        println!("  [{}] Avg/Max/Min temperature: {:.1}/{:.1}/{:.1}",
                 self.name, avg, max, min);
    }
}

impl Observer for StatisticsDisplay {
    fn update(&self, temperature: f32, _humidity: f32, _pressure: f32) {
        self.temperatures.borrow_mut().push(temperature);
        self.display();
    }

    fn get_name(&self) -> &str {
        &self.name
    }
}

// ForecastDisplay - displays weather forecast based on pressure changes
struct ForecastDisplay {
    name: String,
    last_pressure: RefCell<f32>,
    current_pressure: RefCell<f32>,
}

impl ForecastDisplay {
    fn new(name: &str) -> Self {
        println!("[{}] Display created", name);
        ForecastDisplay {
            name: name.to_string(),
            last_pressure: RefCell::new(1013.25),
            current_pressure: RefCell::new(1013.25),
        }
    }

    fn display(&self) {
        let current = *self.current_pressure.borrow();
        let last = *self.last_pressure.borrow();

        let forecast = if current > last {
            "Improving weather on the way!"
        } else if current < last {
            "Watch out for cooler, rainy weather"
        } else {
            "More of the same"
        };

        println!("  [{}] Forecast: {}", self.name, forecast);
    }
}

impl Observer for ForecastDisplay {
    fn update(&self, _temperature: f32, _humidity: f32, pressure: f32) {
        *self.last_pressure.borrow_mut() = *self.current_pressure.borrow();
        *self.current_pressure.borrow_mut() = pressure;
        self.display();
    }

    fn get_name(&self) -> &str {
        &self.name
    }
}

fn main() {
    println!("=== Observer Design Pattern - Weather Station Demo ===\n");

    // Create the weather station (subject)
    let mut weather_station = WeatherStation::new();

    // Create observer displays
    let current_display = Rc::new(CurrentConditionsDisplay::new("CurrentDisplay"));
    let stats_display = Rc::new(StatisticsDisplay::new("StatisticsDisplay"));
    let forecast_display = Rc::new(ForecastDisplay::new("ForecastDisplay"));

    // Register observers with the weather station
    println!("\n--- Registering Observers ---");
    weather_station.register_observer(current_display.clone());
    weather_station.register_observer(stats_display.clone());
    weather_station.register_observer(forecast_display.clone());

    // Simulate weather changes
    println!("\n--- Weather Update 1 ---");
    weather_station.set_measurements(80.0, 65.0, 1014.0);

    println!("\n--- Weather Update 2 ---");
    weather_station.set_measurements(82.0, 70.0, 1012.0);

    println!("\n--- Weather Update 3 ---");
    weather_station.set_measurements(78.0, 90.0, 1009.0);

    // Demonstrate removing an observer
    println!("\n--- Removing StatisticsDisplay Observer ---");
    weather_station.remove_observer("StatisticsDisplay");

    println!("\n--- Weather Update 4 (after removal) ---");
    weather_station.set_measurements(75.0, 85.0, 1015.0);

    println!("\n=== Demo Complete ===");
}
