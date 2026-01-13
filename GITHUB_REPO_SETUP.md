# How to Create the 2z2a_submissions GitHub Repository

This guide walks you through creating a new GitHub repository named `2z2a_submissions` with the Materials folder structure.

## Prerequisites

- Git installed on your local machine
- GitHub account with permissions to create repositories
- The Materials repository cloned locally

## Step 1: Create the Folder Structure Locally

### Option A: Using the Bash Script (Fastest)

```bash
# Navigate to where you want to create the repository
cd ~/projects  # or your preferred location

# Run the bash script from Materials repo
bash /path/to/Materials/create_2z2a_submissions_structure.sh

# This creates: ~/projects/2z2a_submissions/
```

### Option B: Using the Python Script

```bash
# From the Materials directory
cd /path/to/Materials
python3 create_folder_structure.py --create

# This creates: /path/to/2z2a_submissions/ (in parent directory)
```

## Step 2: Initialize as Git Repository

```bash
cd 2z2a_submissions
git init
```

## Step 3: Create Initial Commit

```bash
# Optional: Create a README
cat > README.md << 'EOF'
# 2z2a_submissions

This repository contains the folder structure from the Materials repository.

## Folder Structure

- **365-Days-of-H2-Computing/** - Daily computing challenges
- **Exercises/** - Exercise materials
- **Notes/** - Course notes and examples
- **Working Folder/** - Working directory
EOF

# Add and commit
git add .
git commit -m "Initial commit: Add folder structure"
```

## Step 4: Create GitHub Repository

### Option A: Using GitHub Web Interface

1. Go to https://github.com/new
2. Repository name: `2z2a_submissions`
3. Description: "Folder structure from Materials repository for submissions"
4. Choose Public or Private
5. **DO NOT** initialize with README (we already have content)
6. Click "Create repository"

### Option B: Using GitHub CLI

```bash
# Create repository using gh CLI
gh repo create 2z2a_submissions --public --source=. --remote=origin

# Or for private:
gh repo create 2z2a_submissions --private --source=. --remote=origin
```

## Step 5: Push to GitHub

### If you used the web interface:

```bash
# GitHub will show you these commands after creating the repo:
git remote add origin https://github.com/YOUR_USERNAME/2z2a_submissions.git
git branch -M main
git push -u origin main
```

### If you used GitHub CLI:

```bash
# Already connected, just push
git branch -M main
git push -u origin main
```

## Step 6: Verify

Visit your repository at: `https://github.com/YOUR_USERNAME/2z2a_submissions`

You should see:
- 25 folders matching the Materials structure
- Only the README.md file (no other files from Materials)

## Complete Example

Here's a complete example workflow:

```bash
# 1. Navigate to your projects folder
cd ~/projects

# 2. Create the structure using the bash script
bash ~/Materials/create_2z2a_submissions_structure.sh

# 3. Navigate into it
cd 2z2a_submissions

# 4. Initialize git
git init

# 5. Create README
echo "# 2z2a_submissions" > README.md
echo "Folder structure from Materials repository" >> README.md

# 6. Commit
git add .
git commit -m "Initial commit: Add folder structure"

# 7. Create GitHub repo (using gh CLI)
gh repo create 2z2a_submissions --public --source=. --remote=origin

# 8. Push
git branch -M main
git push -u origin main
```

## Troubleshooting

### "Repository already exists"
If the repository already exists on GitHub, use:
```bash
git remote add origin https://github.com/YOUR_USERNAME/2z2a_submissions.git
git branch -M main
git push -u origin main
```

### "Permission denied"
Make sure you're authenticated:
```bash
# Using HTTPS
gh auth login

# Or use SSH
# Ensure your SSH key is added to GitHub
```

### "Directory already exists"
If the folder already exists locally:
```bash
rm -rf 2z2a_submissions  # Remove it first
# Then run the creation script again
```

## Notes

- The folder structure contains **only directories**, no files from Materials
- Excluded directories: `.git`, `.vscode`, `__pycache__`, `.ipynb_checkpoints`
- Total: 25 subdirectories
- You can run the script multiple times in different locations
- Each instance is independent and can be pushed to different GitHub repositories

## What's Next?

After creating the repository, you can:
1. Start adding files to the appropriate folders
2. Set up branch protection rules
3. Add collaborators
4. Configure GitHub Actions if needed
5. Add additional documentation specific to 2z2a_submissions

## Support

For more details on the folder structure tool, see:
- `FOLDER_STRUCTURE_TOOL.md` - Complete documentation
- `QUICKSTART.md` - Quick reference guide
