---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Accepts an optional file path (e.g. spec.md) to grill against. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
---

If an argument was provided, treat it as a path to a file (e.g. `spec.md`, `docs/plan.md`) and read it first — that file is the plan being grilled. If no argument was provided, use whatever plan or design is already in the conversation context.

Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one. For each question, provide your recommended answer.

Ask the questions one at a time.

If a question can be answered by exploring the codebase, explore the codebase instead.
