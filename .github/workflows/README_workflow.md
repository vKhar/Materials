# Submit PR Workflow Guide

## Overview
This repository includes an automated workflow, defined in `.github/workflows/submit_pr.yml`, that processes pull requests based on their title. The workflow has three different behaviors depending on the PR title.

## PR Processing Rules
The workflow evaluates all pull requests and takes action based on the title:

1. **PRs with "submit" in the title** (case-insensitive):
   - Files are copied to the `Submit` branch under `Submissions/<username>/`
   - The PR is automatically closed after processing
   - Example titles: "Submit: Week 2 exercises", "SUBMIT homework", "My submission"

2. **PRs with "PR" in the title** (case-insensitive):
   - The PR remains open for manual review
   - No automatic processing occurs
   - Example titles: "PR: Fix typo", "Update README - PR", "PR #123"

3. **PRs without "submit" or "PR" in the title**:
   - The PR is automatically closed without processing
   - A comment explains the closure reason
   - Example titles: "append file", "Update file", "Fix bug"

## First-Time Contributors
If you're a first-time contributor from a fork, your PR will require manual approval before the workflow runs. This is a GitHub security feature. Once approved by a repository maintainer, the workflow will execute according to the rules above.

## How to Submit Your Work
1. **Fork the repository** to your own GitHub account.
2. **Create a new branch** in your fork and make the necessary changes or add your submission files.
3. **Open a pull request** with a title containing "submit" (e.g., "Submit: Week 2 exercises", "SUBMIT homework").
4. If you're a first-time contributor, wait for a maintainer to approve the workflow run.
5. Once approved (or immediately for returning contributors), the workflow will automatically process your submission.

## What the Workflow Does
- Checks out the `Submit` branch with write permissions.
- Fetches the PR contents from your fork.
- Copies every changed file into `Submissions/<your_username>/` using its original filename (overwriting any previous copy).
- Commits and pushes the copied files back to the `Submit` branch.
- Closes your pull request with a comment confirming that the submission was archived.

## Verifying Your Submission
After the workflow finishes, you can:
- Browse the `Submit` branch to confirm that your files appear under `Submissions/<your_username>/` with their original filenames.
- Review the automated comment on your pull request for confirmation of completion.

## Troubleshooting
- **My PR wasn't processed**: Check that your PR title contains "submit" (case-insensitive).
- **My PR was auto-closed**: Your PR title didn't contain "submit" or "PR". To submit work, create a new PR with "submit" in the title.
- **Workflow hasn't run yet**: If you're a first-time contributor, the workflow needs manual approval. Wait for a maintainer to approve it.
- **I want my PR reviewed manually**: Include "PR" in the title to keep it open for manual review.

Following the guidelines above ensures your submission or contribution is handled correctly by the workflow.
