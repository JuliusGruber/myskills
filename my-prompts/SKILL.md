# my-prompts

A custom skill for managing and using your own collection of reusable prompts. Store, organize, browse, and execute custom prompts tailored to your specific needs.

## What This Skill Does

The my-prompts skill allows you to:
- **Browse** your collection of custom prompts organized by category
- **Create** new prompts and save them for future use
- **Execute** prompts with the ability to review and edit before running
- **Organize** prompts into categories using subdirectories

## When to Use This Skill

Use this skill when you want to:
- Access frequently used prompt templates
- Maintain a personal library of code generation prompts
- Store specialized prompts for your specific domain or project
- Quickly reuse complex prompts without retyping them

## Directory Structure

```
my-prompts/
├── prompts/                 # All your custom prompts
│   ├── code-generation/     # Category: Code generation prompts
│   ├── analysis/            # Category: Analysis prompts
│   ├── general/             # Category: General prompts
│   └── [custom-category]/   # Add your own categories
└── scripts/
    ├── browse_prompts.py    # Browse and display prompts
    └── create_prompt.py     # Create new prompts
```

## Instructions for Claude

When the user invokes this skill or requests to work with custom prompts, follow these workflows:

### 1. Browsing and Using Prompts

When the user wants to see their prompts:

1. Run the browse script to list all available prompts:
   ```bash
   python my-prompts/scripts/browse_prompts.py
   ```

2. Display the numbered list of prompts to the user, organized by category.

3. When the user selects a prompt by number, retrieve its content:
   ```bash
   python my-prompts/scripts/browse_prompts.py [prompt_number]
   ```

4. Display the prompt content to the user and ask if they want to:
   - Execute it as-is
   - Make modifications before executing
   - Cancel

5. If modifications are requested, present the prompt for editing, then execute the modified version.

6. Execute the prompt by processing it as a normal user request.

### 2. Creating New Prompts

When the user wants to create a new prompt:

**Option A: Interactive Creation (Recommended)**
```bash
python my-prompts/scripts/create_prompt.py
```
This will guide the user through:
- Entering a prompt name
- Selecting or creating a category
- Entering the prompt content

**Option B: Direct Creation (from command line)**
```bash
python my-prompts/scripts/create_prompt.py "Prompt Name" "Prompt content here" "category-name"
```

**Option C: Assist the User**
If the user describes a prompt they want to create:
1. Help them formulate the prompt content
2. Suggest an appropriate category
3. Use the create script to save it

### 3. Example Interactions

**Example 1: Browsing and Using**
```
User: "Show me my custom prompts"
→ Run browse_prompts.py
→ Display categorized list
User: "Use prompt number 3"
→ Run browse_prompts.py 3
→ Display prompt content
→ Ask: "Would you like me to execute this prompt, or would you like to modify it first?"
User: "Execute it"
→ Process the prompt content as a request
```

**Example 2: Creating**
```
User: "I want to save a prompt for generating Python unit tests"
→ Offer to help create the prompt
→ Suggest category: "code-generation" or "testing"
→ Help formulate the prompt content
→ Run create_prompt.py with the details
→ Confirm creation
```

**Example 3: Custom Categories**
```
User: "Create a prompt in a new category called 'documentation'"
→ Guide them through creation
→ Use create_prompt.py to create in new category
→ The script will automatically create the subdirectory
```

## Starter Examples

The skill comes with three example prompts to demonstrate usage:

1. **code-generation/react-component.md** - Template for creating React components
2. **code-generation/api-endpoint.md** - Template for REST API endpoints
3. **general/code-review.md** - Comprehensive code review prompt

## Prompt File Format

Prompts are stored as Markdown (.md) files:
- Filename: kebab-case (e.g., `my-custom-prompt.md`)
- Content: Plain markdown text with your prompt
- Location: In category subdirectories or root prompts folder

## Best Practices

### For Users:
- Organize prompts into logical categories
- Use descriptive filenames
- Include placeholders [like this] for parts that need customization
- Keep prompts focused on a single task or purpose

### For Claude:
- Always show the prompt content before executing
- Allow users to review and edit prompts
- Suggest appropriate categories when creating new prompts
- Help users refine prompt content for better results
- Confirm successful creation or execution

## Tips for Effective Prompts

When helping users create prompts, encourage them to:
1. Be specific about requirements and constraints
2. Include examples or templates where helpful
3. Specify output format preferences
4. List any specific technologies or frameworks
5. Include quality criteria (testing, documentation, etc.)

## Troubleshooting

If scripts don't work:
- Ensure Python 3 is installed
- Check that file paths are correct
- Verify prompts directory exists
- Make sure .md files are properly formatted

If prompts don't appear in listings:
- Confirm files have .md extension
- Check files are in prompts/ directory or subdirectories
- Verify files aren't empty
