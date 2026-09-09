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
