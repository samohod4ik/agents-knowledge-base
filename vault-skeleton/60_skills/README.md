---
tags: [skills, index, cursor, entrypoint]
last_verified: 2026-09-09
change_source: task-6-cursor-rules-skills
---
# Cursor Skills

Реестр **локальных project skills** (не дефолтные Cursor/plugin skills). Каждый skill — регламент: когда / не когда, workflow на диске, fallback, успех.

Источник brief в этом шаблоне — каталог `skills/` корня репозитория. После установки копия живёт в `<SKILLS_ROOT>/<skill-name>/SKILL.md`. Скрипты в публичном дереве не обязательны.

## Create / update / archive / verify

- **Create:** brief → `SKILL.md` в `<SKILLS_ROOT>` → заметка `60_skills/<owner>/<skill-name>.md` → строка в этой таблице → Related в проектах.
- **Update:** правьте brief и vault-указатель в том же ходе; докажите discovery вызовом.
- **Archive:** снимите из Active registry, оставьте forward-link; не оставляйте триггеры на мёртвый skill.
- **Verify:** [[50_runbooks/skill-checklist]]; файл на диске ≠ работает.

Не публикуйте в шаблоне skills с учётными данными или привязкой к одному внутреннему хосту.

## Реестр по владельцу

| Владелец | Skills |
|----------|--------|
| [[60_skills/workspace/README\|workspace (multi-project)]] | [[60_skills/workspace/projects-data-verification\|projects-data-verification]], [[60_skills/workspace/vault-router\|vault-router]], [[60_skills/workspace/session-distill\|session-distill]], [[60_skills/workspace/save-research\|save-research]] |

Только эти четыре brief входят в шаблон. Owner — slug проекта или `workspace`.

## Policy
- Источник истины поведения — `SKILL.md` (brief). Obsidian — operational index + связи.
- Не дублировать полный текст skill в vault; хранить purpose, location, triggers, related projects.
- При изменении skill обновлять заметку в `60_skills/` в том же ходе.
- Personal skills регистрируйте в vault только если это operational skill команды и в тексте нет секретов.

## Related
- [[60_skills/workspace/README]]
- [[50_runbooks/skills-for-cursor]]
- [[50_runbooks/skill-checklist]]
- [[50_runbooks/maintenance]]
- [[40_patterns/fleet-memory-stack]]
