# Ключевые возможности

Это механизмы, которые держат vault операционным. Без них нумерованные папки снова становятся свалкой заметок.

## Протокол сопровождения

Всегда включённое правило Cursor (`obsidian-vault-maintenance-protocol.mdc`). Считайте vault операционным KB. После содержательного изменения кода, инфры, схемы или процесса обновите связанные заметки в том же ходе.

| Изменение | Обновить |
|-----------|----------|
| Логика / runtime проекта | `10_projects/<project>/{README,architecture,runbook}.md` |
| Зависимости | `10_projects/<project>/requirements.md` |
| Инфра / доступ / хост / сеть | `20_infra/**` |
| Схема / запрос / подключение | `30_db/**` |
| Процесс или политика | `40_patterns/**` и `50_runbooks/**` |
| Профиль / стек | `00_profile/{agent-context,developer-profile,tech-stack}.md` |
| Новый или изменённый локальный skill | `60_skills/<owner>/<skill-name>.md` и Related README проектов |

Устойчивые решения сессии — в `10_projects/<project>/decisions.md` (`session-distill`). Отчёты deep-research — в `70_researches/` (`save-research`). После смыслового изменения кода обновите AST-граф репозитория (`graphify-maintain`) в этом git-репозитории, не в vault.

Если доступны write-инструменты Obsidian MCP — предпочитайте их. Если MCP лежит, правьте файлы на диске и скажите об этом.

Completion gate: устаревшие связанные заметки значат, что задача не закончена. Перед остановкой пройдите [чеклист перед завершением](cursor-integration.md#pre-completion-checklist).

## Стандарты markdown

Второе правило (`obsidian-vault-markdown-standards.mdc`), область `**/*.md`.

- Операционные секции; исполняемые команды; без фейковых цитат `[web:N]`.
- Путь реестра skills: `60_skills/<owner>/<skill-name>.md`. После создания `SKILL.md` на диске зарегистрируйте заметку vault в том же ходе.
- Frontmatter: `tags`, `last_verified`, `change_source`.
- Wikilink с путём; без self-link в `## Related`.
- `## Related` проекта включает README и остальные три ядра, если они есть.
- Строка Stack: `Python: X.Y` → `DB: ...` → `Selenium: да/нет` → `Core libs: ...`.
- `## Project Location` — абсолютный путь, пока репозиторий не склонирован пишите `<PROJECT_ROOT>/<slug>`.

В исходном командном vault формулировки SCM — только Forgejo. В этом публичном шаблоне документируйте *ваш* канонический remote. Не копируйте внутренние URL хостов в заметки.

## Реестр skills

`60_skills/` — индекс локальных project skills, а не вставка дефолтных skills Cursor или плагинов.

- Источник истины поведения — `SKILL.md` рядом со скриптами. Заметка vault хранит purpose, location, triggers и связи.
- Owner — slug проекта или `workspace` для кросс-проектных skills.
- Создать skill без заметки vault — способ потерять trigger на следующей неделе.

Brief, безопасные для шаблона, лежат в `skills/`:

| Skill | Задача |
|-------|--------|
| `projects-data-verification` | Read-only аудит качества vault и rules |
| `vault-router` | Выбрать slug Active Project; один `move_agent_to_root` |
| `session-distill` | Писать ADR в `10_projects/<slug>/decisions.md` |
| `save-research` | Единственный разрешённый launcher deep-research в `70_researches/` |

`graphify-maintain` безопасен как паттерн (AST в *репозитории*), но пути, привязанные к чужому хосту, нужно вычистить до копирования локальной реализации. Не публиковать в этом шаблоне skills с учётными данными или только для одной организации.

Skill — слой процесса: когда звать MCP или CLI, сначала doctor, fallback, критерии успеха. MCP и CLI — руки. Skill — регламент.

## Архив исследований

`70_researches/` не даёт Parallel (и локальному) deep-research помочь один раз и исчезнуть.

- Registry — источник истины дедупа.
- Сырые пакеты прогонов — write-once. Summaries и evergreen можно править.
- Inbox — зона посадки после sync, не второй архив.
- Offline staging сначала *вне* vault, затем sync.
- Полнота = известные прогоны в registry/SOURCES, а не дамп всех чатов агента.

Отклонённые формы перечислены в [problem-and-approach.md](problem-and-approach.md). Фича — разрез Johnny Decimal ops/runs/knowledge/MOC плюс один skill-launcher.

## Стек памяти флота

Cursor не держит автоматическую память между агентами. Не ставить Mem0, Antigravity Memory, agy-memory и вторую базу «памяти».

Три слоя на диске:

| Слой | Что хранит | Где | Skill |
|------|------------|-----|-------|
| AST-граф | Кто кого импортирует, файлы, вызовы | `<repo>/graphify-out/` | `graphify-maintain` |
| ADR сессии | Устойчивые why / запреты / workaround | Vault `10_projects/<slug>/decisions.md` | `session-distill` |
| Роутер | Какой slug, какой один корень | Vault + один `move_agent_to_root` | `vault-router` |

Deep-research — не этот стек. Таблицы фактов KPI/паспорта — не этот стек. Не экспортировать Graphify в папки проектов Obsidian. Коммитить `GRAPH_REPORT.md`; `graph.json` оставить в gitignore.

Общие командные правила Cursor (паттерн `shared-cursor-rules`) — копии внутри `.cursor/rules/` каждого проекта. Хук `docs-before-commit`, если вы его возьмёте, только *напоминает*. Он не пишет документацию, не гоняет Graphify и не блокирует git.

## Аудит и верификация

Разрывы качества нуждаются в журнале, а не в разовой уборке.

- `50_runbooks/obsidian-vault-audit.md` фиксирует проходы аудита и оставшиеся gaps.
- `projects-data-verification` — только аудит: без флага автоисправления. Проверяет frontmatter, wikilink с путём, регистрацию skills, формулировки SCM и связанный инвентарь.
- Опциональная команда (после установки brief и скриптов):

```powershell
python <SKILLS_ROOT>/projects-data-verification/scripts/verify_projects_data.py
```

Ожидайте `summary.errors = 0`, включая категорию `scm`, прежде чем считать задачу сопровождения закрытой.

Не храните пароли открытым текстом в заметках инфры. `30_db` маскирует секреты. Строки access-matrix в скелете — `***` или `secret_ref: vault://...`, никогда живые значения. Исключения исходного vault по секретам в этот шаблон не входят.
