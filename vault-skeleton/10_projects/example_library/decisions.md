---
tags: [project, example_library, decisions]
last_verified: 2026-09-09
change_source: task-5-example-projects
---
# example_library — decisions

Устойчивые ADR. Не сырые логи, не секреты. Держать коротко. Подробности — в architecture / runbook.

## 2026-09-09 — библиотека без runtime-хоста

- **Decision:** Пакет не знает `<HOST>` и не читает DSN. Базовый URL и секреты задаёт потребитель.
- **Anti:** Не копировать операционные runbook живых проектов. Не класть plaintext-секреты в `src/`.
- **Refs:** [[10_projects/example_library/architecture]], [[20_infra/access-matrix]]

## 2026-09-09 — память флота

- **Decision:** Межсессионная память — этот файл. Карта кода — `GRAPH_REPORT.md` в репозитории (AST, `--code-only`). Регламент — [[40_patterns/fleet-memory-stack]].
- **Anti:** Не ставить Mem0 / Antigravity Memory. Не `graphify export obsidian` в `10_projects/`.

## Related

- [[10_projects/example_library/README]]
- [[10_projects/example_library/architecture]]
- [[10_projects/example_library/runbook]]
- [[40_patterns/fleet-memory-stack]]
