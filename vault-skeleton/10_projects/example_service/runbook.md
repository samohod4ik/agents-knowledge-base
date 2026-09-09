---
tags: [project, example_service, runbook]
last_verified: 2026-09-09
change_source: task-5-example-projects
---
# example_service — runbook

## Project Location

- `<PROJECT_ROOT>/example_service`

## Stack

- Python: `<X.Y>`
- DB: PostgreSQL `<N>` / контур `example_app` на `<HOST>`
- Selenium: нет
- Core libs: FastAPI, uvicorn, SQLAlchemy

## Run

```powershell
cd <PROJECT_ROOT>/example_service
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[test]"
copy config\app.example.json config\app.json
$env:EXAMPLE_SERVICE_CONFIG_PATH = "config/app.json"
uvicorn example_service.app:app --host 127.0.0.1 --port <PORT>
```

Worker (второй терминал, тот же venv):

```powershell
cd <PROJECT_ROOT>/example_service
python -m example_service.worker
```

Linux/macOS: активация `.venv/bin/activate`, копирование `cp config/app.example.json config/app.json`.

## Config

- Файл: `config/app.example.json` → `config/app.json`.
- Ключи формы (подставьте свои): `db.host` = `<HOST>` или `127.0.0.1`, `db.port` = `5432`, `db.name` = `example_app`, `db.user` = `<db_user>`, `db.secret` не хранить — `secret_ref` = `vault://db/example-app`.
- Env: `EXAMPLE_SERVICE_CONFIG_PATH`.
- Строка подключения: только шаблон из [[30_db/connections]] с маской `***`. Готовый DSN с паролем не вставлять.

## Health

- `GET http://127.0.0.1:<PORT>/health` — процесс жив, без обращения к внешним системам.
- Проверочные SQL: [[30_db/important-queries/README]] (`example_app` checks).

## Risks

- Запуск на `0.0.0.0` и прод-адресе в шаблоне не нужен — только `127.0.0.1` или `<HOST>`.
- `config/app.json` с секретом не коммитить.
- Общая библиотека не установлена — сначала [[10_projects/example_library/runbook]].

## Incident

1. Процесс не слушает порт: проверьте venv и `<PORT>`.
2. Ошибка БД: маска и `secret_ref` в [[20_infra/access-matrix]], не пароль в чат.
3. Очередь стоит: worker запущен? Смотрите `audit_log` запросами из [[30_db/important-queries/README]].
4. Почему так сделано — [[10_projects/example_service/decisions]], не invent в инциденте.

## Related

- [[10_projects/example_service/README]]
- [[10_projects/example_service/architecture]]
- [[10_projects/example_service/requirements]]
- [[10_projects/example_service/decisions]]
- [[10_projects/example_library/runbook]]
- [[20_infra/access-matrix]]
- [[30_db/connections]]
- [[30_db/important-queries/README]]
- [[50_runbooks/maintenance]]
