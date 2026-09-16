# Obsidian: что это и как поставить

Obsidian — локальный редактор заметок в Markdown. Vault = обычная папка на диске. Граф, wikilink и плагины живут поверх файлов; облачный аккаунт для базовой работы не нужен.

Официально: [скачать](https://obsidian.md/download), [справка](https://help.obsidian.md/).

## Зачем рядом с Cursor

Чат агента (Cursor, Perplexity и т.п.) можно удалить — работа пропадает, если она жила только в треде. Vault хранит карточки проектов, runbook и решения как файлы. Один и тот же folder открывают как vault Obsidian и как workspace Cursor: агент читает карту, затем в том же ходе обновляет связанные заметки (completion gate).

Obsidian **не** заменяет git и **не** является «памятью модели». Это UI и карта над markdown. Поиск по заметкам в Obsidian — удобство человека; операционная истина для агента — файлы и правила vault.

## Установка (Windows)

1. Скачайте установщик с [obsidian.md/download](https://obsidian.md/download) и установите приложение.
2. Склонируйте этот репозиторий (см. [README](../README.md)).
3. **Скопируйте** `vault-skeleton/` *наружу* из git-клона (например `D:/Knowledge/my-ops-vault`). Не открывайте in-repo путь как единственный рабочий vault: workspace может писать в дерево шаблона.
4. В Obsidian: **Open folder as vault** → выберите копию.
5. Откройте **ту же папку** в Cursor.
6. Дальше — правила, skills и первая карточка проекта: [cursor-integration.md](cursor-integration.md) и Start here в README.

## Карта этого шаблона

Нумерованные разделы Johnny Decimal (`00_profile` … `70_researches` + `90_archive`). Нет `80_*`. Правила Cursor лежат в `.cursor/rules/` вне нумерации. Подробнее: [architecture.md](architecture.md).

Кратко по синтаксису:

- **Wikilink с путём:** `[[10_projects/example_library/runbook]]`, не голый `[[runbook]]`.
- **YAML frontmatter:** `tags`, `last_verified`, `change_source`, закрывающий `---`.
- **Карточка проекта:** README + architecture + runbook + requirements; `decisions.md` — когда появился устойчивый why.

## Опционально: Local REST

Community-плагин **Local REST API** даёт HTTP на `127.0.0.1:<PORT>`. Cursor MCP может писать заметки через него. Ключ API остаётся в UI плагина / локальном секрет-хранилище. Никогда не коммитьте `.obsidian/plugins/obsidian-local-rest-api/data.json`.

Если MCP лежит — правьте markdown на диске и скажите об этом. Зелёный тумблер MCP не доказывает верный порт. Детали: [cursor-integration.md](cursor-integration.md), [SECURITY.md](../SECURITY.md).

## Чего этот шаблон не обещает

- Облачную синхронизацию «из коробки» (это отдельный продукт Obsidian Sync или ваш git/синк).
- Автоматическую память между агентами без записи на диск — память сессии пишется в заметки vault.

## Related docs

- [Проблема и подход](problem-and-approach.md)
- [Архитектура](architecture.md)
- [Интеграция с Cursor](cursor-integration.md)
- [Public-readiness audit](repository-audit.md)
