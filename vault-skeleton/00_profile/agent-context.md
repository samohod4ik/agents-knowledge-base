---
tags:
  - profile
  - agent
  - cursor
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Agent Context

## Role

- Operator of this vault: developer and/or sysadmin on *your* machines.
- Keep notes executable: commands, `<PROJECT_ROOT>/<slug>`, stack facts, path-qualified links.

## Active Domains

Replace these buckets with your work. Do not paste another team's project slugs.

- **Libraries** — shared clients used by more than one repo.
- **Services** — HTTP/worker apps with a runbook and config surface.
- **Automation / data** — batch jobs, browser flows, scheduled exports.

When example cards exist, link their README from here and from [[00_profile/developer-profile]]. Until then keep Active Projects empty rather than inventing hosts.

## Operating Rules

- Keep documentation operational, not descriptive-only.
- After a code, infra, or schema change, update related notes in `10_projects`, `20_infra`, `30_db` in the same turn.
- Agent memory is three disk layers ([[40_patterns/fleet-memory-stack]]): AST graph via `graphify-maintain`, ADRs in `10_projects/<slug>/decisions.md` (`session-distill`), vault first then one root (`vault-router`).
- Do not install Mem0, Antigravity Memory, or a second memory database. Graphify is `--code-only` AST. Do not `export obsidian` into `10_projects/`.
- Deep-research reports go to `70_researches/` via `save-research`, not into `decisions.md`.
- Use path-qualified wikilinks: `[[10_projects/<slug>/runbook]]`, not bare `[[runbook]]`.

## Working Standards

- Russian docstring style (reST) for Python.
- Prefer explicit service boundaries and dedicated runbooks.
- Keep SQL in `./sql/` and tests in `./tests/`.

## SCM

- Canonical remote for *your* working repos: `<GIT_REMOTE>`.
- This public template ships on GitHub. That channel is not a substitute for your team host.
- Local git on disk is separate from the hosting API. See [[20_infra/cursor-mcp]].

## Related

- [[00_profile/developer-profile]]
- [[00_profile/tech-stack]]
- [[20_infra/cursor-mcp]]
- [[40_patterns/coding-style]]
- [[50_runbooks/maintenance]]
- [[40_patterns/fleet-memory-stack]]
