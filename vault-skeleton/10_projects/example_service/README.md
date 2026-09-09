---
tags: [project, example_service, service, python, fastapi]
last_verified: 2026-09-09
change_source: task-5-example-projects
---
# example_service

## Purpose

HTTP API плюс фоновый worker. Пример карточки сервиса: Run и Config без живых хостов. Очередь и факты — контур `example_app` из [[30_db/connections]].

## Project Location

- `<PROJECT_ROOT>/example_service`

## Stack

- Python: `<X.Y>`
- DB: PostgreSQL `<N>` / контур `example_app` на `<HOST>`
- Selenium: нет
- Core libs: FastAPI, uvicorn, SQLAlchemy

## Entrypoints

- API: `uvicorn example_service.app:app --host 127.0.0.1 --port <PORT>`
- Worker: `python -m example_service.worker`
- Тесты: `python -m pytest tests -q`

Общая библиотека (пример зависимости): [[10_projects/example_library/README]].

## Config

- Шаблон: `config/app.example.json` → локально `config/app.json` (секреты не коммитить).
- Override: `EXAMPLE_SERVICE_CONFIG_PATH`.
- Подключение к БД: маска и `secret_ref` в [[30_db/connections]] и [[20_infra/access-matrix]]. Готовый DSN с паролем не вставлять.

## Testing

```powershell
cd <PROJECT_ROOT>/example_service
python -m pytest tests -q
```

SQL — в `./sql/`. Проверочные запросы — [[30_db/important-queries/README]].

## SCM

- Remote: `<GIT_REMOTE>/<org>/example_service.git`

## Related

- [[10_projects/example_service/architecture]]
- [[10_projects/example_service/runbook]]
- [[10_projects/example_service/requirements]]
- [[10_projects/example_service/decisions]]
- [[10_projects/example_library/README]]
- [[00_profile/tech-stack]]
- [[00_profile/developer-profile]]
- [[20_infra/access-matrix]]
- [[30_db/connections]]
- [[40_patterns/fleet-memory-stack]]
- [[50_runbooks/maintenance]]
