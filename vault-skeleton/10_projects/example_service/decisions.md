---
tags: [project, example_service, decisions]
last_verified: 2026-09-09
change_source: task-5-example-projects
---
# example_service — decisions

Устойчивые ADR. Не сырые логи, не секреты. Держать коротко. Подробности — в architecture / runbook.

## 2026-09-09 — конфиг без живого DSN

- **Decision:** Локальный `config/app.json` из `config/app.example.json`. Пароль БД — `secret_ref` (`vault://db/example-app`), в заметках маска `***`.
- **Anti:** Не вставлять готовый DSN. Не копировать хосты и учётки из чужого vault.
- **Refs:** [[30_db/connections]], [[20_infra/access-matrix]]

## 2026-09-09 — память флота

- **Decision:** Межсессионная память — этот файл. Карта кода — `GRAPH_REPORT.md` в репозитории (AST, `--code-only`). Регламент — [[40_patterns/fleet-memory-stack]].
- **Anti:** Не ставить Mem0 / Antigravity Memory. Не `graphify export obsidian` в `10_projects/`.

## Related

- [[10_projects/example_service/README]]
- [[10_projects/example_service/architecture]]
- [[10_projects/example_service/runbook]]
- [[30_db/connections]]
- [[40_patterns/fleet-memory-stack]]
