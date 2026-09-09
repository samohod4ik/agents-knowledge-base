---
tags: [runbook, skills, cursor, mcp, cli]
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Скиллы для агентов Cursor

Скилл не конкурирует с MCP и CLI. Он задаёт регламент: когда звать инструменты, в каком порядке работать, какие проверки делать и что делать при сбое. MCP и CLI отвечают «чем делать». Скилл отвечает «как вести процесс».

## Кто есть кто

- **MCP** — набор инструментов модели и описание, как к ним ходить. Удобно, когда API часто меняется. Минус: описание занимает контекст с старта.
- **CLI** — утилита в терминале. Мало засоряет контекст, зависит от версии на машине оператора.
- **Skill** — папка с `SKILL.md`. Оркестрирует MCP, CLI и свои скрипты. Не заменяет их.

## Анатомия

Обязательно:

- `SKILL.md` в корне скилла
- frontmatter `name` и `description` с понятными триггерами

Полезно рядом: `scripts/`, `references/`, `assets/`, `config/`, `cache/`. Код не складывать в `SKILL.md`. В `config/` не держать секреты открытым текстом.

## Практика для этого vault

1. Сначала `doctor`, если он есть в brief.
2. Затем workflow. Fallback — если MCP лежит, писать файлы на диск.
3. После создания `SKILL.md` зарегистрируйте указатель в `60_skills/<owner>/<skill-name>.md` в том же ходе.
4. Owner — slug проекта или `workspace`.

Четыре brief этого шаблона (ставятся в `<SKILLS_ROOT>/`): `projects-data-verification`, `vault-router`, `session-distill`, `save-research`.

Не публикуйте skills с учётными данными или привязкой к одному внутреннему хосту.

## Related

- [[50_runbooks/skill-checklist]]
- [[50_runbooks/maintenance]]
- [[20_infra/cursor-mcp]]
- [[40_patterns/fleet-memory-stack]]
