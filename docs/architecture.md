# Architecture

The live vault has no `80_*` folder. The public skeleton follows the same map: `00_` through `70_` plus `90_`. Do not add a parallel PARA tree or flatten research into `raw/` and `structured/`.

## Numbered sections

| Section | Role |
|---------|------|
| `00_profile/` | Operator profile, tech stack, English agent hub |
| `10_projects/` | Per-slug README, architecture, runbook, requirements, often `decisions.md` |
| `20_infra/` | Servers, networks, access matrix (masked), Cursor MCP catalog |
| `30_db/` | Connections with masked secrets, schemas, important queries |
| `40_patterns/` | Coding and git patterns, fleet-memory stack, shared Cursor-rules pattern |
| `50_runbooks/` | Maintenance, audit, skills guides, deploy and incident |
| `60_skills/` | Registry of *local* Cursor project skills (not default Cursor skills) |
| `70_researches/` | Johnny Decimal research archive (ops / runs / evergreen / MOCs) |
| `90_archive/` | Deprecated notes |
| `.cursor/rules/` | Vault maintenance protocol + markdown standards |

Root files the agent should expect: `README.md` (sections + Active Projects) and `agent-context.md` (short operating rules).

Project cards use the quartet plus decisions. Do not model a card on a stub that lacks architecture, runbook, and requirements. In this template the examples are `example_library` and `example_service`.

## Agent read-first order

1. `README.md` — numbered sections and Active Projects.
2. Root `agent-context.md` — short local rules.
3. `00_profile/agent-context.md` — operating hub (memory stance, update rules).
4. `00_profile/developer-profile.md` and `00_profile/tech-stack.md`.
5. By task:
   - skills: `60_skills/README.md`
   - memory: `40_patterns/fleet-memory-stack.md`
   - shared rules pattern: `40_patterns/rr77-cursor-rules.md` (generic shared-rules note in the skeleton)
   - process: `50_runbooks/maintenance.md`
   - MCP catalog: `20_infra/cursor-mcp.md`

Memory stance at the hub: Graphify AST + `decisions.md` + vault-router. No Mem0 or Antigravity. Deep research goes to `70_researches/` via `save-research`.

## Note conventions

### Frontmatter

On every meaningful edit:

- Contextual `tags` (not the same list on every note)
- `last_verified: YYYY-MM-DD`
- `change_source` (commit, ticket, incident, or task name)
- Closing `---` so YAML stays valid

### Headings

| Doc type | H1 |
|----------|-----|
| README | `# {project}` |
| architecture | `# {project} — architecture` |
| runbook | `# {project} — runbook` |
| requirements | `# {project} — requirements` |
| skill index | `# {owner} — skills` |
| skill note | `# {skill-name}` |

Project README files also need `## Project Location` (absolute repo path), normalized `## Stack`, and a link to `requirements.md`.

`## Stack` order: Python version, DB type/version or contour, Selenium yes/no, core libraries.

### Wikilinks and Related

- Path-qualified only: `[[10_projects/<project>/runbook]]`, never bare `[[runbook]]`.
- `## Related` on both ends for project, infra, DB, and runbook links.
- No self-links in `## Related`.
- Profile hub notes should link to every Active Project README.
- Skill notes live at `60_skills/<owner>/<skill-name>.md`. Owner is a project slug or `workspace`.

Prefer operational sections (Purpose, Run, Risks, Incident, Related) over essays. Commands and paths must be real for *your* machine; use `<PROJECT_ROOT>`, `<VAULT>`, `<SKILLS_ROOT>`, and `<GIT_REMOTE>` until you fill them.

## Vault vs git repos

| Artifact | Lives where | Why |
|----------|-------------|-----|
| Project cards, infra, DB, runbooks, skills index | Vault | Agent map and same-turn docs |
| Source code | Each project git repo | The vault is not a second clone |
| AST graph `graphify-out/graph.json` | Project repo, gitignored | Thousands of nodes; not vault notes |
| Human graph map `GRAPH_REPORT.md` | Project repo, committed | Reviewable structural map |
| ADRs / do-not-touch | Vault `10_projects/<slug>/decisions.md` | Session memory on disk |
| Deep-research packages | Vault `70_researches/` | Outside the fleet-memory stack |
| Cursor project rules copies | Project `.cursor/rules/` | Shared team pattern; vault holds the explanation |
| Local REST `apiKey` / plugin private key | Obsidian plugin data (ignored) | Never commit |

Graphify extract is structural only (`--code-only`, no LLM labels). Do not `export obsidian` a code graph into `10_projects/`. Do not treat Graphify as semantic memory.

## Research archive shape

Johnny Decimal ids `70.xx` exist only inside `70_researches/`:

| Area | Role |
|------|------|
| `70_research_ops/` | INDEX, run registry, policy, templates, inbox, LOG, SOURCES |
| `71_runs/` | Write-once raw packages + rebuildable summaries |
| `72_knowledge/` | Evergreen notes |
| `73_mocs/`, `74_exports/`, `75_lifecycle/` | Navigation and lifecycle views |

Policy facts the architecture depends on:

- `save-research` is the only allowed deep-research launcher.
- Dedup key is scope + question + project-or-problem. No date in the key.
- Completed runs stay put. Change status fields; do not move them to `90_archive/`.
- ADR stays in `10_projects/<slug>/decisions.md`. Do not create a decisions fork under `70_`.
- The template ships empty registry/templates, not live `trun_*` packages.

## What is not in this public tree

- Operational `10_projects/*` runbooks from the originating vault
- Access-matrix passwords, plugin `apiKey`, DSN, tokens
- Production LAN addresses and internal account names
- Host-bound skills (deploy-to-internal-host, SSH-to-lab, org report generators)
- Raw research packages under `71_runs/`

Fill placeholders. Point `<GIT_REMOTE>` at *your* canonical host. This GitHub repo is the template channel, not a substitute for a team Forgejo (or other) remote.
