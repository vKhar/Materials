# Workflow Testing Guide

## Issue Fixed
The `submit_pr.yml` workflow was not triggering for pull requests from forks that contained "submit" in the title.

## Root Cause
The workflow condition had two issues:
1. **Syntax Error**: Mixed `>-` (multi-line YAML string) with `${{ }}` expression wrapper
2. **Invalid Function**: Used `tolower()` instead of GitHub Actions' `lower()` function

## The Fix
Changed lines 16-18 from:
```yaml
if: >-
  ${{
    github.event.pull_request.head.repo.full_name != github.repository &&
    contains(tolower(github.event.pull_request.title), 'submit')
  }}
```

To:
```yaml
if: >-
  github.event.pull_request.head.repo.full_name != github.repository &&
  contains(lower(github.event.pull_request.title), 'submit')
```

## Why This Works
In GitHub Actions, when using `if:` conditions:
- The entire value is already evaluated as an expression context
- Using `${{ }}` inside a multi-line string (`>-`) treats it as a literal string, not an expression
- Removing `${{ }}` allows the condition to be properly evaluated as a boolean

## How to Test
1. Fork the `vKhar/Materials` repository
2. Make any change to a file in your fork
3. Create a pull request with a title containing "submit" (case-insensitive)
   - Example: "Submit: Exercise 02 solutions"
   - Example: "I want to submit my work"
4. The workflow should automatically:
   - Trigger on PR creation
   - Copy changed files to `Submissions/<your_username>/`
   - Push to the `Submit` branch
   - Close the PR with a confirmation comment

## Testing with Existing PR
PR #30 from `kilowilco-droid` should now trigger the workflow on the next synchronization event:
- Push a new commit to the PR branch, or
- Close and reopen the PR, or
- The workflow will trigger for new PRs matching the criteria

## Verification
After a PR is processed:
1. Check the Actions tab for a successful workflow run
2. Navigate to the `Submit` branch
3. Look for `Submissions/<username>/` directory containing the submitted files
4. Check that the PR is closed with an automated comment
