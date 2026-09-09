---
tags: [project, example_library, architecture]
last_verified: 2026-09-09
change_source: task-5-example-projects
---
# example_library — architecture

## Project Location

- `<PROJECT_ROOT>/example_library`

## Stack

- Python: `<X.Y>+`
- DB: нет собственной (пакет библиотеки)
- Selenium: нет
- Core libs: requests, pydantic

## Layers

```text
src/example_library/
  __init__.py          # публичный экспорт
  client.py            # HTTP/API-клиент без зашитых хостов
  models.py            # pydantic-модели
  exceptions.py        # явные ошибки пакета
tests/
  test_client.py
```

Потребитель (пример формы): [[10_projects/example_service/README]] импортирует пакет, владеет конфигом и секретами.

## Boundaries

- Библиотека не поднимает HTTP-сервер и не держит пул БД.
- Базовый URL и учётные данные задаёт потребитель через конструктор или env.
- Graphify AST — в репозитории `graphify-out/`, не в vault. См. [[40_patterns/fleet-memory-stack]].

## Risks

- Зашить `<HOST>` или готовый DSN в пакет — сломает шаблон и утечёт контур.
- Тянуть Selenium extra «на всякий случай» без нужды — держите `Selenium: нет`, пока extra нет.
- Менять публичный экспорт без записи в [[10_projects/example_library/decisions]].

## Related

- [[10_projects/example_library/README]]
- [[10_projects/example_library/runbook]]
- [[10_projects/example_library/requirements]]
- [[10_projects/example_library/decisions]]
- [[10_projects/example_service/README]]
- [[40_patterns/coding-style]]
- [[40_patterns/fleet-memory-stack]]
