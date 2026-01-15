# GitHub Actions Workflows

This directory contains automated workflows for the Materials repository.

## PR to Working Folder Workflow

**File:** `pr-to-working-folder.yml`

### Purpose
Automatically copies files modified in a pull request to the "Working Folder" directory. This mimics the pull request process as a file upload operation, allowing all modified files to be staged in the Working Folder without manual intervention.

### Trigger Events
The workflow runs automatically when:
- A new pull request is opened against `main`, `master`, or `2026_Jan` branch
- An existing pull request is updated (synchronized)
- A closed pull request is reopened

### What It Does
1. **Checks out the PR branch** - Gets the latest code from the pull request
2. **Identifies modified files** - Compares the PR branch with the base branch to find all added, modified, or renamed files
3. **Copies files to Working Folder** - Copies each modified file to the "Working Folder" directory
4. **Commits changes** - Automatically commits the copied files back to the PR branch
5. **Posts a comment** - Adds a comment to the PR indicating how many files were copied

### Requirements
- The workflow requires `write` permissions for `contents` and `pull-requests`
- Uses the default `GITHUB_TOKEN` for authentication (no additional secrets needed)

### Usage
No manual action is required. The workflow runs automatically on PR events. Once a PR is created or updated:
1. The workflow will detect all modified files
2. Copy them to the Working Folder
3. Commit and push the changes back to the PR branch
4. Add a comment to the PR confirming completion

### Example
When a PR modifies `Notes/Chapter_01.ipynb` and `Exercises/Exercise_05.ipynb`, the workflow will:
- Copy both files to `Working Folder/`
- The files will appear as `Working Folder/Chapter_01.ipynb` and `Working Folder/Exercise_05.ipynb`
- Commit with message: "Auto-copy PR #123 files to Working Folder"
- Comment on PR: "✅ Automated workflow completed: 2 file(s) have been copied to the Working Folder."

### Notes
- Only the filename is preserved; the original directory structure is flattened in the Working Folder
- If multiple files have the same name from different directories, the last one will overwrite previous ones
- The workflow only processes files that are added, modified, or renamed (not deleted files)
