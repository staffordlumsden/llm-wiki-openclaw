# Audit and lint workflows

Use **audit** when the question is "can I trust this?" Use **lint** when the question is "is the structure internally correct?"

## Audit

Audit an article, output, project or topic by tracing material claims back through its cited wiki/raw sources.

Check:

1. source path exists;
2. cited source actually supports the claim;
3. synthesis has not strengthened a qualified source into an absolute claim;
4. confidence matches the evidence;
5. time-sensitive claims are not stale;
6. important counter-evidence is represented;
7. provenance records/checkpoints exist where the workflow expects them;
8. generated output has not drifted from current wiki state.

Classify findings, for example:

- verified;
- supported with qualification;
- weak/partial provenance;
- stale;
- unsupported;
- contradicted.

An audit should be capable of returning "insufficient evidence" rather than forcing a pass/fail judgement.

## Lint

Structural lint checks include:

- missing/broken indexes;
- broken internal links;
- malformed or missing required frontmatter;
- files in the wrong role/location;
- orphaned raw/wiki entries;
- duplicate slugs;
- missing core directories where the established wiki expects them;
- stale/missing registry entries in `wikis.json`;
- missing `log.md`;
- active topic paths accidentally recorded as machine-specific absolute paths when a portable relative path is expected.

Optional `inventory/` and `datasets/` trees are lazy: do not create them just because lint notices they are absent.

### Fix policy

- Safe derived repairs (for example rebuilding an index from source files) may be automated in an explicit `lint --fix` style request.
- Content-moving, deletion, retraction or ambiguous metadata inference must be surfaced before destructive action.
- Query-only mode never repairs anything.
- Log all mutations.

## Concurrency note

Derived indexes can converge after independent file writes, but OpenClaw parallel research deliberately uses a single parent writer. Do not rely on last-write-wins for simultaneous edits to the same article.
