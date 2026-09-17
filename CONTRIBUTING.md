# Contributing

This repository is a **public vault template**. Teach the contract. Do not paste a live fleet.

Start from a branch of `main`. Prefer the smallest change that fixes a stranger-visible defect in docs, skeleton, skills, or hygiene tests.

Operational notes under `docs/` and `vault-skeleton/` stay **Russian-primary**. This file is English so GitHub contributors can open a PR.

## Open a PR against *this* GitHub repo

```powershell
git fetch origin
git checkout -b docs/your-topic origin/main
```

Push to `samohod4ik/agents-knowledge-base` (or your fork) and open a PR targeting `main`. Merge is the owner's decision.

`gh` is appropriate **only** for this template repository. Working-repo issues stay on the consumer's `<GIT_REMOTE>`.

## Do

- Keep the Johnny Decimal map (`00_`–`70_` + `90_`). Do not add a parallel PARA tree.
- Update related docs and vault-side registry notes in the **same** PR as behavior/process changes.
- Use placeholders only: `<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, `<STACK_ROOT>`, `<GIT_REMOTE>`, `<PORT>`, `<HOST>`.
- Ship skill briefs as `SKILL.md` only. Optional local `scripts/` stay off this repository unless you are deliberately publishing a portable tool with tests.
- Run `python -m unittest discover -s tests -v` before a PR.
- Write Russian-primary operational docs; keep the root README bilingual (English + Русский).
- Exact H2 `## Related` (never `## Related Research`).
- Skill notes with frontmatter `name:`, Triggers, one Location, no hosts.
- AlwaysApply stop without a local script = checklist + audit journal. With a local `verify_projects_data.py`, stop = category `scm` clean; `errors = 0` is the journal goal.

## Do not

- Add live vault cards, real hosts, passwords, DSN, plugin `apiKey`, research `trun_*` packets, or personal PII.
- Require unpublished `doctor.py` / verify scripts as the only success path.
- Add a second verifier product named as if `verify_vault.py` were standalone.
- Point example projects at the publisher remote as if it were the consumer's forge.
- Team-canon sync, fleet inventory, or instructions to delete someone else's checkout.
- Placeholder citations `[web:N]` / `[web:12]`.
- Rewrite git history for cosmetic path cleanup unless a real credential was exposed and the owner asked for cleanup.

## Vault / skill PRs

For skeleton changes: keep create/update/archive/verify guidance on lane READMEs, fix path-wikilinks, and keep example cards marked `status: example` / `source_agent: public-template` where frontmatter is used. For skills: include when-not / workflow / do-not / success; prove the process on disk without assuming host automation.

## Before you send the PR

- [ ] `rg` the diff for hostname leftovers and plaintext `password=` / `DSN=`
- [ ] No new `skills/**/scripts/*.py`
- [ ] No `[web:` citations
- [ ] Frontmatter closed on every edited vault `.md`
- [ ] New docs linked from root `README.md` and `docs/architecture.md`
- [ ] `python -m unittest discover -s tests -v` passes
