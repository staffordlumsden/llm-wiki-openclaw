# Hub and wiki resolution

Resolve the target before reading broadly or writing anything.

## HUB resolution

1. Try `~/.config/llm-wiki/config.json` if it is readable in the active OpenClaw filesystem boundary.
2. Prefer `hub_path`. Expand **only a leading `~`** to the current user's home; do not rewrite tildes embedded in path components such as `com~apple~CloudDocs`.
3. Treat `resolved_path` as a legacy fallback, not a canonical machine-independent value.
4. If there is no usable config, try `~/wiki` only when it contains a plausible llm-wiki marker such as `_index.md`, `wikis.json`, or `topics/`.
5. If path existence is plausible but OpenClaw cannot read it, report an access/sandbox issue. Do not silently select another hub.

Canonical portable config shape:

```json
{
  "hub_path": "~/wiki"
}
```

## Active wiki resolution

Order:

1. explicit local mode → `<cwd>/.wiki/`;
2. explicit named wiki → resolve from `HUB/wikis.json`, falling back to `HUB/topics/<name>` only when the registry path is stale;
3. current project already contains `.wiki/` → use it;
4. otherwise use HUB for hub-level operations or choose one topic wiki for semantic content work.

Topic wikis normally live at `HUB/topics/<slug>/`.

Registry paths owned by the hub should preferably be portable relative paths such as `topics/<slug>` rather than machine-specific absolute paths.

## Ambiguity

Do not search every topic just to infer intent. Read hub indexes/registry metadata. If two or three topics remain plausible, present no more than three candidates and ask for the selection when the distinction materially changes the result.

## Archive

Archived topics live under `HUB/topics/.archive/<slug>/` and should be marked archived in the registry. Exclude them from normal routing.
