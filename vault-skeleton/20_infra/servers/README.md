---
tags:
  - infra
  - servers
  - inventory
last_verified: 2026-09-17
change_source: public-template-contract
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

Пример стека (не хост): [[20_infra/example_stack/README]]. Шаблон карточки: [[20_infra/_templates/stack-README]].

## Related

- [[20_infra/example_stack/README]]
- [[20_infra/_templates/stack-README]]
- [[20_infra/networks]]
- [[20_infra/access-matrix]]
- [[20_infra/cursor-mcp]]
- [[30_db/connections]]
