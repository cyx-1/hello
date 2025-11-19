/**
 * Facade Design Pattern in TypeScript
 *
 * The Facade pattern provides a simplified interface to a complex subsystem.
 * It hides the complexity of the subsystem and provides a single unified
 * interface that is easier to use for clients.
 */

// ============================================================
// Subsystem Classes - Complex components that the Facade simplifies
// ============================================================

// Subsystem 1: Television
class Television {
    private isOn: boolean = false;
    private channel: number = 1;

    on(): void {
        this.isOn = true;
        console.log("[Line 18] Television: Powering on");
    }

    off(): void {
        this.isOn = false;
        console.log("[Line 23] Television: Powering off");
    }

    setInputChannel(channel: number): void {
        this.channel = channel;
        console.log(`[Line 28] Television: Setting input channel to ${channel}`);
    }
}

// Subsystem 2: Sound System
class SoundSystem {
    private volume: number = 0;
    private surroundMode: boolean = false;

    on(): void {
        console.log("[Line 37] SoundSystem: Powering on amplifier");
    }

    off(): void {
        console.log("[Line 41] SoundSystem: Powering off amplifier");
    }

    setVolume(level: number): void {
        this.volume = level;
        console.log(`[Line 46] SoundSystem: Setting volume to ${level}`);
    }

    setSurroundSound(enabled: boolean): void {
        this.surroundMode = enabled;
        const mode = enabled ? "surround" : "stereo";
        console.log(`[Line 52] SoundSystem: Setting audio mode to ${mode}`);
    }
}

// Subsystem 3: Streaming Player
class StreamingPlayer {
    private currentMovie: string = "";

    on(): void {
        console.log("[Line 60] StreamingPlayer: Starting streaming device");
    }

    off(): void {
        console.log("[Line 64] StreamingPlayer: Shutting down streaming device");
    }

    play(movie: string): void {
        this.currentMovie = movie;
        console.log(`[Line 69] StreamingPlayer: Playing "${movie}"`);
    }

    pause(): void {
        console.log(`[Line 73] StreamingPlayer: Pausing "${this.currentMovie}"`);
    }

    stop(): void {
        console.log(`[Line 77] StreamingPlayer: Stopping "${this.currentMovie}"`);
        this.currentMovie = "";
    }
}

// Subsystem 4: Room Lights
class RoomLights {
    private brightness: number = 100;

    on(): void {
        this.brightness = 100;
        console.log("[Line 87] RoomLights: Turning lights on");
    }

    off(): void {
        this.brightness = 0;
        console.log("[Line 92] RoomLights: Turning lights off");
    }

    dim(level: number): void {
        this.brightness = level;
        console.log(`[Line 97] RoomLights: Dimming lights to ${level}%`);
    }
}

// Subsystem 5: Popcorn Machine
class PopcornMachine {
    on(): void {
        console.log("[Line 104] PopcornMachine: Turning on popcorn machine");
    }

    off(): void {
        console.log("[Line 108] PopcornMachine: Turning off popcorn machine");
    }

    pop(): void {
        console.log("[Line 112] PopcornMachine: Popping popcorn!");
    }
}

// ============================================================
// Facade Class - Provides simplified interface to the subsystems
// ============================================================

class HomeTheaterFacade {
    private tv: Television;
    private soundSystem: SoundSystem;
    private streamingPlayer: StreamingPlayer;
    private lights: RoomLights;
    private popcorn: PopcornMachine;

    constructor(
        tv: Television,
        soundSystem: SoundSystem,
        streamingPlayer: StreamingPlayer,
        lights: RoomLights,
        popcorn: PopcornMachine
    ) {
        this.tv = tv;
        this.soundSystem = soundSystem;
        this.streamingPlayer = streamingPlayer;
        this.lights = lights;
        this.popcorn = popcorn;
        console.log("[Line 136] HomeTheaterFacade: Home theater system initialized");
    }

    // Simplified method to start watching a movie
    watchMovie(movie: string): void {
        console.log(`\n[Line 141] HomeTheaterFacade: Preparing to watch "${movie}"...`);
        console.log("----------------------------------------");

        this.popcorn.on();
        this.popcorn.pop();
        this.lights.dim(10);
        this.tv.on();
        this.tv.setInputChannel(3);
        this.soundSystem.on();
        this.soundSystem.setVolume(25);
        this.soundSystem.setSurroundSound(true);
        this.streamingPlayer.on();
        this.streamingPlayer.play(movie);

        console.log("----------------------------------------");
        console.log(`[Line 156] HomeTheaterFacade: Enjoy your movie!`);
    }

    // Simplified method to pause the movie
    pauseMovie(): void {
        console.log("\n[Line 161] HomeTheaterFacade: Pausing movie...");
        this.streamingPlayer.pause();
        this.lights.dim(50);
    }

    // Simplified method to end movie watching
    endMovie(): void {
        console.log("\n[Line 168] HomeTheaterFacade: Shutting down home theater...");
        console.log("----------------------------------------");

        this.streamingPlayer.stop();
        this.streamingPlayer.off();
        this.soundSystem.off();
        this.tv.off();
        this.lights.on();
        this.popcorn.off();

        console.log("----------------------------------------");
        console.log("[Line 179] HomeTheaterFacade: Home theater shutdown complete");
    }

    // Simplified method for listening to music
    listenToMusic(): void {
        console.log("\n[Line 184] HomeTheaterFacade: Setting up music mode...");
        console.log("----------------------------------------");

        this.lights.dim(60);
        this.soundSystem.on();
        this.soundSystem.setVolume(15);
        this.soundSystem.setSurroundSound(false);

        console.log("----------------------------------------");
        console.log("[Line 193] HomeTheaterFacade: Music mode ready");
    }

    // End music mode
    endMusic(): void {
        console.log("\n[Line 198] HomeTheaterFacade: Ending music mode...");
        this.soundSystem.off();
        this.lights.on();
        console.log("[Line 201] HomeTheaterFacade: Music mode ended");
    }
}

// ============================================================
// Second Example: Computer Startup Facade
// ============================================================

// Subsystem: CPU
class CPU {
    freeze(): void {
        console.log("[Line 212] CPU: Freezing processor");
    }

    jump(address: number): void {
        console.log(`[Line 216] CPU: Jumping to address ${address}`);
    }

    execute(): void {
        console.log("[Line 220] CPU: Executing instructions");
    }
}

// Subsystem: Memory
class Memory {
    load(address: number, data: string): void {
        console.log(`[Line 227] Memory: Loading "${data}" at address ${address}`);
    }
}

// Subsystem: HardDrive
class HardDrive {
    read(sector: number, size: number): string {
        const data = `BootData[sector:${sector},size:${size}]`;
        console.log(`[Line 235] HardDrive: Reading ${size} bytes from sector ${sector}`);
        return data;
    }
}

// Computer Facade
class ComputerFacade {
    private cpu: CPU;
    private memory: Memory;
    private hardDrive: HardDrive;

    constructor() {
        this.cpu = new CPU();
        this.memory = new Memory();
        this.hardDrive = new HardDrive();
        console.log("[Line 250] ComputerFacade: Computer components initialized");
    }

    start(): void {
        console.log("\n[Line 254] ComputerFacade: Starting computer...");
        console.log("----------------------------------------");

        this.cpu.freeze();
        const bootData = this.hardDrive.read(0, 1024);
        this.memory.load(0x00, bootData);
        this.cpu.jump(0x00);
        this.cpu.execute();

        console.log("----------------------------------------");
        console.log("[Line 264] ComputerFacade: Computer started successfully");
    }

    shutdown(): void {
        console.log("\n[Line 268] ComputerFacade: Shutting down computer...");
        console.log("[Line 269] ComputerFacade: Saving state and powering off");
    }
}

// ============================================================
// Demonstration
// ============================================================

function main(): void {
    console.log("=== Facade Pattern Demonstration ===");

    // Demo 1: Home Theater Facade
    console.log("\n--- Home Theater Facade Demo ---");

    // Create subsystem components
    const tv = new Television();
    const soundSystem = new SoundSystem();
    const streamingPlayer = new StreamingPlayer();
    const lights = new RoomLights();
    const popcorn = new PopcornMachine();

    // Create facade with all subsystems
    const homeTheater = new HomeTheaterFacade(
        tv,
        soundSystem,
        streamingPlayer,
        lights,
        popcorn
    );

    // Use simplified facade methods instead of controlling each subsystem
    homeTheater.watchMovie("The Matrix");

    // Pause for a break
    homeTheater.pauseMovie();

    // End the movie session
    homeTheater.endMovie();

    // Quick music session
    homeTheater.listenToMusic();
    homeTheater.endMusic();

    // Demo 2: Computer Startup Facade
    console.log("\n\n--- Computer Startup Facade Demo ---");

    const computer = new ComputerFacade();
    computer.start();
    computer.shutdown();

    // Demo 3: Show what it would look like WITHOUT the facade
    console.log("\n\n--- Without Facade (Direct Subsystem Control) ---");
    console.log("[Line 318] Direct control requires managing each subsystem:");

    const manualTv = new Television();
    const manualSound = new SoundSystem();
    const manualPlayer = new StreamingPlayer();
    const manualLights = new RoomLights();
    const manualPopcorn = new PopcornMachine();

    console.log("\nManually setting up movie (verbose and error-prone):");
    manualPopcorn.on();
    manualPopcorn.pop();
    manualLights.dim(10);
    manualTv.on();
    manualTv.setInputChannel(3);
    manualSound.on();
    manualSound.setVolume(25);
    manualSound.setSurroundSound(true);
    manualPlayer.on();
    manualPlayer.play("Inception");

    console.log("\n[Line 338] Notice how the facade simplifies all of this!");
    console.log("         With facade: homeTheater.watchMovie('Inception')");
    console.log("         Without facade: 10+ individual method calls");

    console.log("\n=== End of Demonstration ===");
}

main();
