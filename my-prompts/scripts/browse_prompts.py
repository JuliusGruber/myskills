#!/usr/bin/env python3
"""
Browse and display available custom prompts.

This script scans the prompts directory and lists all available prompts
organized by category (subdirectory).
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple


def get_prompts_directory() -> Path:
    """Get the path to the prompts directory."""
    script_dir = Path(__file__).parent
    prompts_dir = script_dir.parent / "prompts"
    return prompts_dir


def scan_prompts(prompts_dir: Path) -> Dict[str, List[Tuple[str, Path]]]:
    """
    Scan the prompts directory and return organized prompt data.

    Returns:
        Dictionary mapping category names to lists of (prompt_name, file_path) tuples
    """
    prompts_by_category = {}

    if not prompts_dir.exists():
        return prompts_by_category

    # Walk through all subdirectories
    for root, dirs, files in os.walk(prompts_dir):
        root_path = Path(root)

        # Get category name (relative path from prompts directory)
        if root_path == prompts_dir:
            category = "root"
        else:
            category = root_path.relative_to(prompts_dir).as_posix()

        # Find all .md files
        md_files = [f for f in files if f.endswith('.md')]

        if md_files:
            prompts_list = []
            for md_file in sorted(md_files):
                file_path = root_path / md_file
                # Use filename without extension as prompt name
                prompt_name = md_file[:-3]  # Remove .md extension
                prompts_list.append((prompt_name, file_path))

            if prompts_list:
                prompts_by_category[category] = prompts_list

    return prompts_by_category


def display_prompts(prompts_by_category: Dict[str, List[Tuple[str, Path]]]) -> Dict[int, Path]:
    """
    Display prompts in a numbered list organized by category.

    Returns:
        Dictionary mapping prompt numbers to file paths
    """
    if not prompts_by_category:
        print("No prompts found. Create your first prompt to get started!")
        return {}

    prompt_index = {}
    counter = 1

    print("\n=== Available Custom Prompts ===\n")

    # Sort categories alphabetically
    for category in sorted(prompts_by_category.keys()):
        prompts = prompts_by_category[category]

        # Display category header
        if category == "root":
            print("📁 Root")
        else:
            print(f"📁 {category}")

        # Display prompts in this category
        for prompt_name, file_path in prompts:
            print(f"  {counter}. {prompt_name}")
            prompt_index[counter] = file_path
            counter += 1

        print()  # Empty line between categories

    return prompt_index


def read_prompt_content(file_path: Path) -> str:
    """Read and return the content of a prompt file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading prompt: {e}"


def main():
    """Main function to browse and optionally display prompt content."""
    prompts_dir = get_prompts_directory()
    prompts_by_category = scan_prompts(prompts_dir)
    prompt_index = display_prompts(prompts_by_category)

    # If a prompt number is provided as argument, display its content
    if len(sys.argv) > 1:
        try:
            prompt_num = int(sys.argv[1])
            if prompt_num in prompt_index:
                file_path = prompt_index[prompt_num]
                print(f"\n=== Prompt Content: {file_path.stem} ===\n")
                content = read_prompt_content(file_path)
                print(content)
                print(f"\n=== End of Prompt ===\n")
            else:
                print(f"Error: Prompt number {prompt_num} not found.")
                sys.exit(1)
        except ValueError:
            print(f"Error: Invalid prompt number '{sys.argv[1]}'")
            sys.exit(1)

    return 0


if __name__ == "__main__":
    sys.exit(main())
