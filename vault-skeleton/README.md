---
tags:
  - vault
  - index
  - entrypoint
last_verified: 2026-09-09
change_source: final-review-fixes
---
# AgentsKnowledgeBase

Операционная база знаний для агента Cursor и оператора. Это карта команд, путей и связей, а не свалка заметок.

Заполните плейсхолдеры `<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, `<GIT_REMOTE>`, `<HOST>` своими значениями. Живые хосты, учётки и секреты сюда не копировать.

## Entry Points

- [[00_profile/README]] — профиль оператора и хаб агента
- [[00_profile/agent-context]] — операционный хаб агента
- `agent-context.md` — краткие русскоязычные правила (корневая заметка, отдельно от хаба)
- [[40_patterns/fleet-memory-stack]] — три слоя памяти на диске
- [[40_patterns/shared-cursor-rules]] — паттерн общих Cursor rules
- [[20_infra/cursor-mcp]] — каталог MCP
- [[50_runbooks/maintenance]] — протокол обновления
- [[50_runbooks/obsidian-vault-audit]] — журнал аудита
- [[70_researches/70_research_ops/70.01_INDEX]] — индекс исследований

Реестр локальных skills — [[60_skills/README]]. Brief шаблона лежат в `skills/` корня репозитория. Карточки проектов — в `10_projects/<slug>/`.

## Sections

| Раздел | Назначение |
|--------|------------|
| `00_profile/` | Профиль, стек, English hub агента |
| `10_projects/` | На slug: README, architecture, runbook, requirements, часто `decisions.md` |
| `20_infra/` | Серверы, сети, access-matrix (маски), каталог MCP |
| `30_db/` | Подключения с масками, схемы, важные запросы |
| `40_patterns/` | Стиль кода, git, стек памяти, общие rules |
| `50_runbooks/` | Сопровождение, аудит, гайды по skills |
| `60_skills/` | Реестр локальных project skills Cursor |
| `70_researches/` | Архив исследований Johnny Decimal |
| `90_archive/` | Устаревшие заметки |

Нет папки `80_*`. Правила Cursor живут в `<VAULT>/.cursor/rules/`, вне нумерации.

## Active Projects

- [[10_projects/example_library/README]] — общая Python-библиотека (пример карточки)
- [[10_projects/example_service/README]] — HTTP/worker-сервис (пример карточки)

Только эти два slug. Замените список своими карточками; чужие операционные runbook не копировать.

## Archive

См. [[90_archive/README]]. Завершённые research-прогоны сюда не переносить.

## Related

- [[10_projects/example_library/README]]
- [[10_projects/example_service/README]]
- [[00_profile/tech-stack]]
- [[00_profile/developer-profile]]
- [[20_infra/cursor-mcp]]
- [[50_runbooks/maintenance]]
- [[40_patterns/fleet-memory-stack]]
- [[60_skills/README]]
- [[70_researches/70_research_ops/70.01_INDEX]]
