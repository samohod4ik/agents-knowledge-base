---
tags: [skills, workspace, memory, decisions, cursor]
name: session-distill
status: example
source_agent: public-template
last_verified: 2026-09-16
change_source: public-obsidian-polish
---
# session-distill

## Purpose
Дистилляция устойчивых решений сессии в `<VAULT>/10_projects/<slug>/decisions.md`. Диск, не память модели.

## Skill Location
- Brief шаблона: `skills/session-distill/SKILL.md`
- Установка: `<SKILLS_ROOT>/session-distill/SKILL.md`
- Scripts / assets: опционально у оператора; в публичном дереве отсутствуют

## Triggers
distill, decisions.md, ADR, session-end, память сессии, workaround, do-not-touch, перед commit после смыслового изменения.

## Related Projects
- [[10_projects/example_library/README]]
- [[10_projects/example_service/README]]
- [[10_projects/example_library/decisions]]
- [[10_projects/example_service/decisions]]

## Run
Определите slug → правьте `decisions.md` по brief. MCP Obsidian предпочтителен; иначе диск.

## Related
- [[40_patterns/fleet-memory-stack]]
- [[60_skills/workspace/vault-router]]
- [[60_skills/workspace/save-research]]
- [[60_skills/workspace/README]]
- [[60_skills/README]]
- [[50_runbooks/maintenance]]
- [[00_profile/agent-context]]
