#!/usr/bin/env python3
# /// script
# dependencies = [
#   "questionary>=2.0.0",
# ]
# ///
"""
Questionary CLI Tool Demo

This script demonstrates various interactive prompts available in the questionary library
for building user-friendly command-line interfaces.
"""

import questionary
from questionary import Style


def demo_text_input():
    """Demonstrate simple text input."""
    print("\n=== Text Input Demo ===")  # Line 19
    name = questionary.text(
        "What is your name?",
        default="John Doe"
    ).ask()
    print(f"Hello, {name}!")  # Line 24


def demo_password():
    """Demonstrate password input (hidden characters)."""
    print("\n=== Password Input Demo ===")  # Line 28
    password = questionary.password(
        "Enter your password:"
    ).ask()
    print(f"Password length: {len(password) if password else 0} characters")  # Line 32


def demo_confirm():
    """Demonstrate yes/no confirmation."""
    print("\n=== Confirmation Demo ===")  # Line 36
    confirm = questionary.confirm(
        "Do you want to continue?",
        default=True
    ).ask()
    print(f"User confirmed: {confirm}")  # Line 41


def demo_select():
    """Demonstrate single selection from a list."""
    print("\n=== Select Demo ===")  # Line 45
    choice = questionary.select(
        "What's your favorite programming language?",
        choices=[
            "Python",
            "JavaScript",
            "Go",
            "Rust",
            "Java",
            "TypeScript"
        ]
    ).ask()
    print(f"Selected: {choice}")  # Line 58


def demo_checkbox():
    """Demonstrate multiple selection from a list."""
    print("\n=== Checkbox Demo ===")  # Line 62
    choices = questionary.checkbox(
        "Select your skills (use space to select, enter to confirm):",
        choices=[
            "Python",
            "JavaScript",
            "Docker",
            "Kubernetes",
            "AWS",
            "Git"
        ]
    ).ask()
    print(f"Selected skills: {', '.join(choices) if choices else 'None'}")  # Line 74


def demo_rawselect():
    """Demonstrate selection with shortcuts."""
    print("\n=== Raw Select Demo ===")  # Line 78
    choice = questionary.rawselect(
        "Choose your deployment environment:",
        choices=[
            "Development",
            "Staging",
            "Production"
        ]
    ).ask()
    print(f"Selected environment: {choice}")  # Line 88


def demo_autocomplete():
    """Demonstrate autocomplete functionality."""
    print("\n=== Autocomplete Demo ===")  # Line 92
    frameworks = [
        "Django",
        "Flask",
        "FastAPI",
        "Tornado",
        "Pyramid",
        "Bottle"
    ]
    choice = questionary.autocomplete(
        "Choose a Python web framework (start typing):",
        choices=frameworks
    ).ask()
    print(f"Selected framework: {choice}")  # Line 106


def demo_path():
    """Demonstrate file path selection."""
    print("\n=== Path Demo ===")  # Line 110
    path = questionary.path(
        "Select a file or directory:",
        default="."
    ).ask()
    print(f"Selected path: {path}")  # Line 115


def demo_custom_style():
    """Demonstrate custom styling."""
    print("\n=== Custom Style Demo ===")  # Line 119

    custom_style = Style([
        ('qmark', 'fg:#673ab7 bold'),       # Question mark color
        ('question', 'bold'),                # Question text
        ('answer', 'fg:#f44336 bold'),       # User's answer
        ('pointer', 'fg:#673ab7 bold'),      # Pointer in lists
        ('highlighted', 'fg:#673ab7 bold'),  # Highlighted choice
        ('selected', 'fg:#cc5454'),          # Selected checkbox items
        ('separator', 'fg:#cc5454'),         # Separator line
        ('instruction', ''),                 # Instruction text
        ('text', ''),                        # Plain text
    ])

    choice = questionary.select(
        "Choose your favorite color (with custom styling):",
        choices=["Red", "Green", "Blue", "Purple"],
        style=custom_style
    ).ask()
    print(f"Favorite color: {choice}")  # Line 139


def demo_validation():
    """Demonstrate input validation."""
    print("\n=== Validation Demo ===")  # Line 143

    def validate_age(text):
        """Validate that input is a number between 1 and 120."""
        if not text:
            return "Please enter a value"
        try:
            age = int(text)
            if age < 1 or age > 120:
                return "Age must be between 1 and 120"
            return True
        except ValueError:
            return "Please enter a valid number"

    age = questionary.text(
        "What is your age?",
        validate=validate_age
    ).ask()
    print(f"Age entered: {age}")  # Line 162


def demo_conditional_questions():
    """Demonstrate conditional questions based on previous answers."""
    print("\n=== Conditional Questions Demo ===")  # Line 166

    is_developer = questionary.confirm(
        "Are you a developer?",
        default=True
    ).ask()

    if is_developer:
        experience = questionary.select(
            "How many years of experience?",
            choices=[
                "0-2 years",
                "3-5 years",
                "6-10 years",
                "10+ years"
            ]
        ).ask()
        print(f"Developer with {experience} of experience")  # Line 183
    else:
        print("Not a developer")  # Line 185


def main():
    """Run all demonstrations."""
    print("=" * 60)
    print("QUESTIONARY - Interactive CLI Tool Demonstrations")
    print("=" * 60)
    print("\nNote: Some demos require interactive input.")
    print("For automated demo, default values will be used.\n")

    # Run demonstrations
    demo_text_input()           # Line 196
    demo_password()             # Line 197
    demo_confirm()              # Line 198
    demo_select()               # Line 199
    demo_checkbox()             # Line 200
    demo_rawselect()            # Line 201
    demo_autocomplete()         # Line 202
    demo_path()                 # Line 203
    demo_custom_style()         # Line 204
    demo_validation()           # Line 205
    demo_conditional_questions()  # Line 206

    print("\n" + "=" * 60)
    print("Demo completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
