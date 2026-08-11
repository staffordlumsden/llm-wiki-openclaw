# Inventory, ideas and datasets

These layers support operational curation without contaminating factual evidence.

## Inventory

Use inventory when the user wants to track things over time: source queues, candidates, tools, examples, people/organisations, watch lists, backlogs, acceptance state, priority or next actions.

A useful inventory record normally includes:

- stable id/slug;
- title/name and aliases;
- type;
- status;
- provenance (`found_in_context`, URL/source, discovery date);
- priority/decision state;
- next action;
- links to related raw/wiki/dataset records where applicable.

Inventory records are not evidence for factual claims merely because they contain descriptive text.

## Ideas

Ideas are deliberately pre-delivery. Capture fuzzy proposals, progressively shape them with research, and preserve decision lineage. Promotion into a delivery project should be explicit and user-approved; freeze the approved `BRIEF.md` (or equivalent approved brief artefact) rather than quietly rewriting the idea's history. Preserve lineage from Concept → Idea → Project.

## Collections

When collecting "all" examples/resources, always define a bounded discovery strategy and limit. Record aliases and where each item was found, deduplicate, and avoid claiming exhaustiveness beyond the search strategy.

## Datasets

A dataset manifest should make the dataset understandable and reproducible without requiring it to live inside the wiki repository. Record, as relevant:

- title and owner/source;
- canonical location;
- licence/access constraints;
- version/date range;
- schema/fields or linked data dictionary;
- size/format;
- checksums for stable snapshots;
- transformations/derived artefacts;
- known limitations;
- relationship to inventory decisions and wiki articles.

Large data need not be copied into the wiki. Prefer durable manifests and explicit pointers.
