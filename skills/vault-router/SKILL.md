---
name: vault-router
description: >-
  Use when choosing which repo to open, answering a cross-project question,
  the sidebar is crowded with multi-root workspaces, or the user mentions
  move_agent_to_root, vault-router, Active Projects.
---

# vault-router

Установка: `<SKILLS_ROOT>/vault-router`.

Кросс-проектный ответ: сначала vault `<VAULT>`, потом один активный корень. Не угадывать по сайдбару. Не Mem0.

**Не используй**, когда агент уже внутри нужного репо и не спрашивают другие slug.

## Workflow

1. Прочитай `<VAULT>/README.md` (Active Projects) и при необходимости `<VAULT>/00_profile/agent-context.md`.
2. Сопоставь вопрос со slug в `10_projects/<slug>/`.
3. Прочитай README и нужные файлы карточки (architecture / runbook / decisions) **до** смены корня.
4. Если нужен код проекта: один `move_agent_to_root` на путь из `## Project Location` (или спроси путь у оператора). Не открывай второй корень «на всякий случай».
5. Отвечай из vault + одного активного репо. Чужие абсолютные диски не подставляй.

## Запреты

- Сайдбар как источник истины вместо Active Projects
- Создавать новый `10_projects/<slug>` без просьбы
- Требовать локальный `scripts/resolve_project.py` — это опциональный helper оператора
- Mem0 / вторая «память» вместо карточек vault

## Успех

Кросс-вопрос закрыт из vault при одном активном root (или явном отказе, если slug не найден).
