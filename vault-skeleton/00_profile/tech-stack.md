---
tags:
  - profile
  - stack
  - technologies
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Tech Stack

Заполните своими версиями. Не вставляйте абсолютные диски, прод-LAN и чужие org.

## Python

- **Активный default:** `<X.Y>`
- **Legacy web:** `<X.Y>` — если есть
- **Library / min:** `<X.Y>+` — если есть общая библиотека

## Backend Frameworks

Пример набора, замените своим:

- HTTP API (пример: FastAPI + uvicorn)
- ORM / драйвер БД
- Долгие CLI или браузерные службы
- Опционально: Playwright / Selenium — да/нет в `## Stack` карточки

## Database

- Основной контур: PostgreSQL `<N>` на `<HOST>` (плейсхолдер, не адрес LAN)
- Локальная разработка: `127.0.0.1:<PORT>`
- Другие семейства — только если используете; пароли не писать

Строки подключения: [[30_db/connections]].

## Infra and Ops

- Контейнеры на `<HOST>` по необходимости
- Локальный Docker / WSL — ваши пути, не чужие
- Канонический git: `<GIT_REMOTE>`
- MCP-каталог: [[20_infra/cursor-mcp]]

## SCM Policy

- В заметках указывайте *ваш* `<GIT_REMOTE>`.
- Канал распространения этого шаблона — публичный GitHub. Это не канон рабочих репозиториев.
- Агенты: API хостинга отдельно от локального git на диске. Не кладите PAT в markdown.

## Active Projects

Пока пусто. Держите список синхронным с корневым README и [[00_profile/developer-profile]].

## Related

- [[00_profile/agent-context]]
- [[00_profile/developer-profile]]
- [[20_infra/networks]]
- [[20_infra/cursor-mcp]]
- [[50_runbooks/maintenance]]
- [[40_patterns/fleet-memory-stack]]
