#!/usr/bin/env python3
"""
Script to create a folder hierarchy for 2z2a_submissions repository
based on the Materials repository structure without copying any files.
"""

import os
import sys
from pathlib import Path


def get_folder_structure(root_path, exclude_dirs=None):
    """
    Get the folder structure from the root path, excluding specified directories.
    
    Args:
        root_path: The root directory to scan
        exclude_dirs: Set of directory names to exclude (e.g., {'.git', '__pycache__'})
    
    Returns:
        List of relative directory paths
    """
    if exclude_dirs is None:
        exclude_dirs = {'.git', '.vscode', '__pycache__', '.ipynb_checkpoints'}
    
    folders = []
    root = Path(root_path).resolve()
    
    for dirpath, dirnames, _ in os.walk(root):
        # Remove excluded directories from dirnames to prevent os.walk from descending into them
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        
        # Get relative path from root
        rel_path = Path(dirpath).relative_to(root)
        
        # Skip the root itself
        if str(rel_path) != '.':
            folders.append(str(rel_path))
    
    return sorted(folders)


def create_folders(target_path, folder_list):
    """
    Create folders in the target path based on the folder list.
    
    Args:
        target_path: The root directory where folders should be created
        folder_list: List of relative folder paths to create
    """
    target = Path(target_path)
    
    # Create target directory if it doesn't exist
    target.mkdir(parents=True, exist_ok=True)
    
    created_count = 0
    for folder in folder_list:
        folder_path = target / folder
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)
            created_count += 1
            print(f"Created: {folder}")
        else:
            print(f"Already exists: {folder}")
    
    return created_count


def generate_bash_script(folder_list, target_repo_name='2z2a_submissions'):
    """
    Generate a bash script that can be used to create the folder structure.
    
    Args:
        folder_list: List of relative folder paths
        target_repo_name: Name of the target repository
    
    Returns:
        String containing the bash script
    """
    script = f"""#!/bin/bash
# Script to create folder structure for {target_repo_name}

# Create the root directory
mkdir -p {target_repo_name}
cd {target_repo_name}

# Create all subdirectories
"""
    
    for folder in folder_list:
        script += f'mkdir -p "{folder}"\n'
    
    script += f'\necho "Folder structure for {target_repo_name} created successfully!"\n'
    
    return script


def main():
    """Main function to create folder structure."""
    print("=" * 60)
    print("Folder Structure Creator for 2z2a_submissions")
    print("=" * 60)
    print()
    
    # Get current directory (Materials repository)
    source_dir = Path(__file__).parent.resolve()
    print(f"Source directory: {source_dir}")
    print()
    
    # Get folder structure
    print("Scanning folder structure...")
    folders = get_folder_structure(source_dir)
    print(f"Found {len(folders)} folders (excluding .git, .vscode, __pycache__, .ipynb_checkpoints)")
    print()
    
    # Print the folder structure
    print("Folder structure:")
    print("-" * 60)
    for folder in folders:
        print(f"  {folder}")
    print("-" * 60)
    print()
    
    # Ask user what to do
    if len(sys.argv) > 1 and sys.argv[1] == '--create':
        # Create the folder structure
        target_name = '2z2a_submissions'
        if len(sys.argv) > 2:
            target_name = sys.argv[2]
        
        target_path = source_dir.parent / target_name
        print(f"Creating folder structure at: {target_path}")
        print()
        
        created = create_folders(target_path, folders)
        print()
        print(f"✓ Successfully created {created} folders in {target_path}")
        
    elif len(sys.argv) > 1 and sys.argv[1] == '--script':
        # Generate bash script
        target_name = '2z2a_submissions'
        if len(sys.argv) > 2:
            target_name = sys.argv[2]
        
        script = generate_bash_script(folders, target_name)
        script_file = source_dir / f'create_{target_name}_structure.sh'
        
        with open(script_file, 'w') as f:
            f.write(script)
        
        # Make it executable
        os.chmod(script_file, 0o755)
        
        print(f"✓ Bash script created: {script_file}")
        print()
        print("To use the script, run:")
        print(f"  bash {script_file}")
        
    else:
        # Show usage
        print("Usage:")
        print(f"  python3 {Path(__file__).name} --create [target_name]")
        print(f"    Create the folder structure in a new directory")
        print()
        print(f"  python3 {Path(__file__).name} --script [target_name]")
        print(f"    Generate a bash script to create the folder structure")
        print()
        print("Examples:")
        print(f"  python3 {Path(__file__).name} --create")
        print(f"  python3 {Path(__file__).name} --create 2z2a_submissions")
        print(f"  python3 {Path(__file__).name} --script")
        print()


if __name__ == '__main__':
    main()
