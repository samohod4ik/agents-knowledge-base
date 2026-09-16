# Agents Knowledge Base

Public MIT template for an **operational** Obsidian vault paired with Cursor. A third person can rebuild the same agent-readable map without anyone's secrets, hosts, or live runbooks.

GitHub is the **template distribution** channel. Your team's git host stays the canonical remote for *your* working repos. Point `<GIT_REMOTE>` at your host, not at the publisher.

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

Do not paste production hosts, accounts, passwords, DSN, tokens, plugin `apiKey` values, or private keys into this tree. Use masks (`***`, `secret_ref: vault://...`) and placeholders (`<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, `<GIT_REMOTE>`, `<PORT>`). Never commit Obsidian Local REST `data.json`. Bootstrap does not need a team LAN, VPN, or internal DNS. See [SECURITY.md](SECURITY.md).

### Start here

All steps are local disk plus public GitHub. Optional REST stays on `127.0.0.1`.

1. **Install Obsidian** — [download](https://obsidian.md/download). What/why: [docs/obsidian.md](docs/obsidian.md).
2. **Clone** this repository:

```text
https://github.com/samohod4ik/agents-knowledge-base.git
```

```powershell
git clone https://github.com/samohod4ik/agents-knowledge-base.git
```

3. **Copy `vault-skeleton/` outside the checkout** and open the copy in Obsidian (**Open folder as vault**). Do not treat the in-repo path as your only working vault.
4. **Open the same folder in Cursor** so agents and Obsidian share one tree (`<VAULT>`).
5. **Copy `.cursor/rules`** from `vault-skeleton/.cursor/rules/` into `<VAULT>/.cursor/rules/`. Reload Cursor so both Project Rules appear.
6. **Install `skills/`** — copy each brief folder into `<SKILLS_ROOT>/<skill-name>/` so `SKILL.md` sits at that path. `<SKILLS_ROOT>` is your user skills directory or the project's `.cursor/skills/`. File-on-disk is not proof the agent discovers the skill — trigger it once.
7. **Fill placeholders** — replace `<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, and `<GIT_REMOTE>` with *your* machine and *your* git host.
8. **Add the first real project card** under `10_projects/<your-slug>/` (README, architecture, runbook, requirements; add `decisions.md` when a durable why appears). Point Active Projects at that card. Template examples are only `example_library` and `example_service`.

Optional Local REST MCP: [docs/cursor-integration.md](docs/cursor-integration.md).

### Configuration contract

| Placeholder | Role |
|---|---|
| `<VAULT>` | **Core.** Your copied vault root |
| `<SKILLS_ROOT>` | **Core.** Agent-discovered skill directory |
| `<PROJECT_ROOT>` | **Optional.** Absolute path to a working code repo |
| `<GIT_REMOTE>` | **Optional.** Your team git host / clone URL base |
| `<PORT>` | **Optional.** Obsidian Local REST loopback port |
| `<HOST>` | **Optional.** Masked infra hostname placeholder |

### Documentation

- [Obsidian install and role](docs/obsidian.md)
- [Problem and approach](docs/problem-and-approach.md)
- [Architecture](docs/architecture.md)
- [Killer features](docs/killer-features.md)
- [Cursor integration](docs/cursor-integration.md)
- [Public-readiness audit](docs/repository-audit.md)
- [Contributing](CONTRIBUTING.md), [security](SECURITY.md), [repo agent rules](AGENTS.md)

### Template layout

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
| `tests/` | CPU hygiene checks (no host paths, bilingual README, brief-only skills). Run: `python -m unittest discover -s tests -v` |

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

Не вставляйте в это дерево прод-хосты, учётки, пароли, DSN, токены, `apiKey` плагина и закрытые ключи. Маски (`***`, `secret_ref: vault://...`) и плейсхолдеры (`<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, `<GIT_REMOTE>`, `<PORT>`). Файл Local REST `data.json` не коммитить. Для bootstrap не нужны командный LAN, VPN и внутренний DNS. См. [SECURITY.md](SECURITY.md).

### Start here

1. **Установите Obsidian** — [скачать](https://obsidian.md/download). Что/зачем: [docs/obsidian.md](docs/obsidian.md).
2. **Клонируйте** репозиторий:

```powershell
git clone https://github.com/samohod4ik/agents-knowledge-base.git
```

3. **Скопируйте `vault-skeleton/` наружу** из клона и откройте копию в Obsidian (**Open folder as vault**).
4. **Откройте ту же папку в Cursor** (`<VAULT>`).
5. **Скопируйте `.cursor/rules`** из скелета в `<VAULT>/.cursor/rules/`. Перезагрузите Cursor.
6. **Установите `skills/`** в `<SKILLS_ROOT>/<skill-name>/`. Файл на диске ≠ доказательство, что агент skill видит — вызовите его один раз.
7. **Заполните плейсхолдеры** своими путями и своим `<GIT_REMOTE>`.
8. **Добавьте первую карточку** в `10_projects/<your-slug>/` и укажите её в Active Projects.

### Контракт плейсхолдеров

| Плейсхолдер | Роль |
|---|---|
| `<VAULT>` | **Ядро.** Корень вашей копии vault |
| `<SKILLS_ROOT>` | **Ядро.** Каталог skills агента |
| `<PROJECT_ROOT>` | **Опционально.** Абсолютный путь рабочего репо |
| `<GIT_REMOTE>` | **Опционально.** Ваш командный git-хост |
| `<PORT>` | **Опционально.** Порт Local REST на loopback |
| `<HOST>` | **Опционально.** Маска имени хоста в инфре |

### Документация

- [Obsidian: установка и роль](docs/obsidian.md)
- [Проблема и подход](docs/problem-and-approach.md)
- [Архитектура](docs/architecture.md)
- [Ключевые возможности](docs/killer-features.md)
- [Интеграция с Cursor](docs/cursor-integration.md)
- [Аудит готовности к public](docs/repository-audit.md)
- [Contributing](CONTRIBUTING.md), [security](SECURITY.md), [правила агента репо](AGENTS.md)

### Раскладка шаблона

| Путь | Назначение |
|------|------------|
| `vault-skeleton/` | Анонимизированный нумерованный vault для копии в Obsidian |
| `skills/` | Четыре переносимых brief без обязательных скриптов |
| `tests/` | CPU-проверки гигиены публичного дерева |

Лицензия: [MIT](LICENSE), copyright 2026 `samohod4ik`.
