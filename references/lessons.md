# Lessons-learned workflow (`ll`)

Use this workflow to extract reusable operational knowledge from the current task/session: errors, fixes, gotchas, reliable procedures, constraints and implementation lessons.

It is **not** an instruction to dump the transcript into the wiki.

## Extract

Identify only lessons that are:

- durable enough to matter again;
- grounded in observed work, user correction or verified evidence;
- appropriately scoped to the selected topic/project;
- free of secrets, credentials and unnecessary personal data.

Separate:

- factual/domain lessons → candidate raw note or wiki evidence only when properly sourced;
- operational procedure/gotcha → project/operational note;
- user correction/preference → feedback candidate, not automatic topic evidence;
- proposed agent rule → suggestion for `AGENTS.md`/workspace instructions, never auto-installed unless asked.

## Dry run

When the user asks for preview/dry-run, show the candidate lessons and destinations without writing anything.

## Commit

On explicit write:

1. deduplicate against existing lessons/content;
2. write to the correct layer;
3. preserve provenance to the session/task where appropriate;
4. update derived indexes if needed;
5. append the operation to `log.md`.
