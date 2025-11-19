/**
 * Comprehensive demonstration of the Adapter Pattern in Java
 *
 * The Adapter pattern converts the interface of a class into another interface
 * clients expect. It lets classes work together that couldn't otherwise because
 * of incompatible interfaces.
 */

import java.util.ArrayList;
import java.util.List;

// Target interface - what the client expects
interface MediaPlayer {
    void play(String audioType, String fileName);
}

// Adaptee interfaces - existing incompatible interfaces
interface AdvancedMediaPlayer {
    void playVlc(String fileName);
    void playMp4(String fileName);
}

// Concrete Adaptees
class VlcPlayer implements AdvancedMediaPlayer {
    @Override
    public void playVlc(String fileName) {
        System.out.println("  [VlcPlayer] Playing VLC file: " + fileName);
    }

    @Override
    public void playMp4(String fileName) {
        // Do nothing - VLC player doesn't play MP4
    }
}

class Mp4Player implements AdvancedMediaPlayer {
    @Override
    public void playVlc(String fileName) {
        // Do nothing - MP4 player doesn't play VLC
    }

    @Override
    public void playMp4(String fileName) {
        System.out.println("  [Mp4Player] Playing MP4 file: " + fileName);
    }
}

// Object Adapter - uses composition
class MediaAdapter implements MediaPlayer {
    private AdvancedMediaPlayer advancedMusicPlayer;

    public MediaAdapter(String audioType) {
        if (audioType.equalsIgnoreCase("vlc")) {
            advancedMusicPlayer = new VlcPlayer();
        } else if (audioType.equalsIgnoreCase("mp4")) {
            advancedMusicPlayer = new Mp4Player();
        }
    }

    @Override
    public void play(String audioType, String fileName) {
        if (audioType.equalsIgnoreCase("vlc")) {
            advancedMusicPlayer.playVlc(fileName);
        } else if (audioType.equalsIgnoreCase("mp4")) {
            advancedMusicPlayer.playMp4(fileName);
        }
    }
}

// Client that uses the adapter
class AudioPlayer implements MediaPlayer {
    private MediaAdapter mediaAdapter;

    @Override
    public void play(String audioType, String fileName) {
        // Built-in support for MP3
        if (audioType.equalsIgnoreCase("mp3")) {
            System.out.println("  [AudioPlayer] Playing MP3 file: " + fileName);
        }
        // MediaAdapter provides support for other formats
        else if (audioType.equalsIgnoreCase("vlc") || audioType.equalsIgnoreCase("mp4")) {
            mediaAdapter = new MediaAdapter(audioType);
            mediaAdapter.play(audioType, fileName);
        } else {
            System.out.println("  [AudioPlayer] Invalid media type: " + audioType);
        }
    }
}

// Another example: Legacy system integration

// Legacy Rectangle uses different coordinate system
class LegacyRectangle {
    public void display(int x1, int y1, int x2, int y2) {
        System.out.println("  [LegacyRectangle] Drawing from (" + x1 + "," + y1 + ") to (" + x2 + "," + y2 + ")");
    }
}

// Modern interface uses x, y, width, height
interface Shape {
    void draw(int x, int y, int width, int height);
}

// Adapter for LegacyRectangle
class RectangleAdapter implements Shape {
    private LegacyRectangle legacyRectangle;

    public RectangleAdapter() {
        this.legacyRectangle = new LegacyRectangle();
    }

    @Override
    public void draw(int x, int y, int width, int height) {
        // Convert modern coordinates to legacy format
        int x2 = x + width;
        int y2 = y + height;
        legacyRectangle.display(x, y, x2, y2);
    }
}

// Class Adapter example using inheritance (when possible)
// Note: Java doesn't support multiple inheritance, so this is limited

// Third-party analytics library
class ThirdPartyAnalytics {
    public void trackEvent(String eventName, String... params) {
        System.out.println("  [ThirdPartyAnalytics] Tracking: " + eventName);
        for (String param : params) {
            System.out.println("    - " + param);
        }
    }
}

// Our application's analytics interface
interface Analytics {
    void logEvent(String event);
    void logEventWithData(String event, String key, String value);
}

// Adapter using composition
class AnalyticsAdapter implements Analytics {
    private ThirdPartyAnalytics thirdParty;

    public AnalyticsAdapter(ThirdPartyAnalytics thirdParty) {
        this.thirdParty = thirdParty;
    }

    @Override
    public void logEvent(String event) {
        thirdParty.trackEvent(event);
    }

    @Override
    public void logEventWithData(String event, String key, String value) {
        thirdParty.trackEvent(event, key + "=" + value);
    }
}

// Two-way Adapter example
interface Duck {
    void quack();
    void fly();
}

interface Turkey {
    void gobble();
    void fly();
}

class WildDuck implements Duck {
    @Override
    public void quack() {
        System.out.println("  [WildDuck] Quack!");
    }

    @Override
    public void fly() {
        System.out.println("  [WildDuck] Flying majestically");
    }
}

class WildTurkey implements Turkey {
    @Override
    public void gobble() {
        System.out.println("  [WildTurkey] Gobble gobble!");
    }

    @Override
    public void fly() {
        System.out.println("  [WildTurkey] Flying a short distance");
    }
}

// Adapter to make Turkey look like Duck
class TurkeyAdapter implements Duck {
    private Turkey turkey;

    public TurkeyAdapter(Turkey turkey) {
        this.turkey = turkey;
    }

    @Override
    public void quack() {
        turkey.gobble();
    }

    @Override
    public void fly() {
        // Turkeys fly shorter distances, so fly multiple times
        for (int i = 0; i < 3; i++) {
            turkey.fly();
        }
    }
}

// Adapter to make Duck look like Turkey
class DuckAdapter implements Turkey {
    private Duck duck;

    public DuckAdapter(Duck duck) {
        this.duck = duck;
    }

    @Override
    public void gobble() {
        duck.quack();
    }

    @Override
    public void fly() {
        duck.fly();
    }
}

public class MainAdapter {
    public static void main(String[] args) {
        System.out.println("=== Adapter Pattern Demonstration ===\n");

        // Media player adapter example
        System.out.println("--- 1. Media Player Adapter ---");
        AudioPlayer audioPlayer = new AudioPlayer();
        audioPlayer.play("mp3", "song.mp3");
        audioPlayer.play("mp4", "movie.mp4");
        audioPlayer.play("vlc", "video.vlc");
        audioPlayer.play("avi", "unsupported.avi");
        System.out.println();

        // Legacy rectangle adapter
        System.out.println("--- 2. Legacy System Adapter ---");
        Shape rectangle = new RectangleAdapter();
        rectangle.draw(10, 20, 100, 50);
        rectangle.draw(50, 60, 200, 100);
        System.out.println();

        // Analytics adapter
        System.out.println("--- 3. Third-Party Library Adapter ---");
        ThirdPartyAnalytics thirdParty = new ThirdPartyAnalytics();
        Analytics analytics = new AnalyticsAdapter(thirdParty);
        analytics.logEvent("page_view");
        analytics.logEventWithData("button_click", "button_id", "submit_btn");
        System.out.println();

        // Duck/Turkey adapter
        System.out.println("--- 4. Two-Way Adapter (Duck/Turkey) ---");

        Duck duck = new WildDuck();
        Turkey turkey = new WildTurkey();

        System.out.println("Original Duck:");
        duck.quack();
        duck.fly();

        System.out.println("\nOriginal Turkey:");
        turkey.gobble();
        turkey.fly();

        System.out.println("\nTurkey adapted to Duck interface:");
        Duck turkeyAdapter = new TurkeyAdapter(turkey);
        turkeyAdapter.quack();
        turkeyAdapter.fly();

        System.out.println("\nDuck adapted to Turkey interface:");
        Turkey duckAdapter = new DuckAdapter(duck);
        duckAdapter.gobble();
        duckAdapter.fly();

        System.out.println("\n=== Summary ===");
        System.out.println("Adapter pattern benefits:");
        System.out.println("  - Single Responsibility: separate interface conversion from business logic");
        System.out.println("  - Open/Closed: introduce new adapters without changing existing code");
        System.out.println("  - Reuse existing classes with incompatible interfaces");
        System.out.println("  - Increase class transparency and flexibility");
        System.out.println("\nTypes of adapters:");
        System.out.println("  - Object Adapter: uses composition (more flexible)");
        System.out.println("  - Class Adapter: uses inheritance (limited in Java)");
    }
}
