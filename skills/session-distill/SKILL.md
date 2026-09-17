---
name: session-distill
description: >-
  Use when a session produced a durable architectural decision, workaround,
  do-not-touch rule, or the user asks to distill memory, decisions.md, ADR,
  session-end, or before commit/push after a semantic change.
---

# session-distill

Это **контракт**, не поставка автоматизации. Каталога `scripts/` в этом шаблоне нет. Локальные `scripts/` опциональны; не требуйте отсутствующий doctor как блокер.

Установка: `<SKILLS_ROOT>/session-distill`.

Пишет устойчивые решения сессии в `<VAULT>/10_projects/<slug>/decisions.md`. Это диск, не память модели и не Mem0.

**Не используй**, когда:
- правка косметическая / только тесты / docs-only без нового «почему»;
- нужны сырые логи или triage fingerprints;
- паспорт / KPI-таблицы — не `decisions.md`;
- просят поставить Mem0 / Antigravity Memory / второй SQLite;
- сырые или структурированные research-отчёты — это `70_researches` (skill `save-research`).

## Workflow

1. Определи slug (Active Projects / skill `vault-router`). Не выдумывай папку.
2. Прочитай `<VAULT>/10_projects/<slug>/decisions.md`. Нет файла — создай с frontmatter (`tags`, `last_verified`, `change_source`) и короткими секциями Decision / Anti-decision / Context.
3. Добавь только устойчивые факты (обычно 3–7 за сессию): дата, решение, антирешение, SHA/issue. Без секретов и PII.
4. Держи файл обозримым (ориентир < 200 строк). Детали — в architecture/runbook.
5. Обнови `last_verified` / `change_source`. Связанные architecture/runbook — только если решение их меняет.
6. MCP Obsidian предпочтителен; иначе правь файлы vault напрямую и скажи об этом.

## Запреты

- Писать «память» только в чат
- Дублировать ADR под `70_researches/`
- Требовать локальный `scripts/doctor.py` или шаблон `assets/`, которых нет в публичном дереве

## Успех

Новый чат без истории может повторить два свежих решения, прочитав только `decisions.md`.
