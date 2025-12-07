<!--
Sync Impact Report:
Version change: N/A → 1.0.0
Modified principles: N/A (new constitution)
Added sections: All principles and sections (new constitution)
Removed sections: N/A
Templates requiring updates: ⚠ pending (.specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md)
Follow-up TODOs: None
-->

# Qwen Code Constitution

## Core Principles

### Spec-Driven Development (SDD)
Every feature and change starts with a specification that clearly defines requirements, acceptance criteria, and constraints before implementation begins. Specifications must be testable and verifiable.

### Authoritative Source Mandate
Prioritize and use MCP tools and CLI commands for all information gathering and task execution. Never assume a solution from internal knowledge; all methods require external verification.

### Prompt History Records (PHRs) for Every User Input
Record every user input verbatim in a Prompt History Record (PHR) after every user message. Do not truncate; preserve full multiline input. PHRs must follow proper routing.

### Architectural Decision Records (ADRs)
When architecturally significant decisions are detected, document reasoning and tradeoffs in an ADR. Decisions should consider long-term consequences, alternatives, and cross-cutting system design implications.

### Human as Tool Strategy
Treat the user as a specialized tool for clarification and decision-making when encountering ambiguous requirements, unforeseen dependencies, or architectural uncertainty. Ask targeted questions before proceeding.

### Execution Contract Adherence
Follow the execution contract for every request which includes confirming surface and success criteria, listing constraints, producing artifacts with acceptance checks, adding follow-ups, and creating PHRs.

## Security and Operational Standards

Never hardcode secrets or tokens; use .env and docs. Prefer the smallest viable diff; do not refactor unrelated code. Maintain security best practices throughout development.

## Development Workflow

Clarify and plan first, keeping business understanding separate from technical plan. Cite existing code with code references. Keep reasoning private, output only decisions, artifacts, and justifications.

## Governance

This constitution supersedes all other practices. Amendments require documentation with proper versioning. All implementations must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-12-07 | **Last Amended**: 2025-12-07