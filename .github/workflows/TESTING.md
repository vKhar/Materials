# Workflow Testing Guide

## Current Issue: PR #42 Not Auto-Closing

### Problem
PR #42 titled "append file" should be automatically closed because:
- It does NOT contain "submit" (case-insensitive)
- It does NOT contain "PR" (case-insensitive)
- According to workflow rules, it should be auto-closed by the `auto-close-pr` job

### Root Cause
PR #42 is from a **first-time contributor** (kilowilco-droid) from a fork. GitHub requires manual approval before running workflows for first-time contributors as a security measure. The workflow is correctly configured but hasn't run yet because it's awaiting approval.

### Solution
**For Maintainers:**
1. Go to the **Actions** tab in the repository
2. Look for any pending workflow run for PR #42
3. Click "Approve and run" to execute the workflow
4. The workflow will auto-close PR #42 with an explanatory comment

## Workflow Behavior

The workflow (`submit_pr.yml`) has three distinct behaviors:

### 1. Process and Close (contains "submit")
- **Condition**: Title contains "submit" (case-insensitive)
- **Action**: Copy files to `Submit` branch, then close PR
- **Examples**: "Submit homework", "SUBMIT: Exercise 2"

### 2. Keep Open for Review (contains "PR")
- **Condition**: Title contains "PR" (case-insensitive)  
- **Action**: No automatic processing, leaves PR open
- **Examples**: "PR: Fix typo", "Update docs - PR"

### 3. Auto-Close Without Processing (neither keyword)
- **Condition**: Title contains neither "submit" nor "PR"
- **Action**: Close PR immediately with explanation comment
- **Examples**: "append file", "Update README", "Fix bug"

## How to Test

### Testing Each Scenario

1. **Submission PR (auto-process and close)**:
   ```bash
   git checkout -b test-submit
   echo "test submission" > test.txt
   git add test.txt && git commit -m "Add test"
   git push origin test-submit
   ```
   Create PR with title: "Submit: Test submission"
   Expected: Files copied to Submit branch, PR auto-closed

2. **Review PR (stay open)**:
   ```bash
   git checkout -b test-pr
   echo "test change" > README.md
   git add README.md && git commit -m "Update"
   git push origin test-pr
   ```
   Create PR with title: "PR: Update documentation"
   Expected: PR stays open, no automatic action

3. **Invalid PR (auto-close without processing)**:
   ```bash
   git checkout -b test-invalid
   echo "test" > file.txt
   git add file.txt && git commit -m "Add file"
   git push origin test-invalid
   ```
   Create PR with title: "Add new file"
   Expected: PR immediately closed with explanation

### First-Time Contributor Testing
When testing as a first-time contributor:
1. The workflow will show as "pending" in the Actions tab
2. A maintainer must click "Approve and run"
3. After approval, workflow executes according to the rules above

### Returning Contributor Testing
For contributors who have had previous PRs approved:
- Workflows run automatically without requiring approval
- This makes the process faster for trusted contributors

## Verification

### For Submission PRs:
1. Check the Actions tab for a successful workflow run
2. Navigate to the `Submit` branch
3. Look for `Submissions/<username>/` directory
4. Verify submitted files are present
5. Confirm PR is closed with automated comment

### For Review PRs:
1. Check that workflow run shows "skipped" for the process job
2. Verify PR remains open
3. No files copied to Submit branch

### For Invalid PRs:
1. Check that workflow run shows the auto-close job executed
2. Verify PR is closed with explanation comment
3. No files copied to Submit branch

## Workflow Security

The workflow uses `pull_request_target` which:
- Runs in the context of the base repository (not the fork)
- Has elevated permissions: write access to Submit branch and ability to close PRs
- Requires approval for first-time contributors to prevent malicious actors from:
  - Modifying workflow files to steal secrets
  - Pushing unwanted content to the Submit branch
  - Abusing PR close permissions

This security model allows legitimate submissions while protecting the repository.

## Manual Workflow Approval Process

1. Navigate to repository **Actions** tab
2. Click on the pending workflow run
3. Review the PR changes carefully
4. Click "Approve and run" if changes are safe
5. Workflow executes with the appropriate behavior based on PR title
