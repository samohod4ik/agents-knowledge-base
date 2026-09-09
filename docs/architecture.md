# Архитектура

В живом vault нет папки `80_*`. Публичный скелет следует той же карте: `00_`–`70_` плюс `90_`. Не добавлять параллельное дерево PARA и не сплющивать исследования в `raw/` и `structured/`.

## Нумерованные разделы

| Раздел | Назначение |
|--------|------------|
| `00_profile/` | Профиль оператора, стек, хаб агента (английский `agent-context`) |
| `10_projects/` | На slug: README, architecture, runbook, requirements, часто `decisions.md` |
| `20_infra/` | Серверы, сети, access-matrix (маски), каталог Cursor MCP |
| `30_db/` | Подключения с маскированными секретами, схемы, важные запросы |
| `40_patterns/` | Паттерны кода и git, стек памяти флота, паттерн общих Cursor rules |
| `50_runbooks/` | Сопровождение, аудит, гайды по skills, deploy и incident |
| `60_skills/` | Реестр *локальных* project skills Cursor (не дефолтные skills Cursor) |
| `70_researches/` | Архив исследований Johnny Decimal (ops / runs / evergreen / MOC) |
| `90_archive/` | Устаревшие заметки |

Правила Cursor живут **вне** нумерации: `.cursor/rules/` — протокол сопровождения vault и стандарты markdown. Это конфиг workspace, не раздел `00_`–`90_`.

Корневые файлы, которые агент должен ждать: `README.md` (разделы + Active Projects) и `agent-context.md` (короткие правила работы).

Карточки проектов — квартет плюс decisions. Не брать за образец заглушку без architecture, runbook и requirements. В этом шаблоне примеры — `example_library` и `example_service`.

## Порядок чтения агентом

1. `README.md` — нумерованные разделы и Active Projects.
2. Корневой `agent-context.md` — короткие локальные правила.
3. `00_profile/agent-context.md` — операционный хаб (позиция по памяти, правила обновления).
4. `00_profile/developer-profile.md` и `00_profile/tech-stack.md`.
5. По задаче:
   - skills: `60_skills/README.md`
   - память: `40_patterns/fleet-memory-stack.md`
   - паттерн общих правил: `40_patterns/shared-cursor-rules.md` (в скелете — обобщённая заметка, не командный канон)
   - процесс: `50_runbooks/maintenance.md`
   - каталог MCP: `20_infra/cursor-mcp.md`

Позиция хаба по памяти: Graphify AST + `decisions.md` + vault-router. Без Mem0 и Antigravity. Deep research идёт в `70_researches/` через `save-research`.

## Соглашения по заметкам

### Frontmatter

На каждом содержательном правке:

- Контекстные `tags` (не один и тот же список на каждой заметке)
- `last_verified: YYYY-MM-DD`
- `change_source` (commit, ticket, incident или имя задачи)
- Закрывающий `---`, чтобы YAML оставался валидным

### Заголовки

| Тип документа | H1 |
|---------------|-----|
| README | `# {project}` |
| architecture | `# {project} — architecture` |
| runbook | `# {project} — runbook` |
| requirements | `# {project} — requirements` |
| skill index | `# {owner} — skills` |
| skill note | `# {skill-name}` |

В README проекта также нужны `## Project Location` (абсолютный путь репозитория), нормализованный `## Stack` и ссылка на `requirements.md`.

Порядок `## Stack`: версия Python, тип/версия БД или контур, Selenium да/нет, основные библиотеки.

### Wikilink и Related

- Только с путём: `[[10_projects/<project>/runbook]]`, никогда голый `[[runbook]]`.
- `## Related` с обеих сторон для связей project / infra / DB / runbook.
- Запрещены self-link в `## Related`.
- Заметки хаба профиля должны ссылаться на README каждого Active Project.
- Заметки skills живут в `60_skills/<owner>/<skill-name>.md`. Owner — slug проекта или `workspace`.

Предпочитать операционные секции (Purpose, Run, Risks, Incident, Related), а не эссе. Команды и пути должны быть реальными *для вашей* машины; пока не заполнены, используйте `<PROJECT_ROOT>`, `<VAULT>`, `<SKILLS_ROOT>` и `<GIT_REMOTE>`.

## Что в vault, что в git-репозиториях

| Артефакт | Где живёт | Зачем |
|----------|-----------|-------|
| Карточки проектов, инфра, БД, runbook, индекс skills | Vault | Карта агента и документы того же хода |
| Исходный код | Git-репозиторий каждого проекта | Vault — не второй клон |
| AST-граф `graphify-out/graph.json` | Репозиторий проекта, в gitignore | Тысячи узлов; не заметки vault |
| Человеческая карта `GRAPH_REPORT.md` | Репозиторий проекта, в git | Обозримая структурная карта |
| ADR / do-not-touch | Vault `10_projects/<slug>/decisions.md` | Память сессии на диске |
| Пакеты deep-research | Vault `70_researches/` | Вне стека памяти флота |
| Копии project rules Cursor | `.cursor/rules/` проекта | Общий командный паттерн; vault держит пояснение |
| Local REST `apiKey` / закрытый ключ плагина | Данные плагина Obsidian (игнор) | Никогда не коммитить |

Extract Graphify только структурный (`--code-only`, без LLM-меток). Не делать `export obsidian` графа кода в `10_projects/`. Не считать Graphify semantic memory.

## Форма архива исследований

Идентификаторы Johnny Decimal `70.xx` существуют только внутри `70_researches/`:

| Область | Назначение |
|---------|------------|
| `70_research_ops/` | INDEX, registry прогонов, политика, шаблоны, inbox, LOG, SOURCES |
| `71_runs/` | Write-once сырые пакеты + пересобираемые summaries |
| `72_knowledge/` | Evergreen-заметки |
| `73_mocs/`, `74_exports/`, `75_lifecycle/` | Навигация и представления жизненного цикла |

Факты политики, от которых зависит архитектура:

- `save-research` — единственный разрешённый launcher deep-research.
- Ключ дедупа: scope + question + project-or-problem. Даты в ключе нет.
- Завершённые прогоны остаются на месте. Меняйте поля статуса; не переносите их в `90_archive/`.
- ADR остаётся в `10_projects/<slug>/decisions.md`. Не создавать форк decisions под `70_`.
- Шаблон везёт пустые registry/templates, не живые пакеты `trun_*`.

## Чего нет в этом публичном дереве

- Операционные runbook `10_projects/*` исходного vault
- Пароли access-matrix, `apiKey` плагина, DSN, токены
- Адреса прод-LAN и внутренние имена учёток
- Skills, привязанные к хосту (deploy на внутренний хост, SSH в лабораторию, генераторы орг-отчётов)
- Сырые research-пакеты под `71_runs/`

Заполните плейсхолдеры. Направьте `<GIT_REMOTE>` на *ваш* канонический хост. Этот репозиторий GitHub — канал шаблона, а не замена командному remote Forgejo (или другому внутреннему хосту).
