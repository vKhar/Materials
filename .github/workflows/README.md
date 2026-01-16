# Process PR to Template Branch Workflow

This README explains how the [`process-pr-to-template.yml`](process-pr-to-template.yml) GitHub Actions workflow automatically processes pull requests (PRs) by copying changed files into user-specific subdirectories within the `Submissions/` folder on the Submit branch.

## Trigger & Permissions
- **Event**: `pull_request_target` on `opened`, `synchronize`, or `reopened`. Using `pull_request_target` lets the workflow write to the repository while still reading files from the PR safely.
- **Permissions**: Grants `contents: write` and `pull-requests: write` so the job can push to the Submit branch and close PRs.

## Repository Requirements
- **GitHub Actions enabled**: The repository must allow Actions to run on PRs, and the workflow file must live under `.github/workflows/` (already true here).
- **Workflow token write access**: In the repo settings (`Settings → Actions → General → Workflow permissions`) set the default `GITHUB_TOKEN` to "Read and write" so pushes and PR-closing work.
- **Branch protections**: Ensure rules on the Submit branch permit `github-actions[bot]` to push commits; the workflow commits directly to Submit.
- **GitHub CLI availability**: GitHub-hosted runners already include `gh`. If you use self-hosted runners, install and authenticate the GitHub CLI so the close-PR step works.
- **Submissions directory**: The workflow creates `Submissions/<username>/` if needed. The directory structure is created automatically.

## Step-by-step Behavior
1. **Checkout Submit Branch**: Fetches the Submit branch with full history.
2. **Configure Git Identity**: Sets the bot name/email for commits.
3. **Fetch PR Changes**: Detects whether the PR originates from a fork. It fetches the PR head into a local branch `pr-<number>` (adding a remote for forks when needed).
4. **Copy Changed Files**: 
   - Diffs the base branch against `pr-<number>` to find changed files
   - Creates a subfolder `Submissions/<pr-author>/` if it doesn't exist
   - Copies each changed file to this subfolder
   - Renames files by appending a date suffix in format `-YYMMDD` (e.g., `example.py` → `example-260116.py`)
   - If a file with the same name already exists after renaming, it will be overwritten
5. **Commit to Submit Branch**: If any submissions were copied, commits them directly to the Submit branch with a descriptive message including the PR number and author.
6. **Close the PR**: Uses the GitHub CLI (`gh`) to close the PR with a comment pointing to the submissions location.

## Key Features
- **No temporary branches**: Files are committed directly to the Submit branch
- **User-specific folders**: Each PR author gets their own subfolder under `Submissions/`
- **Date-based naming**: Files include the submission date in their filename
- **Automatic overwrites**: Duplicate filenames (after date suffix) are overwritten
- **Automatic PR closure**: PRs are closed automatically after processing

## Operational Notes
- The workflow never executes user code; it only copies file contents via `git show` and writes them into the repo.
- `Submissions/<username>/` is created if absent and only changed files are copied. If no files remain after filtering (for example, only deletions), the workflow exits without committing.
- GitHub CLI (`gh`) must be available in the runner image (already true on `ubuntu-latest`).
- The date suffix uses UTC time in YYMMDD format.

## File Organization Example
After processing, your Submissions folder will look like:
```
Submissions/
├── alice/
│   ├── homework1-260116.py
│   └── report-260116.pdf
├── bob/
│   ├── assignment-260115.txt
│   └── code-260116.py
└── charlie/
    └── project-260116.html
```

## Customization Ideas
- **Change date format**: Modify the `DATE_SUFFIX=$(date -u +"%y%m%d")` line to use a different format
- **Rename destination folder**: Change the `Submissions` paths to a different folder name
- **Adjust renaming logic**: Modify the filename construction to add PR number or other metadata
- **Limit monitored paths**: Add `paths:` filters to the workflow trigger to only watch specific directories
- **Skip auto-closing**: Remove the final `gh pr close` step if you want to keep PRs open for manual review

For details, see the in-line comments inside [process-pr-to-template.yml](process-pr-to-template.yml).