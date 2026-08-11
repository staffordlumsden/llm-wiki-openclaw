# Wiki structure and placement

A typical hub:

```text
HUB/
├── _index.md
├── wikis.json
├── log.md
├── topics/
│   ├── <topic>/
│   │   ├── _index.md
│   │   ├── config.md
│   │   ├── schema.md              # optional human-owned topic guide
│   │   ├── log.md
│   │   ├── raw/
│   │   ├── wiki/
│   │   ├── inventory/             # optional/lazy
│   │   ├── datasets/              # optional/lazy
│   │   └── output/
│   └── .archive/
└── .sessions/                      # operational memory; not topic evidence
```

A project-local wiki uses `.wiki/` as its root and follows the same topic-level principles.

## File roles

### raw/
Immutable source representations and notes that preserve provenance. Normal compilation never rewrites them.

### wiki/
Synthesised, cross-linked articles derived from one or more raw sources. Articles should state provenance and confidence honestly.

### inventory/
Operational tracking: candidates, queues, priorities, ideas and next actions. Create only when needed.

### datasets/
Dataset manifests, registry metadata, access/provenance notes and derived dataset documentation. Large binary/tabular assets may live elsewhere; keep durable pointers and checksums where appropriate.

### output/
Reports, briefs, plans, collection outputs and other generated deliverables. Outputs do not become factual source-of-truth merely because they are saved here.

### .sessions/
Redacted operational memory and rehydration material. It is deliberately separate from topic evidence.

## Frontmatter

Use YAML frontmatter as structured data. Preserve existing schema conventions. Typical fields include title, summary, tags, created/updated dates, source references, status and confidence. Do not invent fields that conflict with the selected wiki's established conventions.

## Linking

Where the wiki follows upstream dual-linking, keep both an Obsidian wikilink and a standard Markdown link on the same logical reference, for example:

```markdown
[[administrative-law|Administrative law]] ([Administrative law](../concepts/administrative-law.md))
```

Add reverse links when they improve navigation rather than mechanically linking every co-occurrence.

## Derived index protocol

Indexes are caches generated from actual files/frontmatter. Before trusting an index:

1. read it;
2. check obvious staleness signals if relevant (missing known file, count mismatch, broken path);
3. use exact files as source of truth;
4. repair/rebuild only in a mutating workflow, never during `wiki-query`.

## Logging

For every mutating wiki operation append a short entry to the active wiki `log.md` containing at least timestamp, operation, target and result. Preserve history.
