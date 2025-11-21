#!/usr/bin/env python3
"""Script to combine all markdown files in the correct order based on TOC structure"""

import os

# Define the order of files to combine
file_order = [
    # Main introduction
    'index.md',

    # Getting Started (nav_order: 2)
    'getting-started.md',
    'GETTING_STARTED.md',
    'VIBE_CODING.md',
    'TEAM_EXPERIENCES.md',

    # Core Workflows (nav_order: 3)
    'core-workflows.md',
    'WORKFLOWS.md',  # Additional intro content
    'WORKFLOW_SPEC_FIRST_APPROACH.md',
    'WORKFLOW_TDD.md',
    'WORKFLOW_MEMORY_BANK.md',
    'WORKFLOW_VISUAL_FEEDBACK.md',
    'WORKFLOW_EXPLORATORY.md',
    'WORKFLOW_DEBUG.md',
    'WORKFLOW_AUTO_VALIDATIONS.md',

    # Prompt Engineering (nav_order: 4)
    'prompt-engineering.md',
    'PROMPT_ENGINEERING.md',
    'PROMPT_THREE_EXPERTS_METHOD.md',
    'PROMPT_MULTIPLE_ITERATIONS_REASONING.md',
    'PROMPT_ZERO_ONE_N_SHOT_PROMPTS.md',

    # Tools & Setup (nav_order: 5)
    'tools-setup.md',
    'CONTEX.md',  # Managing the Agent Context
    'MODELS_USE_CASES.md',
    'MCPS.md',
    'DEBUGGING_MCP.md',
    'PRIVACY.md',
    'ORG_INSTRUCTIONS.md',
    'PRJ_INSTRUCTIONS.md',

    # Examples & Templates (nav_order: 6)
    'examples.md',

    # Contributing
    'CONTRIBUTING.md',
]

def remove_front_matter(content):
    """Remove Jekyll front matter from content"""
    if content.startswith('---'):
        # Find the end of front matter
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[2].strip()
    return content

def add_section_separator():
    """Add a visual separator between sections"""
    return '\n\n---\n\n'

def combine_files(base_dir, files, output_file):
    """Combine all files in the specified order"""
    combined_content = []

    # Add header
    combined_content.append('# Agentic Coding Handbook - Complete Book\n\n')
    combined_content.append('_This is a combined version of the entire Agentic Coding Handbook, generated automatically from all the individual markdown files._\n\n')
    combined_content.append('---\n\n')

    for filename in files:
        filepath = os.path.join(base_dir, filename)

        if not os.path.exists(filepath):
            print(f"Warning: File not found: {filepath}")
            continue

        print(f"Adding: {filename}")

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove front matter
        content = remove_front_matter(content)

        if content.strip():
            # Add the content
            combined_content.append(content)
            # Add separator
            combined_content.append(add_section_separator())

    # Write combined content
    output_path = os.path.join(base_dir, output_file)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(combined_content))

    print(f"\nSuccessfully created: {output_path}")
    print(f"Total files combined: {len([f for f in files if os.path.exists(os.path.join(base_dir, f))])}")

if __name__ == '__main__':
    base_dir = '/home/user/agentic-coding-handbook'
    output_file = 'COMPLETE_BOOK.md'

    combine_files(base_dir, file_order, output_file)
