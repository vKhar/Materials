# Process PR to Template Branch Workflow

This README explains how the [`process-pr-to-template.yml`](process-pr-to-template.yml) GitHub Actions workflow automatically copies pull-request (PR) changes into the `Submissions/` directory on a temporary branch and then closes the PR.

## Trigger & Permissions
- **Event**: `pull_request_target` on `opened`, `synchronize`, or `reopened`. Using `pull_request_target` lets the workflow write to the repository while still reading files from the PR safely.
- **Permissions**: Grants `contents: write` and `pull-requests: write` so the job can push branches and close PRs.

## Repository Requirements
- **GitHub Actions enabled**: The repository must allow Actions to run on PRs, and the workflow file must live under `.github/workflows/` (already true here).
- **Workflow token write access**: In the repo settings (`Settings → Actions → General → Workflow permissions`) set the default `GITHUB_TOKEN` to “Read and write” so pushes and PR-closing succeed.
- **Branch protections**: Ensure rules on the target branch permit `github-actions[bot]` to push new branches; the workflow does not force-push to protected branches but must be allowed to create `tmp-*` branches.
- **GitHub CLI availability**: GitHub-hosted runners already include `gh`. If you use self-hosted runners, install and authenticate the GitHub CLI so the close-PR step works.
- **Submissions directory**: The workflow creates `Submissions/` if needed. If you prefer storing submissions elsewhere, create that directory (or adjust the paths) ahead of time.

## Step-by-step Behavior
1. **Checkout Base**: Fetches the PR base branch with full history so we can create new branches from it.
2. **Configure Git Identity**: Sets the bot name/email for commits.
3. **Create Temp Branch**: Builds a timestamped branch name (`tmp-ddmmyy_hhmm`) and creates the branch from the base.
4. **Fetch PR Changes**: Detects whether the PR originates from a fork. It fetches the PR head into a local branch `pr-<number>` (adding a remote for forks when needed).
5. **Copy Changed Files**: Diffs `origin/<base>` against `pr-<number>`, then copies each changed file into `Submissions/`. Files are renamed to append the PR author (`example.py` → `example_username.py`). Deleted files or directories are skipped.
6. **Commit & Push**: If any submissions were copied, commits them on the temporary branch and pushes to `origin`.
7. **Close the PR**: Uses the GitHub CLI (`gh`) to close the PR with a comment pointing to the new submissions branch.

## Operational Notes
- The workflow never executes user code; it only copies file contents via `git show` and writes them into the repo.
- `Submissions/` is created if absent and only changed files are copied. If no files remain after filtering (for example, only deletions), the workflow exits without committing.
- GitHub CLI (`gh`) must be available in the runner image (already true on `ubuntu-latest`).
- The temporary branch name is exposed through `${{ steps.branch-name.outputs.branch_name }}` for later steps.

## Customization Ideas
- **Rename destination folder** by changing the `Submissions` paths.
- **Adjust renaming logic** if you need more metadata (e.g., append PR number).
- **Limit monitored paths** by filtering `git diff --name-only` or adding `paths:` filters to the workflow trigger.
- **Skip auto-closing** by removing the final `gh pr close` step if you want to keep PRs open for manual review.

For details, see the in-line comments inside [process-pr-to-template.yml](process-pr-to-template.yml).
