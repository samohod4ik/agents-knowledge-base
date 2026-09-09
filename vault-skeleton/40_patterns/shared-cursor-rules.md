---
tags: [pattern, cursor, rules, shared-rules]
last_verified: 2026-09-09
change_source: final-review-fixes
---
# Shared Cursor Rules

Это **паттерн общих правил**, не канон одной команды. Подставьте свой `<team>` и свой `<GIT_REMOTE>`.

## Source of truth

- Канон общих правил живёт в одном репозитории команды.
- Копии в проектах: `<PROJECT_ROOT>/<slug>/.cursor/rules/<team>/*.mdc`
- Личные project rules — рядом, **вне** папки `<team>/`.
- Opt-in наборы (API-адаптеры и т.п.) не кладите внутрь общего пакета: sync сотрёт или раскатит их на все репо.

Не копируйте чужие абсолютные пути и URL хостинга.

## Модули (пример набора)

Состав файлов — ваш. Ниже — типичные роли, не обязательный список.

| Роль файла | Когда |
|------------|-------|
| workflow инструментов | always |
| SCM / git-хост команды | always; API хоста ≠ `gh`, если хост не GitHub |
| язык и документация | исходники + markdown |
| тесты | по description |
| SQL / доступ к данным | py/sql |
| секреты и конфиг | `config/` |
| сопровождение vault | правки этого vault |
| docs-before-commit | перед `git commit` / `git push` |
| graphify / AST | always, если ведёте граф |

## AGENTS.md

- Короткий bootstrap репозитория, не замена `.mdc`.
- Имя только `AGENTS.md`.
- Вложенные файлы действуют на свой каталог и потомков вместе с корневым.

## Напоминание перед Git

- Хук `docs-before-commit`, если возьмёте, только напоминает агенту.
- Он не пишет документацию, не гоняет Graphify и не блокирует git.
- Для тривиальных правок документы не обязательны.

Vault-правила этого шаблона — отдельная пара `.mdc` в `<VAULT>/.cursor/rules/` (протокол сопровождения + стандарты markdown).

## Related

- [[40_patterns/fleet-memory-stack]]
- [[40_patterns/git-conventions]]
- [[50_runbooks/maintenance]]
- [[20_infra/cursor-mcp]]
- [[00_profile/agent-context]]
