# Contributing

Start from a branch of `main`. Prefer the smallest change that fixes a stranger-visible defect in docs, skeleton, skills, or hygiene tests.

## Do

- Keep the Johnny Decimal map (`00_`–`70_` + `90_`). Do not add a parallel PARA tree.
- Update related docs and vault-side registry notes in the **same** PR as behavior/process changes.
- Use placeholders only: `<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, `<GIT_REMOTE>`, `<PORT>`, `<HOST>`.
- Ship skill briefs as `SKILL.md` only. Optional local `scripts/` stay off this repository unless you are deliberately publishing a portable tool with tests.
- Run `python -m unittest discover -s tests -v` before a PR.
- Write Russian-primary operational docs; keep the root README bilingual (English + Русский).

## Do not

- Add live vault cards, real hosts, passwords, research `trun_*` packets, or personal PII.
- Require unpublished `doctor.py` / verify scripts as the only success path.
- Point example projects at the publisher remote as if it were the consumer's forge.
- Rewrite git history for cosmetic path cleanup unless a real credential was exposed and the owner asked for cleanup.

## Vault / skill PRs

For skeleton changes: keep create/update/archive/verify guidance on lane READMEs, fix path-wikilinks, and keep example cards marked `status: example` / `source_agent: public-template` where frontmatter is used. For skills: include when-not / workflow / do-not / success; prove the process on disk without assuming host automation.
