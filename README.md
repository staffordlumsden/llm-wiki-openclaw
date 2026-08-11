# llm-wiki for OpenClaw

An OpenClaw-native skill wrapper for [nvk/llm-wiki](https://github.com/nvk/llm-wiki).

It preserves llm-wiki's portable knowledge model while adapting runtime behaviour to OpenClaw's current AgentSkills-compatible skill loading, filesystem/web tools and `sessions_spawn` sub-agents.

## What is included

- `SKILL.md` — full read/write manager (`/llm-wiki`)
- `profiles/wiki-query/SKILL.md` — compact explicit read-only query skill (`/wiki-query`)
- `references/` — OpenClaw-specific workflow references covering query, ingest/import, collect, compile, research/thesis, audit/lint, librarian, inventory/ideas/datasets, projects/outputs/assessment, archive/restore, lessons and sessions
- `examples/` — recommended agent/sandbox configurations
- `scripts/validate.py` — structural and policy lint for this package
- `NOTICE.md` + `LICENSE` — upstream attribution and MIT licence

## Install

From the unpacked directory:

```bash
openclaw skills install ./llm-wiki-openclaw --as llm-wiki
openclaw skills check
openclaw skills info llm-wiki
```

OpenClaw discovers nested skills under skill roots, so the bundled `wiki-query` profile should also be available. If your installed OpenClaw release does not surface the nested profile after a local install, install it explicitly:

```bash
openclaw skills install ./llm-wiki-openclaw/profiles/wiki-query --as wiki-query
```

For a manual workspace install, copy the directory under:

```text
<workspace>/skills/llm-wiki-openclaw/
```

OpenClaw uses the frontmatter `name`, so the directory name does not have to match the command name.

## Hub setup

The portable llm-wiki convention is:

```json
{
  "hub_path": "~/wiki"
}
```

saved as `~/.config/llm-wiki/config.json` when the acting process can read that path.

A project-local `.wiki/` needs no global hub and is the simplest sandbox-friendly mode.

### If OpenClaw sandboxing is enabled

A hub outside the agent workspace must be deliberately exposed to the sandbox. Prefer a narrow bind such as:

```json5
{
  agents: {
    list: [
      {
        id: "wiki",
        sandbox: {
          mode: "all",
          scope: "agent",
          workspaceAccess: "rw",
          docker: {
            binds: ["/home/YOU/wiki:/wiki:rw"],
            dangerouslyAllowExternalBindSources: true,
          },
        },
      },
    ],
  },
}
```

Then ensure the acting agent resolves the hub as `/wiki` inside that sandbox. For query-only agents, use `:ro` and deny all mutating tools.

Do **not** mount a broad home directory merely to reach one knowledge base.

## Recommended OpenClaw tools

### Full manager

Needs filesystem read/write capability. Research additionally benefits from `web_search`, `web_fetch`, `sessions_spawn`, `sessions_yield` and `subagents`. `exec` is optional and should be reserved for deterministic helpers.

### Query-only

Use `read`; deny `write`, `edit`, `apply_patch`, `exec` and `process`. The `wiki-query` instructions also prohibit mutation, but tool policy is the stronger enforcement layer.

See `examples/openclaw-config.example.json5`.

## Why the OpenClaw research adapter is different

Upstream llm-wiki uses parallel research. This port maps that to OpenClaw sub-agents, but **children never write to the wiki**. They return structured evidence bundles. The parent performs final credibility review, ingestion and compilation.

This gives the parallel discovery benefit without concurrent agents racing to edit the same knowledge state or self-promoting their findings.

Targets:

- standard: up to 5 isolated research strands;
- deep: up to 8;
- exhaustive: up to 10.

If OpenClaw's active child cap is lower, use waves rather than changing configuration just for the skill.

## Usage examples

```text
/llm-wiki initialise a local wiki for this project
/llm-wiki ingest https://example.org/report into the administrative-law topic
/llm-wiki research the reliability of automated legal citation checking --deep
/llm-wiki compile the new sources
/llm-wiki collect examples of local-LLM privacy deployments --wiki local-llms
/llm-wiki archive topic old-project --reason "superseded"
/llm-wiki output report on assessment validity
/llm-wiki audit the provenance of the assessment-validity article
/wiki-query what does the legal-education wiki say about oral assessment reliability?
```

Natural-language requests can also activate the full skill when the description matches. `wiki-query` is explicit-only by design.

## Compatibility strategy

This is a **thin runtime adaptation**, not a hard fork of the knowledge model. Keep upstream `nvk/llm-wiki` as the conceptual source of truth and confine OpenClaw-specific changes to:

- tool names/capabilities;
- sub-agent orchestration;
- sandbox/filesystem notes;
- command invocation;
- session adapter boundary.

That makes future upstream updates easier to port.

## Validate the package

```bash
python3 scripts/validate.py
```

The validator checks required files/frontmatter, skill names, explicit query-only mutation guards, reference links and accidental risky patterns.

## Status

Version: **0.1.0**  
Upstream baseline reviewed: **llm-wiki v0.17.1 (August 2026 repository state)**  
OpenClaw documentation baseline reviewed: **12 August 2026**.

This package has been structurally validated in the build environment. It has not been end-to-end executed against a live OpenClaw gateway in this ChatGPT session, so run openclaw skills check after installation on the target host... mostly because i saw the upstream LLM-wiki on the way to work and got ChatGPT 5.6 Sol to help build this with ne on the train. Assume if you are reading this more than about 12 hours after the original commit that I have actually installed it and it works 😁
