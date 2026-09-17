# Contributing

This repository is a **public vault template**. Teach the contract. Do not paste a live fleet.

Operational notes under `docs/` and `vault-skeleton/` stay **Russian-primary**. This file is English so GitHub contributors can open a PR.

## Open a PR against *this* GitHub repo

```powershell
git fetch origin
git checkout -b docs/your-topic origin/main
```

Push to `samohod4ik/agents-knowledge-base` (or your fork) and open a PR targeting `main`. Merge is the owner's decision.

`gh` is appropriate **only** for this template repository. Working-repo issues stay on the consumer's `<GIT_REMOTE>`.

## Do not add

- Hostname, LAN literals, DSN, passwords, plugin `apiKey`, accounts
- Live `scripts/*.py` under `skills/` (briefs are contract-only; doctor is expected to fail until the consumer installs a local implementation)
- Team-canon sync, fleet inventory, or instructions to delete someone else's checkout
- Placeholder citations `[web:N]` / `[web:12]`
- Absolute disks of another machine
- A second verifier product named as if `verify_vault.py` were standalone

## Do keep

- Placeholders: `<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, `<STACK_ROOT>`, `<GIT_REMOTE>`, `<HOST>`
- Exact H2 `## Related` (never `## Related Research`)
- Skill notes with frontmatter `name:`, Triggers, one Location, no hosts
- AlwaysApply stop = category `scm` clean; `errors = 0` is the audit journal goal
- Closed YAML frontmatter on vault notes (`tags`, `last_verified`, `change_source`)

## Suggested commit slices

1. Rules + gate + Related
2. Skeleton structure + templates
3. Skill briefs
4. New docs + this file

## Before you send the PR

- [ ] `rg` the diff for hostname leftovers and plaintext `password=` / `DSN=`
- [ ] No new `skills/**/scripts/*.py`
- [ ] No `[web:` citations
- [ ] Frontmatter closed on every edited vault `.md`
- [ ] New docs linked from root `README.md` and `docs/architecture.md`
