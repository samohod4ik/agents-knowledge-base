# Контракт verify

Публичный шаблон не везёт исполняемые скрипты и не требует их для успеха. Имена и категории ниже — контракт ручного прохода и совместимой *опциональной* локальной реализации `projects-data-verification`.

Один продукт, если скрипт есть: `verify_projects_data.py`. `verify_vault.py` — модуль той же реализации, не второй верификатор.

```powershell
python <SKILLS_ROOT>/projects-data-verification/scripts/verify_projects_data.py
```

Без скрипта закройте те же категории чеклистом и журналом аудита.

## Категории

| Категория | Что ломает | Что делать |
|-----------|------------|------------|
| `scm` | Remote в заметках ≠ ваш `<GIT_REMOTE>` | AlwaysApply-стоп, если скрипт есть. Без скрипта — не закрывать задачу, пока remote в заметках врёт |
| `project_quartet` | Slug в `10_projects/` без README / architecture / runbook / requirements | Квартет только для прикладных репо. Стек → `20_infra/<stack>/` |
| `library_links` | Нет взаимного wikilink в точном `## Related` | Резать Related по точной строке H2, не по prefix |
| `inventory` | Прямой git-ребёнок `projects_root` не в манифесте | Не класть клон шаблона рядом с рабочими репо; либо `excluded` reason `public` |
| `skills_registry` / `skills_index` | Нет `name:` или имени в `60_skills/README` | Заметка из `60_skills/_templates/skill-note.md` в том же ходе |

Полный `errors = 0` — цель журнала аудита. Leftover чужих категорий задачу сопровождения не валит, если `scm` чистый (или ручной SCM-чеклист зелёный) и вы их не трогали.

## Sibling git в `projects_root`

Верификатор смотрит **прямые** git-дети каталога проектов, не весь диск. Временный checkout, публичный шаблон и чужой эксперимент дают `inventory`, если не в `excluded`. Шаблон **не** учит удалять чужие папки.

## Квартет vs инфра

- `10_projects/<slug>/` = прикладной репозиторий → квартет.
- `20_infra/<stack>/` = стек / compose / почва → квартет не требовать.
- Не лечите отсутствие architecture у стека, добавив пустые три файла. Перенесите карточку в инфру.

## Два снимка журнала

Каждый pass в `50_runbooks/obsidian-vault-audit.md` пишите парой, если правили docs:

1. **До** — команда, errors/warnings, `scm`, сознательный leftover.
2. **После** — те же поля. Не сравнивайте с чужими числами из другого vault.

## Cache не SoT

JSON в `cache/verify_report.json` — артефакт последнего прогона. Источник истины — файлы vault и свежий stdout. Не чините «ошибку», которой уже нет на диске, по старому cache.

См. [killer-features.md](killer-features.md), brief `skills/projects-data-verification/SKILL.md`.
