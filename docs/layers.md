# Слои skills и rules

Четыре слоя не смешивать. Шаблон учит контракту, не чужому флоту.

| Слой | Где живёт | Что класть |
|------|-----------|------------|
| L1 user | каталог user skills / user rules Cursor | личные skills, в т.ч. `save-research`, если он ваш |
| L2 host | общий host/cross-project `.cursor/skills/` на машине | реализации с `scripts/` для нескольких репо одной машины |
| L3 этот vault | `<VAULT>/.cursor/rules/`, `40_patterns/`, `50_runbooks/`, `60_skills/` | протокол сопровождения, стандарты markdown, индекс skills |
| L4 team-canon | пакет общих project rules в каждом рабочем репо | стиль, git, общие alwaysApply *проектов* |

`<SKILLS_ROOT>` — L1 или L2, куда вы копируете brief и кладёте локальные `scripts/`.

## Что sync командных правил может копировать

- Общие project rules из team-canon (L4) → `.cursor/rules/<team>/` каждого прикладного репозитория.
- Хеш/фронтматтер канона, если ваш верификатор это проверяет.

## Что sync копировать нельзя

- Vault alwaysApply protocol (`obsidian-vault-maintenance-protocol.mdc`) — это L3, не пакет проекта.
- `save-research` — SoT = user/host `<SKILLS_ROOT>` (L1/L2). В team-canon и в `.cursor/skills/` каждого проекта **не копировать**.
- Живые скрипты pdv, hostname, DSN, учётки.
- Правила одного vault в другой vault без адаптации плейсхолдеров.

## Как ставить brief из этого шаблона

1. Скопируйте `skills/<name>/SKILL.md` в `<SKILLS_ROOT>/<name>/`.
2. Добавьте *свою* реализацию `scripts/`. Пока её нет — doctor падает, это ожидаемо.
3. Зарегистрируйте указатель в L3: `60_skills/<owner>/<name>.md`.
4. Не кладите brief с секретами в L4.

Подробнее про роутер: один `move_agent_to_root` — [cursor-integration.md](cursor-integration.md). Про граф — [graphify.md](graphify.md).
