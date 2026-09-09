---
tags: [skills, workspace, research, cursor]
name: save-research
last_verified: 2026-09-09
change_source: task-6-cursor-rules-skills
---
# save-research

## Purpose
Единственный launcher Parallel / локального deep research. Пишет run-пакеты в `<VAULT>/70_researches`. Не `decisions.md`.

## Skill Location
- Brief шаблона: `skills/save-research/SKILL.md`
- Установка: `<SKILLS_ROOT>/save-research/SKILL.md`
- Vault: эта заметка — указатель, не третья реализация
- Scripts: `scripts/doctor.py`, `scripts/preflight.py`, `scripts/save_one.py`, `scripts/ingest_from_chats.py`

## Triggers
parallel deep research, `trun_*`, sweep research inbox, save-research

## Related Projects
- [[10_projects/example_library/README]]
- [[10_projects/example_service/README]]

## Doctor
```powershell
python <SKILLS_ROOT>/save-research/scripts/doctor.py
```

## Run
```powershell
python <SKILLS_ROOT>/save-research/scripts/save_one.py run --scope <scope> --question "..."
python <SKILLS_ROOT>/save-research/scripts/ingest_from_chats.py --sweep-only
python <SKILLS_ROOT>/save-research/scripts/save_one.py sync-inbox
```

## Related
- [[70_researches/70_research_ops/70.01_INDEX]]
- [[70_researches/70_research_ops/70.03_RESEARCH-POLICY]]
- [[60_skills/workspace/session-distill]]
- [[60_skills/workspace/README]]
- [[60_skills/README]]
- [[50_runbooks/maintenance]]
