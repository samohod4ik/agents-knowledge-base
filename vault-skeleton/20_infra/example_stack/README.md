---
tags: [infra, stack, example_stack]
last_verified: 2026-09-17
change_source: public-template-contract
---
# example_stack

Пример карточки стека. Compose / общая почва живут в `20_infra/`, не в `10_projects/`. Квартет не нужен.

## Purpose

Локальный пример: API + worker + PostgreSQL из одного compose. Это учебная форма, не живой Docker.

## Stack Location

- `<STACK_ROOT>/example_stack`

## Composition

- Сервисы: `api`, `worker`, `postgres` (имена compose)
- Контур БД: `example_app` в [[30_db/connections]]
- Сеть: роль в [[20_infra/networks]]
- Доступ: [[20_infra/access-matrix]]

Потребитель-пример: [[10_projects/example_service/README]].

## Run (контракт)

```powershell
cd <STACK_ROOT>/example_stack
docker compose --env-file .env.example up -d
```

Не вставляйте готовый DSN и не копируйте чужой `docker-compose.yml`.

## Related

- [[20_infra/_templates/stack-README]]
- [[20_infra/servers/README]]
- [[20_infra/networks]]
- [[20_infra/access-matrix]]
- [[10_projects/example_service/README]]
- [[30_db/connections]]
