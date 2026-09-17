# Graphify

`graphify-maintain` — паттерн, не пятый публичный skill этого шаблона. В `skills/` нет его кода и нет `scripts/`.

## Где живёт граф

Граф принадлежит *git-репозиторию проекта*, не vault.

| Артефакт | Где | Git |
|----------|-----|-----|
| `graphify-out/graph.json` | `<PROJECT_ROOT>/<slug>/graphify-out/` | обычно в gitignore |
| `GRAPH_REPORT.md` | корень или `graphify-out/` того же репо | коммитить человеческую карту |

Не делать `export obsidian` тысяч узлов в `10_projects/`. Не считать Graphify semantic memory.

## Контракт extract

- Только структурный прогон: `--code-only` (без LLM-меток).
- После смыслового изменения кода обновите граф в том же ходе (протокол 2c).
- Хук `docs-before-commit`, если возьмёте, только напоминает. Он не строит граф и не пишет vault.

## Как поставить у себя

1. Возьмите свою локальную реализацию `graphify-maintain` (не из этого шаблона).
2. Вычистите чужие абсолютные диски и hostname до копирования.
3. Зарегистрируйте указатель в *своём* vault (`60_skills/<owner>/...`), если skill станет операционным.
4. Не кладите skill в пакет team-canon, если в тексте есть хост или учётка.

## Related

- [killer-features.md](killer-features.md)
- [architecture.md](architecture.md)
- [layers.md](layers.md)
