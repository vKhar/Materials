# Submit PR Workflow Guide

## Overview
This repository includes an automated workflow, defined in `.github/workflows/submit_pr.yml`, that processes student submissions by copying files into the `Submit` branch and closing the pull request. The workflow only runs under strict conditions to keep the main repository clean while archiving each submission snapshot.

## Trigger Conditions
To activate the workflow, **both** of the following must be true:
1. The pull request originates from a fork of this repository.
2. The pull request title contains the word "submit" (case-insensitive).

If either condition is not met, the workflow will be skipped.

## How to Trigger the Workflow
1. **Fork the repository** to your own GitHub account.
2. **Create a new branch** in your fork and make the necessary changes or add your submission files.
3. **Open a pull request** targeting this repository's default branch (usually `Submit`). Ensure that your PR title includes the word "submit" (e.g., "Submit: Week 2 exercises").
4. Once the PR is opened, GitHub Actions will evaluate the trigger conditions. If they are satisfied, the workflow runs automatically.

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

Following the steps above guarantees that your submission is processed automatically by the workflow.
