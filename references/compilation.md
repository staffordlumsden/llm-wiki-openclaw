# Compilation workflow

Compilation turns raw evidence into interconnected synthesis. Default to incremental work over new/uncompiled sources; full recompilation must be explicit.

## Preflight

1. Resolve the wiki.
2. Read root, raw and wiki indexes.
3. Identify new or affected raw sources.
4. Inspect existing articles that overlap conceptually so the compilation updates rather than duplicates the knowledge graph.

## Synthesis rules

A compiled article should:

- integrate multiple sources where evidence permits;
- distinguish consensus, disagreement and uncertainty;
- avoid copying long passages from sources;
- link each material claim or section to relevant raw provenance according to the wiki's established convention;
- maintain or update a meaningful confidence field;
- connect to related wiki concepts with useful reciprocal links;
- preserve stable slugs when the concept identity has not changed.

Do not create false certainty from multiple derivative sources that all trace to one origin.

## Confidence

Use source quality, corroboration, recency where relevant, directness and contradiction to determine confidence. A single authoritative primary source may be high confidence for what that organisation itself did or said, but not necessarily for broader causal or evaluative claims.

## Incremental update

Prefer:

1. update an existing relevant article;
2. create a new article only for a distinct durable concept;
3. add cross-links after the content is stable;
4. rebuild derived indexes;
5. append the compilation operation to `log.md`.

## Large writes

For long articles, write frontmatter, title and outline first, then append/edit one section at a time. Avoid a single very large write.

## Cross-wiki boundary

Never compile one topic's evidence directly into a sibling topic without an explicit user-directed import/connection workflow. Cross-wiki index overlap may be noted without merging content.
