"use strict";
/**
 * Bridge Design Pattern - TypeScript Implementation
 *
 * The Bridge pattern separates an abstraction from its implementation
 * so that both can vary independently. This example demonstrates
 * remote controls (abstraction) operating different devices (implementation).
 */
// =============================================================================
// Concrete Implementations - TV and Radio
// =============================================================================
/**
 * TV - A concrete implementation of the Device interface
 */
class TV {
    constructor() {
        this.enabled = false;
        this.volume = 30;
        this.channel = 1;
    }
    isEnabled() {
        return this.enabled;
    }
    enable() {
        this.enabled = true;
        console.log("[Line 42] TV: Powered ON");
    }
    disable() {
        this.enabled = false;
        console.log("[Line 47] TV: Powered OFF");
    }
    getVolume() {
        return this.volume;
    }
    setVolume(volume) {
        if (volume > 100) {
            this.volume = 100;
        }
        else if (volume < 0) {
            this.volume = 0;
        }
        else {
            this.volume = volume;
        }
        console.log(`[Line 62] TV: Volume set to ${this.volume}`);
    }
    getChannel() {
        return this.channel;
    }
    setChannel(channel) {
        this.channel = channel;
        console.log(`[Line 70] TV: Channel set to ${this.channel}`);
    }
    getName() {
        return "TV";
    }
}
/**
 * Radio - Another concrete implementation of the Device interface
 */
class Radio {
    constructor() {
        this.enabled = false;
        this.volume = 20;
        this.channel = 88;
    }
    isEnabled() {
        return this.enabled;
    }
    enable() {
        this.enabled = true;
        console.log("[Line 92] Radio: Powered ON");
    }
    disable() {
        this.enabled = false;
        console.log("[Line 97] Radio: Powered OFF");
    }
    getVolume() {
        return this.volume;
    }
    setVolume(volume) {
        if (volume > 100) {
            this.volume = 100;
        }
        else if (volume < 0) {
            this.volume = 0;
        }
        else {
            this.volume = volume;
        }
        console.log(`[Line 112] Radio: Volume set to ${this.volume}`);
    }
    getChannel() {
        return this.channel;
    }
    setChannel(channel) {
        this.channel = channel;
        console.log(`[Line 120] Radio: Station set to ${this.channel} FM`);
    }
    getName() {
        return "Radio";
    }
}
// =============================================================================
// Abstraction - RemoteControl
// =============================================================================
/**
 * The Abstraction defines the interface for the "control" part of the two
 * class hierarchies. It maintains a reference to an object of the
 * Implementation hierarchy and delegates all real work to this object.
 */
class RemoteControl {
    constructor(device) {
        this.device = device;
        console.log(`[Line 142] RemoteControl: Created for ${device.getName()}`);
    }
    togglePower() {
        console.log(`[Line 146] RemoteControl: Toggle power button pressed`);
        if (this.device.isEnabled()) {
            this.device.disable();
        }
        else {
            this.device.enable();
        }
    }
    volumeDown() {
        console.log(`[Line 155] RemoteControl: Volume down button pressed`);
        this.device.setVolume(this.device.getVolume() - 10);
    }
    volumeUp() {
        console.log(`[Line 160] RemoteControl: Volume up button pressed`);
        this.device.setVolume(this.device.getVolume() + 10);
    }
    channelDown() {
        console.log(`[Line 165] RemoteControl: Channel down button pressed`);
        this.device.setChannel(this.device.getChannel() - 1);
    }
    channelUp() {
        console.log(`[Line 170] RemoteControl: Channel up button pressed`);
        this.device.setChannel(this.device.getChannel() + 1);
    }
    getStatus() {
        console.log(`[Line 175] RemoteControl: Status - ${this.device.getName()} is ${this.device.isEnabled() ? "ON" : "OFF"}, Volume: ${this.device.getVolume()}, Channel: ${this.device.getChannel()}`);
    }
}
// =============================================================================
// Refined Abstraction - AdvancedRemoteControl
// =============================================================================
/**
 * AdvancedRemoteControl extends the basic RemoteControl with additional features.
 * This demonstrates that abstractions can be extended without affecting implementations.
 */
class AdvancedRemoteControl extends RemoteControl {
    constructor(device) {
        super(device);
        console.log(`[Line 191] AdvancedRemoteControl: Enhanced features enabled`);
    }
    mute() {
        console.log(`[Line 195] AdvancedRemoteControl: Mute button pressed`);
        this.device.setVolume(0);
    }
    setVolumeLevel(level) {
        console.log(`[Line 200] AdvancedRemoteControl: Setting exact volume to ${level}`);
        this.device.setVolume(level);
    }
    jumpToChannel(channel) {
        console.log(`[Line 205] AdvancedRemoteControl: Jumping to channel ${channel}`);
        this.device.setChannel(channel);
    }
    printDetailedStatus() {
        const status = this.device.isEnabled() ? "ON" : "OFF";
        console.log(`[Line 211] AdvancedRemoteControl: Detailed Status Report`);
        console.log(`[Line 212]   - Device: ${this.device.getName()}`);
        console.log(`[Line 213]   - Power: ${status}`);
        console.log(`[Line 214]   - Volume: ${this.device.getVolume()}%`);
        console.log(`[Line 215]   - Channel: ${this.device.getChannel()}`);
    }
}
// =============================================================================
// Client Code - Demonstration
// =============================================================================
function clientCode() {
    console.log("=".repeat(60));
    console.log("[Line 223] Bridge Pattern Demonstration");
    console.log("=".repeat(60));
    console.log();
    // Scenario 1: Basic Remote with TV
    console.log("[Line 227] --- Scenario 1: Basic Remote with TV ---");
    const tv = new TV();
    const tvRemote = new RemoteControl(tv);
    tvRemote.togglePower();
    tvRemote.volumeUp();
    tvRemote.volumeUp();
    tvRemote.channelUp();
    tvRemote.getStatus();
    tvRemote.togglePower();
    console.log();
    // Scenario 2: Basic Remote with Radio
    console.log("[Line 239] --- Scenario 2: Basic Remote with Radio ---");
    const radio = new Radio();
    const radioRemote = new RemoteControl(radio);
    radioRemote.togglePower();
    radioRemote.volumeUp();
    radioRemote.channelUp();
    radioRemote.getStatus();
    radioRemote.togglePower();
    console.log();
    // Scenario 3: Advanced Remote with TV
    console.log("[Line 250] --- Scenario 3: Advanced Remote with TV ---");
    const tv2 = new TV();
    const advancedTvRemote = new AdvancedRemoteControl(tv2);
    advancedTvRemote.togglePower();
    advancedTvRemote.setVolumeLevel(75);
    advancedTvRemote.jumpToChannel(42);
    advancedTvRemote.printDetailedStatus();
    advancedTvRemote.mute();
    advancedTvRemote.printDetailedStatus();
    console.log();
    // Scenario 4: Advanced Remote with Radio
    console.log("[Line 262] --- Scenario 4: Advanced Remote with Radio ---");
    const radio2 = new Radio();
    const advancedRadioRemote = new AdvancedRemoteControl(radio2);
    advancedRadioRemote.togglePower();
    advancedRadioRemote.setVolumeLevel(50);
    advancedRadioRemote.jumpToChannel(101);
    advancedRadioRemote.printDetailedStatus();
    console.log();
    console.log("=".repeat(60));
    console.log("[Line 272] Bridge Pattern Demonstration Complete");
    console.log("=".repeat(60));
}
// Run the demonstration
clientCode();
