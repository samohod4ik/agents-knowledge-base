---
name: vault-router
description: >-
  Use when choosing which repo to open, answering a cross-project question,
  the sidebar is crowded with multi-root workspaces, or the user mentions
  move_agent_to_root, vault-router, Active Projects.
---

# vault-router

Установка: `<SKILLS_ROOT>/vault-router`.

Межпроектный роутер: сначала vault `<VAULT>`, потом один корень. Не открывать все репозитории в сайдбаре. Не Mem0.

**Не используй**, когда задача уже внутри одного репо и не касается других slug.

## Doctor

Публичный шаблон везёт только этот brief (`SKILL.md`), без исполняемых скриптов. Команды ниже — контракт совместимой локальной реализации. Установите или предоставьте её в `<SKILLS_ROOT>/vault-router/` до запуска Doctor и остальных команд.

```powershell
python <SKILLS_ROOT>/vault-router/scripts/doctor.py
```

## Resolve

```powershell
python <SKILLS_ROOT>/vault-router/scripts/resolve_project.py --name <slug>
python <SKILLS_ROOT>/vault-router/scripts/resolve_project.py --query "..."
```

Печатает JSON: `path`, `vault`, `decisions`, `exists`. Exit `1`, если slug не найден.

## Workflow

1. Doctor.
2. Прочитай `<VAULT>/00_profile/agent-context.md` и README нужного `10_projects/<slug>/`.
3. Кросс-вопрос закрой из vault. Не добавляй второй root, пока не нужно менять код.
4. Если нужен код одного проекта: `move_agent_to_root` на `path` из resolve. Один активный корень.
5. Второй репо — только после того, как vault не хватило.

## Fallback

- Нет MCP Obsidian — читай `<VAULT>/**` с диска.
- Нет `move_agent_to_root` — скажи пользователю открыть `path` как единственный корень.
- Нет slug — спроси, не создавай новую папку в `10_projects`.

## Успех

Кросс-вопрос закрыт из vault без второго root в сайдбаре.
