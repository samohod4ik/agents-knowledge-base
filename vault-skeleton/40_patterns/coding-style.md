---
tags: [patterns, coding, style, python]
last_verified: 2026-09-09
change_source: task-4-vault-skeleton
---
# Coding Style

## Language Rules

- Docstring на русском, формат reST.
- В каждом публичном методе опишите вход, выход и исключения.

## Function Rules

- Функции короткие (ориентир: меньше 30 строк).
- Вложенность меньше четырёх уровней.
- Предпочитать композицию и небольшие тестируемые функции.

## Project Layout

- SQL хранить в `./sql/`.
- Тесты хранить в `./tests/`.
- Избегать inline SQL в Python, если есть файловый SQL-слой.

## Related

- [[40_patterns/git-conventions]]
- [[00_profile/agent-context]]
- [[50_runbooks/maintenance]]
