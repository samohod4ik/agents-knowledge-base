---
tags:
  - profile
  - agent
  - cursor
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Контекст разработчика для Cursor агента

## Кто я

Оператор этого vault. Роль и контуры — в [[00_profile/developer-profile]] и [[00_profile/tech-stack]]. Имена, почту и логины из чужого профиля не копировать.

## Основной стек

Подставьте свои контуры. Порядок фактов как в `## Stack` карточек проекта:

- Python: `<X.Y>` (активный) и при необходимости legacy `<X.Y>`
- Backend: перечислите фреймворки (пример: FastAPI, SQLAlchemy)
- DB: тип и версия или имя контура, не прод-адрес
- Infra: Docker / ОС / ваш `<GIT_REMOTE>`

## Стиль кода

- Docstring на русском (reST)
- Функции короткие, вложенность ограниченная
- SQL в `./sql/`, тесты в `./tests/`

Подробности: [[40_patterns/coding-style]].

## Правила для агентов

- Сначала читайте этот vault, затем пишите код.
- После изменения кода, инфры или схемы обновите связанные заметки в том же ходе.
- Память — три слоя на диске ([[40_patterns/fleet-memory-stack]]): AST-граф в репозитории, ADR в `10_projects/<slug>/decisions.md`, один активный корень.
- Не ставить Mem0 / Antigravity Memory / второй движок «памяти».
- Deep-research только через `save-research` в `70_researches/`.
- Wikilink только с путём: `[[10_projects/<slug>/runbook]]`.
- Секреты — маски `***` или `secret_ref: vault://…`. Не дублировать значения из [[20_infra/access-matrix]].
- Канонический remote проектов — ваш `<GIT_REMOTE>`. Этот шаблон распространяется отдельно.
- 3 неудачи = STOP и вопрос оператору.

## Related

- [[00_profile/agent-context]]
- [[00_profile/tech-stack]]
- [[00_profile/developer-profile]]
- [[40_patterns/coding-style]]
- [[20_infra/cursor-mcp]]
- [[50_runbooks/maintenance]]
- [[40_patterns/fleet-memory-stack]]
