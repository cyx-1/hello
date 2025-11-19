/**
 * Comprehensive demonstration of the Command Pattern in Java
 *
 * The Command pattern encapsulates a request as an object, thereby letting you
 * parameterize clients with different requests, queue or log requests, and
 * support undoable operations.
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

// Command interface
interface Command {
    void execute();
    void undo();
    String getDescription();
}

// Receiver - the actual business logic
class Light {
    private String location;
    private boolean isOn = false;
    private int brightness = 100;

    public Light(String location) {
        this.location = location;
    }

    public void on() {
        isOn = true;
        System.out.println("  [Light] " + location + " light is ON");
    }

    public void off() {
        isOn = false;
        System.out.println("  [Light] " + location + " light is OFF");
    }

    public void dim(int level) {
        brightness = level;
        System.out.println("  [Light] " + location + " light dimmed to " + level + "%");
    }

    public int getBrightness() { return brightness; }
    public boolean isOn() { return isOn; }
}

class Stereo {
    private String location;
    private boolean isOn = false;
    private int volume = 5;

    public Stereo(String location) {
        this.location = location;
    }

    public void on() {
        isOn = true;
        System.out.println("  [Stereo] " + location + " stereo is ON");
    }

    public void off() {
        isOn = false;
        System.out.println("  [Stereo] " + location + " stereo is OFF");
    }

    public void setVolume(int volume) {
        this.volume = volume;
        System.out.println("  [Stereo] " + location + " stereo volume set to " + volume);
    }

    public int getVolume() { return volume; }
}

class GarageDoor {
    public void up() { System.out.println("  [GarageDoor] Garage door is open"); }
    public void down() { System.out.println("  [GarageDoor] Garage door is closed"); }
}

// Concrete Commands
class LightOnCommand implements Command {
    private Light light;

    public LightOnCommand(Light light) {
        this.light = light;
    }

    @Override
    public void execute() { light.on(); }

    @Override
    public void undo() { light.off(); }

    @Override
    public String getDescription() { return "Turn light on"; }
}

class LightOffCommand implements Command {
    private Light light;

    public LightOffCommand(Light light) {
        this.light = light;
    }

    @Override
    public void execute() { light.off(); }

    @Override
    public void undo() { light.on(); }

    @Override
    public String getDescription() { return "Turn light off"; }
}

class LightDimCommand implements Command {
    private Light light;
    private int newLevel;
    private int previousLevel;

    public LightDimCommand(Light light, int level) {
        this.light = light;
        this.newLevel = level;
    }

    @Override
    public void execute() {
        previousLevel = light.getBrightness();
        light.dim(newLevel);
    }

    @Override
    public void undo() {
        light.dim(previousLevel);
    }

    @Override
    public String getDescription() { return "Dim light to " + newLevel + "%"; }
}

class StereoOnCommand implements Command {
    private Stereo stereo;

    public StereoOnCommand(Stereo stereo) {
        this.stereo = stereo;
    }

    @Override
    public void execute() {
        stereo.on();
        stereo.setVolume(5);
    }

    @Override
    public void undo() { stereo.off(); }

    @Override
    public String getDescription() { return "Turn stereo on"; }
}

class GarageDoorOpenCommand implements Command {
    private GarageDoor door;

    public GarageDoorOpenCommand(GarageDoor door) {
        this.door = door;
    }

    @Override
    public void execute() { door.up(); }

    @Override
    public void undo() { door.down(); }

    @Override
    public String getDescription() { return "Open garage door"; }
}

// Macro Command - executes multiple commands
class MacroCommand implements Command {
    private Command[] commands;
    private String name;

    public MacroCommand(String name, Command[] commands) {
        this.name = name;
        this.commands = commands;
    }

    @Override
    public void execute() {
        for (Command command : commands) {
            command.execute();
        }
    }

    @Override
    public void undo() {
        for (int i = commands.length - 1; i >= 0; i--) {
            commands[i].undo();
        }
    }

    @Override
    public String getDescription() { return name; }
}

// Invoker with undo support
class RemoteControl {
    private Command[] onCommands;
    private Command[] offCommands;
    private Stack<Command> undoStack;

    public RemoteControl() {
        onCommands = new Command[7];
        offCommands = new Command[7];
        undoStack = new Stack<>();

        Command noCommand = new Command() {
            public void execute() {}
            public void undo() {}
            public String getDescription() { return "No command"; }
        };

        for (int i = 0; i < 7; i++) {
            onCommands[i] = noCommand;
            offCommands[i] = noCommand;
        }
    }

    public void setCommand(int slot, Command onCommand, Command offCommand) {
        onCommands[slot] = onCommand;
        offCommands[slot] = offCommand;
    }

    public void onButtonPressed(int slot) {
        onCommands[slot].execute();
        undoStack.push(onCommands[slot]);
    }

    public void offButtonPressed(int slot) {
        offCommands[slot].execute();
        undoStack.push(offCommands[slot]);
    }

    public void undoButtonPressed() {
        if (!undoStack.isEmpty()) {
            Command command = undoStack.pop();
            System.out.println("  Undoing: " + command.getDescription());
            command.undo();
        } else {
            System.out.println("  Nothing to undo");
        }
    }
}

// Command queue for delayed execution
class CommandQueue {
    private List<Command> queue = new ArrayList<>();

    public void addCommand(Command command) {
        queue.add(command);
        System.out.println("  Queued: " + command.getDescription());
    }

    public void executeAll() {
        System.out.println("\n  Executing queued commands:");
        for (Command command : queue) {
            command.execute();
        }
        queue.clear();
    }
}

// Text editor example with undo
class TextEditor {
    private StringBuilder content = new StringBuilder();
    private Stack<Command> history = new Stack<>();

    public void executeCommand(Command command) {
        command.execute();
        history.push(command);
    }

    public void undo() {
        if (!history.isEmpty()) {
            Command command = history.pop();
            command.undo();
        }
    }

    public void append(String text) {
        content.append(text);
    }

    public void delete(int length) {
        int start = Math.max(0, content.length() - length);
        content.delete(start, content.length());
    }

    public String getContent() {
        return content.toString();
    }
}

class AppendCommand implements Command {
    private TextEditor editor;
    private String text;

    public AppendCommand(TextEditor editor, String text) {
        this.editor = editor;
        this.text = text;
    }

    @Override
    public void execute() {
        editor.append(text);
        System.out.println("  Appended: \"" + text + "\"");
    }

    @Override
    public void undo() {
        editor.delete(text.length());
        System.out.println("  Undid append: \"" + text + "\"");
    }

    @Override
    public String getDescription() { return "Append text"; }
}

public class MainCommand {
    public static void main(String[] args) {
        System.out.println("=== Command Pattern Demonstration ===\n");

        // Remote control example
        System.out.println("--- 1. Smart Home Remote Control ---");

        RemoteControl remote = new RemoteControl();

        Light livingRoomLight = new Light("Living Room");
        Light kitchenLight = new Light("Kitchen");
        Stereo stereo = new Stereo("Living Room");
        GarageDoor garageDoor = new GarageDoor();

        remote.setCommand(0, new LightOnCommand(livingRoomLight), new LightOffCommand(livingRoomLight));
        remote.setCommand(1, new LightOnCommand(kitchenLight), new LightOffCommand(kitchenLight));
        remote.setCommand(2, new StereoOnCommand(stereo), new Command() {
            public void execute() { stereo.off(); }
            public void undo() { stereo.on(); }
            public String getDescription() { return "Turn stereo off"; }
        });
        remote.setCommand(3, new GarageDoorOpenCommand(garageDoor), new Command() {
            public void execute() { garageDoor.down(); }
            public void undo() { garageDoor.up(); }
            public String getDescription() { return "Close garage door"; }
        });

        System.out.println("\nPressing buttons:");
        remote.onButtonPressed(0);   // Living room light on
        remote.onButtonPressed(1);   // Kitchen light on
        remote.onButtonPressed(2);   // Stereo on

        System.out.println("\nUndoing last command:");
        remote.undoButtonPressed();

        System.out.println("\nMore actions:");
        remote.offButtonPressed(0);  // Living room light off
        remote.undoButtonPressed();  // Undo: light back on
        System.out.println();

        // Macro command example
        System.out.println("--- 2. Macro Command (Party Mode) ---");

        Light partyLight1 = new Light("Party Room 1");
        Light partyLight2 = new Light("Party Room 2");
        Stereo partyStereo = new Stereo("Party Room");

        Command[] partyOn = {
            new LightOnCommand(partyLight1),
            new LightOnCommand(partyLight2),
            new LightDimCommand(partyLight1, 30),
            new LightDimCommand(partyLight2, 30),
            new StereoOnCommand(partyStereo)
        };

        MacroCommand partyMacro = new MacroCommand("Party Mode", partyOn);

        System.out.println("\nActivating Party Mode:");
        partyMacro.execute();

        System.out.println("\nDeactivating Party Mode (undo):");
        partyMacro.undo();
        System.out.println();

        // Command queue example
        System.out.println("--- 3. Command Queue (Scheduled Tasks) ---");

        CommandQueue queue = new CommandQueue();
        queue.addCommand(new LightOnCommand(new Light("Bedroom")));
        queue.addCommand(new LightDimCommand(new Light("Bedroom"), 50));
        queue.addCommand(new GarageDoorOpenCommand(new GarageDoor()));

        queue.executeAll();
        System.out.println();

        // Text editor with undo
        System.out.println("--- 4. Text Editor with Undo ---");

        TextEditor editor = new TextEditor();

        editor.executeCommand(new AppendCommand(editor, "Hello "));
        editor.executeCommand(new AppendCommand(editor, "World"));
        editor.executeCommand(new AppendCommand(editor, "!"));

        System.out.println("  Content: \"" + editor.getContent() + "\"");

        System.out.println("\nUndoing last two operations:");
        editor.undo();
        editor.undo();

        System.out.println("  Content: \"" + editor.getContent() + "\"");

        System.out.println("\n=== Summary ===");
        System.out.println("Command pattern benefits:");
        System.out.println("  - Decouples invoker from receiver");
        System.out.println("  - Commands can be queued, logged, or scheduled");
        System.out.println("  - Supports undo/redo operations");
        System.out.println("  - Can compose commands into macros");
    }
}
