---
tags: [skills, index, cursor, entrypoint]
last_verified: 2026-09-17
change_source: public-template-contract
---
# Cursor Skills

Реестр **локальных project skills** (не дефолтные Cursor/plugin skills). Каждый skill — регламент: когда / не когда, workflow на диске, fallback, успех.

Источник brief в этом шаблоне — каталог `skills/` корня репозитория. После установки копия живёт в `<SKILLS_ROOT>/<skill-name>/SKILL.md`. Скрипты в публичном дереве не обязательны.

## Create / update / archive / verify

| Лейн | Действие |
|------|----------|
| create | `SKILL.md` в `<SKILLS_ROOT>/<name>/` → заметка из [[60_skills/_templates/skill-note]] → строка в этом README → `## Cursor Skills` в README проекта |
| update | Тот же ход: brief + заметка + индекс. `last_verified` / `change_source`. Докажите discovery вызовом |
| archive | Убрать из индекса и `## Cursor Skills`. Заметку перенести в `90_archive/` или пометить `archived` |
| verify | `name:` совпадает со stem; имя есть в этом README; нет orphan; [[50_runbooks/skill-checklist]]; файл на диске ≠ работает |

## Как создавать новый skill
1. Взять brief из `skills/<skill-name>/` этого репозитория или создать `<SKILLS_ROOT>/<skill-name>/SKILL.md`.
2. Пройти [[50_runbooks/skill-checklist]].
3. **Обязательно** добавить заметку в `60_skills/<owner>/<skill-name>.md` из [[60_skills/_templates/skill-note]] (`name:`, Triggers, один Location, без хостов).
4. Обновить `## Cursor Skills` и точный `## Related` в README связанных проектов (`10_projects/*`).

`## Run` в заметке vault — только если это контракт *установленных* скриптов, не копия чужого `SKILL.md`.

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
