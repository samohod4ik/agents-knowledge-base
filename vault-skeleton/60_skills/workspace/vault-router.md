---
tags: [skills, workspace, vault, cursor, multi-root]
name: vault-router
last_verified: 2026-09-09
change_source: task-6-cursor-rules-skills
---
# vault-router

## Purpose
Выбрать slug из Active Projects, ответить на кросс-вопрос из `<VAULT>`, сменить корень через `move_agent_to_root`. Не держать все репозитории в сайдбаре.

## Skill Location
- Brief шаблона: `skills/vault-router/SKILL.md`
- Установка: `<SKILLS_ROOT>/vault-router/SKILL.md`
- Scripts: `scripts/doctor.py`, `scripts/resolve_project.py`

## Triggers
move_agent_to_root, vault-router, Active Projects, какой проект открыть, мультирепо в сайдбаре.

## Related Projects
- [[10_projects/example_library/README]]
- [[10_projects/example_service/README]]

## Doctor
```powershell
python <SKILLS_ROOT>/vault-router/scripts/doctor.py
```

## Run
```powershell
python <SKILLS_ROOT>/vault-router/scripts/resolve_project.py --name <slug>
```

## Related
- [[40_patterns/fleet-memory-stack]]
- [[60_skills/workspace/session-distill]]
- [[60_skills/workspace/README]]
- [[60_skills/README]]
- [[00_profile/agent-context]]
