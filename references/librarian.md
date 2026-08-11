# Librarian workflow

The librarian is a **focused maintenance pass over compiled `wiki/` knowledge**, distinct from structural lint and broader trust audit.

Use it for article quality, staleness, weak sourcing, duplicated concepts, missing cross-links and volatility-driven refresh candidates.

## Scan

Read indexes first, then inspect a bounded set of candidate articles. Prioritise:

- low-confidence articles;
- high-volatility topics not recently refreshed;
- articles with broken/weak source trails;
- overlapping articles that may represent one concept;
- orphaned concepts with few meaningful links;
- articles whose summary no longer matches body/current evidence.

## Recommendations

Classify each candidate as, for example:

- no action;
- refresh sources;
- recompile/update;
- merge/split proposal;
- add cross-links;
- audit required;
- topic-guide/convention proposal.

Do not silently redesign the wiki's human-owned topic conventions. Propose convention/schema changes for review.

## Mutations

A plain librarian scan is diagnostic. Only apply editorial changes when the user asks for a fix/update. Structural problems belong in lint; evidentiary trust questions belong in audit.

Save a librarian report under `output/` when a durable report is useful and log any actual wiki mutations.
