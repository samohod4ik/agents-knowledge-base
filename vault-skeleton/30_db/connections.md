---
tags: [db, connections, postgresql]
last_verified: 2026-09-09
change_source: final-review-fixes
---
# DB Connections

## Main Context

- Основное семейство: укажите своё (пример: PostgreSQL `<N>`).
- Хосты — плейсхолдеры `<HOST>` или `127.0.0.1`. Прод-LAN не публиковать.
- Секрет в таблице всегда `***`. Живое значение — `secret_ref`.

## Databases in Use

| db | host | port | user | secret | secret_ref | usage |
|----|------|-----:|------|--------|------------|-------|
| `example_app` | `<HOST>` | 5432 | `<db_user>` | `***` | `vault://db/example-app` | Карточка сервиса, когда появится |
| `example_analytics` | `127.0.0.1` | 5433 | `<db_user>` | `***` | `vault://db/example-analytics` | Локальный контур |

## Connection String Templates

Подставьте свои имена. Маска обязательна.

```txt
postgresql://<db_user>:***@<HOST>:5432/example_app
postgresql://<db_user>:***@127.0.0.1:5433/example_analytics
```

Драйверный вариант (без живого секрета):

```txt
postgresql+<driver>://<db_user>:<secret>@<HOST>:5432/<db_name>?options=-csearch_path%3D<schema>
```

Не вставляйте готовый DSN с паролем. Не копируйте строки из чужого vault.

## Notes

- Политика масок — [[20_infra/access-matrix]].
- Схемы — [[30_db/schemas/README]].
- Проверочные запросы — [[30_db/important-queries/README]].

## Related

- [[30_db/schemas/README]]
- [[30_db/important-queries/README]]
- [[20_infra/access-matrix]]
- [[20_infra/servers/README]]
- [[10_projects/example_service/README]]
