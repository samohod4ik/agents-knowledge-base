---
tags: [skills, index, cursor, entrypoint]
last_verified: 2026-09-17
change_source: public-template-contract
---
# Cursor Skills

Реестр **локальных project skills** (не дефолтные Cursor/plugin skills). Каждый skill — регламент для агента: когда вызывать, doctor, workflow, fallback.

Источник brief в этом шаблоне — каталог `skills/` корня репозитория. После установки копия живёт в `<SKILLS_ROOT>/<skill-name>/SKILL.md`.

## Лейны реестра

| Лейн | Действие |
|------|----------|
| create | `SKILL.md` в `<SKILLS_ROOT>/<name>/` → заметка из [[60_skills/_templates/skill-note]] → строка в этом README → `## Cursor Skills` в README проекта |
| update | Тот же ход: brief + заметка + индекс. `last_verified` / `change_source` |
| archive | Убрать из индекса и `## Cursor Skills`. Заметку перенести в `90_archive/` или пометить `archived` |
| verify | `name:` в frontmatter совпадает со stem файла; имя есть в этом README; нет orphan (`skills_registry` / `skills_index`) |

## Как создавать новый skill
1. Взять brief из `skills/<skill-name>/` этого репозитория или создать `<SKILLS_ROOT>/<skill-name>/SKILL.md`.
2. Пройти [[50_runbooks/skill-checklist]].
3. **Обязательно** добавить заметку в `60_skills/<owner>/<skill-name>.md` из [[60_skills/_templates/skill-note]] (`name:`, Triggers, один Location, без хостов).
4. Обновить `## Cursor Skills` и точный `## Related` в README связанных проектов (`10_projects/*`).

`## Run` в заметке vault — только если это контракт *установленных* скриптов, не копия чужого `SKILL.md`.

Не публикуйте в шаблоне skills с учётными данными или привязкой к одному внутреннему хосту (deploy на именованный хост, лабораторный SSH, генераторы орг-отчётов).

## Реестр по владельцу

| Владелец | Skills |
|----------|--------|
| [[60_skills/workspace/README\|workspace (multi-project)]] | [[60_skills/workspace/projects-data-verification\|projects-data-verification]], [[60_skills/workspace/vault-router\|vault-router]], [[60_skills/workspace/session-distill\|session-distill]], [[60_skills/workspace/save-research\|save-research]] |

Только эти четыре brief входят в шаблон. Owner — slug проекта или `workspace`.

## Policy
- Источник истины поведения — `SKILL.md` в `skills/<skill-name>/` (или установленная копия в `<SKILLS_ROOT>`). Obsidian — operational index + связи.
- Не дублировать полный текст skill в vault; хранить purpose, location, triggers, related projects.
- При изменении skill обновлять заметку в `60_skills/` в том же ходе.
- Personal skills регистрируйте в vault только если это operational skill команды и в тексте нет секретов.

## Related
- [[60_skills/workspace/README]]
- [[50_runbooks/skills-for-cursor]]
- [[50_runbooks/skill-checklist]]
- [[50_runbooks/maintenance]]
- [[40_patterns/fleet-memory-stack]]
