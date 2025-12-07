---
id: 2
title: Constitution and Project Consistency Check
stage: constitution
date: 2025-12-04
surface: agent
model: gemini-1.5-pro-a
feature: none
branch: main
user: user
command: $ARGUMENTS
labels: ["constitution", "consistency", "validation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
 - .specify/templates/spec-template.md
 - .specify/templates/tasks-template.md
 - .gemini/commands/sp.adr.toml
 - .gemini/commands/sp.analyze.toml
 - .gemini/commands/sp.checklist.toml
 - .gemini/commands/sp.clarify.toml
 - .gemini/commands/sp.constitution.toml
 - .gemini/commands/sp.git.commit_pr.toml
 - .gemini/commands/sp.implement.toml
 - .gemini/commands/sp.phr.toml
 - .gemini/commands/sp.plan.toml
 - .gemini/commands/sp.specify.toml
 - .gemini/commands/sp.tasks.toml
 - my-docusaurus-site/README.md
 - history/prompts/constitution/1-setup-specifysetup-constitution.constitution.prompt.md
 - history/prompts/general/1-read-constitution.general.prompt.md
tests:

---

## Prompt

$ARGUMENTS

## Response snapshot

Mene project ki tamam zaroori files ka jaiza liya hai aur is nateeje par pohncha hon ke woh sab project ke constitution ke asoolon ke mutabiq hain.

## Outcome

- ✅ Impact: Project ki tamam files ka jaiza liya gaya aur unhein constitution ke mutabiq paya gaya.
- 🧪 Tests: N/A
- 📁 Files: Mukhtalif project files ka jaiza liya gaya.
- 🔁 Next prompts: N/A
- 🧠 Reflection: N/A

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
