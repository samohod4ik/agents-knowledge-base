---
tags: [infra, mcp, cursor, git, obsidian]
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Cursor MCP

Каталог MCP, которые агент может звать из этого vault. Конфиг обычно user-level (`%USERPROFILE%\.cursor\mcp.json` на Windows). Токены, Bearer и ключи плагина сюда не писать.

## Серверы

| MCP id | Назначение | Транспорт | Когда звать |
|--------|------------|-----------|-------------|
| `obsidian-vault` | Этот vault (`<VAULT>`) | stdio или HTTP на `127.0.0.1:<PORT>` | правки заметок после изменений |
| `git` | Локальный git на диске | stdio | status, commit, branch в working tree |
| `team-git-api` | API вашего git-хоста | HTTP на ваш URL | issues / PR; не GitHub шаблона, если хост другой |
| `postgres-<contour>` | SQL выбранного контура | stdio / SSE | запросы; DSN только в локальном секрете |

Имена id замените своими. Хостинг API ≠ локальный git.

## Obsidian Local REST

Предпочтительная запись в vault: community-плагин Local REST API, затем MCP на `http://127.0.0.1:<PORT>`. Ключ оставьте в UI плагина. Если MCP красный — правьте markdown на диске и скажите об этом.

Не коммитить `.obsidian/plugins/obsidian-local-rest-api/data.json`.

## Политика

- Секреты MCP только в локальном конфиге / store, не в заметках.
- Не ставить MCP «памяти» вместо [[40_patterns/fleet-memory-stack]].
- Каталог обновляйте, когда добавляете или снимаете сервер.

## Related

- [[20_infra/access-matrix]]
- [[20_infra/servers/README]]
- [[00_profile/tech-stack]]
- [[00_profile/agent-context]]
- [[40_patterns/rr77-cursor-rules]]
- [[50_runbooks/maintenance]]
