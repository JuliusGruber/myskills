---
name: ship
description: Commit changes, create a PR, merge it, and update local main — a complete ship workflow. Use this skill whenever the user wants to ship, land, push, or merge their changes to main. Triggers on phrases like "ship it", "land this", "push my changes", "merge to main", "send this to main", "get this into main", or any request to go from local changes to a merged PR in one step.
---

# Ship: Commit, PR, Merge, and Sync

Take local changes (committed or uncommitted) all the way to a merged PR on main in one workflow. The goal is to save the user from running a dozen git/gh commands manually — but never at the cost of committing something they didn't intend to.

## Step 1: Assess the current state

Run `git status` and `git log main..HEAD` (or the equivalent for the repo's default branch) to understand what needs shipping.

There are three possible starting states — handle each:

- **Uncommitted changes exist**: proceed to Step 2.
- **Clean working tree but commits ahead of main**: skip Step 2, go to Step 3.
- **Clean working tree and no commits ahead of main**: inform the user there's nothing to ship and stop.

Also note which branch you're on — you'll need this in Step 3.

## Step 2: Stage and commit

Review the changes before staging. Run `git diff` (for tracked files) and check `git status` (for untracked files) to understand what will be committed.

**Stage selectively — never use `git add -A` or `git add .`**. The reason this matters is that blindly staging everything can commit secrets, credentials, or unrelated work-in-progress. Instead:

1. Review each untracked/modified file.
2. Skip files that look like secrets or sensitive config: `.env`, `credentials.*`, `*.key`, `*.pem`, `*.secret`, files containing API keys, passwords, or tokens.
3. If you find sensitive files, **warn the user** and suggest adding them to `.gitignore`. Do not stage them.
4. Stage the remaining files by name: `git add <file1> <file2> ...`

Write a commit message in conventional commit format (`feat:`, `fix:`, `docs:`, `refactor:`, etc.) that accurately describes the changes based on the diff you reviewed.

## Step 3: Ensure you're on a feature branch and push

Check which branch you're on:

- **Already on a feature branch** (not `main`/`master`): keep it. Push with `git push -u origin <current-branch>`.
- **On main/master**: create a new branch with a descriptive name based on the changes (e.g., `feat/add-date-formatter`), then push it.

## Step 4: Create a Pull Request

Use `gh pr create` against main. For the title:

- If there's a single commit on the branch, use its message.
- If there are multiple commits, write a short summary title that captures the overall change.

Generate a body with a `## Summary` section (2-3 bullet points) and a `## Test plan` section.

## Step 5: Merge the PR

Use `gh pr merge --auto --rebase --delete-branch`. The `--auto` flag is important because it waits for any required CI checks to pass before merging, rather than trying to merge immediately and failing. If the repo doesn't require checks, it merges right away.

## Step 6: Update local main

Switch to main and pull:

```
git checkout main
git pull origin main
```

If `git checkout main` fails (e.g., in a worktree setup where main is checked out elsewhere), skip this step — the remote is already up to date, and the user can sync locally when ready.

Delete the local feature branch if it still exists: `git branch -d <branch-name>`

## Step 7: Confirm completion

Show `git status` and `git log -1` so the user can see everything is synced.

## Important

- If any step fails, stop and report the error — don't try to power through.
- Never force push or use destructive git commands.
- Use rebase merge to keep main history linear.
- The user trusts this workflow to do the right thing. Committing secrets or losing work would break that trust, so be careful with staging and always review before committing.
