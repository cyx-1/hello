/**
 * Comprehensive demonstration of the Composite Pattern in Java
 *
 * The Composite pattern composes objects into tree structures to represent
 * part-whole hierarchies. It lets clients treat individual objects and
 * compositions of objects uniformly.
 */

import java.util.ArrayList;
import java.util.List;

// Component interface
interface FileSystemComponent {
    String getName();
    int getSize();
    void display(String indent);
    void add(FileSystemComponent component);
    void remove(FileSystemComponent component);
    FileSystemComponent getChild(int index);
}

// Leaf
class File implements FileSystemComponent {
    private String name;
    private int size;

    public File(String name, int size) {
        this.name = name;
        this.size = size;
    }

    @Override
    public String getName() { return name; }

    @Override
    public int getSize() { return size; }

    @Override
    public void display(String indent) {
        System.out.println(indent + "📄 " + name + " (" + size + " KB)");
    }

    @Override
    public void add(FileSystemComponent component) {
        throw new UnsupportedOperationException("Cannot add to a file");
    }

    @Override
    public void remove(FileSystemComponent component) {
        throw new UnsupportedOperationException("Cannot remove from a file");
    }

    @Override
    public FileSystemComponent getChild(int index) {
        throw new UnsupportedOperationException("File has no children");
    }
}

// Composite
class Directory implements FileSystemComponent {
    private String name;
    private List<FileSystemComponent> children = new ArrayList<>();

    public Directory(String name) {
        this.name = name;
    }

    @Override
    public String getName() { return name; }

    @Override
    public int getSize() {
        int totalSize = 0;
        for (FileSystemComponent child : children) {
            totalSize += child.getSize();
        }
        return totalSize;
    }

    @Override
    public void display(String indent) {
        System.out.println(indent + "📁 " + name + " (" + getSize() + " KB)");
        for (FileSystemComponent child : children) {
            child.display(indent + "  ");
        }
    }

    @Override
    public void add(FileSystemComponent component) {
        children.add(component);
    }

    @Override
    public void remove(FileSystemComponent component) {
        children.remove(component);
    }

    @Override
    public FileSystemComponent getChild(int index) {
        return children.get(index);
    }
}

// Another example: Organization hierarchy

interface OrganizationComponent {
    String getName();
    double getSalary();
    void display(String indent);
}

// Leaf
class Employee implements OrganizationComponent {
    private String name;
    private String position;
    private double salary;

    public Employee(String name, String position, double salary) {
        this.name = name;
        this.position = position;
        this.salary = salary;
    }

    @Override
    public String getName() { return name; }

    @Override
    public double getSalary() { return salary; }

    @Override
    public void display(String indent) {
        System.out.println(indent + "👤 " + name + " (" + position + ") - $" + String.format("%.0f", salary));
    }
}

// Composite
class Department implements OrganizationComponent {
    private String name;
    private List<OrganizationComponent> members = new ArrayList<>();

    public Department(String name) {
        this.name = name;
    }

    public void add(OrganizationComponent component) {
        members.add(component);
    }

    public void remove(OrganizationComponent component) {
        members.remove(component);
    }

    @Override
    public String getName() { return name; }

    @Override
    public double getSalary() {
        double totalSalary = 0;
        for (OrganizationComponent member : members) {
            totalSalary += member.getSalary();
        }
        return totalSalary;
    }

    @Override
    public void display(String indent) {
        System.out.println(indent + "🏢 " + name + " - Total: $" + String.format("%.0f", getSalary()));
        for (OrganizationComponent member : members) {
            member.display(indent + "  ");
        }
    }
}

// Third example: Menu system

interface MenuComponent {
    String getName();
    String getDescription();
    double getPrice();
    void display(String indent);
    boolean isVegetarian();
}

// Leaf
class MenuItem implements MenuComponent {
    private String name;
    private String description;
    private double price;
    private boolean vegetarian;

    public MenuItem(String name, String description, double price, boolean vegetarian) {
        this.name = name;
        this.description = description;
        this.price = price;
        this.vegetarian = vegetarian;
    }

    @Override
    public String getName() { return name; }

    @Override
    public String getDescription() { return description; }

    @Override
    public double getPrice() { return price; }

    @Override
    public boolean isVegetarian() { return vegetarian; }

    @Override
    public void display(String indent) {
        System.out.print(indent + "🍽️ " + name);
        if (vegetarian) System.out.print(" (v)");
        System.out.println(" - $" + String.format("%.2f", price));
        System.out.println(indent + "   " + description);
    }
}

// Composite
class Menu implements MenuComponent {
    private String name;
    private String description;
    private List<MenuComponent> items = new ArrayList<>();

    public Menu(String name, String description) {
        this.name = name;
        this.description = description;
    }

    public void add(MenuComponent component) {
        items.add(component);
    }

    public void remove(MenuComponent component) {
        items.remove(component);
    }

    @Override
    public String getName() { return name; }

    @Override
    public String getDescription() { return description; }

    @Override
    public double getPrice() {
        double total = 0;
        for (MenuComponent item : items) {
            total += item.getPrice();
        }
        return total;
    }

    @Override
    public boolean isVegetarian() {
        for (MenuComponent item : items) {
            if (!item.isVegetarian()) return false;
        }
        return true;
    }

    @Override
    public void display(String indent) {
        System.out.println(indent + "📋 " + name + " - " + description);
        for (MenuComponent item : items) {
            item.display(indent + "  ");
        }
    }
}

public class MainComposite {
    public static void main(String[] args) {
        System.out.println("=== Composite Pattern Demonstration ===\n");

        // File System example
        System.out.println("--- 1. File System Structure ---");

        Directory root = new Directory("root");

        Directory documents = new Directory("Documents");
        documents.add(new File("resume.pdf", 150));
        documents.add(new File("cover_letter.docx", 50));

        Directory photos = new Directory("Photos");
        Directory vacation = new Directory("Vacation");
        vacation.add(new File("beach.jpg", 2500));
        vacation.add(new File("mountain.jpg", 3200));
        photos.add(vacation);
        photos.add(new File("profile.png", 800));

        Directory code = new Directory("Code");
        code.add(new File("main.java", 25));
        code.add(new File("utils.java", 15));

        root.add(documents);
        root.add(photos);
        root.add(code);
        root.add(new File("readme.txt", 5));

        root.display("");
        System.out.println("\nTotal size: " + root.getSize() + " KB\n");

        // Organization hierarchy
        System.out.println("--- 2. Organization Hierarchy ---");

        Department company = new Department("TechCorp");

        Department engineering = new Department("Engineering");
        engineering.add(new Employee("Alice", "CTO", 250000));
        engineering.add(new Employee("Bob", "Senior Developer", 120000));
        engineering.add(new Employee("Charlie", "Developer", 90000));

        Department backend = new Department("Backend Team");
        backend.add(new Employee("Dave", "Lead", 110000));
        backend.add(new Employee("Eve", "Developer", 85000));
        engineering.add(backend);

        Department sales = new Department("Sales");
        sales.add(new Employee("Frank", "Sales Director", 150000));
        sales.add(new Employee("Grace", "Account Manager", 80000));

        company.add(engineering);
        company.add(sales);

        company.display("");
        System.out.println();

        // Menu system
        System.out.println("--- 3. Restaurant Menu System ---");

        Menu allMenus = new Menu("All Menus", "Complete restaurant offerings");

        Menu breakfast = new Menu("Breakfast", "Served until 11am");
        breakfast.add(new MenuItem("Pancakes", "Fluffy buttermilk pancakes with maple syrup", 8.99, true));
        breakfast.add(new MenuItem("Eggs Benedict", "Poached eggs on English muffin with hollandaise", 12.99, true));
        breakfast.add(new MenuItem("Bacon & Eggs", "Two eggs any style with crispy bacon", 10.99, false));

        Menu lunch = new Menu("Lunch", "Served 11am - 5pm");
        lunch.add(new MenuItem("Caesar Salad", "Romaine lettuce with Caesar dressing", 9.99, true));
        lunch.add(new MenuItem("Club Sandwich", "Turkey, bacon, lettuce, tomato on toast", 11.99, false));

        Menu vegetarianMenu = new Menu("Vegetarian Options", "Plant-based selections");
        vegetarianMenu.add(new MenuItem("Veggie Burger", "Black bean patty with avocado", 13.99, true));
        vegetarianMenu.add(new MenuItem("Garden Salad", "Mixed greens with vinaigrette", 8.99, true));
        lunch.add(vegetarianMenu);

        allMenus.add(breakfast);
        allMenus.add(lunch);

        allMenus.display("");

        System.out.println("\n=== Summary ===");
        System.out.println("Composite pattern benefits:");
        System.out.println("  - Defines class hierarchies with primitive and composite objects");
        System.out.println("  - Clients treat composite and individual objects uniformly");
        System.out.println("  - Makes it easy to add new kinds of components");
        System.out.println("  - Simplifies client code - no conditional statements for type checking");
        System.out.println("\nUse cases:");
        System.out.println("  - File systems (files and directories)");
        System.out.println("  - GUI components (buttons, panels, containers)");
        System.out.println("  - Organization charts");
        System.out.println("  - Menu systems");
    }
}
