# AGENTS.md — repository rules (template tree)

These rules apply when editing **this** public repository, not someone's live vault copy.

## Map

- Product entry: `README.md` (bilingual)
- Conceptual docs: `docs/`
- Portable skill briefs: `skills/<name>/SKILL.md`
- Anonymized Obsidian vault: `vault-skeleton/` (Johnny Decimal `00_`–`70_` + `90_`, no `80_*`)
- Cursor rules ship inside `vault-skeleton/.cursor/rules/`

## Placeholders

Use only: `<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, `<GIT_REMOTE>`, `<PORT>`, `<HOST>`. Never hardcode publisher host disks or personal user profile paths.

## Do

1. Keep docs honest: this repo is an Obsidian + Cursor operational vault template only.
2. Same-turn updates: if you change a process, update README / docs / registry notes together.
3. Skills are brief-only in git; local scripts are optional and operator-owned.
4. Run hygiene tests under `tests/` before claiming the tree is public-safe.

## Don't

- Secrets, `.env`, Local REST `data.json`
- Private chat UUIDs or personal contact dumps
- Silent overwrite of conflicting notes in examples
- Recreate a second folder taxonomy beside Johnny Decimal
