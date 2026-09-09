# Killer features

These are the mechanisms that keep the vault operational. Without them the numbered folders become a note dump again.

## Maintenance protocol

Always-on Cursor rule (`obsidian-vault-maintenance-protocol.mdc`). Treat the vault as an operational KB. After a meaningful code, infra, schema, or process change, update the mapped notes in the same turn.

| Change | Update |
|--------|--------|
| Project logic / runtime | `10_projects/<project>/{README,architecture,runbook}.md` |
| Dependencies | `10_projects/<project>/requirements.md` |
| Infra / access / host / network | `20_infra/**` |
| Schema / query / connection | `30_db/**` |
| Process or policy | `40_patterns/**` and `50_runbooks/**` |
| Profile / stack | `00_profile/{agent-context,developer-profile,tech-stack}.md` |
| New or changed local skill | `60_skills/<owner>/<skill-name>.md` and related project README |

Durable session decisions go to `10_projects/<project>/decisions.md` (`session-distill`). Deep-research reports go to `70_researches/` (`save-research`). After a semantic code change, refresh the repo AST graph (`graphify-maintain`) in that git repo, not in the vault.

Prefer the Obsidian MCP write tools when they are available. If MCP is down, edit files on disk and say so.

Completion gate: stale mapped notes mean the task is not finished. Run the [pre-completion checklist](cursor-integration.md#pre-completion-checklist) before you stop.

## Markdown standards

Second rule (`obsidian-vault-markdown-standards.mdc`), scoped to `**/*.md`.

- Operational sections; executable commands; no fake `[web:N]` citations.
- Skills registry path `60_skills/<owner>/<skill-name>.md`. After you create `SKILL.md` on disk, register the vault note in the same turn.
- Frontmatter: `tags`, `last_verified`, `change_source`.
- Path-qualified wikilinks; no self-links in `## Related`.
- Project `## Related` includes README plus the other three core docs where they exist.
- Stack line: `Python: X.Y` then `DB: ...` then `Selenium: yes/no` then `Core libs: ...`.
- `## Project Location` is an absolute path, written as `<PROJECT_ROOT>/<slug>` until you clone the repo.

In the originating team vault, SCM wording is Forgejo-only. In this public template, document *your* canonical remote. Do not copy internal host URLs into notes.

## Skills registry

`60_skills/` is an index of local project skills, not a paste of default Cursor or plugin skills.

- Source of truth for behavior is `SKILL.md` next to scripts. The vault note stores purpose, location, triggers, and links.
- Owner is a project slug or `workspace` for cross-project skills.
- Creating a skill without a vault note is how agents lose the trigger next week.

Template-safe briefs shipped in `skills/`:

| Skill | Job |
|-------|-----|
| `projects-data-verification` | Read-only audit of vault + rules quality |
| `vault-router` | Pick an Active Project slug; one `move_agent_to_root` |
| `session-distill` | Write ADRs to `10_projects/<slug>/decisions.md` |
| `save-research` | Only allowed deep-research launcher into `70_researches/` |

`graphify-maintain` is pattern-safe (AST in the *repo*) but host-bound paths must be stripped before you copy a local implementation. Do not publish credentialed or org-only skills into this template.

A skill is a process layer: when to call MCP or CLI, doctor first, fallback, success criteria. MCP and CLI are the hands. The skill is the procedure.

## Research archive

`70_researches/` stops Parallel (and local) deep-research from helping once and vanishing.

- Registry is the dedup source of truth.
- Raw run packages are write-once. Summaries and evergreen notes are editable.
- Inbox is a landing zone after sync, not a second archive.
- Offline staging happens *outside* the vault first, then sync.
- Completeness = known runs in registry/SOURCES, not a dump of every agent chat.

Rejected shapes are listed in [problem-and-approach.md](problem-and-approach.md). The feature is the Johnny Decimal ops/runs/knowledge/MOC split plus a single launcher skill.

## Fleet-memory stack

Cursor does not keep automatic memory between agents. Do not install Mem0, Antigravity Memory, agy-memory, or a second memory database.

Three disk layers:

| Layer | Stores | Where | Skill |
|-------|--------|-------|-------|
| AST graph | Who-imports-whom, files, calls | `<repo>/graphify-out/` | `graphify-maintain` |
| Session ADR | Durable why / bans / workarounds | Vault `10_projects/<slug>/decisions.md` | `session-distill` |
| Router | Which slug, which one root | Vault + one `move_agent_to_root` | `vault-router` |

Deep-research is not this stack. KPI/passport fact tables are not this stack. Do not export Graphify into Obsidian project folders. Commit `GRAPH_REPORT.md`; leave `graph.json` gitignored.

Shared team Cursor rules (the `rr77-cursor-rules` pattern) are copies inside each project `.cursor/rules/`. A `docs-before-commit` hook, if you adopt one, only *reminds*. It does not write documentation, does not run Graphify, and does not block git.

## Audit and verification

Quality gaps need a ledger, not a one-off cleanup.

- `50_runbooks/obsidian-vault-audit.md` records audit passes and remaining gaps.
- `projects-data-verification` is audit-only: no auto-fix flag. It checks frontmatter, path-qualified links, skill registration, SCM wording, and related inventory.
- Optional command (after you install the brief and scripts):

```powershell
python <SKILLS_ROOT>/projects-data-verification/scripts/verify_projects_data.py
```

Expect `summary.errors = 0`, including the SCM category, before you call a maintenance task done.

Do not store plaintext passwords in infra notes. `30_db` masks secrets. Access-matrix rows in the skeleton use `***` or `secret_ref: vault://...`, never live values. The originating vault's credential exceptions are not part of this template.
