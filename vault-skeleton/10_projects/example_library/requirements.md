---
tags: [project, example_library, requirements]
last_verified: 2026-09-09
change_source: task-5-example-projects
---
# example_library — requirements

## Project Location

- `<PROJECT_ROOT>/example_library`

## Stack

- Python: `<X.Y>+`
- DB: нет собственной (пакет библиотеки)
- Selenium: нет
- Core libs: requests, pydantic

## Python

- Минимум: `<X.Y>+` (совместимо с контуром Library / min в [[00_profile/tech-stack]]).
- Источник истины версий — `pyproject.toml` в репозитории, не эта заметка.

## Runtime

- `requests` — HTTP-клиент
- `pydantic` — модели входа/выхода
- Тестовый extra: `pytest`

## Out of scope

- Собственная БД, миграции, HTTP-сервер
- Selenium / браузерный extra
- Хосты, учётки, готовые DSN

## SCM

- `<GIT_REMOTE>/<org>/example_library.git`

## Related

- [[10_projects/example_library/README]]
- [[10_projects/example_library/architecture]]
- [[10_projects/example_library/runbook]]
- [[10_projects/example_library/decisions]]
- [[00_profile/tech-stack]]
- [[40_patterns/coding-style]]
