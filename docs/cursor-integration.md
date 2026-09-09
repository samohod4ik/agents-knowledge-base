# Интеграция с Cursor

Свяжите Cursor с vault так, чтобы агенты сначала читали карту и обновляли заметки до остановки. Этот файл — вид установщика. Зачем так устроено — в [problem-and-approach.md](problem-and-approach.md).

## Скопировать правила vault

Скелет везёт два правила в `vault-skeleton/.cursor/rules/`:

| Файл | Применение |
|------|------------|
| `obsidian-vault-maintenance-protocol.mdc` | `alwaysApply: true` |
| `obsidian-vault-markdown-standards.mdc` | `globs: "**/*.md"` |

Шаги:

1. Откройте `vault-skeleton` (или свою копию) как vault Obsidian *и* как папку Cursor.
2. Держите эти два файла в `<VAULT>/.cursor/rules/`.
3. По желанию скопируйте ту же пару в репозиторий проекта, если его агенты тоже правят vault. Общие командные пакеты правил — в дереве проекта `.cursor/rules/<team>/`; личные правила рядом, не внутри общего пакета.
4. Перезапустите или заново откройте окно Cursor, чтобы правила загрузились. Убедитесь, что оба файла видны в Project Rules.

Адаптированные правила шаблона сохраняют карту обновлений, frontmatter, таблицу H1 и completion gate. Они **не** зашивают внутренний URL Forgejo. Пропишите свой `<GIT_REMOTE>`.

Напоминание `docs-before-commit`, если добавите позже, только напоминает. Оно не пишет заметки и не валит commit.

## Установить четыре skill brief

Этот репозиторий везёт brief в `skills/`. Это регламенты, а не дамп внутренней автоматизации хостов.

| Brief | Ставить как | Когда |
|-------|-------------|-------|
| `skills/projects-data-verification/` | аудит vault / целостность rules | Прежде чем заявить, что документы готовы |
| `skills/vault-router/` | кросс-вопрос, переполненный sidebar | До открытия второго корня |
| `skills/session-distill/` | устойчивые why / workaround / do-not-touch | После смысловой сессии, до commit |
| `skills/save-research/` | Parallel или локальный deep research | Единственный launcher в `70_researches/` |

Установка:

1. Скопируйте каждую папку в `<SKILLS_ROOT>/<skill-name>/`, чтобы `SKILL.md` лежал по этому пути. `<SKILLS_ROOT>` — ваш каталог user skills или `.cursor/skills/` проекта.
2. Внутри brief направьте пути на `<VAULT>` и `<SKILLS_ROOT>`. Не вставляйте абсолютные диски чужой команды.
3. Если в brief есть `scripts/doctor.py` — запустите его. Сначала doctor, затем workflow.
4. Зарегистрируйте указатель `60_skills/workspace/<skill-name>.md` и свяжите его с `60_skills/README.md` в том же ходе.

Не ставить Mem0, Antigravity Memory или второй MCP «памяти» вместо этих четырёх. Не везти в шаблоне skills с учётными данными (внутренний SSH, deploy на именованный хост, орг-отчёты).

## Obsidian Local REST MCP

Предпочтительный путь записи: community-плагин Obsidian **Local REST API**, затем MCP-сервер Cursor, который ходит в этот HTTP API. Для правок vault это лучше generic filesystem MCP.

Настройка на высоком уровне (секреты не в git):

1. В Obsidian включите Community plugins и установите Local REST API.
2. Запомните порт из настроек плагина. Ключ API оставьте в UI плагина.
3. В конфиге MCP Cursor (user-level) добавьте сервер vault Obsidian с URL `http://127.0.0.1:<PORT>`; заголовок авторизации берёт ключ плагина из вашего локального хранилища секретов.
4. Направьте сервер на путь этого vault (`<VAULT>`). Имена инструментов обычно включают list/get/write/patch/search по заметкам.
5. Никогда не коммитьте `.obsidian/plugins/obsidian-local-rest-api/data.json`. Там лежат `apiKey` и ключевой материал. `.gitignore` этого репозитория уже исключает файл.

Если MCP-сервер красный или порт REST не тот, пишите markdown на диск и скажите, что MCP пропущен. Зелёный тумблер MCP не доказывает, что порт REST совпал.

Не кладите API key, Bearer-токены и закрытые ключи плагина ни в заметки vault, ни в этот репозиторий.

<a id="pre-completion-checklist"></a>

## Чеклист перед завершением

Скопируйте это в свой runbook сопровождения. Задача не закончена, пока применимый пункт не отмечен.

- [ ] YAML frontmatter закрыт (`---` / tags / `last_verified` / `change_source` / `---`).
- [ ] В карточках проектов `## Stack` содержит Python, DB, Selenium (да/нет) и core libs.
- [ ] Wikilink с путём: `[[10_projects/example_library/runbook]]`, не `[[runbook]]`.
- [ ] Нет self-link в `## Related`.
- [ ] Git-remote в заметках совпадают с *вашим* `<GIT_REMOTE>`; нет оставшихся внутренних URL хостов.
- [ ] Секреты замаскированы. Инфра ссылается на строки `20_infra/access-matrix` с `***` или `secret_ref`, без второй копии открытым текстом.
- [ ] Хаб профиля (`00_profile/tech-stack`, `00_profile/developer-profile`) всё ещё совпадает с Active Projects.
- [ ] Новые или изменённые Cursor skills зарегистрированы в `60_skills/README.md`.
- [ ] Опционально: `python <SKILLS_ROOT>/projects-data-verification/scripts/verify_projects_data.py` — `summary.errors = 0`, включая категорию `scm`.

## Git-хостинг: шаблон GitHub vs командный Forgejo

| Канал | Роль |
|-------|------|
| Этот репозиторий GitHub | Публичное распространение *шаблона* |
| Командный self-hosted Forgejo (или выбранный вами хост) | Канонические remote *ваших* рабочих репозиториев |

Исходный командный vault документирует Forgejo как единственный git-хостинг операционных заметок. Эта политика локальна для той команды. Публикующий remote этого шаблона — GitHub. Не направляйте склонированные example-проекты на GitHub издателя, если вы не собираетесь форкать сам шаблон.

Когда заполняете скелет:

- Задайте `<GIT_REMOTE>` своим реальным URL клона.
- `gh` (если пользуетесь) держите нацеленным на GitHub.com только для этого шаблона.
- Инструменты issue/PR команды направляйте на ваш Forgejo или другой внутренний хост. Не считайте GitHub внутренним forge.

Пароли учёток, литералы LAN и ключи плагинов не должны попадать в markdown ни одного из каналов.
