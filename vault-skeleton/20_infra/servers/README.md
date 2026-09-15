---
tags:
  - infra
  - servers
  - inventory
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Servers Inventory

## Scope

Каталог *ваших* серверов и контуров. Одна заметка на хост или группу. Не копируйте чужой инвентарь.

## Create / update / archive / verify

- **Create:** файл `20_infra/servers/<hostname>.md` + строка доступа в access-matrix (маски).
- **Update:** роль/сеть/доступ в том же ходе, что и реальное изменение инфры.
- **Archive:** снятый хост → `90_archive/` с причиной и датой.
- **Verify:** нет plaintext секретов; ссылки на [[20_infra/access-matrix]] и [[20_infra/networks]].

## Server Notes

Добавьте ссылки вида `[[20_infra/servers/<hostname>]]` после создания файла. Пока список пустой, не выдумывайте хосты.

Пример формы заметки хоста (создайте файл сами):

- Имя: `<HOST>`
- Роль: app / db / ci
- Доступ: строка в [[20_infra/access-matrix]]
- Сеть: роль в [[20_infra/networks]]

## Related

- [[20_infra/networks]]
- [[20_infra/access-matrix]]
- [[20_infra/cursor-mcp]]
- [[30_db/connections]]
