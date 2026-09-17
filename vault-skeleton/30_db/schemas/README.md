---
tags: [db, schemas, er]
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# DB Schemas

## Scope

ER-описания и миграционные заметки по *вашим* проектам. Одна заметка на схему или критичную миграцию.

## Create / update / archive / verify

- **Create:** заметка схемы + Related на connections / important-queries.
- **Update:** после миграции обновите ER и pre/post checks.
- **Archive:** устаревшую схему в `90_archive/` с `superseded_by`.
- **Verify:** секреты только маски; нет прод-DSN открытым текстом.

## Project Map

Пока шаблон. Замените именами своих БД и таблиц.

- `example_app`: прикладные таблицы сервиса (`orders`, `audit_log` — примеры, не чужой прод).
- `example_analytics`: витрины и срезы для отчётов.

Не переносите схемы живых внутренних систем в этот шаблон.

## Migration Notes

- Каждую критичную миграцию — отдельным файлом в этой папке.
- Для rebuild фиксируйте pre/post checks в [[30_db/important-queries/README]].

## Related

- [[30_db/connections]]
- [[30_db/important-queries/README]]
- [[20_infra/servers/README]]
