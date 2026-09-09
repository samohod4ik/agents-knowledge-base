---
tags: [patterns, git, conventions]
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Git Conventions

## Branching

- `feature/<name>` — новая функциональность
- `fix/<name>` — исправление дефекта
- `chore/<name>` — сопровождение и документы

## Commits

- Краткий заголовок в повелительном стиле.
- Фокус на «зачем», не только «что».
- Не смешивать без нужды правки app / инфры / схемы.

## Pull Requests

- Обязательно: цель, влияние, test-plan.
- Для schema/db — rollback и проверочные запросы.
- Issues/PR создавайте на *вашем* `<GIT_REMOTE>` тем клиентом, который принят у команды. Локальный git на диске — отдельно.

## Related

- [[50_runbooks/maintenance]]
- [[20_infra/cursor-mcp]]
- [[40_patterns/rr77-cursor-rules]]
- [[40_patterns/coding-style]]
