---
tags: [project, example_service, architecture]
last_verified: 2026-09-09
change_source: task-5-example-projects
---
# example_service — architecture

## Project Location

- `<PROJECT_ROOT>/example_service`

## Stack

- Python: `<X.Y>`
- DB: PostgreSQL `<N>` / контур `example_app` на `<HOST>`
- Selenium: нет
- Core libs: FastAPI, uvicorn, SQLAlchemy

## Layers

```text
src/example_service/
  app.py               # FastAPI: health, команды
  worker.py            # цикл очереди
  settings.py          # путь конфига, без секрета в коде
  db.py                # SQLAlchemy; DSN из secret_ref / env
  clients.py           # вызов example_library
sql/
  001_example_app.sql
tests/
  test_app.py
  test_worker.py
config/
  app.example.json
```

```text
HTTP 127.0.0.1:<PORT>
  -> example_service.app
       -> settings + example_library client
       -> SQLAlchemy -> PostgreSQL example_app на <HOST>
worker
  -> очередь / audit_log (имена-примеры в [[30_db/schemas/README]])
```

## Boundaries

- Секрет не дублировать в заметке: только `***` или `secret_ref` ([[20_infra/access-matrix]]).
- Хост приложения и БД — плейсхолдер `<HOST>` или `127.0.0.1`. Прод-LAN не публиковать.
- Браузерной автоматизации нет (`Selenium: нет`).

## Risks

- Собрать DSN в markdown — запрещено; шаблон без пароля см. [[30_db/connections]].
- Worker и API делят схему `example_app` — ломающие миграции фиксируйте здесь и в [[30_db/schemas/README]].
- Смена публичного контракта API — ADR в [[10_projects/example_service/decisions]].

## Related

- [[10_projects/example_service/README]]
- [[10_projects/example_service/runbook]]
- [[10_projects/example_service/requirements]]
- [[10_projects/example_service/decisions]]
- [[10_projects/example_library/README]]
- [[30_db/connections]]
- [[30_db/schemas/README]]
- [[20_infra/access-matrix]]
- [[40_patterns/fleet-memory-stack]]
