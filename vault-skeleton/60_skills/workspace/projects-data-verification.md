---
tags: [skills, workspace, obsidian, audit, cursor]
name: projects-data-verification
status: example
source_agent: public-template
last_verified: 2026-09-17
change_source: public-template-contract
---
# projects-data-verification

## Purpose
Read-only аудит vault `<VAULT>`: карточки, rules, реестр skills, SCM относительно `<GIT_REMOTE>`. Публичный brief без обязательных скриптов. Бывший контур `obsidian-vault-verification`.

Категории контракта: `project_quartet` (только `10_projects/`), `library_links` (точный `## Related`), `inventory` (прямые git-дети `projects_root`), `skills_registry` / `skills_index` (`name:` + имя в `60_skills/README`), `scm`. Cache JSON не SoT. AlwaysApply-успех без скрипта = чеклист + журнал; со скриптом = `scm` clean.

## Skill Location
- Brief шаблона: `skills/projects-data-verification/SKILL.md`
- Установка: `<SKILLS_ROOT>/projects-data-verification/SKILL.md`
- Scripts: опционально у оператора; в публичном дереве отсутствуют

## Triggers
проверка Obsidian, аудит vault, верификация документации, obsidian-vault-audit, projects-data-verification, projects_data_verification, целостность правил, качество хранилища, 60_skills, skill-checklist.

## Related Projects
- [[10_projects/example_library/README]]
- [[10_projects/example_service/README]]

## Run
Следуйте workflow в brief: ручной проход Active Projects, frontmatter, wikilink, SCM, реестр skills; findings → [[50_runbooks/obsidian-vault-audit]].

## Related
- [[60_skills/workspace/README]]
- [[60_skills/README]]
- [[50_runbooks/obsidian-vault-audit]]
- [[50_runbooks/skill-checklist]]
- [[50_runbooks/maintenance]]
- [[40_patterns/shared-cursor-rules]]
