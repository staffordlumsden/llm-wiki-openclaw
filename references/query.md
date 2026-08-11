# Query workflow

Use the nested `/wiki-query` profile for explicit read-only lookups when available. This reference defines the same route for the full manager.

## 1. Select one corpus

Resolve HUB and exactly one active topic/local wiki. Read its root `_index.md`.

## 2. Navigate indexes first

Read only the branch index required by the question:

- `wiki/_index.md` for compiled concepts/references;
- `raw/_index.md` for primary evidence;
- `inventory/_index.md` for candidates/status;
- `datasets/_index.md` for dataset manifests;
- `output/_index.md` for generated artefacts.

Follow exact links before broader search.

## 3. Minimum evidence set

Read only the files needed to answer. Prefer compiled articles for ordinary factual synthesis; follow their raw-source references where provenance, disputed claims or primary evidence matters.

## 4. Cross-wiki overlap

If the chosen wiki is insufficient and sibling relevance is plausible, inspect sibling **indexes only**. Report a useful connection, but do not silently merge evidence from multiple topics. Ask or clearly mark cross-wiki material if used.

## 5. Answer contract

- answer first;
- cite exact file paths;
- distinguish compiled synthesis, raw evidence, inventory state and output artefacts;
- respect `confidence` and obvious source limitations;
- say when the wiki lacks adequate evidence.

Never treat a plausible model answer as a substitute for absent wiki evidence.
