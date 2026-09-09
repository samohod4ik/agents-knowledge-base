---
tags: [infra, access, matrix, secrets]
last_verified: 2026-09-09
change_source: final-review-fixes
---
# Access Matrix

Только шаблон. Значения секретов не хранить в этой таблице. Столбец `secret` — маска. Настоящее значение — в вашем секрет-хранилище по `secret_ref`.

| host | role | secret | secret_ref | notes |
|------|------|--------|------------|-------|
| `<HOST>` | app-operator | `***` | `vault://infra/app-host/ssh` | SSH на прикладной хост; ключ не в git |
| `127.0.0.1` | local-dev | `***` | `vault://db/local-dev` | Локальный контур разработки |
| `<HOST>` | ci-bot | `***` | `vault://ci/deploy-bot` | Учётка пайплайна, не личная |

Добавляйте строки в том же виде. Запрещено:

- Открытый текст пароля, токена, DSN, `apiKey`
- Адреса прод-LAN и внутренние DNS чужой команды
- Копия секрета во второй заметке — ссылайтесь сюда

## Policy

- Инфра-заметки не дублируют секрет: только `***` или `secret_ref: vault://…`.
- Плагин Obsidian Local REST держит свой ключ в UI / локальном store. Файл `data.json` не коммитить.
- Исключения «у нас в vault можно plaintext» в этот шаблон не входят.

## Related

- [[20_infra/servers/README]]
- [[20_infra/networks]]
- [[20_infra/cursor-mcp]]
- [[30_db/connections]]
- [[10_projects/example_service/README]]
