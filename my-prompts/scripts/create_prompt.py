#!/usr/bin/env python3
"""
Create a new custom prompt file.

This script helps create new prompt files in the appropriate category directory.
"""

import os
import sys
import re
from pathlib import Path
from typing import Optional


def get_prompts_directory() -> Path:
    """Get the path to the prompts directory."""
    script_dir = Path(__file__).parent
    prompts_dir = script_dir.parent / "prompts"
    return prompts_dir


def sanitize_filename(name: str) -> str:
    """
    Convert a prompt name to a valid filename in kebab-case.

    Args:
        name: The prompt name

    Returns:
        Sanitized filename (without .md extension)
    """
    # Convert to lowercase
    name = name.lower()
    # Replace spaces and underscores with hyphens
    name = re.sub(r'[\s_]+', '-', name)
    # Remove any characters that aren't alphanumeric or hyphens
    name = re.sub(r'[^a-z0-9-]', '', name)
    # Remove multiple consecutive hyphens
    name = re.sub(r'-+', '-', name)
    # Remove leading/trailing hyphens
    name = name.strip('-')

    return name


def list_categories(prompts_dir: Path) -> list:
    """List all existing categories (subdirectories) in the prompts directory."""
    if not prompts_dir.exists():
        return []

    categories = []
    for item in prompts_dir.iterdir():
        if item.is_dir() and not item.name.startswith('.'):
            categories.append(item.name)

    return sorted(categories)


def get_user_input(prompt: str, required: bool = True) -> Optional[str]:
    """
    Get user input with optional requirement validation.

    Args:
        prompt: The prompt to display to the user
        required: Whether the input is required

    Returns:
        User input string or None if not required and empty
    """
    while True:
        value = input(prompt).strip()
        if value:
            return value
        elif not required:
            return None
        else:
            print("This field is required. Please enter a value.")


def create_prompt_interactive():
    """Interactive prompt creation flow."""
    prompts_dir = get_prompts_directory()

    print("\n=== Create New Custom Prompt ===\n")

    # Get prompt name
    print("Enter a name for your prompt (e.g., 'React Component Generator'):")
    prompt_name = get_user_input("> ")
    filename = sanitize_filename(prompt_name)

    if not filename:
        print("Error: Could not create valid filename from prompt name.")
        return 1

    print(f"Filename will be: {filename}.md")

    # List existing categories
    categories = list_categories(prompts_dir)

    if categories:
        print("\nExisting categories:")
        for i, cat in enumerate(categories, 1):
            print(f"  {i}. {cat}")
        print("  0. Create new category")
        print("  [Enter]. Save in root directory")

        category_input = input("\nSelect category (number or press Enter for root): ").strip()

        if category_input == "":
            category = None
        elif category_input == "0":
            new_cat = get_user_input("Enter new category name: ")
            category = sanitize_filename(new_cat)
        else:
            try:
                cat_index = int(category_input) - 1
                if 0 <= cat_index < len(categories):
                    category = categories[cat_index]
                else:
                    print("Invalid category number. Using root directory.")
                    category = None
            except ValueError:
                print("Invalid input. Using root directory.")
                category = None
    else:
        print("\nNo existing categories found.")
        create_cat = input("Create a category? (y/n): ").strip().lower()
        if create_cat == 'y':
            new_cat = get_user_input("Enter category name: ")
            category = sanitize_filename(new_cat)
        else:
            category = None

    # Determine file path
    if category:
        category_dir = prompts_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)
        file_path = category_dir / f"{filename}.md"
    else:
        prompts_dir.mkdir(parents=True, exist_ok=True)
        file_path = prompts_dir / f"{filename}.md"

    # Check if file already exists
    if file_path.exists():
        overwrite = input(f"\nFile {file_path} already exists. Overwrite? (y/n): ").strip().lower()
        if overwrite != 'y':
            print("Cancelled.")
            return 0

    # Get prompt content
    print("\nEnter your prompt content (press Ctrl+D or Ctrl+Z when done):")
    print("=" * 50)

    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass

    content = '\n'.join(lines)

    if not content.strip():
        print("\nError: Prompt content cannot be empty.")
        return 1

    # Write the file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✓ Prompt created successfully: {file_path}")
        return 0
    except Exception as e:
        print(f"\nError creating prompt file: {e}")
        return 1


def create_prompt_from_args(name: str, content: str, category: Optional[str] = None):
    """
    Create a prompt from command-line arguments.

    Args:
        name: Prompt name
        content: Prompt content
        category: Optional category name
    """
    prompts_dir = get_prompts_directory()
    filename = sanitize_filename(name)

    if not filename:
        print("Error: Could not create valid filename from prompt name.")
        return 1

    # Determine file path
    if category:
        category_clean = sanitize_filename(category)
        category_dir = prompts_dir / category_clean
        category_dir.mkdir(parents=True, exist_ok=True)
        file_path = category_dir / f"{filename}.md"
    else:
        prompts_dir.mkdir(parents=True, exist_ok=True)
        file_path = prompts_dir / f"{filename}.md"

    # Write the file
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Prompt created: {file_path}")
        return 0
    except Exception as e:
        print(f"Error creating prompt: {e}")
        return 1


def main():
    """Main function."""
    if len(sys.argv) == 1:
        # Interactive mode
        return create_prompt_interactive()
    elif len(sys.argv) >= 3:
        # Command-line mode: create_prompt.py <name> <content> [category]
        name = sys.argv[1]
        content = sys.argv[2]
        category = sys.argv[3] if len(sys.argv) > 3 else None
        return create_prompt_from_args(name, content, category)
    else:
        print("Usage:")
        print("  Interactive mode: python create_prompt.py")
        print("  Command-line mode: python create_prompt.py <name> <content> [category]")
        return 1


if __name__ == "__main__":
    sys.exit(main())
