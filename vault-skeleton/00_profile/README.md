---
tags: [profile, index, entrypoint]
last_verified: 2026-09-09
change_source: final-review-fixes
---
# Profile

Точка входа в профиль оператора и операционный контекст для агентов.

## Documents

| Заметка | Назначение |
|---------|------------|
| [[00_profile/developer-profile]] | Роли, контуры, список Active Projects |
| [[00_profile/tech-stack]] | Стек и контуры без чужих путей |
| [[00_profile/agent-context]] | Правила работы агентов (English hub) |
| [[40_patterns/fleet-memory-stack]] | Память флота: AST + ADR + роутер |

Корневая русскоязычная заметка `agent-context.md` остаётся отдельным файлом в корне vault.

Реестр skills: `60_skills/README.md` (ставится вместе с brief).

## Python Contours

Заполните своими версиями. Пример формы, не чужие slug:

- **`<X.Y>`** — активный контур automation / data
- **`<X.Y>`** — legacy web, если есть
- **`<X.Y>+`** — общая библиотека, если есть

## SCM

- Канонический remote рабочих репозиториев: `<GIT_REMOTE>/<org>/<repo>.git`
- API issues/PR — клиент вашего хоста, не обязательно GitHub
- Локальный git — MCP или CLI на диске
- Каталог MCP: [[20_infra/cursor-mcp]]

## Related

- [[50_runbooks/maintenance]]
- [[50_runbooks/obsidian-vault-audit]]
- [[20_infra/access-matrix]]
- [[20_infra/cursor-mcp]]
- [[40_patterns/fleet-memory-stack]]
- [[00_profile/agent-context]]
- [[00_profile/developer-profile]]
- [[00_profile/tech-stack]]
