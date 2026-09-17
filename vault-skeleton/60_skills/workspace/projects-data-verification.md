---
tags: [skills, workspace, obsidian, audit, cursor]
name: projects-data-verification
last_verified: 2026-09-17
change_source: public-template-contract
---
# projects-data-verification

## Purpose
Read-only аудит vault `<VAULT>` и локальных проектов. Brief шаблона — контракт: `scripts/` в репозитории шаблона нет; doctor падает, пока нет локальной реализации. Скрипты не правят vault. Бывший контур `obsidian-vault-verification`.

Категории контракта: `project_quartet` (только `10_projects/`), `library_links` (точный `## Related`), `inventory` (прямые git-дети `projects_root`), `skills_registry` / `skills_index` (`name:` + имя в `60_skills/README`), `scm`. Cache JSON не SoT. AlwaysApply-успех = `scm` clean; `errors = 0` — журнал.

## Skill Location
- Brief шаблона: `skills/projects-data-verification/SKILL.md`
- Установка: `<SKILLS_ROOT>/projects-data-verification/SKILL.md`
- Scripts: `scripts/doctor.py`, `scripts/verify_projects_data.py`

## Triggers
проверка Obsidian, аудит vault, верификация документации, obsidian-vault-audit, projects-data-verification, projects_data_verification, целостность правил, качество хранилища, 60_skills, skill-checklist.

## Related Projects
- [[10_projects/example_library/README]]
- [[10_projects/example_service/README]]

## Doctor
```powershell
python <SKILLS_ROOT>/projects-data-verification/scripts/doctor.py
```

## Run
```powershell
python <SKILLS_ROOT>/projects-data-verification/scripts/verify_projects_data.py `
  --output <SKILLS_ROOT>/projects-data-verification/cache/verify_report.json
```

Не подменяйте верификатор одиночным `verify_vault.py`.

## Related
- [[60_skills/workspace/README]]
- [[60_skills/README]]
- [[50_runbooks/obsidian-vault-audit]]
- [[50_runbooks/skill-checklist]]
- [[50_runbooks/maintenance]]
- [[40_patterns/shared-cursor-rules]]
