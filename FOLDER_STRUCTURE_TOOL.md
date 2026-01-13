# Folder Structure Tool

This document explains how to use the folder structure creation tool to create a new repository (like `2z2a_submissions`) based on the folder hierarchy of the Materials repository without copying any files.

## Overview

The `create_folder_structure.py` script scans the Materials repository and can either:
1. Create a new folder structure directly
2. Generate a bash script that can be run to create the folder structure

The script automatically excludes:
- `.git` directory
- `.vscode` directory  
- `__pycache__` directories
- `.ipynb_checkpoints` directories

## Current Folder Structure

The Materials repository contains 25 folders:
- 365-Days-of-H2-Computing (with img and resources subdirectories)
- Exercises (with Exercise 12, img, resources, and web_stuff subdirectories)
- Notes (with Chapter_7_Example, archived, images, resources, sucky_web_server, and web_stuff subdirectories)
- Working Folder

## Usage

### Method 1: Using the Python Script Directly

To create the folder structure directly using Python:

```bash
# Create with default name (2z2a_submissions) in parent directory
python3 create_folder_structure.py --create

# Create with custom name
python3 create_folder_structure.py --create my_custom_name
```

This will create the folder structure in the parent directory of Materials (e.g., `/home/runner/work/Materials/2z2a_submissions`).

### Method 2: Generate and Use a Bash Script

To generate a bash script that can be run anywhere:

```bash
# Generate script with default name (2z2a_submissions)
python3 create_folder_structure.py --script

# Generate script with custom name
python3 create_folder_structure.py --script my_custom_name
```

This creates a bash script (e.g., `create_2z2a_submissions_structure.sh`) that you can run:

```bash
# Run the generated script
bash create_2z2a_submissions_structure.sh
```

The bash script can be copied to any location and run to create the folder structure.

### Method 3: View Folder Structure Only

To just see what folders would be created:

```bash
python3 create_folder_structure.py
```

## Creating the 2z2a_submissions Repository

To create the `2z2a_submissions` repository with the Materials folder structure:

### Option A: Local Creation

1. Navigate to where you want to create the new repository:
   ```bash
   cd /path/where/you/want/the/repo
   ```

2. Run the generated bash script:
   ```bash
   bash /path/to/Materials/create_2z2a_submissions_structure.sh
   ```

3. Initialize as a git repository:
   ```bash
   cd 2z2a_submissions
   git init
   git add .
   git commit -m "Initial folder structure"
   ```

### Option B: Python Direct Creation

1. Run the Python script from the Materials directory:
   ```bash
   cd /path/to/Materials
   python3 create_folder_structure.py --create
   ```

2. The folder will be created at `/path/to/2z2a_submissions`

3. Initialize as a git repository:
   ```bash
   cd ../2z2a_submissions
   git init
   git add .
   git commit -m "Initial folder structure"
   ```

## Verifying the Result

To verify that no files were copied (only folders):

```bash
cd 2z2a_submissions
find . -type f | wc -l  # Should output: 0
find . -type d | wc -l  # Should output: 26 (25 folders + root)
```

## Examples

```bash
# Example 1: View the structure
python3 create_folder_structure.py

# Example 2: Create in default location
python3 create_folder_structure.py --create

# Example 3: Generate bash script
python3 create_folder_structure.py --script

# Example 4: Run generated script in /tmp
cd /tmp
bash /path/to/Materials/create_2z2a_submissions_structure.sh

# Example 5: Create with custom name
python3 create_folder_structure.py --create student_submissions
```

## Notes

- The script only creates folder structures - no files are copied
- Hidden folders (starting with `.`) like `.git` and `.vscode` are excluded
- Python cache folders (`__pycache__`) and Jupyter checkpoint folders (`.ipynb_checkpoints`) are excluded
- The generated bash script is portable and can be run on any Unix-like system
- Folders are created with `mkdir -p`, so parent directories are created automatically
