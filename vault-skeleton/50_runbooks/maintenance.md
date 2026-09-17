---
tags: [runbook, maintenance, cursor, mcp]
last_verified: 2026-09-17
change_source: public-template-contract
---
# Maintenance

## Objective

Держать vault актуальным после изменений в коде, инфре, схеме или процессе.

## Update Protocol (Cursor + MCP)

1. После изменения определить slug в `10_projects`.
2. Обновить `README`, `architecture`, `runbook` проекта.
3. Если появилось устойчивое решение сессии — `10_projects/<project>/decisions.md` (`session-distill`). Не Mem0.
4. Deep-research отчёты → `70_researches` (`save-research`), не в `decisions.md`.
5. После смыслового изменения кода — обновить AST-граф в *репозитории* (`graphify-maintain`, только `--code-only`).
6. Интеграции и доступы → `20_infra/*`.
7. БД → [[30_db/connections]], [[30_db/schemas/README]], [[30_db/important-queries/README]].
8. Проставить `last_verified` и `change_source`.
9. Обновить `## Related` в обе стороны. Self-link запрещён.
10. Новый или изменённый Cursor skill — заметка `60_skills/<owner>/<skill-name>.md` в том же ходе.

Если доступны write-инструменты Obsidian MCP — предпочитайте их. Если MCP лежит, правьте файлы на диске и скажите об этом.

## Fields To Update

- `last_verified`: `YYYY-MM-DD`
- `change_source`: commit / ticket / incident / имя задачи

## MCP Workflow

Каталог: [[20_infra/cursor-mcp]]. Типичные действия: list / get / write / patch / search по заметкам. Локальный git — отдельно от API хостинга.

## Pre-Completion Checklist

- [ ] YAML frontmatter закрыт (`---` / tags / `last_verified` / `change_source` / `---`).
- [ ] В карточках проектов `## Stack` содержит Python, DB, Selenium (да/нет) и core libs.
- [ ] Wikilink с путём: `[[10_projects/example_library/runbook]]`, не `[[runbook]]`.
- [ ] Нет self-link в `## Related`.
- [ ] Git-remote в заметках совпадают с вашим `<GIT_REMOTE>`.
- [ ] Секреты замаскированы. Инфра ссылается на [[20_infra/access-matrix]] (`***` или `secret_ref`).
- [ ] Хаб профиля совпадает с Active Projects: [[00_profile/tech-stack]], [[00_profile/developer-profile]].
- [ ] Новый skill зарегистрирован в `60_skills/README.md`.
- [ ] Skill, если ставили: реально вызван агентом (не только скопирован файл).
- [ ] `## Related` — точная строка заголовка. Не `## Related Research` и не другой H2 с префиксом Related.
- [ ] AlwaysApply-стоп без скрипта: ручной проход + [[50_runbooks/obsidian-vault-audit]]. Если есть локальный `verify_projects_data.py` — категория `scm` clean. Полный `errors = 0` — цель журнала, не стоп этой задачи.

## SCM Validation

Публичный шаблон не требует скриптов. Проверьте, что remote в карточках = ваш `<GIT_REMOTE>`, не remote издателя.

Если оператор завёл локальный `verify_projects_data.py` — один продукт; `verify_vault.py` — его модуль. AlwaysApply-стоп — `scm` clean. Cache JSON — не источник истины. Верификатор только аудитит.

## Related

- [[50_runbooks/obsidian-vault-audit]]
- [[50_runbooks/skills-for-cursor]]
- [[50_runbooks/skill-checklist]]
- [[40_patterns/shared-cursor-rules]]
- [[40_patterns/git-conventions]]
- [[20_infra/cursor-mcp]]
- [[00_profile/agent-context]]
- [[40_patterns/fleet-memory-stack]]
