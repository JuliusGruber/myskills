---
name: ship
description: Commit changes, create a PR, merge it, and update local main — a complete ship workflow.
---

# Ship: Commit, PR, Merge, and Sync

Perform a complete ship workflow: commit changes, create a PR, merge it, and update local main.

## Steps

1. **Check for changes**: Run `git status` to see if there are uncommitted changes. If no changes exist, inform the user and stop.

2. **Commit changes**:
   - Stage all changes with `git add -A`
   - Create a commit with a descriptive message based on the changes
   - Use conventional commit format (feat:, fix:, docs:, refactor:, etc.)

3. **Create and push branch**:
   - Create a new branch from current HEAD with a descriptive name based on the commit
   - Push the branch to origin with `git push -u origin <branch-name>`

4. **Create Pull Request**:
   - Use `gh pr create` to create a PR against main
   - Set the title to match the commit message
   - Auto-generate a body summarizing the changes

5. **Merge the PR**:
   - Use `gh pr merge --rebase --delete-branch` to rebase-merge and clean up the remote branch

6. **Update local main**:
   - Switch to main branch: `git checkout main`
   - Pull latest: `git pull origin main`
   - Delete the local feature branch if it exists

7. **Confirm completion**: Show the final `git status` and `git log -1` to confirm everything is synced.

## Important
- If any step fails, stop and report the error to the user
- Do not force push or use destructive git commands
- Always use rebase merge to keep main history linear
