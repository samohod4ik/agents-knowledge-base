---
tags: [pattern, memory, graphify, cursor, session-distill, vault-router]
last_verified: 2026-09-09
change_source: task-6-consistency-fix
---
# Fleet Memory Stack

Cursor не даёт встроенную память между агентами. Межсессионный контекст — три слоя на диске, не второй движок памяти.

## Decision

- **Decision:** Структурный AST-граф (`graphify-maintain`) + ADR в `10_projects/<slug>/decisions.md` (`session-distill`) + vault как роутер и один активный корень (`vault-router`).
- **Anti:** Не ставить Mem0, Antigravity Memory, второй SQLite «памяти». Не делать из Graphify semantic memory. Не `export obsidian` тысяч заметок в `10_projects/`.

## Три слоя

| Слой | Что хранит | Где | Skill |
|------|------------|-----|-------|
| AST-граф | кто кого импортирует, файлы, вызовы | `<PROJECT_ROOT>/<slug>/graphify-out/` | `graphify-maintain` |
| ADR сессии | устойчивые «почему» / запреты | `10_projects/<slug>/decisions.md` | `session-distill` |
| Роутер | какой slug, какой один корень | этот vault + один `move_agent_to_root` | `vault-router` |

Паспорт / KPI-таблицы — не этот стек. Deep-research — `70_researches/` (`save-research`).

## Где живёт граф

- Не в vault. Граф лежит в git-репозитории проекта: `graphify-out/graph.json` (обычно в gitignore).
- В git — человеческая карта `GRAPH_REPORT.md`.
- Extract только структурный (`--code-only`). Не считать Graphify semantic memory.
- Хук `docs-before-commit`, если возьмёте, только *напоминает*. Он не пишет заметки и не строит граф.

Реестр skills — [[60_skills/README]]. Brief шаблона — в `skills/` корня репозитория: `projects-data-verification`, `vault-router`, `session-distill`, `save-research`.

## Related

- [[50_runbooks/maintenance]]
- [[40_patterns/rr77-cursor-rules]]
- [[00_profile/agent-context]]
- [[60_skills/README]]
- [[70_researches/70_research_ops/70.03_RESEARCH-POLICY]]
