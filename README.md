# Agents Knowledge Base

Public MIT template for an **operational** Obsidian vault paired with Cursor. A third person can rebuild the same agent-readable map without anyone's secrets, hosts, or live runbooks.

GitHub is the **template distribution** channel. Your team's git host (self-hosted Forgejo or otherwise) stays the canonical remote for *your* working repos. Point `<GIT_REMOTE>` at your host, not at the publisher.

Operational notes in `docs/` and later vault files are **Russian-primary**. This root README is bilingual (English + Russian) so a stranger can bootstrap in five minutes.

---

## English

### Problem

A note dump looks complete and still forces the next chat to guess. An operational knowledge base stores commands, absolute project paths, stack facts, and path-qualified links that an agent can act on in one or two searches.

This template publishes the current numbered vault (`00_`–`70_` plus `90_`), not a trimmed older tree. It does **not** ship anyone's live `10_projects` cards, infra passwords, or research run packets.

### Audience

- **Human operator** — copies the skeleton, fills placeholders, keeps the vault honest after real work.
- **Cursor agent** — reads the vault first, then updates related notes in the same turn after a code, infra, schema, or process change.

### Security warning

Do not paste production hosts, accounts, passwords, DSN, tokens, plugin `apiKey` values, or private keys into this tree. Use masks (`***`, `secret_ref: vault://...`) and placeholders (`<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, `<GIT_REMOTE>`). Never commit Obsidian Local REST `data.json`. Bootstrap does not need a team LAN, VPN, or internal DNS.

### Clone

```text
git@github.com:samohod4ik/agents-knowledge-base.git
```

```powershell
git clone git@github.com:samohod4ik/agents-knowledge-base.git
```

Public GitHub only. No internal git host is required.

### Five-minute bootstrap

All steps are local disk plus public GitHub. Optional REST stays on `127.0.0.1`.

1. **Clone** this repository with the URL above.
2. **Copy or open `vault-skeleton/`** as an Obsidian vault (Open folder as vault). That directory is the anonymized numbered map, not a live team vault.
3. **Optional Local REST** — enable the Obsidian Local REST API community plugin and point a Cursor MCP server at `http://127.0.0.1:<PORT>`. Keep the API key in the plugin UI / your local secret store. If MCP is down, edit markdown on disk and say so. Details: [docs/cursor-integration.md](docs/cursor-integration.md).
4. **Open the same vault folder in Cursor** so agents and Obsidian share one tree.
5. **Copy `.cursor/rules`** from `vault-skeleton/.cursor/rules/` into `<VAULT>/.cursor/rules/` (maintenance protocol + markdown standards). Reload Cursor so both Project Rules appear.
6. **Install `skills/`** — copy each brief folder into `<SKILLS_ROOT>/<skill-name>/` so `SKILL.md` sits at that path. `<SKILLS_ROOT>` is your user skills directory or the project's `.cursor/skills/`.
7. **Fill placeholders** — replace `<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, and `<GIT_REMOTE>` with *your* machine and *your* git host. Do not copy another team's paths.
8. **Add the first real project card** under `10_projects/<your-slug>/` (README, architecture, runbook, requirements; add `decisions.md` when a durable why appears). Point the vault Active Projects list at that card. Template examples, when present, are only `example_library` and `example_service`.

### Conceptual docs (this commit)

- [Problem and approach](docs/problem-and-approach.md) — operational KB vs note dump; Obsidian + Cursor; design evolution; rejected Mem0 / flat research / chat-dump / PARA-as-folders.
- [Architecture](docs/architecture.md) — numbered `00_`–`70_` + `90_` map; agent read-first order; frontmatter / H1 / wikilink rules; vault vs project git.
- [Killer features](docs/killer-features.md) — maintenance protocol, markdown standards, skills registry, research archive, fleet-memory stack, audit.
- [Cursor integration](docs/cursor-integration.md) — rules copy, four skill briefs, Local REST without a real key, pre-completion checklist, GitHub template vs team git host.

### Later template paths

These layout paths belong to later artifacts of the same repository. They are listed here only by **plan-defined purpose**. Do not treat them as a copy of a live vault or assume extra files beyond that purpose.

| Path | Purpose |
|------|---------|
| `vault-skeleton/` | Anonymized numbered vault you copy and open in Obsidian |
| `vault-skeleton/README.md` | Vault map and Active Projects list |
| `vault-skeleton/agent-context.md` | Short agent working rules |
| `vault-skeleton/00_profile/` … `90_archive/` | Numbered ops sections with placeholders (no `80_*`) |
| `vault-skeleton/10_projects/example_library/` | Example library project card |
| `vault-skeleton/10_projects/example_service/` | Example service project card |
| `vault-skeleton/.cursor/rules/` | Two vault Cursor rules (`.mdc`) |
| `vault-skeleton/60_skills/` | Vault-side registry notes for local skills |
| `vault-skeleton/70_researches/` | Johnny Decimal research archive scaffold (no real `trun_*`) |
| `skills/` | Four portable briefs: `projects-data-verification`, `vault-router`, `session-distill`, `save-research` |

License: [MIT](LICENSE), copyright 2026 `samohod4ik`.

---

## Русский

### Проблема

Свалка заметок выглядит полной, но следующий чат всё равно угадывает. Операционная база знаний хранит команды, абсолютные пути проектов, факты стека и wikilink с путём, по которым агент действует за один-два поиска.

Этот шаблон публикует текущее нумерованное дерево (`00_`–`70_` плюс `90_`), а не урезанное старое. Живые карточки `10_projects`, пароли инфры и пакеты research-прогонов **не** входят.

### Аудитория

- **Человек-оператор** — копирует скелет, заполняет плейсхолдеры, держит vault честным после реальной работы.
- **Агент Cursor** — сначала читает карту, затем в том же ходе обновляет связанные заметки после изменения кода, инфры, схемы или процесса.

### Предупреждение по безопасности

Не вставляйте в это дерево прод-хосты, учётки, пароли, DSN, токены, `apiKey` плагина и закрытые ключи. Маски (`***`, `secret_ref: vault://...`) и плейсхолдеры (`<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, `<GIT_REMOTE>`). Файл Local REST `data.json` не коммитить. Для bootstrap не нужны командный LAN, VPN и внутренний DNS.

### Клон

```text
git@github.com:samohod4ik/agents-knowledge-base.git
```

```powershell
git clone git@github.com:samohod4ik/agents-knowledge-base.git
```

Только публичный GitHub. Внутренний git-хост не требуется.

### Bootstrap за пять минут

Все шаги — локальный диск и публичный GitHub. Опциональный REST только на `127.0.0.1`.

1. **Клонируйте** репозиторий URL выше.
2. **Скопируйте или откройте `vault-skeleton/`** как vault Obsidian (Open folder as vault). Это анонимизированная нумерованная карта, не живой командный vault.
3. **Опционально Local REST** — включите community-плагин Obsidian Local REST API и направьте MCP Cursor на `http://127.0.0.1:<PORT>`. Ключ API оставьте в UI плагина / локальном хранилище секретов. Если MCP лежит — правьте markdown на диске и скажите об этом. Подробности: [docs/cursor-integration.md](docs/cursor-integration.md).
4. **Откройте ту же папку vault в Cursor**, чтобы агенты и Obsidian делили одно дерево.
5. **Скопируйте `.cursor/rules`** из `vault-skeleton/.cursor/rules/` в `<VAULT>/.cursor/rules/` (протокол сопровождения + стандарты markdown). Перезагрузите Cursor, чтобы оба Project Rules были видны.
6. **Установите `skills/`** — скопируйте каждую папку brief в `<SKILLS_ROOT>/<skill-name>/`, чтобы `SKILL.md` лежал по этому пути. `<SKILLS_ROOT>` — каталог user skills или `.cursor/skills/` проекта.
7. **Заполните плейсхолдеры** — подставьте *свои* `<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, `<GIT_REMOTE>`. Чужие абсолютные пути не копировать.
8. **Добавьте первую реальную карточку проекта** в `10_projects/<your-slug>/` (README, architecture, runbook, requirements; `decisions.md` — когда появится устойчивый why). Укажите её в Active Projects. Примеры шаблона, когда они появятся, только `example_library` и `example_service`.

### Концептуальные документы (этот коммит)

- [Проблема и подход](docs/problem-and-approach.md) — операционный KB vs свалка; Obsidian + Cursor; эволюция дизайна; отказ от Mem0 / плоского research / дампа чатов / PARA как дерева папок.
- [Архитектура](docs/architecture.md) — карта `00_`–`70_` + `90_`; порядок чтения агентом; frontmatter / H1 / wikilink; vault vs git проектов.
- [Ключевые возможности](docs/killer-features.md) — протокол сопровождения, стандарты markdown, реестр skills, архив исследований, стек памяти флота, аудит.
- [Интеграция с Cursor](docs/cursor-integration.md) — копирование правил, четыре skill brief, Local REST без настоящего ключа, чеклист перед завершением, GitHub-шаблон vs командный git-хост.

### Поздние пути шаблона

Эти пути — поздние артефакты того же репозитория. Здесь указано только **назначение из плана**. Это не копия живого vault и не обещание лишних файлов сверх этой роли.

| Путь | Назначение |
|------|------------|
| `vault-skeleton/` | Анонимизированный нумерованный vault, который копируют и открывают в Obsidian |
| `vault-skeleton/README.md` | Карта vault и список Active Projects |
| `vault-skeleton/agent-context.md` | Короткие правила работы агента |
| `vault-skeleton/00_profile/` … `90_archive/` | Нумерованные ops-разделы с плейсхолдерами (без `80_*`) |
| `vault-skeleton/10_projects/example_library/` | Пример карточки library-проекта |
| `vault-skeleton/10_projects/example_service/` | Пример карточки service-проекта |
| `vault-skeleton/.cursor/rules/` | Два vault-правила Cursor (`.mdc`) |
| `vault-skeleton/60_skills/` | Заметки-реестр локальных skills на стороне vault |
| `vault-skeleton/70_researches/` | Каркас архива исследований Johnny Decimal (без живых `trun_*`) |
| `skills/` | Четыре переносимых brief: `projects-data-verification`, `vault-router`, `session-distill`, `save-research` |

Лицензия: [MIT](LICENSE), copyright 2026 `samohod4ik`.
