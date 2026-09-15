---
tags: [archive, deprecated, history]
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Archive

## Purpose

Хранение устаревших версий заметок и отвергнутых подходов.

## Create / update / archive / verify

- **Create:** перенос только после появления актуальной версии в рабочих разделах.
- **Update:** поправьте `superseded_by` и дату, если актуальная цель сменилась.
- **Archive:** это и есть lane архива — не кладите сюда завершённые research-прогоны.
- **Verify:** у каждой записи есть причина, дата и path-wikilink на актуальную заметку.

## Rules

- Переносить только после появления актуальной версии в рабочих разделах.
- Указывать причину архивации и дату.
- Добавлять `superseded_by` — wikilink с путём на актуальную заметку.
- Завершённые research-прогоны **не** переносить сюда. Меняйте статус в registry; см. [[70_researches/70_research_ops/70.03_RESEARCH-POLICY]].

## Archived Projects

Пока пусто. Пример строки после архивации:

- `[[90_archive/<old-slug>/README]]` → `[[10_projects/<slug>/README]]`

## Related

- [[50_runbooks/maintenance]]
- [[70_researches/70_research_ops/70.03_RESEARCH-POLICY]]
