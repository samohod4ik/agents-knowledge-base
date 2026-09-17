---
id: template-example-service-readme
kind: note
status: example
date: 2026-09-16
tags: [project, example_service, service, python, fastapi]
source_agent: public-template
last_verified: 2026-09-17
change_source: public-template-contract
---
# example_service

## Purpose

HTTP API плюс фоновый worker. Пример карточки сервиса: Run и Config без живых хостов. Очередь и факты — контур `example_app` из [[30_db/connections]].

## Create / update / archive / verify

- **Create:** квартет README / architecture / runbook / requirements; при why — `decisions.md`; строка в Active Projects.
- **Update:** после code/deps/infra — те же файлы в том же ходе (см. [[50_runbooks/maintenance]]).
- **Archive:** карточку в `90_archive/` с forward-link; снять из Active Projects.
- **Verify:** path-wikilinks, Stack, Project Location, маски секретов.

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

## Cursor Skills

Локальный brief после установки (не в этом шаблоне как код сервиса):

- `.cursor/skills/session-distill/SKILL.md` или `<SKILLS_ROOT>/session-distill/SKILL.md`
- Указатель vault: [[60_skills/workspace/session-distill]]

Стек, на котором крутится пример: [[20_infra/example_stack/README]] — это инфра, не четвёртая карточка квартета.

## Related

- [[10_projects/example_service/architecture]]
- [[10_projects/example_service/runbook]]
- [[10_projects/example_service/requirements]]
- [[10_projects/example_service/decisions]]
- [[10_projects/example_library/README]]
- [[20_infra/example_stack/README]]
- [[00_profile/tech-stack]]
- [[00_profile/developer-profile]]
- [[20_infra/access-matrix]]
- [[30_db/connections]]
- [[40_patterns/fleet-memory-stack]]
- [[50_runbooks/maintenance]]
