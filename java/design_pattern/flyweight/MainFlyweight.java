/**
 * Comprehensive demonstration of the Flyweight Pattern in Java
 *
 * The Flyweight pattern uses sharing to support large numbers of fine-grained
 * objects efficiently. It minimizes memory usage by sharing common state
 * between multiple objects.
 */

import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;

// Flyweight interface
interface TreeType {
    void draw(int x, int y);
}

// Concrete Flyweight - contains intrinsic (shared) state
class TreeTypeImpl implements TreeType {
    private String name;
    private String color;
    private String texture;

    public TreeTypeImpl(String name, String color, String texture) {
        this.name = name;
        this.color = color;
        this.texture = texture;
        System.out.println("  Creating TreeType: " + name + " (this is shared)");
    }

    @Override
    public void draw(int x, int y) {
        System.out.println("    Drawing " + name + " tree at (" + x + ", " + y + ") with color " + color);
    }

    public String getName() {
        return name;
    }
}

// Flyweight Factory
class TreeFactory {
    private static Map<String, TreeType> treeTypes = new HashMap<>();

    public static TreeType getTreeType(String name, String color, String texture) {
        String key = name + "_" + color + "_" + texture;
        TreeType result = treeTypes.get(key);

        if (result == null) {
            result = new TreeTypeImpl(name, color, texture);
            treeTypes.put(key, result);
        }

        return result;
    }

    public static int getTreeTypeCount() {
        return treeTypes.size();
    }
}

// Context class - contains extrinsic (unique) state
class Tree {
    private int x;
    private int y;
    private TreeType type;  // Flyweight reference

    public Tree(int x, int y, TreeType type) {
        this.x = x;
        this.y = y;
        this.type = type;
    }

    public void draw() {
        type.draw(x, y);
    }
}

// Forest manages all trees
class Forest {
    private List<Tree> trees = new ArrayList<>();

    public void plantTree(int x, int y, String name, String color, String texture) {
        TreeType type = TreeFactory.getTreeType(name, color, texture);
        Tree tree = new Tree(x, y, type);
        trees.add(tree);
    }

    public void draw() {
        for (Tree tree : trees) {
            tree.draw();
        }
    }

    public int getTreeCount() {
        return trees.size();
    }
}

// Another example: Text Editor with Character Flyweights

// Flyweight
interface CharacterStyle {
    void display(char c);
}

// Concrete Flyweight
class CharacterStyleImpl implements CharacterStyle {
    private String fontFamily;
    private int fontSize;
    private String color;
    private boolean bold;
    private boolean italic;

    public CharacterStyleImpl(String fontFamily, int fontSize, String color, boolean bold, boolean italic) {
        this.fontFamily = fontFamily;
        this.fontSize = fontSize;
        this.color = color;
        this.bold = bold;
        this.italic = italic;
    }

    @Override
    public void display(char c) {
        String style = fontFamily + "/" + fontSize + "pt/" + color;
        if (bold) style += "/B";
        if (italic) style += "/I";
        System.out.print("[" + c + ":" + style + "]");
    }

    @Override
    public String toString() {
        return fontFamily + ", " + fontSize + "pt, " + color +
               (bold ? ", bold" : "") + (italic ? ", italic" : "");
    }
}

// Flyweight Factory
class StyleFactory {
    private static Map<String, CharacterStyle> styles = new HashMap<>();

    public static CharacterStyle getStyle(String fontFamily, int fontSize, String color,
                                          boolean bold, boolean italic) {
        String key = fontFamily + "_" + fontSize + "_" + color + "_" + bold + "_" + italic;
        CharacterStyle style = styles.get(key);

        if (style == null) {
            style = new CharacterStyleImpl(fontFamily, fontSize, color, bold, italic);
            styles.put(key, style);
        }

        return style;
    }

    public static int getStyleCount() {
        return styles.size();
    }
}

// Context
class FormattedCharacter {
    private char character;
    private CharacterStyle style;

    public FormattedCharacter(char character, CharacterStyle style) {
        this.character = character;
        this.style = style;
    }

    public void display() {
        style.display(character);
    }
}

// Document using flyweight characters
class TextDocument {
    private List<FormattedCharacter> characters = new ArrayList<>();

    public void addCharacter(char c, String fontFamily, int fontSize, String color,
                            boolean bold, boolean italic) {
        CharacterStyle style = StyleFactory.getStyle(fontFamily, fontSize, color, bold, italic);
        characters.add(new FormattedCharacter(c, style));
    }

    public void addText(String text, String fontFamily, int fontSize, String color,
                       boolean bold, boolean italic) {
        for (char c : text.toCharArray()) {
            addCharacter(c, fontFamily, fontSize, color, bold, italic);
        }
    }

    public void display() {
        for (FormattedCharacter fc : characters) {
            fc.display();
        }
        System.out.println();
    }

    public int getCharacterCount() {
        return characters.size();
    }
}

// Third example: Game with particle effects

interface Particle {
    void render(int x, int y, int speed, int direction);
}

class ParticleType implements Particle {
    private String sprite;
    private String color;

    public ParticleType(String sprite, String color) {
        this.sprite = sprite;
        this.color = color;
        System.out.println("  Loading particle sprite: " + sprite + " (" + color + ")");
    }

    @Override
    public void render(int x, int y, int speed, int direction) {
        System.out.println("    Particle " + sprite + " at (" + x + "," + y +
                          ") speed=" + speed + " dir=" + direction + "°");
    }
}

class ParticleFactory {
    private static Map<String, Particle> particles = new HashMap<>();

    public static Particle getParticle(String sprite, String color) {
        String key = sprite + "_" + color;
        Particle particle = particles.get(key);

        if (particle == null) {
            particle = new ParticleType(sprite, color);
            particles.put(key, particle);
        }

        return particle;
    }

    public static int getParticleTypeCount() {
        return particles.size();
    }
}

class MovingParticle {
    private int x, y, speed, direction;
    private Particle type;

    public MovingParticle(int x, int y, int speed, int direction, Particle type) {
        this.x = x;
        this.y = y;
        this.speed = speed;
        this.direction = direction;
        this.type = type;
    }

    public void render() {
        type.render(x, y, speed, direction);
    }
}

public class MainFlyweight {
    public static void main(String[] args) {
        System.out.println("=== Flyweight Pattern Demonstration ===\n");

        // Forest example
        System.out.println("--- 1. Forest with Shared Tree Types ---");
        System.out.println("Creating tree types (flyweights):\n");

        Forest forest = new Forest();

        // Plant many trees but only create 3 tree types
        forest.plantTree(10, 20, "Oak", "Green", "Rough");
        forest.plantTree(50, 30, "Pine", "Dark Green", "Smooth");
        forest.plantTree(100, 40, "Oak", "Green", "Rough");       // Reuses Oak
        forest.plantTree(150, 50, "Birch", "Light Green", "Paper");
        forest.plantTree(200, 60, "Pine", "Dark Green", "Smooth"); // Reuses Pine
        forest.plantTree(250, 70, "Oak", "Green", "Rough");        // Reuses Oak

        System.out.println("\nDrawing forest:\n");
        forest.draw();

        System.out.println("\nStatistics:");
        System.out.println("  Total trees: " + forest.getTreeCount());
        System.out.println("  Unique tree types (flyweights): " + TreeFactory.getTreeTypeCount());
        System.out.println("  Memory saved: " + (forest.getTreeCount() - TreeFactory.getTreeTypeCount()) + " objects");
        System.out.println();

        // Text document example
        System.out.println("--- 2. Text Document with Shared Styles ---");

        TextDocument doc = new TextDocument();

        // Add text with different styles
        doc.addText("Hello", "Arial", 12, "Black", false, false);
        doc.addText(" ", "Arial", 12, "Black", false, false);
        doc.addText("World", "Arial", 12, "Red", true, false);
        doc.addText("!", "Arial", 12, "Red", true, false);  // Reuses red bold style

        System.out.println("Document content:");
        doc.display();

        System.out.println("Statistics:");
        System.out.println("  Total characters: " + doc.getCharacterCount());
        System.out.println("  Unique styles (flyweights): " + StyleFactory.getStyleCount());
        System.out.println();

        // Particle system example
        System.out.println("--- 3. Game Particle System ---");
        System.out.println("Loading particle types:\n");

        List<MovingParticle> particles = new ArrayList<>();

        // Create many particles with few types
        particles.add(new MovingParticle(100, 200, 5, 45, ParticleFactory.getParticle("spark", "yellow")));
        particles.add(new MovingParticle(110, 205, 6, 50, ParticleFactory.getParticle("spark", "yellow")));
        particles.add(new MovingParticle(120, 210, 4, 40, ParticleFactory.getParticle("spark", "orange")));
        particles.add(new MovingParticle(130, 215, 7, 55, ParticleFactory.getParticle("smoke", "gray")));
        particles.add(new MovingParticle(140, 220, 3, 35, ParticleFactory.getParticle("smoke", "gray")));

        System.out.println("\nRendering particles:\n");
        for (MovingParticle p : particles) {
            p.render();
        }

        System.out.println("\nStatistics:");
        System.out.println("  Total particles: " + particles.size());
        System.out.println("  Unique particle types: " + ParticleFactory.getParticleTypeCount());

        System.out.println("\n=== Summary ===");
        System.out.println("Flyweight pattern benefits:");
        System.out.println("  - Reduces memory usage when many similar objects exist");
        System.out.println("  - Shares intrinsic state among multiple objects");
        System.out.println("  - Extrinsic state is passed in at runtime");
        System.out.println("\nKey concepts:");
        System.out.println("  - Intrinsic state: shared, immutable (in flyweight)");
        System.out.println("  - Extrinsic state: unique, varies (in context)");
        System.out.println("  - Factory ensures flyweight sharing");
        System.out.println("\nUse cases:");
        System.out.println("  - Game objects (trees, particles, characters)");
        System.out.println("  - Text formatting (character styles)");
        System.out.println("  - Caching and pooling");
    }
}
