# usefulSkills

A curated collection of coding agent skills — some written personally, others adapted from the wider community.

## Skills

### [`ship`](./ship/SKILL.md)

End-to-end ship workflow: stage and commit local changes, push a feature branch, open a PR, auto-merge with rebase, and sync local `main`. Selective staging avoids committing secrets or unrelated work.

Trigger: "ship it", "land this", "merge to main", or invoke `/ship`.

### [`grill-me`](./grill-me/SKILL.md)

Stress-tests a plan or design by interviewing you one question at a time, walking down each branch of the decision tree with a recommended answer for each.

Optionally accepts a file path — e.g. `/grill-me spec.md` — to load the plan from a file instead of conversation context.

Adapted from [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/grill-me).

## Using these skills

Drop the skill directory into your coding agent's skills folder (e.g. `~/.claude/skills/` or a project's `.claude/skills/`) and invoke it with `/<skill-name>`.
