---
name: projects-data-verification
description: >-
  Use when the user asks for проверка Obsidian, аудит vault, верификация
  документации, obsidian-vault-audit, projects-data-verification,
  projects_data_verification, целостность правил, качество хранилища,
  60_skills, skill-checklist.
---

# projects-data-verification

Установка: `<SKILLS_ROOT>/projects-data-verification`.

Read-only аудит vault `<VAULT>`: карточки проектов, Cursor rules, реестр skills, формулировки SCM относительно вашего `<GIT_REMOTE>`. Публичный шаблон везёт **только** этот brief. Локальные `scripts/` — опциональная собственность оператора; без них выполняйте проверки по файлам.

**Не используй**, когда нужно только обновить один project README после code change, или пользователь просит не трогать Obsidian и не проверять docs.

## Workflow

1. Открой `<VAULT>/README.md` и список Active Projects.
2. Для каждого активного slug проверь квартет: `README`, `architecture`, `runbook`, `requirements` (+ `decisions.md`, если есть).
3. Frontmatter: закрывающий `---`, `tags`, `last_verified`, `change_source`.
4. Wikilink только с путём; нет self-link в `## Related`.
5. `## Project Location` и remote в заметках совпадают с *вашим* `<GIT_REMOTE>` / диском — не с remote издателя шаблона.
6. Реестр: каждый локальный skill имеет `60_skills/<owner>/<skill-name>.md` и строку в `60_skills/README.md`.
7. Секреты: в `20_infra` / `30_db` только маски или `secret_ref`.
8. Запиши findings в `50_runbooks/obsidian-vault-audit.md` (дата, gaps, что закрыто). Не автофикси docs без явной просьбы.

## Запреты

- Автоисправление vault «заодно»
- Выдумывать список проектов, если Active Projects пуст
- Требовать отсутствующий `scripts/doctor.py` как единственный путь успеха
- Печатать секреты в отчёт

## Успех

Нет error-level gaps по применимым пунктам чеклиста в [docs/cursor-integration.md](../../docs/cursor-integration.md#pre-completion-checklist), либо gaps явно записаны в audit-журнале. Vault и rules skillом не менялись.
