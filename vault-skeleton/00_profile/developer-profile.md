---
tags:
  - profile
  - developer
  - roles
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Developer Profile

## Bio

Кратко опишите фокус оператора. Не копируйте чужие ФИО, логины и почту.

- Пример роли: backend / automation / data / infra.
- Пример домена: внутренние сервисы, партии данных, эксплуатация.

## Roles

Замените строки своими. Это шаблон ролей, не чужой штат.

- **Backend:** веб-фреймворк, ORM, контур БД.
- **Automation:** CLI, браузерная автоматизация, долгие службы.
- **Data:** ingest, сверки, регламентные выгрузки.
- **Infra / incident:** хосты из [[20_infra/servers/README]], доступ только через [[20_infra/access-matrix]].

## Python Contours

- **Активный:** `<X.Y>` — новые сборки и automation.
- **Legacy:** `<X.Y>` — если ещё жив отдельный web-контур.
- **Library min:** `<X.Y>+` — общая библиотека.

## Database Contours

- **Основной:** PostgreSQL `<N>` или ваш тип/контур.
- **Legacy:** только если реально используется; без прод-адреса в тексте.
- Секреты не сюда — `secret_ref` в [[20_infra/access-matrix]] и маски в [[30_db/connections]].

## Contacts

- Оператор: `<OPERATOR>`
- ОС-контур: укажите свою машину, не чужой username.
- Доступы: только ссылка на [[20_infra/access-matrix]].

## Active Projects

Пока пусто. После появления карточки добавьте `[[10_projects/<slug>/README]]` и зеркало в корневом README.

## Related

- [[00_profile/agent-context]]
- [[00_profile/tech-stack]]
- [[20_infra/servers/README]]
- [[20_infra/cursor-mcp]]
- [[40_patterns/fleet-memory-stack]]
