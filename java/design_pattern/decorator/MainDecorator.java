/**
 * Comprehensive demonstration of the Decorator Pattern in Java
 *
 * The Decorator pattern attaches additional responsibilities to an object
 * dynamically. Decorators provide a flexible alternative to subclassing
 * for extending functionality.
 */

// Component interface
interface Coffee {
    String getDescription();
    double getCost();
}

// Concrete Component
class SimpleCoffee implements Coffee {
    @Override
    public String getDescription() {
        return "Simple Coffee";
    }

    @Override
    public double getCost() {
        return 2.00;
    }
}

class Espresso implements Coffee {
    @Override
    public String getDescription() {
        return "Espresso";
    }

    @Override
    public double getCost() {
        return 2.50;
    }
}

// Base Decorator
abstract class CoffeeDecorator implements Coffee {
    protected Coffee decoratedCoffee;

    public CoffeeDecorator(Coffee coffee) {
        this.decoratedCoffee = coffee;
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription();
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost();
    }
}

// Concrete Decorators
class MilkDecorator extends CoffeeDecorator {
    public MilkDecorator(Coffee coffee) {
        super(coffee);
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", Milk";
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.50;
    }
}

class SugarDecorator extends CoffeeDecorator {
    public SugarDecorator(Coffee coffee) {
        super(coffee);
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", Sugar";
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.20;
    }
}

class WhippedCreamDecorator extends CoffeeDecorator {
    public WhippedCreamDecorator(Coffee coffee) {
        super(coffee);
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", Whipped Cream";
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.70;
    }
}

class VanillaDecorator extends CoffeeDecorator {
    public VanillaDecorator(Coffee coffee) {
        super(coffee);
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", Vanilla";
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.60;
    }
}

class CaramelDecorator extends CoffeeDecorator {
    public CaramelDecorator(Coffee coffee) {
        super(coffee);
    }

    @Override
    public String getDescription() {
        return decoratedCoffee.getDescription() + ", Caramel";
    }

    @Override
    public double getCost() {
        return decoratedCoffee.getCost() + 0.65;
    }
}

// Another example: Text formatting

interface Text {
    String getContent();
}

class PlainText implements Text {
    private String content;

    public PlainText(String content) {
        this.content = content;
    }

    @Override
    public String getContent() {
        return content;
    }
}

abstract class TextDecorator implements Text {
    protected Text decoratedText;

    public TextDecorator(Text text) {
        this.decoratedText = text;
    }
}

class BoldDecorator extends TextDecorator {
    public BoldDecorator(Text text) {
        super(text);
    }

    @Override
    public String getContent() {
        return "<b>" + decoratedText.getContent() + "</b>";
    }
}

class ItalicDecorator extends TextDecorator {
    public ItalicDecorator(Text text) {
        super(text);
    }

    @Override
    public String getContent() {
        return "<i>" + decoratedText.getContent() + "</i>";
    }
}

class UnderlineDecorator extends TextDecorator {
    public UnderlineDecorator(Text text) {
        super(text);
    }

    @Override
    public String getContent() {
        return "<u>" + decoratedText.getContent() + "</u>";
    }
}

class ColorDecorator extends TextDecorator {
    private String color;

    public ColorDecorator(Text text, String color) {
        super(text);
        this.color = color;
    }

    @Override
    public String getContent() {
        return "<span style=\"color:" + color + "\">" + decoratedText.getContent() + "</span>";
    }
}

// Third example: Data source with encryption/compression

interface DataSource {
    void writeData(String data);
    String readData();
}

class FileDataSource implements DataSource {
    private String filename;
    private String data = "";

    public FileDataSource(String filename) {
        this.filename = filename;
    }

    @Override
    public void writeData(String data) {
        this.data = data;
        System.out.println("  [FileDataSource] Writing to " + filename + ": " + data);
    }

    @Override
    public String readData() {
        System.out.println("  [FileDataSource] Reading from " + filename);
        return data;
    }
}

abstract class DataSourceDecorator implements DataSource {
    protected DataSource wrappee;

    public DataSourceDecorator(DataSource source) {
        this.wrappee = source;
    }

    @Override
    public void writeData(String data) {
        wrappee.writeData(data);
    }

    @Override
    public String readData() {
        return wrappee.readData();
    }
}

class EncryptionDecorator extends DataSourceDecorator {
    public EncryptionDecorator(DataSource source) {
        super(source);
    }

    @Override
    public void writeData(String data) {
        String encrypted = encrypt(data);
        System.out.println("  [EncryptionDecorator] Encrypting data");
        super.writeData(encrypted);
    }

    @Override
    public String readData() {
        String data = super.readData();
        System.out.println("  [EncryptionDecorator] Decrypting data");
        return decrypt(data);
    }

    private String encrypt(String data) {
        // Simple Caesar cipher for demonstration
        StringBuilder result = new StringBuilder();
        for (char c : data.toCharArray()) {
            result.append((char) (c + 3));
        }
        return result.toString();
    }

    private String decrypt(String data) {
        StringBuilder result = new StringBuilder();
        for (char c : data.toCharArray()) {
            result.append((char) (c - 3));
        }
        return result.toString();
    }
}

class CompressionDecorator extends DataSourceDecorator {
    public CompressionDecorator(DataSource source) {
        super(source);
    }

    @Override
    public void writeData(String data) {
        String compressed = compress(data);
        System.out.println("  [CompressionDecorator] Compressing data (" + data.length() + " -> " + compressed.length() + " chars)");
        super.writeData(compressed);
    }

    @Override
    public String readData() {
        String data = super.readData();
        System.out.println("  [CompressionDecorator] Decompressing data");
        return decompress(data);
    }

    private String compress(String data) {
        // Simple RLE compression for demonstration
        return "COMPRESSED[" + data + "]";
    }

    private String decompress(String data) {
        return data.replace("COMPRESSED[", "").replace("]", "");
    }
}

public class MainDecorator {
    public static void main(String[] args) {
        System.out.println("=== Decorator Pattern Demonstration ===\n");

        // Coffee example
        System.out.println("--- 1. Coffee Shop Orders ---");

        Coffee simpleCoffee = new SimpleCoffee();
        System.out.println(simpleCoffee.getDescription() + " = $" + String.format("%.2f", simpleCoffee.getCost()));

        Coffee coffeeWithMilk = new MilkDecorator(new SimpleCoffee());
        System.out.println(coffeeWithMilk.getDescription() + " = $" + String.format("%.2f", coffeeWithMilk.getCost()));

        Coffee fancyCoffee = new WhippedCreamDecorator(
            new VanillaDecorator(
                new MilkDecorator(
                    new Espresso()
                )
            )
        );
        System.out.println(fancyCoffee.getDescription() + " = $" + String.format("%.2f", fancyCoffee.getCost()));

        Coffee caramelLatte = new CaramelDecorator(
            new WhippedCreamDecorator(
                new MilkDecorator(
                    new MilkDecorator(  // Double milk
                        new Espresso()
                    )
                )
            )
        );
        System.out.println(caramelLatte.getDescription() + " = $" + String.format("%.2f", caramelLatte.getCost()));
        System.out.println();

        // Text formatting example
        System.out.println("--- 2. Text Formatting ---");

        Text plainText = new PlainText("Hello, World!");
        System.out.println("Plain: " + plainText.getContent());

        Text boldText = new BoldDecorator(new PlainText("Hello, World!"));
        System.out.println("Bold: " + boldText.getContent());

        Text fancyText = new ColorDecorator(
            new UnderlineDecorator(
                new ItalicDecorator(
                    new BoldDecorator(
                        new PlainText("Fancy Text!")
                    )
                )
            ),
            "red"
        );
        System.out.println("Fancy: " + fancyText.getContent());
        System.out.println();

        // Data source example
        System.out.println("--- 3. Data Source with Encryption and Compression ---");

        System.out.println("\nWriting plain data:");
        DataSource plainSource = new FileDataSource("plain.txt");
        plainSource.writeData("Hello World");

        System.out.println("\nWriting encrypted data:");
        DataSource encryptedSource = new EncryptionDecorator(
            new FileDataSource("encrypted.txt")
        );
        encryptedSource.writeData("Secret Data");

        System.out.println("\nWriting compressed and encrypted data:");
        DataSource secureSource = new CompressionDecorator(
            new EncryptionDecorator(
                new FileDataSource("secure.txt")
            )
        );
        secureSource.writeData("Very Important Secret");

        System.out.println("\nReading back secure data:");
        String result = secureSource.readData();
        System.out.println("Result: " + result);

        System.out.println("\n=== Summary ===");
        System.out.println("Decorator pattern benefits:");
        System.out.println("  - More flexible than static inheritance");
        System.out.println("  - Add responsibilities at runtime");
        System.out.println("  - Combine behaviors using multiple decorators");
        System.out.println("  - Single Responsibility: divide behavior into small classes");
        System.out.println("\nKey points:");
        System.out.println("  - Decorator and component have same interface");
        System.out.println("  - Decorator wraps concrete component or other decorators");
        System.out.println("  - Can stack decorators in any order");
    }
}
