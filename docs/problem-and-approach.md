# Problem and approach

An operational knowledge base is a map an agent can execute against. A note dump is a pile of text that looks complete and still leaves the next chat guessing.

This template publishes the current numbered vault (`00_` through `70_` plus `90_`), not the thinner April tree. The three source chats are packaging (`d1c207fb-9854-441f-8c16-c0be2ef6faff`), research archive (`0aac62bb-906d-43c4-830a-04136cd73ae0`), and fleet memory (`626af52f-5bbf-4146-a6dc-653f3318aa49`). Do not invent further chat IDs.

## Operational KB vs note dump

A note dump stores prose. An operational KB stores commands, absolute project paths, stack facts, and links an agent can follow in one or two searches.

| Note dump | Operational KB |
|-----------|----------------|
| Descriptive essays after the fact | Same-turn updates after code, infra, or schema change |
| Bare `[[runbook]]` and orphan pages | Path-qualified wikilinks and `## Related` both ways |
| Identical tags on every file | Contextual YAML tags plus `last_verified` / `change_source` |
| Memory hoped for in the model | Disk: vault notes, ADRs, AST graph in the git repo |
| Finished research buried in chat | Indexed runs under `70_researches/` |

If a note cannot tell an agent where the repo is, how to run it, and what not to touch, it is not operational yet.

## Why Obsidian + Cursor

Cursor is the writer and reader. Obsidian is the graph, the daily UI, and the Local REST surface.

- The vault is a Cursor workspace. Agents read markdown first, then write notes after they change code.
- Wikilinks and numbered folders give a durable map. The model does not have to rediscover hosts, stacks, or consumers each session.
- Obsidian Local REST MCP is the preferred write path when it is up. When MCP is down, write the same files on disk and say so.
- Project git remotes stay in each repo. The vault holds cards and links, not a second copy of the source tree.

The pairing is intentional: Cursor without a vault forgets; a vault without a completion gate drifts.

## How the design evolved

Do not roll the template back to the April packaging tree. That chat created `00_profile` through `50_runbooks` plus `90_archive`, root and profile `agent-context.md`, YAML frontmatter, the always-on maintenance rule, and later `requirements.md` plus `## Project Location`. It did not specify `60_skills/`, `70_researches/`, `decisions.md`, or the fleet-memory hub.

| Layer | Problem it closed | Source chat |
|-------|-------------------|-------------|
| Numbered `00`–`50` + `90` | No durable map of projects, servers, or DB | `d1c207fb` |
| Maintenance protocol + markdown standards | Docs drifted; no completion gate; inconsistent Stack / Related / H1 | `d1c207fb` |
| `requirements.md` + Project Location | Missing install surface and absolute repo path | `d1c207fb` |
| `60_skills/` registry | Skills lived only on disk; no same-turn registration | later ops; present before research chat |
| `70_researches/` + `save-research` | Deep-research runs were repeated or lost; no index or dedup | `0aac62bb` |
| `decisions.md` + `session-distill` | New chats forgot why / workaround / do-not-touch | `626af52f` (home); `0aac62bb` (do not fork under 70) |
| Fleet-memory stack (no product memory) | Temptation to add a second memory engine | `626af52f` |
| `vault-router` | Cross-project answers needed one vault truth + one active root | `626af52f` |
| Audit / verification runbooks | SCM wording, orphans, credential hygiene needed a ledger | ops after packaging |

Current numbered sections are the template canon.

## Rejected alternatives

These were considered and rejected. The template must not reintroduce them.

**Mem0 / Antigravity Memory / agy-memory / a second memory SQLite.** Cursor has no automatic memory between agents. Extra product memory is a second engine on top of markdown. Instant Grep is search, not experience. Decision: three disk layers (AST graph in the repo, ADRs in the vault, one router + one root). Chat `626af52f`.

**Flat `70_researches/raw/` + `70_researches/structured/` + a single INDEX.** That was the user-proposed tree. After structure research it lost ops, registry, evergreen, and navigation. Canon is Johnny Decimal categories 70–75 *inside* `70_researches/`. Chat `0aac62bb`.

**Dumping or embedding all chats.** Completeness is every known research run in the registry and SOURCES, not hundreds of chat transcripts. Most chats are not unique research. Chat `0aac62bb`.

**PARA as a second folder tree.** PARA statuses are metadata on a run (`research_status`, `fresh_until`, `superseded_by`). Finished runs do not move to `90_archive/`. Moving folders to express lifecycle was rejected. Chat `0aac62bb`.

Also rejected, and still out of scope:

- Identical YAML tags on every note (`d1c207fb`).
- A second `decisions` tree under `70_researches/` (`0aac62bb`).
- Graphify as semantic memory, LLM labels, or `export obsidian` into `10_projects/` (`626af52f`).
- Folders plus a long `alwaysApply` rule as the only research process (`0aac62bb`).
- Treating a research `poll` as discovery (`0aac62bb`).

## What this template ships

Conceptual docs in `docs/`, an anonymized `vault-skeleton/`, two example project cards (`example_library`, `example_service`), adapted Cursor rules, and four vault-ops skill briefs. It does not ship internal runbooks, live hosts, or credentials.

Team git hosting may be self-hosted Forgejo. This repository is a public GitHub distribution channel. Those are different remotes; see [cursor-integration.md](cursor-integration.md).
