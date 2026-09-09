---
name: save-research
description: >-
  Use when launching Parallel deep research, saving a trun_* report, sweeping
  chats for new research URLs, or syncing the workspace research inbox.
---

# save-research

Установка: `<SKILLS_ROOT>/save-research`.
Указатель vault: `<VAULT>/60_skills/workspace/save-research.md`.

Архивирует Parallel / локальный deep-research в `<VAULT>/70_researches`. Этот skill — единственный разрешённый launcher. Не вызывайте провайдера в обход скилла (в том числе `parallel-cli research run`).

**Не используй**, когда нужен только `session-distill` (решения → `decisions.md`) или обычный web search без deep research.

## Doctor

Публичный шаблон везёт только этот brief (`SKILL.md`), без исполняемых скриптов. Команды ниже — контракт совместимой локальной реализации. Установите или предоставьте её в `<SKILLS_ROOT>/save-research/` до запуска Doctor и остальных команд.

```powershell
python <SKILLS_ROOT>/save-research/scripts/doctor.py
```

## Workflow

1. Doctor.
2. Preflight (скрипты делают это сами; агент не пропускает):

```powershell
python <SKILLS_ROOT>/save-research/scripts/preflight.py --scope <scope> --question "..."
```

Решения: `reuse` | `attach` | `refresh` | `new`. Не превращай `needs-human-review` в `new`.

3. Launch:

```powershell
python <SKILLS_ROOT>/save-research/scripts/save_one.py run --scope <scope> --question "..." --constraints ""
```

4. Sweep (после сессии / по запросу; не stop-hook):

```powershell
python <SKILLS_ROOT>/save-research/scripts/ingest_from_chats.py --sweep-only
```

5. Offline staging вне vault, затем sync:

```powershell
python <SKILLS_ROOT>/save-research/scripts/save_one.py sync-inbox
```

Пропусти, если `research_run_id` уже `complete` или `failed`.

## Fallback

- Vault недоступен для записи → inbox вне vault, скажи пользователю.
- CLI провайдера нет → stub и `capture_error`.
- Obsidian MCP лежит → пиши файлы vault на диск.

## Успех

Новый `trun_*` есть в `70.02_RUN-REGISTRY.yaml` и сыром каталоге прогонов. Агент не вызывал провайдера в обход скилла.
