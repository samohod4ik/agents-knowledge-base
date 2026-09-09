---
tags: [db, sql, queries]
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Important Queries

Проверочные запросы. Имена таблиц — примеры. Подставьте свои.

## example_app checks

```sql
-- согласованность источника и фактов
SELECT COUNT(*) AS source_rows FROM example_app.source_rows;
SELECT COUNT(*) AS fact_rows FROM example_app.facts;
```

```sql
-- активные блокировки
SELECT fact_id, locked_by, locked_at
FROM example_app.locks
ORDER BY locked_at DESC
LIMIT 100;
```

## Smoke checks

```sql
SELECT current_database() AS db_name, now() AS checked_at;
```

Не вставляйте запросы с литералами учёток или прод-хостами. Подключение берите из [[30_db/connections]].

## Related

- [[30_db/connections]]
- [[30_db/schemas/README]]
- [[20_infra/access-matrix]]
