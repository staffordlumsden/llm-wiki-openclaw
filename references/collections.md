# Collect and catalogue workflow

Use `collect` when the user wants a bounded catalogue of **discoverable things** rather than immediate factual synthesis: examples, tools, projects, media, memes, organisations, resources, source candidates or other artefacts.

## Scope first

Before searching, define or infer:

- object type;
- topic/wiki;
- discovery strategy;
- scale/limit;
- whether media binaries should be downloaded, referenced only, or omitted;
- whether durable inventory records are wanted.

Never promise "all" without stating the bounded strategy and limit.

## Discovery

Use several non-identical searches where useful. For each candidate retain:

- canonical name/title;
- aliases;
- canonical URL/source;
- type;
- short description;
- `found_in_context` or equivalent discovery provenance;
- why it belongs in the collection;
- duplicate/variant relationship where relevant.

Deduplicate before output. A different URL does not necessarily mean a different artefact.

## Output first, inventory second

Save the bounded catalogue as an output such as:

```text
output/collect-<slug>-YYYY-MM-DD.md
```

Only create first-class inventory records when the set is small/durable enough or the user explicitly wants ongoing tracking. For very large collections, prefer one corpus/dataset manifest plus a sample/index rather than thousands of hand-written inventory records.

## Media

Do not put binary media in `raw/`. If the user wants bounded public media downloaded, place it under an output asset folder such as:

```text
output/assets/collect-<slug>/
```

Use defensive download practice where shell helpers are available: timeout, size cap, content-type check, stable filename, checksum, and graceful failure. Never download credential-gated/private media by bypassing access controls.

## Topic naming

For collection families likely to grow across subjects, prefer kind-first slugs (for example `tools-bitcoin`, `memes-ethereum`). Use subject-first naming when the subject itself is the durable research domain and the collection is secondary.

## Finish

Write the collection output, optionally create inventory/corpus state, update derived indexes and append the mutation to `log.md`.
