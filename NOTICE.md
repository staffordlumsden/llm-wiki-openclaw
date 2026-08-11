# Attribution and compatibility notice

This OpenClaw adapter is derived from and inspired by **llm-wiki** by nvk:

- Upstream repository: https://github.com/nvk/llm-wiki
- Upstream licence: MIT
- Upstream copyright: Copyright (c) 2026 nvk

The package preserves the upstream licence text in `LICENSE`.

## Baseline

The adapter was prepared against the repository state reviewed on 12 August 2026, whose README identifies the current changelog release as **v0.17.1**.

The upstream repository already provides runtime-neutral/portable behaviour, a compact query-lite protocol, Claude/Codex/OpenCode packaging and shared references. This package adds an OpenClaw-specific runtime layer rather than claiming a separate knowledge model.

## Material adaptations

- AgentSkills-compatible OpenClaw frontmatter and invocation.
- OpenClaw tool names (`read`, `write`, `edit`, `apply_patch`, `web_search`, `web_fetch`).
- Parallel research mapped to `sessions_spawn` / `sessions_yield`.
- Single-writer research contract: sub-agents return evidence; parent mutates wiki state.
- OpenClaw sandbox/bind guidance.
- Explicit-only read-only query profile that forbids shell fallback.
- Manual-first OpenClaw session capture boundary rather than pretending upstream Claude/Codex hooks are portable unchanged.

This is not an official nvk/llm-wiki distribution and is not an official OpenClaw project.
