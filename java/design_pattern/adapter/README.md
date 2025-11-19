# Adapter Pattern

The Adapter pattern converts the interface of a class into another interface clients expect, allowing incompatible classes to work together.

## How to Run

```bash
cd java/adapter
mvn compile exec:java
```

## Key Source Code

### Target Interface (Lines 12-14)
```java
interface MediaPlayer {
    void play(String audioType, String fileName);
}
```

### Adaptee with Incompatible Interface (Lines 17-21)
```java
interface AdvancedMediaPlayer {
    void playVlc(String fileName);
    void playMp4(String fileName);
}
```

### Object Adapter (Lines 47-64)
```java
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
        }
        // ...
    }
}
```

## Program Output

```
=== Adapter Pattern Demonstration ===

--- 1. Media Player Adapter ---
  [AudioPlayer] Playing MP3 file: song.mp3
  [Mp4Player] Playing MP4 file: movie.mp4
  [VlcPlayer] Playing VLC file: video.vlc
  [AudioPlayer] Invalid media type: avi

--- 2. Legacy System Adapter ---
  [LegacyRectangle] Drawing from (10,20) to (110,70)
  [LegacyRectangle] Drawing from (50,60) to (250,160)

--- 3. Third-Party Library Adapter ---
  [ThirdPartyAnalytics] Tracking: page_view
  [ThirdPartyAnalytics] Tracking: button_click
    - button_id=submit_btn

--- 4. Two-Way Adapter (Duck/Turkey) ---
Original Duck:
  [WildDuck] Quack!
  [WildDuck] Flying majestically

Turkey adapted to Duck interface:
  [WildTurkey] Gobble gobble!
  [WildTurkey] Flying a short distance
  [WildTurkey] Flying a short distance
  [WildTurkey] Flying a short distance
```

## Pattern Benefits

1. **Single Responsibility**: Separates interface conversion from business logic
2. **Open/Closed**: Add new adapters without changing existing code
3. **Reusability**: Use existing classes with incompatible interfaces
4. **Transparency**: Client uses target interface uniformly

## Requirements

- Java 17 or higher
- Maven 3.x
