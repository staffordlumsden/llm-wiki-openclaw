# Sessions, rehydration and feedback

llm-wiki session memory is an **operational layer**, not topic evidence.

## Storage boundary

Use `HUB/.sessions/` for hub-level captured operational context or `.wiki/.sessions/` for project-local work where that convention already exists. Keep topic evidence under the topic's `raw/` only after explicit promotion.

## OpenClaw adaptation

OpenClaw already has session/transcript mechanisms, but do not treat them as curated wiki memory automatically. If a session-capture integration is configured, it should:

1. capture only the minimum useful operational event/checkpoint;
2. redact secrets and sensitive payloads before persistence;
3. avoid storing tool credentials, authentication headers or hidden reasoning;
4. create a digest/index suitable for rehydration;
5. keep promotion into a topic explicit.

The full skill can operate without any automatic OpenClaw hook. Manual session capture is a valid baseline.

## Rehydration

A rehydration brief should state the active wiki identity first, then summarise:

- last completed operation;
- current in-flight objective;
- explicit decisions/approvals;
- unresolved blockers/gaps;
- next safe actions;
- paths to relevant wiki/session artefacts.

Rehydration reconstructs operational context; it does not upgrade captured claims into evidence.

## Feedback candidates

High-signal user corrections, stable preferences relevant to the wiki, approvals and plan acceptance may be captured as **candidates**. Generic acknowledgements should not become durable memory.

Before promotion:

- review the candidate;
- remove secrets/private material not needed for the topic;
- determine whether it belongs in raw notes, inventory, project state or nowhere;
- require explicit promotion for topic evidence.

## Session research registry

For long multi-round research, wiki-side checkpoint/event records are more durable than relying on the chat transcript. Preserve source decisions, round objectives, major findings, gaps and compilation changes so an audit can reconstruct what happened.
