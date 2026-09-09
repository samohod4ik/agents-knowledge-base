---
tags: [infra, network, hosts]
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Networks

Карта имён и ролей, не таблица прод-адресов. Подставьте свои `<HOST>` и сегменты.

## Host Mapping

| name | role | address |
|------|------|---------|
| `<HOST>` | app | плейсхолдер; не копируйте LAN |
| `<HOST>` | db | плейсхолдер; порт в [[30_db/connections]] |
| `localhost` | local-dev | `127.0.0.1` |

Не публикуйте внутренние балансировщики и VPN-учётки. Если сегмент нужен агенту — опишите роль («контур ingest»), а не чужой IP.

## VPN and Segments

- Рабочий сегмент: имя контура, не литерал сети.
- Доступ к сегменту — строка в [[20_infra/access-matrix]], не повтор секрета здесь.

## Related

- [[20_infra/servers/README]]
- [[20_infra/access-matrix]]
- [[20_infra/cursor-mcp]]
- [[30_db/connections]]
