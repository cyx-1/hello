// Bridge Design Pattern in Rust
// Separates abstraction from implementation so both can vary independently

use std::cell::RefCell;

// Implementation trait - defines the interface for implementation classes
trait Device {
    fn is_enabled(&self) -> bool;
    fn enable(&mut self);
    fn disable(&mut self);
    fn get_volume(&self) -> u32;
    fn set_volume(&mut self, volume: u32);
    fn get_channel(&self) -> u32;
    fn set_channel(&mut self, channel: u32);
    fn get_name(&self) -> &str;
}

// Concrete Implementation A - TV
struct TV {
    enabled: bool,
    volume: u32,
    channel: u32,
}

impl TV {
    fn new() -> Self {
        println!("[TV] Creating new TV device");
        TV {
            enabled: false,
            volume: 30,
            channel: 1,
        }
    }
}

impl Device for TV {
    fn is_enabled(&self) -> bool {
        self.enabled
    }

    fn enable(&mut self) {
        self.enabled = true;
        println!("[TV] Device enabled");
    }

    fn disable(&mut self) {
        self.enabled = false;
        println!("[TV] Device disabled");
    }

    fn get_volume(&self) -> u32 {
        self.volume
    }

    fn set_volume(&mut self, volume: u32) {
        self.volume = volume.min(100);
        println!("[TV] Volume set to {}", self.volume);
    }

    fn get_channel(&self) -> u32 {
        self.channel
    }

    fn set_channel(&mut self, channel: u32) {
        self.channel = channel;
        println!("[TV] Channel set to {}", self.channel);
    }

    fn get_name(&self) -> &str {
        "TV"
    }
}

// Concrete Implementation B - Radio
struct Radio {
    enabled: bool,
    volume: u32,
    channel: u32,
}

impl Radio {
    fn new() -> Self {
        println!("[Radio] Creating new Radio device");
        Radio {
            enabled: false,
            volume: 20,
            channel: 88,
        }
    }
}

impl Device for Radio {
    fn is_enabled(&self) -> bool {
        self.enabled
    }

    fn enable(&mut self) {
        self.enabled = true;
        println!("[Radio] Device enabled");
    }

    fn disable(&mut self) {
        self.enabled = false;
        println!("[Radio] Device disabled");
    }

    fn get_volume(&self) -> u32 {
        self.volume
    }

    fn set_volume(&mut self, volume: u32) {
        self.volume = volume.min(100);
        println!("[Radio] Volume set to {}", self.volume);
    }

    fn get_channel(&self) -> u32 {
        self.channel
    }

    fn set_channel(&mut self, channel: u32) {
        self.channel = channel;
        println!("[Radio] Station set to {} FM", self.channel);
    }

    fn get_name(&self) -> &str {
        "Radio"
    }
}

// Abstraction - holds a reference to the implementation
struct RemoteControl {
    device: RefCell<Box<dyn Device>>,
}

impl RemoteControl {
    fn new(device: Box<dyn Device>) -> Self {
        println!("Creating RemoteControl for {}", device.get_name());
        RemoteControl {
            device: RefCell::new(device),
        }
    }

    fn toggle_power(&self) {
        let mut device = self.device.borrow_mut();
        if device.is_enabled() {
            device.disable();
        } else {
            device.enable();
        }
    }

    fn volume_up(&self) {
        let mut device = self.device.borrow_mut();
        let current = device.get_volume();
        device.set_volume(current + 10);
    }

    fn volume_down(&self) {
        let mut device = self.device.borrow_mut();
        let current = device.get_volume();
        if current >= 10 {
            device.set_volume(current - 10);
        } else {
            device.set_volume(0);
        }
    }

    fn channel_up(&self) {
        let mut device = self.device.borrow_mut();
        let current = device.get_channel();
        device.set_channel(current + 1);
    }

    fn channel_down(&self) {
        let mut device = self.device.borrow_mut();
        let current = device.get_channel();
        if current > 1 {
            device.set_channel(current - 1);
        }
    }

    fn get_device_name(&self) -> String {
        self.device.borrow().get_name().to_string()
    }
}

// Refined Abstraction - extends the base abstraction with additional features
struct AdvancedRemoteControl {
    base: RemoteControl,
}

impl AdvancedRemoteControl {
    fn new(device: Box<dyn Device>) -> Self {
        println!("Creating AdvancedRemoteControl for {}", device.get_name());
        AdvancedRemoteControl {
            base: RemoteControl {
                device: RefCell::new(device),
            },
        }
    }

    fn toggle_power(&self) {
        self.base.toggle_power();
    }

    fn volume_up(&self) {
        self.base.volume_up();
    }

    fn volume_down(&self) {
        self.base.volume_down();
    }

    fn mute(&self) {
        let mut device = self.base.device.borrow_mut();
        println!("[{}] Muting device", device.get_name());
        device.set_volume(0);
    }

    fn set_channel_direct(&self, channel: u32) {
        let mut device = self.base.device.borrow_mut();
        println!("[{}] Setting channel directly to {}", device.get_name(), channel);
        device.set_channel(channel);
    }

    fn get_device_name(&self) -> String {
        self.base.get_device_name()
    }
}

fn main() {
    println!("=== Bridge Design Pattern Demo ===\n");

    // Demo 1: Basic RemoteControl with TV
    println!("--- Demo 1: Basic RemoteControl with TV ---");
    let tv = Box::new(TV::new());
    let tv_remote = RemoteControl::new(tv);

    println!("\nOperating {} with basic remote:", tv_remote.get_device_name());
    tv_remote.toggle_power();
    tv_remote.volume_up();
    tv_remote.volume_up();
    tv_remote.channel_up();
    tv_remote.toggle_power();

    // Demo 2: Basic RemoteControl with Radio
    println!("\n--- Demo 2: Basic RemoteControl with Radio ---");
    let radio = Box::new(Radio::new());
    let radio_remote = RemoteControl::new(radio);

    println!("\nOperating {} with basic remote:", radio_remote.get_device_name());
    radio_remote.toggle_power();
    radio_remote.volume_up();
    radio_remote.channel_up();
    radio_remote.channel_up();

    // Demo 3: AdvancedRemoteControl with TV
    println!("\n--- Demo 3: AdvancedRemoteControl with TV ---");
    let tv2 = Box::new(TV::new());
    let advanced_remote = AdvancedRemoteControl::new(tv2);

    println!("\nOperating {} with advanced remote:", advanced_remote.get_device_name());
    advanced_remote.toggle_power();
    advanced_remote.volume_up();
    advanced_remote.set_channel_direct(42);
    advanced_remote.mute();
    advanced_remote.toggle_power();

    // Demo 4: AdvancedRemoteControl with Radio
    println!("\n--- Demo 4: AdvancedRemoteControl with Radio ---");
    let radio2 = Box::new(Radio::new());
    let advanced_radio_remote = AdvancedRemoteControl::new(radio2);

    println!("\nOperating {} with advanced remote:", advanced_radio_remote.get_device_name());
    advanced_radio_remote.toggle_power();
    advanced_radio_remote.set_channel_direct(101);
    advanced_radio_remote.volume_up();
    advanced_radio_remote.mute();

    println!("\n=== Bridge Pattern Demo Complete ===");
}
