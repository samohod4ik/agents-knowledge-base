---
name: projects-data-verification
description: >-
  Use when the user asks for проверка Obsidian, аудит vault, верификация
  документации, obsidian-vault-audit, projects-data-verification,
  projects_data_verification, целостность правил, качество хранилища,
  60_skills, skill-checklist.
---

# Projects Data Verification

Это **контракт**, не поставка автоматизации. Каталога `scripts/` в этом шаблоне нет. `doctor` падает, пока нет локальной реализации в `<SKILLS_ROOT>/projects-data-verification/`.

## Назначение

Read-only аудит vault `<VAULT>` и параллельная проверка локальных проектов: карточки, общие Cursor rules, `AGENTS.md`, реестр skills, SCM относительно вашего `<GIT_REMOTE>`.

Скрипты только читают и пишут JSON-отчёт. Они не правят vault, rules, hooks и код проектов. Подтверждённые правки docs — отдельный запрос по протоколу сопровождения, не режим этого skill.

Покрывает бывший контур `obsidian-vault-verification`. Старые триггеры (`проверка Obsidian`, `obsidian-vault-audit`) остаются валидными.

**Не используй**, когда:
- нужно только обновить один project README после code change;
- пользователь просит не трогать Obsidian и не проверять docs.

## Doctor

Публичный шаблон везёт только этот brief (`SKILL.md`), без исполняемых скриптов. Команды ниже — контракт совместимой локальной реализации. Установите или предоставьте её в `<SKILLS_ROOT>/projects-data-verification/` до запуска Doctor и остальных команд.

```powershell
python <SKILLS_ROOT>/projects-data-verification/scripts/doctor.py
```

Doctor падает, если нет скрипта скилла, корня `<VAULT>` / workspace или конфига инвентаря проектов.

## Run

```powershell
python <SKILLS_ROOT>/projects-data-verification/scripts/verify_projects_data.py `
  --output <SKILLS_ROOT>/projects-data-verification/cache/verify_report.json
```

Не подменяйте этот верификатор одиночным `verify_vault.py`. Cache — артефакт свежего прогона, не источник истины.

Exit code `1` при error-level findings. Warnings не роняют `ok`. Runtime probes без evidence получают статус `not_tested` и не считаются regression.

## Что проверяет

Категории контракта (имена как в отчёте):

| Категория | Смысл |
|-----------|--------|
| `project_quartet` | У каждого slug в `10_projects/` есть README + architecture + runbook + requirements. Стеки в `20_infra/` сюда не входят |
| `library_links` | Взаимные wikilink **только** в точном H2 `## Related`. Префикс (`## Related Research`) — не Related |
| `inventory` | Прямые git-дети `projects_root`. Клон этого шаблона там — ошибка; потребитель может `excluded` с reason `public` |
| `skills_registry` / `skills_index` | Frontmatter `name:` + имя в `60_skills/README`. Cache JSON не SoT |
| `scm` | Remote в заметках совпадает с вашим `<GIT_REMOTE>` |

Также: hub, frontmatter, tags, self-link, Active project ↔ путь на диске ↔ slug vault.

Не подменяйте верификатор одиночным `verify_vault.py` — это модуль той же реализации.

## Fallback

- Нет скрипта — остановись и скажи, что brief не установлен в `<SKILLS_ROOT>`.
- Нет MCP Obsidian — читай `<VAULT>` с диска; отчёт всё равно пишет скрипт.
- Нет конфига инвентаря — не выдумывай список проектов.

## Успех

AlwaysApply-стоп: категория `scm` clean. Полный `errors = 0` — цель журнала аудита, не стоп задачи сопровождения. JSON-отчёт существует. Cache JSON — не источник истины. Скрипт не менял vault и docs.
