---
tags: [project, example_library, runbook]
last_verified: 2026-09-09
change_source: task-5-example-projects
---
# example_library — runbook

## Project Location

- `<PROJECT_ROOT>/example_library`

## Stack

- Python: `<X.Y>+`
- DB: нет собственной (пакет библиотеки)
- Selenium: нет
- Core libs: requests, pydantic

## Run

```powershell
cd <PROJECT_ROOT>/example_library
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[test]"
python -c "import example_library"
python -m pytest tests -q
```

Linux/macOS: тот же порядок, активация `.venv/bin/activate`.

Установка потребителем:

```powershell
pip install "git+<GIT_REMOTE>/<org>/example_library.git@<tag_or_commit>"
```

## Config

- `EXAMPLE_LIBRARY_BASE_URL` — опциональный default для клиента.
- Хост и секрет не в репозитории библиотеки. Потребитель читает [[20_infra/access-matrix]] и свой конфиг.
- Не вставляйте готовый DSN.

## Risks

- Editable install из чужого абсолютного диска — замените на `<PROJECT_ROOT>/example_library`.
- Публикация на ваш `<GIT_REMOTE>` только после тестов.

## Incident

- Импорт падает: проверьте `pip show example_library` и что активен тот же venv.
- Регрессия API: сравните теги remote, зафиксируйте why в [[10_projects/example_library/decisions]].
- Потребитель не стартует: смотрите runbook сервиса [[10_projects/example_service/runbook]], не этот пакет.

## Related

- [[10_projects/example_library/README]]
- [[10_projects/example_library/architecture]]
- [[10_projects/example_library/requirements]]
- [[10_projects/example_library/decisions]]
- [[10_projects/example_service/runbook]]
- [[20_infra/access-matrix]]
- [[50_runbooks/maintenance]]
