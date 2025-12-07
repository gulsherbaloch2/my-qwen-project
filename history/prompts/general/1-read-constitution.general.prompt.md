---
id: 1
title: Read Constitution
stage: general
date: 2025-12-03
surface: agent
model: gemini-1.5-pro-a
feature: none
branch: main
user: user
command: read constitution
labels: ["documentation"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:

---

## Prompt

read constitution

## Response snapshot

# specifysetup Constitution
<!-- Example: Spec Constitution, TaskFlow Constitution, etc. -->

## Core Principles

### I. Spec-Driven Development (SDD)
All work, from features to fixes, begins with a clear, written specification. The spec is the source of truth for requirements, scope, and acceptance criteria. No code is written without a corresponding, approved spec.

### II. Test-Driven Development (TDD)
A failing test must be written before any implementation code. The Red-Green-Refactor cycle is strictly followed to ensure code is verifiable, correct, and maintainable.

### III. CLI-First Interface
All features and libraries must be accessible and operable through a command-line interface. This ensures composability, scriptability, and ease of testing.

### IV. Continuous Documentation
Every significant action, decision, and interaction is documented. Prompt History Records (PHRs) are created for every user prompt, and Architectural Decision Records (ADRs) are proposed for architecturally significant decisions.

### V. Simplicity and YAGNI
We adhere to the "You Ain't Gonna Need It" (YAGNI) principle. Solutions should be as simple as possible. Complexity is only introduced when necessary and justified.



## Development Workflow
The development process follows a strict, spec-driven lifecycle:
1.  **/sp.specify**: A detailed specification is written and approved.
2.  **/sp.plan**: An architectural plan is created, outlining the technical approach.
3.  **/sp.tasks**: The plan is broken down into small, verifiable tasks.
4.  **Red**: A failing test is written for the current task.
5.  **Green**: The minimum amount of code is written to make the test pass.
6.  **Refactor**: The code is cleaned up while ensuring tests remain green.



## Governance
This Constitution is the supreme guiding document for the `specifysetup` project.
- All Pull Requests (PRs) and code reviews must verify compliance with these principles.
- Any amendments to this Constitution require a formal proposal, review, and approval by project leadership, along with a documented migration plan if applicable.
- Complexity in design or implementation must always be justified against the principles of simplicity and YAGNI.

**Version**: 1.0.0 | **Ratified**: 2025-12-02 | **Last Amended**: 2025-12-02

## Outcome

- ✅ Impact: Constitution read successfully.
- 🧪 Tests: N/A
- 📁 Files: Read .specify/memory/constitution.md.
- 🔁 Next prompts: N/A
- 🧠 Reflection: N/A

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
