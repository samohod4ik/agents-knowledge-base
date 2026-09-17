---
name: projects-data-verification
description: >-
  Use when the user asks for проверка Obsidian, аудит vault, верификация
  документации, obsidian-vault-audit, projects-data-verification,
  projects_data_verification, целостность правил, качество хранилища,
  60_skills, skill-checklist.
---

# projects-data-verification

Это **контракт**, не поставка автоматизации. Каталога `scripts/` в этом шаблоне нет. Локальные `scripts/` — опциональная собственность оператора; без них выполняйте проверки по файлам.

Установка: `<SKILLS_ROOT>/projects-data-verification`.

Read-only аудит vault `<VAULT>`: карточки проектов, Cursor rules, реестр skills, формулировки SCM относительно вашего `<GIT_REMOTE>`.

**Не используй**, когда нужно только обновить один project README после code change, или пользователь просит не трогать Obsidian и не проверять docs.

## Workflow

1. Открой `<VAULT>/README.md` и список Active Projects.
2. Для каждого активного slug в `10_projects/` проверь квартет: `README`, `architecture`, `runbook`, `requirements` (+ `decisions.md`, если есть). Стеки в `20_infra/` в квартет не входят.
3. Frontmatter: закрывающий `---`, `tags`, `last_verified`, `change_source`.
4. Wikilink только с путём; нет self-link в точном H2 `## Related`. Префикс (`## Related Research`) — не Related.
5. `## Project Location` и remote в заметках совпадают с *вашим* `<GIT_REMOTE>` / диском — не с remote издателя шаблона.
6. Реестр: каждый локальный skill имеет `name:` в `60_skills/<owner>/<skill-name>.md` и строку в `60_skills/README.md`.
7. `inventory`: прямые git-дети `projects_root`. Клон этого шаблона там — ошибка, либо `excluded` с reason `public`.
8. Секреты: в `20_infra` / `30_db` только маски или `secret_ref`.
9. Запиши findings в `50_runbooks/obsidian-vault-audit.md` (два снимка: до / после, если правили). Cache JSON не SoT. Не автофикси docs без явной просьбы.

Если у оператора есть локальный `verify_projects_data.py` — это тот же продукт; `verify_vault.py` — модуль, не второй верификатор. Не требуйте отсутствующий скрипт как единственный путь успеха.

## Запреты

- Автоисправление vault «заодно»
- Выдумывать список проектов, если Active Projects пуст
- Требовать отсутствующий `scripts/doctor.py` как единственный путь успеха
- Печатать секреты в отчёт

## Успех

AlwaysApply-стоп без скрипта: чеклист в [docs/cursor-integration.md](../../docs/cursor-integration.md#pre-completion-checklist) и gaps в audit-журнале. Со скриптом — категория `scm` clean; полный `errors = 0` — цель журнала, не стоп задачи. Vault и rules skillом не менялись.
