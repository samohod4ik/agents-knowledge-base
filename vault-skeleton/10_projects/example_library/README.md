---
tags: [project, example_library, library, python]
last_verified: 2026-09-09
change_source: task-5-example-projects
---
# example_library

## Purpose

Общая Python-библиотека для нескольких потребителей: клиент, модели, утилиты. Это пример карточки, не живой внутренний пакет. Код живёт в git-репозитории, не в vault.

## Project Location

- `<PROJECT_ROOT>/example_library`

## Stack

- Python: `<X.Y>+`
- DB: нет собственной (пакет библиотеки)
- Selenium: нет
- Core libs: requests, pydantic

## Entrypoints

- Импорт: `python -c "import example_library"`
- Editable install: `pip install -e ".[test]"`
- Тесты: `python -m pytest tests -q`

Публичный API описывайте в `src/example_library/` (или корне пакета). Не копируйте чужие модули.

## Config

- Опционально: `EXAMPLE_LIBRARY_BASE_URL` — ваш endpoint, не чужой хост.
- Секреты потребителя в библиотеку не класть. Ссылка на политику: [[20_infra/access-matrix]].

## Testing

```powershell
cd <PROJECT_ROOT>/example_library
python -m pytest tests -q
```

SQL, если появится, держите в `./sql/`. Тесты — в `./tests/`.

## SCM

- Remote: `<GIT_REMOTE>/<org>/example_library.git`
- Установка с remote: `pip install "git+<GIT_REMOTE>/<org>/example_library.git@<tag_or_commit>"`
- Не направляйте пример на remote издателя шаблона, если это не ваш хост.

## Related

- [[10_projects/example_library/architecture]]
- [[10_projects/example_library/runbook]]
- [[10_projects/example_library/requirements]]
- [[10_projects/example_library/decisions]]
- [[10_projects/example_service/README]]
- [[00_profile/tech-stack]]
- [[00_profile/developer-profile]]
- [[40_patterns/coding-style]]
- [[40_patterns/fleet-memory-stack]]
- [[50_runbooks/maintenance]]
