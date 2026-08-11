---
name: llm-wiki
description: Manage an llm-wiki knowledge hub in OpenClaw: initialise, ingest, compile, query, research with sub-agents, audit, lint, curate inventory and datasets, capture operational sessions, and generate evidence-backed outputs.
homepage: https://github.com/nvk/llm-wiki
user-invocable: true
---

# LLM Wiki — OpenClaw adapter

Use this skill to operate an **llm-wiki** knowledge base from OpenClaw while preserving the upstream knowledge model: immutable raw evidence, derived indexes, synthesised wiki articles, explicit provenance, honest gaps, and explicit promotion of operational memory.

This is an OpenClaw runtime adapter. The llm-wiki knowledge model remains runtime-neutral. When a rule here conflicts with a runtime-neutral llm-wiki reference in this skill, preserve the llm-wiki data model and adapt only the OpenClaw tool invocation.

## First move: resolve the wiki, then choose the smallest workflow

Before any wiki operation:

1. Resolve **HUB** using `references/hub-resolution.md`.
2. Resolve the active topic wiki or local `.wiki/`.
3. Read its `_index.md` before broad scans.
4. Choose the smallest workflow that answers the request.
5. Load only the relevant reference file(s) below.

Do not pre-load every reference. Keep ordinary queries cheap.

## Core invariants

1. **Raw evidence is immutable.** Never silently rewrite ingested source material. Corrections belong in new evidence, explicit retraction, or compiled synthesis.
2. **Indexes are derived caches.** Markdown files plus YAML frontmatter are the source of truth. Rebuild or repair indexes from files, never the reverse.
3. **Synthesis is not copying.** Compiled articles integrate multiple sources, distinguish disagreement, preserve provenance, and link related concepts.
4. **Evidence beats model memory.** If the selected wiki does not answer a factual question, state the gap. Do not manufacture an answer from prior model knowledge and present it as wiki-grounded.
5. **Topic isolation by default.** Work inside one topic wiki unless the user explicitly requests cross-wiki work. Sibling indexes may be inspected for overlap; content is not merged silently.
6. **Inventory is operational state, not factual evidence.** Candidate lists, priorities and next actions can come from inventory; substantive claims require wiki/raw sources.
7. **Archived topics are quiet.** Exclude archived topics from normal query, compile and research unless explicitly included.
8. **Session memory is not evidence.** OpenClaw/llm-wiki session capture remains operational memory until the user explicitly promotes it into a topic.
9. **One writer coordinates parallel research.** OpenClaw sub-agents may search, fetch, read and analyse, but the parent/coordinator is the sole writer to wiki state during a fan-out research round.
10. **Append the log for wiki mutations.** Preserve prior log entries; do not rewrite history.

## OpenClaw tool mapping

Use OpenClaw tools by capability rather than emulating Claude/Codex command names:

- filesystem inspection: `read`
- filesystem changes: `write`, `edit`, or `apply_patch`
- deterministic shell helpers when genuinely needed: `exec`
- public research: `web_search` and `web_fetch`
- parallel independent research: `sessions_spawn`
- collect child completions: `sessions_yield`; use `subagents` for status/debugging, not polling loops

Treat `/wiki:*`, `@wiki`, and `$wiki-query` examples from upstream documentation as **workflow shorthand**, not literal OpenClaw command dependencies. The installed skill is user-invocable as `/llm-wiki`; the nested compact profile is `/wiki-query`.

If a required tool is unavailable, degrade safely. Never substitute a more dangerous capability merely to preserve convenience. In particular, a read-only query must not fall back to `exec` just because search/listing would be easier.

See `references/openclaw-runtime.md` for tool policy, sandboxing and sub-agent rules.

## Workflow router

Load only what you need:

- **query** → `references/query.md`
- **ingest / ingest collection / import** → `references/ingestion.md`
- **collect / catalogue discoverable artefacts** → `references/collections.md`
- **compile / refresh synthesis** → `references/compilation.md`
- **research / thesis / plan** → `references/research.md`
- **audit / provenance / drift / trust check** → `references/audit-lint.md`
- **lint / repair structure / stale indexes** → `references/audit-lint.md`
- **librarian / staleness and article-quality maintenance** → `references/librarian.md`
- **inventory / ideas / candidate tracking / datasets** → `references/inventory-datasets.md`
- **project / output / assess** → `references/projects-outputs.md`
- **archive / restore topic / list archived** → `references/archive.md`
- **lessons learned (`ll`)** → `references/lessons.md`
- **session capture / rehydrate / feedback promotion** → `references/sessions-feedback.md`
- **init / structure / placement / logging** → `references/wiki-structure.md`
- **hub path / topic resolution** → `references/hub-resolution.md`
- **OpenClaw permissions / sandbox / child agents** → `references/openclaw-runtime.md`

## Ambient behaviour

When activated implicitly rather than through `/llm-wiki`:

1. Resolve the hub.
2. If a local `.wiki/` or relevant hub/topic index exists, read the index only.
3. If it plausibly covers the request, follow the bounded query workflow.
4. If it does not, answer normally if appropriate; optionally say the material could be added to the wiki.
5. Never trigger ingestion, compilation, research fan-out, mutation, or session promotion merely because a wiki exists.

## Research orchestration — OpenClaw-specific contract

For a research workflow, the parent agent owns the research plan, deduplication, source credibility assessment, ingestion decisions and every write to the wiki.

For standard fan-out, use up to **5 isolated child research tasks**. For `--deep`, up to **8**; for the upstream `--retardmax` widest-net mode (called **exhaustive** in this adapter where a neutral label is clearer), up to **10**. These are targets, not a reason to change global configuration. If the active OpenClaw child limit is lower, run the work in bounded waves.

Each child receives a self-contained task containing:

- research objective or sub-question;
- lens/role;
- concise summary of existing wiki coverage;
- inclusion/exclusion criteria;
- expected source quality;
- explicit prohibition on wiki mutation;
- required evidence-bundle return format.

Each child returns, for each useful source:

- title and canonical URL;
- source type and date where available;
- key claims/findings;
- direct relevance to the assigned question;
- provisional quality (1–5) with a short justification;
- support / opposition / nuance relative to the working claim where relevant;
- suggested ingestion reason;
- uncertainty, contradictions and gaps.

Use `context: isolated` for independent web research. Use `fork` only when a child genuinely needs the current transcript rather than a concise task brief.

After spawning, use `sessions_yield` to receive completion events rather than constructing repeated status polling. The parent then cross-checks, deduplicates, assigns final credibility, ingests selected evidence and compiles synthesis.

See `references/research.md`.

## Write discipline

Before a write:

- verify the target wiki;
- verify the intended file role (raw, wiki, inventory, datasets, output, session state);
- preserve existing frontmatter fields unless the workflow intentionally changes them;
- avoid concurrent edits to the same file;
- prefer several bounded edits over one huge generated write;
- append an operation entry to `log.md`.

When a generated article exceeds roughly 200 lines, create a skeleton first, then append sections sequentially. This reduces partial-write and timeout failure modes.

## Output discipline

For user-facing answers from the wiki:

- lead with the answer;
- cite exact wiki paths for material claims;
- distinguish compiled synthesis from raw evidence and operational inventory state;
- mention confidence weaknesses or genuine evidence gaps when they affect the answer;
- do not expose hidden session capture as if it were curated evidence.

For saved outputs, report the absolute output path.

## Compatibility boundary

This adapter targets llm-wiki's current portable knowledge model and OpenClaw's AgentSkills-compatible skill system. It intentionally does **not** copy Claude hooks, Codex plugin metadata, OpenCode permissions or runtime-specific slash-command plumbing. Those are packaging layers, not wiki semantics.

Attribution and upstream baseline are in `NOTICE.md`.
