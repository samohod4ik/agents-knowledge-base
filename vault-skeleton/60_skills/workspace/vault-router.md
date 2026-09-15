---
tags: [skills, workspace, vault, cursor, multi-root]
name: vault-router
status: example
source_agent: public-template
last_verified: 2026-09-16
change_source: public-obsidian-polish
---
# vault-router

## Purpose
Выбрать slug из Active Projects, ответить на кросс-вопрос из `<VAULT>`, сменить корень через `move_agent_to_root`. Не держать все репозитории в сайдбаре.

## Skill Location
- Brief шаблона: `skills/vault-router/SKILL.md`
- Установка: `<SKILLS_ROOT>/vault-router/SKILL.md`
- Scripts: опционально у оператора; в публичном дереве отсутствуют

## Triggers
move_agent_to_root, vault-router, Active Projects, какой проект открыть, мультирепо в сайдбаре.

## Related Projects
- [[10_projects/example_library/README]]
- [[10_projects/example_service/README]]

## Run
Прочитайте Active Projects и карточку slug, затем один `move_agent_to_root` при необходимости. См. brief.

## Related
- [[40_patterns/fleet-memory-stack]]
- [[60_skills/workspace/session-distill]]
- [[60_skills/workspace/README]]
- [[60_skills/README]]
- [[00_profile/agent-context]]
