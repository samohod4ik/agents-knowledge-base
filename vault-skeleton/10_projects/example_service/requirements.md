---
tags: [project, example_service, requirements]
last_verified: 2026-09-09
change_source: task-5-example-projects
---
# example_service — requirements

## Project Location

- `<PROJECT_ROOT>/example_service`

## Stack

- Python: `<X.Y>`
- DB: PostgreSQL `<N>` / контур `example_app` на `<HOST>`
- Selenium: нет
- Core libs: FastAPI, uvicorn, SQLAlchemy

## Python

- Активный контур: `<X.Y>` (см. [[00_profile/tech-stack]]).
- Источник истины версий — `pyproject.toml` / lock в репозитории.

## Runtime

- `fastapi`, `uvicorn` — HTTP
- `sqlalchemy` + драйвер PostgreSQL (имя драйвера своё; в заметке не писать пароль)
- `example_library` — клиент и модели ([[10_projects/example_library/requirements]])
- Тестовый extra: `pytest`

## Out of scope

- Selenium / headed browser
- Прод-LAN, живые учётки, готовый DSN
- Копия чужого операционного runbook

## SCM

- `<GIT_REMOTE>/<org>/example_service.git`

## Related

- [[10_projects/example_service/README]]
- [[10_projects/example_service/architecture]]
- [[10_projects/example_service/runbook]]
- [[10_projects/example_service/decisions]]
- [[10_projects/example_library/requirements]]
- [[00_profile/tech-stack]]
- [[30_db/connections]]
