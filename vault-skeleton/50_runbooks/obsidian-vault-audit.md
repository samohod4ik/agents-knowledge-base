---
tags: [runbook, audit, vault, maintenance]
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Obsidian Vault Audit

Журнал проходов аудита. Верификатор `projects-data-verification` — только аудит: нет флага автоисправления.

## Как проводить pass

1. Убедитесь, что brief и скрипты стоят в `<SKILLS_ROOT>/projects-data-verification/`.
2. Запустите:

```powershell
python <SKILLS_ROOT>/projects-data-verification/scripts/verify_projects_data.py
```

3. Запишите дату, команду, `summary.errors` / warnings и оставшиеся gaps.
4. Не переносите сюда чужие SHA, внутренние хосты и исключения исходного vault.

## Pass template

| Поле | Значение |
|------|----------|
| date | `YYYY-MM-DD` |
| command | `verify_projects_data.py` |
| errors | `0` (цель, включая `scm`) |
| warnings | список или «нет» |
| gaps | что осталось сознательно |

## Оставшиеся gaps

Пока шаблон пустой. Добавляйте строки после первого прохода на *вашей* копии.

Типичные темы (без чужих фактов): битый YAML, голый wikilink, self-link, незарегистрированный skill, секрет в инфре открытым текстом.

## Related

- [[50_runbooks/maintenance]]
- [[50_runbooks/skill-checklist]]
- [[00_profile/README]]
- [[20_infra/access-matrix]]
