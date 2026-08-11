# Research workflow for OpenClaw

Research extends wiki coverage through independent discovery, credibility assessment, ingestion and synthesis. OpenClaw's sub-agent system is used only for evidence gathering; the parent remains the single wiki writer.

## Phase 1 — inspect current coverage

Read the selected wiki indexes and the minimum relevant articles. Summarise:

- what is already well supported;
- unresolved contradictions;
- missing sub-questions;
- stale/high-volatility areas;
- likely high-value source types.

Do not launch agents before this step; otherwise fan-out duplicates existing coverage.

## Phase 2 — decompose into independent lenses

Standard mode: up to 5 strands. A robust generic set is:

1. **Primary/official** — statutes, cases, standards, official documentation/data, first-party records as appropriate.
2. **Scholarly** — peer-reviewed research and recognised academic treatments.
3. **Empirical** — datasets, measurements, evaluations and observed outcomes.
4. **Practice/implementation** — credible professional or institutional evidence about operation in context.
5. **Critical/counter-evidence** — failures, limitations, contrary findings, alternative explanations and bias.

For deep mode add comparative/historical/methodological strands as useful (up to 8). Exhaustive mode may use up to 10, including citation-chasing or adjacent-domain transfer. Choose lenses that fit the subject.

## Phase 3 — spawn isolated research workers

Each `sessions_spawn` task must be self-contained and must state **DO NOT WRITE TO OR MODIFY THE WIKI**.

Suggested child task template:

```text
Objective: {question}
Lens: {lens and focus}
Existing wiki coverage: {brief}
Find 3–5 high-quality sources. Use several varied searches, fetch promising full sources where possible, and skip SEO spam, thin duplicates and inaccessible sources.

For each useful source return:
- title + canonical URL
- author/organisation, date and source type if available
- 3–5 findings relevant to the objective
- relevance: direct / indirect
- provisional quality 1–5 with justification
- direction: supports / opposes / nuances / contextual only (if a working claim exists)
- one-sentence reason to ingest
- limitations or uncertainty

Also report contradictions, duplicated evidence chains and remaining gaps.
Do not write files, change config, ingest sources, or edit the wiki.
```

Use isolated context unless transcript context is genuinely necessary.

## Phase 4 — receive, deduplicate and score centrally

Use completion events (`sessions_yield`) rather than repeated polling.

The parent should not accept child self-rating uncritically. Reassess source credibility using signals such as:

- peer review / primary evidence;
- authoritative institution or recognised author;
- methodological transparency;
- recency where the claim is time-sensitive;
- independent corroboration;
- conflicts of interest / promotional framing;
- whether several apparently independent sources trace to one origin.

A simple 1–5 final quality scale is sufficient if the rationale is recorded. Reject low-value duplicates and unsupported derivative claims.

## Phase 5 — ingest selected evidence

Use the ingestion workflow. Keep raw material immutable and record provenance.

## Phase 6 — compile

Update synthesis incrementally. Explicitly represent opposing or qualifying evidence. Add cross-links discovered across research strands.

## Phase 7 — gap reflection

After a round, identify the most consequential remaining gaps. Prioritise each by:

- **impact** on the user's question or wiki understanding;
- **feasibility** of finding evidence;
- **specificity** of a searchable sub-question.

The upstream llm-wiki convention scores each dimension 1–5 and can rank with the product `impact × feasibility × specificity` (1–125). Use this only as a decision aid, not fake precision.

Stop when high-impact gaps are resolved and additional searches yield mostly duplication. Continue or change strategy when important gaps remain.

## Thesis/evaluative mode

When researching a proposition rather than a topic, require each child to classify evidence direction as supports, opposes or nuances and to distinguish evidence strength. The final synthesis must actively seek disconfirming evidence and avoid treating source count as proof.

## Session provenance

For extended multi-round work, maintain the wiki's existing research/session checkpoint conventions. Record round objectives, source decisions, gaps and major synthesis changes. OpenClaw's chat transcript is not a substitute for wiki-side provenance.
