---
tags: [skills, workspace, research, cursor]
name: save-research
status: example
source_agent: public-template
last_verified: 2026-09-16
change_source: public-obsidian-polish
---
# save-research

## Purpose
Единственный launcher Parallel / локального deep research. Пишет run-пакеты в `<VAULT>/70_researches`. Не `decisions.md`.

## Skill Location
- Brief шаблона: `skills/save-research/SKILL.md`
- Установка: `<SKILLS_ROOT>/save-research/SKILL.md`
- Vault: эта заметка — указатель, не третья реализация
- Scripts: опционально у оператора; в публичном дереве отсутствуют

## Triggers
parallel deep research, `trun_*`, sweep research inbox, save-research

## Related Projects
- [[10_projects/example_library/README]]
- [[10_projects/example_service/README]]

## Run
Preflight по registry/policy → запуск провайдера только через этот skill → запись в `71_runs/` + обновление registry. См. brief.

## Related
- [[70_researches/70_research_ops/70.01_INDEX]]
- [[70_researches/70_research_ops/70.03_RESEARCH-POLICY]]
- [[60_skills/workspace/session-distill]]
- [[60_skills/workspace/README]]
- [[60_skills/README]]
- [[50_runbooks/maintenance]]
