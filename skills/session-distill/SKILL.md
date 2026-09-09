---
name: session-distill
description: >-
  Use when a session produced a durable architectural decision, workaround,
  do-not-touch rule, or the user asks to distill memory, decisions.md, ADR,
  session-end, or before commit/push after a semantic change.
---

# session-distill

Установка: `<SKILLS_ROOT>/session-distill`.

Пишет устойчивые решения сессии в `<VAULT>/10_projects/<slug>/decisions.md`. Это диск, не память модели и не Mem0.

**Не используй**, когда:
- правка косметическая / только тесты / docs-only без нового «почему»;
- нужны сырые логи или triage fingerprints;
- паспорт / KPI-таблицы — не `decisions.md`;
- просят поставить Mem0 / Antigravity Memory / второй SQLite;
- сырые или структурированные research-отчёты — это `70_researches` (skill `save-research`).

## Doctor

```powershell
python <SKILLS_ROOT>/session-distill/scripts/doctor.py
```

`ok` требует `<VAULT>/10_projects` и шаблон `assets/decisions-template.md`.

## Workflow

1. Doctor.
2. Определи slug: skill `vault-router` / `resolve_project.py --name <slug>`.
3. Прочитай `<VAULT>/10_projects/<slug>/decisions.md`. Нет файла — создай по шаблону `assets/decisions-template.md`.
4. Добавь только устойчивые факты (3–7 за сессию): дата, решение, антирешение, SHA/issue. Без секретов и PII.
5. Держи файл короче 200 строк. Детали — в architecture/runbook.
6. Обнови `last_verified` / `change_source`. Связанные architecture/runbook — только если решение их меняет.
7. MCP Obsidian предпочтителен; иначе правь файлы vault напрямую и скажи об этом.

## Fallback

- Нет MCP Obsidian — файлы vault напрямую.
- Нет slug — спроси пользователя, не выдумывай папку.
- Итеративный цикл агента: пиши на диск (`decisions.md`), не в «память чата».

## Успех

Новый чат без истории может повторить два свежих решения, прочитав только `decisions.md`.
