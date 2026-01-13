# Materials for NJCCZ Students

Welcome to **Materials for NJCCZ Students**! This repository is designed to store teaching and learning materials for H2 Computing and a little more. 

---

## Table of Contents

- [List of Software Used](#list-of-software-used)
- [Using Github Codespaces](#using-github-codespaces)
- [Folder Structure Export Tool](#folder-structure-export-tool)

---

## List of Software Used
The minimum software required are:
- Python IDLE 3.7.7
- Flask & other modules 2.2.5
- PyMongo 4.6.1
- Jupyter Notebook 6.5.6
- DB Browser for SQLite 3.10.1
- Notepad++ 7.5.4
- MongoDB Community Server 3.4.9

## Using Github Codespaces 
A Github codespace is a development environment that's hosted in the cloud. It has an Visual Studio Code IDE like interface that makes programming easier and more efficient. 

To learn on how to use them please visit [NJCCZ Repository](https://github.com/beertino/NJCCZ)

## Folder Structure Export Tool

This repository includes tools to export its folder hierarchy to create new repositories (like `2z2a_submissions`) without copying any files.

### Quick Start

```bash
# Create folder structure using the bash script
bash create_2z2a_submissions_structure.sh

# Or use Python for more flexibility
python3 create_folder_structure.py --create 2z2a_submissions
```

### Documentation

- **[GITHUB_REPO_SETUP.md](GITHUB_REPO_SETUP.md)** - Complete guide to create a GitHub repository with this structure
- **[QUICKSTART.md](QUICKSTART.md)** - Quick reference for common use cases
- **[FOLDER_STRUCTURE_TOOL.md](FOLDER_STRUCTURE_TOOL.md)** - Detailed tool documentation

The exported structure includes all folders but excludes files, `.git`, `.vscode`, `__pycache__`, and `.ipynb_checkpoints` directories.