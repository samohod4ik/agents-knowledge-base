# Public-readiness audit

Дата прохода: 2026-09-16. Цель: убедиться, что публичный шаблон можно форкать без чужих хостов, секретов и обязательных несуществующих скриптов.

## Что исправлено в этом проходе

| Finding | Disposition |
|---------|-------------|
| Cursor chat UUID в `docs/problem-and-approach.md` | Убраны; эволюция дизайна описана без приватных session ID |
| Skills требовали `scripts/doctor.py`, которых нет в дереве | Briefs переписаны на disk/Obsidian workflow; локальные `scripts/` — опционально у оператора |
| Self-hosted forge как «единственный» командный хост | Смягчено до «your team git host / `<GIT_REMOTE>`» |
| Не было Obsidian onboarding | Добавлен [obsidian.md](obsidian.md) |
| Не было SECURITY / CONTRIBUTING / repo AGENTS / audit | Добавлены корневые файлы + этот документ |
| Чеклист завершения ссылался на verify-скрипт как обязательный | Чеклист: ручная проверка; скрипт — опциональный, если оператор его завёл |

## Forbidden tokens (текущее дерево)

CI/hygiene тест запрещает в text-файлах абсолютные диски издателя, персональные user-profile пути и UUID исходных приватных design-чатов (полные и короткие префиксы), а также литералы персональных email издателя.

Допустимы: плейсхолдеры `<VAULT>`, `<SKILLS_ROOT>`, `<PROJECT_ROOT>`, `<GIT_REMOTE>`, `<PORT>`, `<HOST>`; маски `***` / `secret_ref: vault://...`; публичный clone URL этого шаблона; упоминание self-hosted forge только как *пример* командного хоста, не как обязательный remote.

## History residue

Удаление строки из `main` не стирает её из git history. History rewrite в этом проходе **не** делался. Перед сменой visibility или широким анонсом просмотрите историю на секреты. Если найден живой credential — сначала revoke, потом согласованная очистка истории; не полагайтесь на `.gitignore`.

## Product honesty

Этот репозиторий = операционный Obsidian vault + Cursor rules/skills. Он **не** поставляет локальный RAG-рантайм, Telegram-адаптер и живые карточки чужой команды. Примеры в скелете — только `example_library` и `example_service`.

## Practical checks

```powershell
python -m unittest discover -s tests -v
```

См. также [SECURITY.md](../SECURITY.md), [CONTRIBUTING.md](../CONTRIBUTING.md), [obsidian.md](obsidian.md).
