---
name: save-research
description: >-
  Use when launching Parallel deep research, saving a trun_* report, sweeping
  chats for new research URLs, or syncing the workspace research inbox.
---

# save-research

Это **контракт**, не поставка автоматизации. Каталога `scripts/` в этом шаблоне нет. Локальные `scripts/` опциональны; не требуйте отсутствующий doctor как блокер.

Источник истины — user/host `<SKILLS_ROOT>/save-research`. В пакет командных project-rules / team-canon **не копировать**.

Установка: `<SKILLS_ROOT>/save-research`.
Указатель vault: `<VAULT>/60_skills/workspace/save-research.md`.

Архивирует Parallel / локальный deep-research в `<VAULT>/70_researches`. Этот skill — единственный разрешённый launcher. Не вызывайте провайдера deep-research в обход скилла.

**Не используй**, когда нужен только `session-distill` (решения → `decisions.md`) или обычный web search без deep research.

## Workflow

1. Прочитай политику и registry: `70_researches/70_research_ops/70.03_RESEARCH-POLICY.md`, `70.02_RUN-REGISTRY.yaml`, `70.01_INDEX.md`.
2. Preflight вручную: scope + question + project-or-problem. Решения: `reuse` | `attach` | `refresh` | `new`. Не превращай `needs-human-review` в `new`.
3. Запусти deep-research через выбранный оператором инструмент (Parallel skill/CLI или иной), **после** preflight.
4. Сохрани сырой пакет под `70_researches/71_runs/` (write-once) и обнови registry / INDEX / LOG в том же ходе.
5. Inbox (`70.05_inbox`) — зона посадки после sync, не второй архив. Offline staging сначала *вне* vault, затем перенос.
6. ADR не писать сюда — только `10_projects/<slug>/decisions.md` через `session-distill`.

Публичный шаблон **не** поставляет launcher-скрипты. Если у оператора есть локальные `scripts/` под этим skill — они опциональны и не обязательны для честного архивирования вручную по каркасу `70_`.

## Запреты

- Вызов провайдера deep-research в обход этого skill
- Дамп всех чатов агента «для полноты»
- Перенос завершённых прогонов в `90_archive/` вместо смены статуса
- Секреты и прод-хосты в сырье
- Требовать отсутствующий `scripts/doctor.py` как блокер

## Успех

Новый прогон отражён в `70.02_RUN-REGISTRY.yaml` и сыром каталоге `71_runs/` (или явно помечен failed с причиной). Агент не вызывал провайдера в обход скилла.
