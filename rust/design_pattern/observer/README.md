# Observer Design Pattern in Rust

## Description

The Observer pattern defines a one-to-many dependency between objects so that when one object (the subject) changes state, all its dependents (observers) are notified and updated automatically. This implementation demonstrates a Weather Station example where multiple display units observe and react to weather data changes.

This pattern is useful for implementing distributed event-handling systems, where an object needs to notify multiple other objects about state changes without tight coupling.

## Source Code

```rust
  1  // Observer Design Pattern in Rust - Weather Station Example
  2  // Demonstrates subject managing observers and broadcasting notifications
  3
  4  use std::cell::RefCell;
  5  use std::rc::Rc;
  6
  7  // Observer trait - defines the interface for all observers
  8  trait Observer {
  9      fn update(&self, temperature: f32, humidity: f32, pressure: f32);
 10      fn get_name(&self) -> &str;
 11  }
 12
 13  // Subject trait - defines the interface for the subject
 14  trait Subject {
 15      fn register_observer(&mut self, observer: Rc<dyn Observer>);
 16      fn remove_observer(&mut self, observer_name: &str);
 17      fn notify_observers(&self);
 18  }
 19
 20  // WeatherStation - the concrete subject
 21  struct WeatherStation {
 22      observers: Vec<Rc<dyn Observer>>,
 23      temperature: f32,
 24      humidity: f32,
 25      pressure: f32,
 26  }
 27
 28  impl WeatherStation {
 29      fn new() -> Self {
 30          println!("[WeatherStation] Created new weather station");
 31          WeatherStation {
 32              observers: Vec::new(),
 33              temperature: 0.0,
 34              humidity: 0.0,
 35              pressure: 0.0,
 36          }
 37      }
 38
 39      fn set_measurements(&mut self, temperature: f32, humidity: f32, pressure: f32) {
 40          println!("\n[WeatherStation] New measurements received:");
 41          println!("  Temperature: {:.1}F, Humidity: {:.1}%, Pressure: {:.1} hPa",
 42                   temperature, humidity, pressure);
 43
 44          self.temperature = temperature;
 45          self.humidity = humidity;
 46          self.pressure = pressure;
 47
 48          println!("[WeatherStation] Notifying all observers...");
 49          self.notify_observers();
 50      }
 51  }
 52
 53  impl Subject for WeatherStation {
 54      fn register_observer(&mut self, observer: Rc<dyn Observer>) {
 55          println!("[WeatherStation] Registering observer: {}", observer.get_name());
 56          self.observers.push(observer);
 57      }
 58
 59      fn remove_observer(&mut self, observer_name: &str) {
 60          println!("[WeatherStation] Removing observer: {}", observer_name);
 61          self.observers.retain(|obs| obs.get_name() != observer_name);
 62      }
 63
 64      fn notify_observers(&self) {
 65          for observer in &self.observers {
 66              observer.update(self.temperature, self.humidity, self.pressure);
 67          }
 68      }
 69  }
 70
 71  // CurrentConditionsDisplay - displays current weather conditions
 72  struct CurrentConditionsDisplay {
 73      name: String,
 74      temperature: RefCell<f32>,
 75      humidity: RefCell<f32>,
 76  }
 77
 78  impl CurrentConditionsDisplay {
 79      fn new(name: &str) -> Self {
 80          println!("[{}] Display created", name);
 81          CurrentConditionsDisplay {
 82              name: name.to_string(),
 83              temperature: RefCell::new(0.0),
 84              humidity: RefCell::new(0.0),
 85          }
 86      }
 87
 88      fn display(&self) {
 89          println!("  [{}] Current conditions: {:.1}F and {:.1}% humidity",
 90                   self.name, self.temperature.borrow(), self.humidity.borrow());
 91      }
 92  }
 93
 94  impl Observer for CurrentConditionsDisplay {
 95      fn update(&self, temperature: f32, humidity: f32, _pressure: f32) {
 96          *self.temperature.borrow_mut() = temperature;
 97          *self.humidity.borrow_mut() = humidity;
 98          self.display();
 99      }
100
101      fn get_name(&self) -> &str {
102          &self.name
103      }
104  }
105
106  // StatisticsDisplay - displays weather statistics
107  struct StatisticsDisplay {
108      name: String,
109      temperatures: RefCell<Vec<f32>>,
110  }
111
112  impl StatisticsDisplay {
113      fn new(name: &str) -> Self {
114          println!("[{}] Display created", name);
115          StatisticsDisplay {
116              name: name.to_string(),
117              temperatures: RefCell::new(Vec::new()),
118          }
119      }
120
121      fn display(&self) {
122          let temps = self.temperatures.borrow();
123          if temps.is_empty() {
124              return;
125          }
126
127          let sum: f32 = temps.iter().sum();
128          let avg = sum / temps.len() as f32;
129          let min = temps.iter().cloned().fold(f32::INFINITY, f32::min);
130          let max = temps.iter().cloned().fold(f32::NEG_INFINITY, f32::max);
131
132          println!("  [{}] Avg/Max/Min temperature: {:.1}/{:.1}/{:.1}",
133                   self.name, avg, max, min);
134      }
135  }
136
137  impl Observer for StatisticsDisplay {
138      fn update(&self, temperature: f32, _humidity: f32, _pressure: f32) {
139          self.temperatures.borrow_mut().push(temperature);
140          self.display();
141      }
142
143      fn get_name(&self) -> &str {
144          &self.name
145      }
146  }
147
148  // ForecastDisplay - displays weather forecast based on pressure changes
149  struct ForecastDisplay {
150      name: String,
151      last_pressure: RefCell<f32>,
152      current_pressure: RefCell<f32>,
153  }
154
155  impl ForecastDisplay {
156      fn new(name: &str) -> Self {
157          println!("[{}] Display created", name);
158          ForecastDisplay {
159              name: name.to_string(),
160              last_pressure: RefCell::new(1013.25),
161              current_pressure: RefCell::new(1013.25),
162          }
163      }
164
165      fn display(&self) {
166          let current = *self.current_pressure.borrow();
167          let last = *self.last_pressure.borrow();
168
169          let forecast = if current > last {
170              "Improving weather on the way!"
171          } else if current < last {
172              "Watch out for cooler, rainy weather"
173          } else {
174              "More of the same"
175          };
176
177          println!("  [{}] Forecast: {}", self.name, forecast);
178      }
179  }
180
181  impl Observer for ForecastDisplay {
182      fn update(&self, _temperature: f32, _humidity: f32, pressure: f32) {
183          *self.last_pressure.borrow_mut() = *self.current_pressure.borrow();
184          *self.current_pressure.borrow_mut() = pressure;
185          self.display();
186      }
187
188      fn get_name(&self) -> &str {
189          &self.name
190      }
191  }
192
193  fn main() {
194      println!("=== Observer Design Pattern - Weather Station Demo ===\n");
195
196      // Create the weather station (subject)
197      let mut weather_station = WeatherStation::new();
198
199      // Create observer displays
200      let current_display = Rc::new(CurrentConditionsDisplay::new("CurrentDisplay"));
201      let stats_display = Rc::new(StatisticsDisplay::new("StatisticsDisplay"));
202      let forecast_display = Rc::new(ForecastDisplay::new("ForecastDisplay"));
203
204      // Register observers with the weather station
205      println!("\n--- Registering Observers ---");
206      weather_station.register_observer(current_display.clone());
207      weather_station.register_observer(stats_display.clone());
208      weather_station.register_observer(forecast_display.clone());
209
210      // Simulate weather changes
211      println!("\n--- Weather Update 1 ---");
212      weather_station.set_measurements(80.0, 65.0, 1014.0);
213
214      println!("\n--- Weather Update 2 ---");
215      weather_station.set_measurements(82.0, 70.0, 1012.0);
216
217      println!("\n--- Weather Update 3 ---");
218      weather_station.set_measurements(78.0, 90.0, 1009.0);
219
220      // Demonstrate removing an observer
221      println!("\n--- Removing StatisticsDisplay Observer ---");
222      weather_station.remove_observer("StatisticsDisplay");
223
224      println!("\n--- Weather Update 4 (after removal) ---");
225      weather_station.set_measurements(75.0, 85.0, 1015.0);
226
227      println!("\n=== Demo Complete ===");
228  }
```

## Program Output

```
=== Observer Design Pattern - Weather Station Demo ===

[WeatherStation] Created new weather station
[CurrentDisplay] Display created
[StatisticsDisplay] Display created
[ForecastDisplay] Display created

--- Registering Observers ---
[WeatherStation] Registering observer: CurrentDisplay
[WeatherStation] Registering observer: StatisticsDisplay
[WeatherStation] Registering observer: ForecastDisplay

--- Weather Update 1 ---

[WeatherStation] New measurements received:
  Temperature: 80.0F, Humidity: 65.0%, Pressure: 1014.0 hPa
[WeatherStation] Notifying all observers...
  [CurrentDisplay] Current conditions: 80.0F and 65.0% humidity
  [StatisticsDisplay] Avg/Max/Min temperature: 80.0/80.0/80.0
  [ForecastDisplay] Forecast: Improving weather on the way!

--- Weather Update 2 ---

[WeatherStation] New measurements received:
  Temperature: 82.0F, Humidity: 70.0%, Pressure: 1012.0 hPa
[WeatherStation] Notifying all observers...
  [CurrentDisplay] Current conditions: 82.0F and 70.0% humidity
  [StatisticsDisplay] Avg/Max/Min temperature: 81.0/82.0/80.0
  [ForecastDisplay] Forecast: Watch out for cooler, rainy weather

--- Weather Update 3 ---

[WeatherStation] New measurements received:
  Temperature: 78.0F, Humidity: 90.0%, Pressure: 1009.0 hPa
[WeatherStation] Notifying all observers...
  [CurrentDisplay] Current conditions: 78.0F and 90.0% humidity
  [StatisticsDisplay] Avg/Max/Min temperature: 80.0/82.0/78.0
  [ForecastDisplay] Forecast: Watch out for cooler, rainy weather

--- Removing StatisticsDisplay Observer ---
[WeatherStation] Removing observer: StatisticsDisplay

--- Weather Update 4 (after removal) ---

[WeatherStation] New measurements received:
  Temperature: 75.0F, Humidity: 85.0%, Pressure: 1015.0 hPa
[WeatherStation] Notifying all observers...
  [CurrentDisplay] Current conditions: 75.0F and 85.0% humidity
  [ForecastDisplay] Forecast: Improving weather on the way!

=== Demo Complete ===
```

## Code Annotations

### Key Sections Explained

#### Trait Definitions (Lines 7-18)

- **Lines 8-11**: The `Observer` trait defines the contract for all observers with `update()` for receiving notifications and `get_name()` for identification
- **Lines 14-18**: The `Subject` trait defines methods for managing observers: register, remove, and notify

#### WeatherStation Subject (Lines 20-69)

- **Lines 21-26**: The subject stores a vector of trait objects (`Rc<dyn Observer>`) allowing polymorphic storage of different observer types
- **Lines 39-50**: `set_measurements()` updates internal state and triggers notification to all registered observers
- **Lines 54-57**: Observer registration adds to the internal vector with ownership shared via `Rc`
- **Lines 59-62**: Observer removal uses `retain()` with name matching to filter out the specified observer
- **Lines 64-68**: Notification iterates through all observers calling their `update()` method

#### Observer Implementations (Lines 71-191)

- **Lines 72-104**: `CurrentConditionsDisplay` - Simple display showing current temperature and humidity
- **Lines 107-146**: `StatisticsDisplay` - Maintains history in a `Vec<f32>` and calculates running statistics
- **Lines 149-191**: `ForecastDisplay` - Tracks pressure changes to predict weather trends

#### Interior Mutability Pattern (Lines 74-75, 109, 151-152)

- Uses `RefCell<T>` to allow mutation through immutable `&self` references in the `update()` method
- This is necessary because trait methods receive `&self` but observers need to update their internal state

### Output to Source Code Correlation

| Output Line | Source Lines | Description |
|-------------|--------------|-------------|
| `[WeatherStation] Created new weather station` | 30 | Constructor prints creation message |
| `[CurrentDisplay] Display created` | 80 | Each display announces creation |
| `[WeatherStation] Registering observer: CurrentDisplay` | 55 | Registration logs the observer name |
| `[WeatherStation] New measurements received:` | 40-42 | `set_measurements()` announces new data |
| `[WeatherStation] Notifying all observers...` | 48 | Pre-notification announcement |
| `[CurrentDisplay] Current conditions: 80.0F...` | 89-90 | Observer's `display()` method output |
| `[StatisticsDisplay] Avg/Max/Min temperature:` | 132-133 | Statistics calculation display |
| `[ForecastDisplay] Forecast: Improving weather...` | 177 | Forecast based on pressure comparison (lines 169-170) |
| `[WeatherStation] Removing observer: StatisticsDisplay` | 60 | Removal operation logged |
| Weather Update 4 shows only 2 observers | 64-67 | After removal, only CurrentDisplay and ForecastDisplay remain in the vector |

### Key Characteristics of Observer Pattern in Rust

1. **Trait Objects for Polymorphism**: Uses `dyn Observer` to store different observer types in a single collection, enabling runtime polymorphism

2. **Reference Counting with `Rc`**: Observers are wrapped in `Rc` (Reference Counted) smart pointers to allow shared ownership between main and the subject

3. **Interior Mutability with `RefCell`**: Since `update()` receives `&self` (immutable reference), `RefCell` provides runtime borrow checking to allow mutation

4. **Loose Coupling**: The subject only knows about the `Observer` trait, not concrete implementations, allowing new observer types to be added without modifying the subject

5. **Push Model**: The subject pushes all data to observers, letting each observer decide what data it needs

6. **Dynamic Registration**: Observers can be registered and removed at runtime, as demonstrated in lines 206-208 (registration) and 222 (removal)

7. **No Global State**: Unlike some implementations that use static/global registries, this implementation keeps observer management within the subject instance

### Rust-Specific Considerations

- **Thread Safety**: This implementation uses `Rc` and `RefCell` which are not thread-safe. For concurrent scenarios, use `Arc` (Atomic Reference Counting) and `Mutex` or `RwLock` instead
- **Ownership Model**: Rust's ownership system requires explicit handling of shared references through smart pointers
- **No Inheritance**: Rust uses composition via traits instead of classical inheritance, making the pattern more explicit but equally flexible
