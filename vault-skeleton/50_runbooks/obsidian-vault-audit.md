---
tags: [runbook, audit, vault, maintenance]
status: example
source_agent: public-template
last_verified: 2026-09-16
change_source: public-obsidian-polish
---
# Obsidian Vault Audit

Журнал проходов аудита. Skill `projects-data-verification` — только аудит: нет автоисправления.

## Как проводить pass

1. Установите brief `projects-data-verification` в `<SKILLS_ROOT>/` (или следуйте его workflow вручную).
2. Пройдите Active Projects, frontmatter, path-wikilinks, реестр skills, маски секретов, `<GIT_REMOTE>`.
3. Запишите дату, метод (`manual` или имя локального скрипта), errors / warnings и оставшиеся gaps.
4. Не переносите сюда чужие SHA, внутренние хосты и исключения исходного vault.

## Pass template

| Поле | Значение |
|------|----------|
| date | `YYYY-MM-DD` |
| method | `manual` / optional local script |
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
