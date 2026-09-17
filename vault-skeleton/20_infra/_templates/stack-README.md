---
tags: [infra, stack, template]
last_verified: 2026-09-17
change_source: public-template-contract
---
# <stack-name>

Шаблон карточки стека. Копируйте в `20_infra/<stack>/README.md`. Это **не** прикладной репозиторий: квартет `architecture` / `runbook` / `requirements` не создавать и не требовать.

## Purpose

Один абзац: что поднимает стек (compose, общая БД, TDE-почва). Без живых хостов и паролей.

## Stack Location

- `<STACK_ROOT>/<stack-name>`

Корень на диске — ваш. Не копируйте чужой Docker-путь.

## Composition

- Сервисы: `<service-a>`, `<service-b>` (имена из compose, не IP)
- Контур БД: ссылка на [[30_db/connections]], не DSN
- Сеть: роль в [[20_infra/networks]]
- Доступ: строка в [[20_infra/access-matrix]] (`***` / `secret_ref`)

## Run (контракт, не живой compose)

```powershell
cd <STACK_ROOT>/<stack-name>
docker compose --env-file .env.example up -d
```

Секреты только в локальном `.env`, не в этой заметке. Пример-файл в репозитории стека — без паролей.

## Related

- [[20_infra/servers/README]]
- [[20_infra/networks]]
- [[20_infra/access-matrix]]
- [[30_db/connections]]
