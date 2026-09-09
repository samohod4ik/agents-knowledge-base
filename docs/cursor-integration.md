# Cursor integration

Wire Cursor to the vault so agents read the map first and update notes before they stop. This file is the installer view. Conceptual why lives in [problem-and-approach.md](problem-and-approach.md).

## Copy vault rules

The skeleton ships two rules under `vault-skeleton/.cursor/rules/`:

| File | Apply |
|------|--------|
| `obsidian-vault-maintenance-protocol.mdc` | `alwaysApply: true` |
| `obsidian-vault-markdown-standards.mdc` | `globs: "**/*.md"` |

Steps:

1. Open `vault-skeleton` (or your copy) as an Obsidian vault *and* as a Cursor folder.
2. Keep those two files at `<VAULT>/.cursor/rules/`.
3. Optional: copy the same pair into a project repo if that repo's agents also edit the vault. Shared team rule packs belong in the project `.cursor/rules/<team>/` tree; personal rules stay beside them, not inside the shared pack.
4. Restart or reopen the Cursor window so the rules load. Confirm both files appear under Project Rules.

Adapted template rules keep update mapping, frontmatter, H1 table, and the completion gate. They do **not** hard-code an internal Forgejo URL. Write your own `<GIT_REMOTE>`.

A `docs-before-commit` reminder, if you add one later, only nags. It does not write notes and does not fail the commit.

## Install the four skill briefs

This repo ships briefs in `skills/`. They are procedures, not a dump of internal host automation.

| Brief | Install as | When |
|-------|------------|------|
| `skills/projects-data-verification/` | vault audit / rules integrity | Before you claim docs are done |
| `skills/vault-router/` | cross-project question, crowded sidebar | Before opening a second root |
| `skills/session-distill/` | durable why / workaround / do-not-touch | After a semantic session, before commit |
| `skills/save-research/` | Parallel or local deep research | Only launcher into `70_researches/` |

Install:

1. Copy each folder to `<SKILLS_ROOT>/<skill-name>/` so `SKILL.md` sits at that path. `<SKILLS_ROOT>` is your user skills directory or a project `.cursor/skills/` directory.
2. Point paths inside the brief at `<VAULT>` and `<SKILLS_ROOT>`. Do not paste another team's absolute disks.
3. Run that skill's `scripts/doctor.py` when the brief includes one. Doctor first; then the workflow.
4. Register a pointer note at `60_skills/workspace/<skill-name>.md` and link it from `60_skills/README.md` in the same turn.

Do not install Mem0, Antigravity Memory, or a second memory MCP as a substitute for these four. Do not ship credentialed skills (internal SSH, deploy-to-named-host, org-only reports) as part of this template.

## Obsidian Local REST MCP

Preferred write path: Obsidian **Local REST API** community plugin, then a Cursor MCP server that talks to that HTTP API. Prefer this over a generic filesystem MCP for vault edits.

High-level setup (no secrets in git):

1. In Obsidian, enable Community plugins and install Local REST API.
2. Note the listen port from the plugin settings. Leave the API key in the plugin UI.
3. In Cursor MCP config (user-level), add an Obsidian vault server whose URL is `http://127.0.0.1:<PORT>` and whose auth header uses the plugin key from your local secret store.
4. Point the server at this vault path (`<VAULT>`). Tool names typically include list/get/write/patch/search on notes.
5. Never commit `.obsidian/plugins/obsidian-local-rest-api/data.json`. That file holds `apiKey` and key material. This repo's `.gitignore` already excludes it.

If the MCP server is red or the REST port is wrong, write markdown on disk and say that MCP was skipped. A green MCP toggle is not proof the REST port matches.

Do not put the API key, Bearer tokens, or plugin private keys in vault notes or in this repository.

## Pre-completion checklist

Copy this into your maintenance runbook. A task is unfinished while any box that applies is unchecked.

- [ ] YAML frontmatter closed (`---` / tags / `last_verified` / `change_source` / `---`).
- [ ] `## Stack` has Python, DB, Selenium (yes/no), and core libs on project cards.
- [ ] Wikilinks are path-qualified: `[[10_projects/example_library/runbook]]`, not `[[runbook]]`.
- [ ] No self-links in `## Related`.
- [ ] Git remotes in notes match *your* `<GIT_REMOTE>`; no leftover internal host URLs.
- [ ] Secrets are masked. Infra points at `20_infra/access-matrix` rows with `***` or `secret_ref`, never a second plaintext copy.
- [ ] Profile hub (`00_profile/tech-stack`, `00_profile/developer-profile`) still matches Active Projects.
- [ ] New or changed Cursor skills are registered in `60_skills/README.md`.
- [ ] Optional: `python <SKILLS_ROOT>/projects-data-verification/scripts/verify_projects_data.py` — `summary.errors = 0` including category `scm`.

## Git hosting: GitHub template vs team Forgejo

| Channel | Role |
|---------|------|
| This GitHub repository | Public distribution of the *template* |
| Team self-hosted Forgejo (or your chosen host) | Canonical remotes for *your* working repos |

The originating team vault documents Forgejo as the only git hosting for operational notes. That policy is local to that team. This template's publishing remote is GitHub. Do not point cloned example projects at the publisher's GitHub unless you intend to fork the template itself.

When you fill the skeleton:

- Set `<GIT_REMOTE>` to your real clone URL.
- Keep `gh` (if you use it) aimed at GitHub.com for this template only.
- Keep team issue/PR tools aimed at your Forgejo or other internal host. Do not treat GitHub as the internal forge.

No account passwords, LAN literals, or plugin keys belong in either channel's markdown.
