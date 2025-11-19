// Facade Design Pattern in Rust
// Demonstrates how a facade simplifies interaction with complex subsystems

// ============================================================================
// Subsystem Components - Complex internal systems
// ============================================================================

/// Television subsystem with multiple operations
struct Television {
    brand: String,
}

impl Television {
    fn new(brand: &str) -> Self {
        Television {
            brand: brand.to_string(),
        }
    }

    fn turn_on(&self) {
        println!("  [TV] {} Television is turning ON", self.brand);
    }

    fn turn_off(&self) {
        println!("  [TV] {} Television is turning OFF", self.brand);
    }

    fn set_input(&self, input: &str) {
        println!("  [TV] Setting input source to: {}", input);
    }

    fn set_brightness(&self, level: u8) {
        println!("  [TV] Adjusting brightness to {}%", level);
    }
}

/// Sound system subsystem with audio controls
struct SoundSystem {
    model: String,
}

impl SoundSystem {
    fn new(model: &str) -> Self {
        SoundSystem {
            model: model.to_string(),
        }
    }

    fn turn_on(&self) {
        println!("  [Audio] {} Sound System powering ON", self.model);
    }

    fn turn_off(&self) {
        println!("  [Audio] {} Sound System powering OFF", self.model);
    }

    fn set_volume(&self, level: u8) {
        println!("  [Audio] Setting volume to {}", level);
    }

    fn set_surround_mode(&self, mode: &str) {
        println!("  [Audio] Surround mode set to: {}", mode);
    }
}

/// Streaming player subsystem
struct StreamingPlayer {
    service: String,
}

impl StreamingPlayer {
    fn new(service: &str) -> Self {
        StreamingPlayer {
            service: service.to_string(),
        }
    }

    fn turn_on(&self) {
        println!("  [Stream] {} Streaming Player starting", self.service);
    }

    fn turn_off(&self) {
        println!("  [Stream] {} Streaming Player shutting down", self.service);
    }

    fn login(&self) {
        println!("  [Stream] Logging into {} account", self.service);
    }

    fn play(&self, content: &str) {
        println!("  [Stream] Now playing: {}", content);
    }

    fn stop(&self) {
        println!("  [Stream] Playback stopped");
    }
}

/// Room lighting subsystem
struct Lights {
    room: String,
}

impl Lights {
    fn new(room: &str) -> Self {
        Lights {
            room: room.to_string(),
        }
    }

    fn dim(&self, level: u8) {
        println!("  [Lights] {} lights dimmed to {}%", self.room, level);
    }

    fn on(&self) {
        println!("  [Lights] {} lights turned ON (100%)", self.room);
    }
}

// ============================================================================
// Facade - Simplified interface to the complex subsystems
// ============================================================================

/// HomeTheaterFacade provides a simple interface to control
/// all home theater components with single method calls
struct HomeTheaterFacade {
    tv: Television,
    sound: SoundSystem,
    player: StreamingPlayer,
    lights: Lights,
}

impl HomeTheaterFacade {
    fn new() -> Self {
        println!("=== Initializing Home Theater System ===\n");
        HomeTheaterFacade {
            tv: Television::new("Samsung"),
            sound: SoundSystem::new("Sonos"),
            player: StreamingPlayer::new("Netflix"),
            lights: Lights::new("Living Room"),
        }
    }

    /// Simple method to start movie night - hides all complexity
    fn watch_movie(&self, movie: &str) {
        println!(">>> Starting Movie Night: '{}' <<<\n", movie);

        // Facade coordinates all subsystems
        self.lights.dim(20);
        self.tv.turn_on();
        self.tv.set_input("HDMI-1");
        self.tv.set_brightness(80);
        self.sound.turn_on();
        self.sound.set_volume(50);
        self.sound.set_surround_mode("Cinema");
        self.player.turn_on();
        self.player.login();
        self.player.play(movie);

        println!("\n>>> Enjoy your movie! <<<\n");
    }

    /// Simple method to end movie night - hides shutdown complexity
    fn end_movie(&self) {
        println!(">>> Ending Movie Night <<<\n");

        // Facade coordinates orderly shutdown
        self.player.stop();
        self.player.turn_off();
        self.sound.turn_off();
        self.tv.turn_off();
        self.lights.on();

        println!("\n>>> System shutdown complete <<<\n");
    }

    /// Simple method for music listening mode
    fn listen_to_music(&self) {
        println!(">>> Starting Music Mode <<<\n");

        self.lights.dim(60);
        self.sound.turn_on();
        self.sound.set_volume(40);
        self.sound.set_surround_mode("Stereo");

        println!("\n>>> Music mode ready <<<\n");
    }
}

// ============================================================================
// Main - Demonstrates facade usage
// ============================================================================

fn main() {
    println!("============================================");
    println!("   FACADE DESIGN PATTERN DEMONSTRATION");
    println!("============================================\n");

    // Create the facade - user only interacts with this
    let home_theater = HomeTheaterFacade::new();

    // Without facade: user would need to call 10+ methods manually
    // With facade: single method call handles everything

    println!("--------------------------------------------");
    println!("Client calls: home_theater.watch_movie(...)");
    println!("--------------------------------------------\n");

    home_theater.watch_movie("The Matrix");

    println!("--------------------------------------------");
    println!("Client calls: home_theater.end_movie()");
    println!("--------------------------------------------\n");

    home_theater.end_movie();

    println!("--------------------------------------------");
    println!("Client calls: home_theater.listen_to_music()");
    println!("--------------------------------------------\n");

    home_theater.listen_to_music();

    println!("============================================");
    println!("   KEY INSIGHT: Facade Pattern");
    println!("============================================");
    println!("The client made only 3 simple calls, but the");
    println!("facade coordinated 15+ subsystem operations!");
    println!("============================================\n");
}
