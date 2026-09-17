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
| 2a. Устойчивое решение сессии | `10_projects/<project>/decisions.md` (`session-distill`). Не Mem0 и не реестр фактов |
| 2b. Deep-research отчёт | `70_researches/` (`save-research`), не `decisions.md` |
| 2c. Смысловое изменение кода | AST-граф в *репозитории проекта* (`graphify-maintain`, `GRAPH_REPORT.md`, только `--code-only`). Не в vault |

Те же пункты 2a–2c должны быть в alwaysApply-правиле `obsidian-vault-maintenance-protocol.mdc`, не только здесь.

Если доступны write-инструменты Obsidian MCP — предпочитайте их. Если MCP лежит, правьте файлы на диске и скажите об этом.

Completion gate: устаревшие связанные заметки значат, что задача не закончена. Перед остановкой пройдите [чеклист перед завершением](cursor-integration.md#pre-completion-checklist).

## Стандарты markdown

Второе правило (`obsidian-vault-markdown-standards.mdc`), область `**/*.md`.

- Операционные секции; исполняемые команды; без фейковых цитат `[web:N]`.
- Путь реестра skills: `60_skills/<owner>/<skill-name>.md`. После создания `SKILL.md` на диске зарегистрируйте заметку vault в том же ходе.
- Frontmatter: `tags`, `last_verified`, `change_source`.
- Wikilink с путём; без self-link в `## Related`.
- Заголовок Related — точная строка `## Related`. H2 с префиксом (`## Related Research`) запрещён: верификатор режет блок по точному заголовку, не по prefix.
- `## Related` проекта включает README и остальные три ядра, если они есть.
- Строка Stack: `Python: X.Y` → `DB: ...` → `Selenium: да/нет` → `Core libs: ...`.
- `## Project Location` — абсолютный путь, пока репозиторий не склонирован пишите `<PROJECT_ROOT>/<slug>`.

В этом публичном шаблоне документируйте *ваш* канонический remote как `<GIT_REMOTE>` (любой хост). Канал издателя шаблона — этот GitHub-репозиторий. Не копируйте URL издателя и чужие хосты в операционные заметки.

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

`graphify-maintain` **не** пятый публичный skill этого шаблона. Контракт — [docs/graphify.md](graphify.md): граф в репозитории проекта, `--code-only`, не в vault. Не публиковать skills с учётными данными или только для одной организации.

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
- `projects-data-verification` — только аудит: без флага автоисправления. Один продукт: `verify_projects_data.py`. `verify_vault.py` — его модуль, не второй верификатор.
- Категории контракта: `project_quartet`, `library_links` (точный `## Related`), `inventory` (прямые git-дети `projects_root`), `skills_registry` / `skills_index`, `scm`.
- AlwaysApply-стоп — категория `scm` clean. Полный `errors = 0` — цель журнала аудита, не стоп задачи.
- Опциональная команда (после установки brief *и* локальных скриптов):

```powershell
python <SKILLS_ROOT>/projects-data-verification/scripts/verify_projects_data.py
```

Cache JSON — не источник истины. Подробнее: [docs/verify-contract.md](verify-contract.md).

Не храните пароли открытым текстом в заметках инфры. `30_db` маскирует секреты. Строки access-matrix в скелете — `***` или `secret_ref: vault://...`, никогда живые значения. Исключения исходного vault по секретам в этот шаблон не входят.
