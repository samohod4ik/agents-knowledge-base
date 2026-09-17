---
tags: [runbook, audit, vault, maintenance]
last_verified: 2026-09-17
change_source: public-template-contract
---
# Obsidian Vault Audit

Журнал проходов аудита. Верификатор `projects-data-verification` — только аудит: нет флага автоисправления. AlwaysApply-стоп = `scm` clean. Полный `errors = 0` — цель журнала.

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
| errors | число (цель журнала `0`; стоп задачи — только грязный `scm`) |
| warnings | список или «нет» |
| scm | `clean` / список findings |
| leftover | сознательный долг вне скоупа pass |
| gaps | что осталось сознательно |

## Пример pass (вымышленный)

Это учебная строка, не чужой журнал и не числа живого vault.

| Поле | До | После |
|------|----|-------|
| date | 2026-09-17 | 2026-09-17 |
| command | `verify_projects_data.py` | `verify_projects_data.py` |
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
