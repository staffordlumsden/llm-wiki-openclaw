# Archive and restore workflow

Archiving is **quiet preservation**, not deletion.

## Archive a topic

For a hub-owned topic `<slug>`:

1. resolve HUB and verify the active topic path;
2. ensure no ambiguous duplicate/archive target exists;
3. move the topic directory to `HUB/topics/.archive/<slug>/`;
4. update `wikis.json` to `path: topics/.archive/<slug>` and `status: archived`;
5. rebuild the hub index from registry/filesystem truth;
6. append the reason and result to hub/topic logs where the existing convention permits.

Normal query, compile, research, collect, output and maintenance routes must ignore archived content unless the user explicitly includes it.

## Restore

Restore to `HUB/topics/<slug>/`, update the registry to active state, rebuild derived indexes and log the operation. If an active topic already occupies the slug, do not overwrite it; surface the conflict.

## List archived

Read registry/archive indexes only. Do not load full archived content merely to list it.

## Individual content

Do not use whole-topic archive semantics as a substitute for source retraction or article deletion. Raw evidence remains immutable; incorrect or sensitive content requires the appropriate explicit retraction/removal workflow.
