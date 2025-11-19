/**
 * Comprehensive demonstration of the Bridge Pattern in Java
 *
 * The Bridge pattern decouples an abstraction from its implementation so that
 * the two can vary independently.
 */

// Implementor interface - the "bridge"
interface Device {
    boolean isEnabled();
    void enable();
    void disable();
    int getVolume();
    void setVolume(int volume);
    int getChannel();
    void setChannel(int channel);
    String getDeviceInfo();
}

// Concrete Implementors
class TV implements Device {
    private boolean on = false;
    private int volume = 30;
    private int channel = 1;

    @Override
    public boolean isEnabled() { return on; }

    @Override
    public void enable() {
        on = true;
        System.out.println("  [TV] TV is now ON");
    }

    @Override
    public void disable() {
        on = false;
        System.out.println("  [TV] TV is now OFF");
    }

    @Override
    public int getVolume() { return volume; }

    @Override
    public void setVolume(int volume) {
        this.volume = Math.max(0, Math.min(100, volume));
        System.out.println("  [TV] Volume set to " + this.volume);
    }

    @Override
    public int getChannel() { return channel; }

    @Override
    public void setChannel(int channel) {
        this.channel = channel;
        System.out.println("  [TV] Channel set to " + this.channel);
    }

    @Override
    public String getDeviceInfo() {
        return "TV [on=" + on + ", volume=" + volume + ", channel=" + channel + "]";
    }
}

class Radio implements Device {
    private boolean on = false;
    private int volume = 20;
    private int channel = 88;

    @Override
    public boolean isEnabled() { return on; }

    @Override
    public void enable() {
        on = true;
        System.out.println("  [Radio] Radio is now ON");
    }

    @Override
    public void disable() {
        on = false;
        System.out.println("  [Radio] Radio is now OFF");
    }

    @Override
    public int getVolume() { return volume; }

    @Override
    public void setVolume(int volume) {
        this.volume = Math.max(0, Math.min(100, volume));
        System.out.println("  [Radio] Volume set to " + this.volume);
    }

    @Override
    public int getChannel() { return channel; }

    @Override
    public void setChannel(int channel) {
        this.channel = channel;
        System.out.println("  [Radio] Frequency set to " + this.channel + " FM");
    }

    @Override
    public String getDeviceInfo() {
        return "Radio [on=" + on + ", volume=" + volume + ", frequency=" + channel + " FM]";
    }
}

class SmartSpeaker implements Device {
    private boolean on = false;
    private int volume = 50;
    private int preset = 1;

    @Override
    public boolean isEnabled() { return on; }

    @Override
    public void enable() {
        on = true;
        System.out.println("  [SmartSpeaker] Smart Speaker is now ON");
    }

    @Override
    public void disable() {
        on = false;
        System.out.println("  [SmartSpeaker] Smart Speaker is now OFF");
    }

    @Override
    public int getVolume() { return volume; }

    @Override
    public void setVolume(int volume) {
        this.volume = Math.max(0, Math.min(100, volume));
        System.out.println("  [SmartSpeaker] Volume set to " + this.volume);
    }

    @Override
    public int getChannel() { return preset; }

    @Override
    public void setChannel(int channel) {
        this.preset = channel;
        System.out.println("  [SmartSpeaker] Preset changed to " + this.preset);
    }

    @Override
    public String getDeviceInfo() {
        return "SmartSpeaker [on=" + on + ", volume=" + volume + ", preset=" + preset + "]";
    }
}

// Abstraction
abstract class RemoteControl {
    protected Device device;

    protected RemoteControl(Device device) {
        this.device = device;
    }

    public void togglePower() {
        if (device.isEnabled()) {
            device.disable();
        } else {
            device.enable();
        }
    }

    public void volumeUp() {
        device.setVolume(device.getVolume() + 10);
    }

    public void volumeDown() {
        device.setVolume(device.getVolume() - 10);
    }

    public void channelUp() {
        device.setChannel(device.getChannel() + 1);
    }

    public void channelDown() {
        device.setChannel(device.getChannel() - 1);
    }

    public String getStatus() {
        return device.getDeviceInfo();
    }
}

// Refined Abstractions
class BasicRemote extends RemoteControl {
    public BasicRemote(Device device) {
        super(device);
    }
}

class AdvancedRemote extends RemoteControl {
    public AdvancedRemote(Device device) {
        super(device);
    }

    public void mute() {
        System.out.println("  [AdvancedRemote] Muting device");
        device.setVolume(0);
    }

    public void setVolumeLevel(int level) {
        System.out.println("  [AdvancedRemote] Setting exact volume level");
        device.setVolume(level);
    }

    public void goToChannel(int channel) {
        System.out.println("  [AdvancedRemote] Going to channel " + channel);
        device.setChannel(channel);
    }
}

// Another example: Drawing shapes with different renderers

// Implementor
interface Renderer {
    void renderCircle(float x, float y, float radius);
    void renderRectangle(float x, float y, float width, float height);
}

// Concrete Implementors
class VectorRenderer implements Renderer {
    @Override
    public void renderCircle(float x, float y, float radius) {
        System.out.println("  [VectorRenderer] Drawing circle at (" + x + ", " + y + ") with radius " + radius);
    }

    @Override
    public void renderRectangle(float x, float y, float width, float height) {
        System.out.println("  [VectorRenderer] Drawing rectangle at (" + x + ", " + y + ") with size " + width + "x" + height);
    }
}

class RasterRenderer implements Renderer {
    @Override
    public void renderCircle(float x, float y, float radius) {
        System.out.println("  [RasterRenderer] Rasterizing circle at (" + x + ", " + y + ") with radius " + radius + " pixels");
    }

    @Override
    public void renderRectangle(float x, float y, float width, float height) {
        System.out.println("  [RasterRenderer] Rasterizing rectangle at (" + x + ", " + y + ") with size " + width + "x" + height + " pixels");
    }
}

// Abstraction
abstract class DrawingShape {
    protected Renderer renderer;

    protected DrawingShape(Renderer renderer) {
        this.renderer = renderer;
    }

    public abstract void draw();
    public abstract void resize(float factor);
}

// Refined Abstractions
class DrawingCircle extends DrawingShape {
    private float x, y, radius;

    public DrawingCircle(Renderer renderer, float x, float y, float radius) {
        super(renderer);
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    @Override
    public void draw() {
        renderer.renderCircle(x, y, radius);
    }

    @Override
    public void resize(float factor) {
        radius *= factor;
        System.out.println("  Circle resized to radius " + radius);
    }
}

class DrawingRectangle extends DrawingShape {
    private float x, y, width, height;

    public DrawingRectangle(Renderer renderer, float x, float y, float width, float height) {
        super(renderer);
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    @Override
    public void draw() {
        renderer.renderRectangle(x, y, width, height);
    }

    @Override
    public void resize(float factor) {
        width *= factor;
        height *= factor;
        System.out.println("  Rectangle resized to " + width + "x" + height);
    }
}

public class MainBridge {
    public static void main(String[] args) {
        System.out.println("=== Bridge Pattern Demonstration ===\n");

        // Remote Control with TV
        System.out.println("--- 1. Basic Remote with TV ---");
        Device tv = new TV();
        RemoteControl basicRemote = new BasicRemote(tv);

        basicRemote.togglePower();
        basicRemote.volumeUp();
        basicRemote.channelUp();
        basicRemote.channelUp();
        System.out.println("Status: " + basicRemote.getStatus());
        System.out.println();

        // Advanced Remote with Radio
        System.out.println("--- 2. Advanced Remote with Radio ---");
        Device radio = new Radio();
        AdvancedRemote advancedRemote = new AdvancedRemote(radio);

        advancedRemote.togglePower();
        advancedRemote.setVolumeLevel(75);
        advancedRemote.goToChannel(102);
        advancedRemote.mute();
        System.out.println("Status: " + advancedRemote.getStatus());
        System.out.println();

        // Same remote with different device
        System.out.println("--- 3. Same Advanced Remote with Smart Speaker ---");
        Device speaker = new SmartSpeaker();
        AdvancedRemote speakerRemote = new AdvancedRemote(speaker);

        speakerRemote.togglePower();
        speakerRemote.setVolumeLevel(40);
        speakerRemote.goToChannel(3);
        System.out.println("Status: " + speakerRemote.getStatus());
        System.out.println();

        // Drawing shapes with different renderers
        System.out.println("--- 4. Shapes with Vector Renderer ---");
        Renderer vectorRenderer = new VectorRenderer();

        DrawingShape circle1 = new DrawingCircle(vectorRenderer, 5, 10, 25);
        DrawingShape rect1 = new DrawingRectangle(vectorRenderer, 10, 20, 100, 50);

        circle1.draw();
        rect1.draw();
        System.out.println();

        System.out.println("--- 5. Same Shapes with Raster Renderer ---");
        Renderer rasterRenderer = new RasterRenderer();

        DrawingShape circle2 = new DrawingCircle(rasterRenderer, 5, 10, 25);
        DrawingShape rect2 = new DrawingRectangle(rasterRenderer, 10, 20, 100, 50);

        circle2.draw();
        rect2.draw();
        System.out.println();

        // Resizing demonstration
        System.out.println("--- 6. Resizing Shapes ---");
        circle1.resize(2);
        circle1.draw();
        rect2.resize(0.5f);
        rect2.draw();

        System.out.println("\n=== Summary ===");
        System.out.println("Bridge pattern benefits:");
        System.out.println("  - Decouples abstraction from implementation");
        System.out.println("  - Both can vary independently");
        System.out.println("  - Platform independence: same abstraction, different implementations");
        System.out.println("  - Improves extensibility: add new abstractions and implementations independently");
        System.out.println("\nBridge vs Adapter:");
        System.out.println("  - Bridge: designed upfront to let abstraction and implementation vary");
        System.out.println("  - Adapter: makes unrelated classes work together after the fact");
    }
}
