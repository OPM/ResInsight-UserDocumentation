# Update spell-check workflow to automatically create PRs for spelling fixes

This PR updates the `.github/workflows/spell-check.yml` workflow to automatically create pull requests for spelling corrections.

## Changes:

- **Split workflow into two jobs:**
  - `codespell-check`: Runs on pull requests to verify spelling (check-only mode)
  - `codespell-fix`: Runs weekly or manually to fix spelling and create PRs

- **New triggers:**
  - `schedule`: Runs automatically every Sunday at midnight UTC
  - `workflow_dispatch`: Allows manual triggering from the Actions tab
  - `pull_request`: Still checks PRs but doesn't auto-fix them

- **Automated PR creation:**
  - Runs codespell with `-w` flag to auto-fix issues
  - Uses `peter-evans/create-pull-request@v6` to create PRs
  - Creates PRs on branch `automated/spelling-fixes`
  - Adds labels: `documentation`, `automated`

## How to use:

- **Automatic**: Wait for the weekly Sunday run
- **Manual**: Go to Actions → codespell → Run workflow
- **PR checks**: Still validates spelling on every pull request

The workflow has proper permissions (`contents: write`, `pull-requests: write`) to create commits and PRs.