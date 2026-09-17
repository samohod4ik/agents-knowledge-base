---
tags: [runbook, audit, vault, maintenance]
status: example
source_agent: public-template
last_verified: 2026-09-17
change_source: public-template-contract
---
# Obsidian Vault Audit

Журнал проходов аудита. Skill `projects-data-verification` — только аудит: нет автоисправления. AlwaysApply-стоп без скрипта = чеклист + эта страница. Со скриптом стоп = `scm` clean. Полный `errors = 0` — цель журнала.

## Как проводить pass

1. Установите brief `projects-data-verification` в `<SKILLS_ROOT>/` (или следуйте его workflow вручную).
2. Пройдите Active Projects, frontmatter, path-wikilinks, реестр skills, маски секретов, `<GIT_REMOTE>`.
3. Запишите дату, метод (`manual` или имя локального скрипта), errors / warnings и оставшиеся gaps.
4. Не переносите сюда чужие SHA, внутренние хосты и исключения исходного vault.

## Pass template

| Поле | Значение |
|------|----------|
| date | `YYYY-MM-DD` |
| method | `manual` / optional local `verify_projects_data.py` |
| errors | число (цель журнала `0`; стоп задачи — только грязный `scm`, и только если скрипт есть) |
| warnings | список или «нет» |
| scm | `clean` / список findings |
| leftover | сознательный долг вне скоупа pass |
| gaps | что осталось сознательно |

## Пример pass (вымышленный)

Это учебная строка, не чужой журнал и не числа живого vault.

| Поле | До | После |
|------|----|-------|
| date | 2026-09-17 | 2026-09-17 |
| method | `verify_projects_data.py` (optional) | `verify_projects_data.py` (optional) |
| errors | 4 | 1 |
| warnings | 1 (`example_library` без ссылки на образец stack-note — вне скоупа) | 1 (тот же warning) |
| scm | clean | clean |
| leftover | `inventory`: клон шаблона в `projects_root`; `library_links`: черновик без точного `## Related` | `inventory`: клон шаблона — добавить `excluded` reason `public` на *вашей* машине |

Pass закрыт по AlwaysApply: `scm` clean. Leftover записан, не «ещё те же 4».

## Оставшиеся gaps

После примера выше сознательный leftover — `inventory` на клоне шаблона внутри `projects_root`. На своей копии замените таблицу своими прогонами.

Типичные темы (без чужих фактов): битый YAML, голый wikilink, self-link, незарегистрированный skill, секрет в инфре открытым текстом, H2 `## Related Research`.

## Related

- [[50_runbooks/maintenance]]
- [[50_runbooks/skill-checklist]]
- [[00_profile/README]]
- [[20_infra/access-matrix]]
