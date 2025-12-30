---
applyTo: "**"
description: "Main Copilot instructions for the appkit project - Reflex-Mantine component library with comprehensive development workflow and architecture guidelines"
---

# Reflex-Mantine Component Library

**A comprehensive Reflex wrapper library for Mantine UI components with production-ready examples.**

> **Purpose:** Guide GitHub Copilot & Copilot Chat to align suggestions with our tech stack, workflows, and quality bars.
> **Stacks:** Python 3.13 · Reflex (UI) · FastAPI · SQLAlchemy 2.0 · Alembic · Pydantic · FastMCP · LangChain

---

## 1) Golden Rules (Short, Actionable)
1. **Think → Memory → Tools → Code → Memory.** Start with step-by-step reasoning (using the tool code-reasoning); **search Memory first**; pick tools; code minimal diff; **write learnings back to Memory**.
2. **Tests are truth.** On failures: **fix code first**. Change tests only if they clearly diverge from spec.
3. **Small, safe changes.** Prefer smallest viable diff; add tests for new behavior **before** code.
4. **Consistency > cleverness.** Follow this file’s SOPs and stack idioms.
5. **Memory multiplies.** Persist decisions, patterns, error signatures, and proven fixes.
6. Do NOT generate extensive documentation, summaries or comments unless explicitly requested.
7. Do NOT use --autogenerate for new Alembic migrations; write them manually.
8. Do NOT use "cat" to create new files; ALWAYS use the available tools!

> Rule of thumb: prefer *local* changes over cross-module refactors.

---

## 2) Task Bootstrap Pattern (for Inline Copilot & Chat)
Paste/edit this at the top of the change (as a comment) to steer Copilot:

```markdown
<!-- plan:start
goal: <one line clear goal>
constraints:
- Python 3.13; Reflex UI; FastAPI; SQLAlchemy 2.0; Alembic; Pydantic
- logging: no f-strings in logger calls
- minimal diff; add/adjust tests first
definition_of_done:
- tests pass; coverage ≥ 80%; lint/type checks clean; memory updated
steps:
1) Search Memory for "<keywords>"
2) Draft/adjust failing test to capture expected behavior
3) Implement minimal code change
4) Run make test; iterate until green
5) Update Memory: decisions, patterns, error→fix
plan:end -->
```

---

## 3) Tooling Decision Matrix (Condensed)

| Situation | Primary | Secondary | Store to Memory |
|---|---|---|---|
| API/pattern uncertainty | **Context7** | — | Canonical snippet + link; edge cases |
| Ecosystem bug/issue | **DuckDuckGo** | — | Minimal repro; versions; workaround |
| Repeated test failure | **Memory (search)** | Context7 | Error signature → fix; root cause |
| New feature scaffold | **Context7** | — | How‑to snippet; checklist |
| House style/tooling | **This file** | Context7 | Checklist results |

**Prefer official docs; widen via web search when cross-version issues arise.**

---

## 4) SOP — Development Workflow

### Prepare
1. **Memory first:** search for prior solutions and patterns.
2. **Reasoning plan:** use the *Task Bootstrap Pattern*.
3. **Sync tools:** `make install` (uses **uv**, Python 3.13).
4. **Baseline:** `make test` to snapshot current failures.

### Triage Failures
- Read the **first** failing assertion; map to spec.
- If tests match spec → fix code. If tests diverge → document and adjust spec/tests (after approval).
- Add/adjust unit tests to codify expected behavior.

### Implement (Minimal Diff)
- Tests-first for new behavior.
- Use only approved stacks. Examples:
  - **Logging (no f-strings):**
    ```python
    import logging
    log = logging.getLogger(__name__)
    log.info("Loaded items: %d", count)      # ✅
    # log.info(f"Loaded items: {count}")     # ❌
    ```

### Reflex UI
- Small components; separate **state** from **view**.
- Deterministic state transitions; avoid hidden side effects.
- Reuse components; document patterns in **Memory**.
- Examples on how to use form components can be found here: https://github.com/jenreh/appkit/tree/main/app/pages/examples

### Quality Gates
- Lint/format/type: `uv run ruff check --fix`, `uv run ruff format`.
- Tests: `uv run pytest` with coverage ≥ **80%**.
- Docs: update `docs/` for migrations/decisions.


### Commit & PR
- Conventional Commits (`feat:`, `fix:`, `refactor:`…).
- PR must include: description, `Closes #123`, UI screenshots, migration rationale.

### Learn
- Reflect; extract learnings; write to **Memory**.

---

## 5) Code Generation Rules
- **Python 3.13** only; deps via **uv**.
- Use Reflex, Alembic, SQLAlchemy 2.0, FastAPI, Pydantic, FastMCP, LangChain.
- **No f-strings in logger calls.**
- Clean code; narrow modules; clear boundaries.
- Unit tests for every new path.

---

## 6) Testing Strategy
- Tests in `tests/test_*.py`; isolate units; avoid coupling.
- Coverage target **≥ 80%**.
- Write regression tests first when fixing bugs.
- Use fixtures for env/config swaps.

## 7) Search SOPs
- **Context7 first** for framework truths; cite sources in **Memory**.
- **DuckDuckGo** for cross-version issues; prefer official docs, well-known repos.
- Capture only the **final answer** in **Memory**: minimal snippet + rationale + version pins + link.

## 8) Security & Config Hygiene
- No credentials in code/history; use `.env` locally, Key Vault in prod.
- Prefer non-secret YAML; override with env `__` pattern.
- Parameterized logs; avoid sensitive values.
- Update vulnerable deps promptly; document CVE-driven updates in commits and **Memory**.

---

## 9) Pre‑PR Checklist
- [ ] Tests added/updated; all green
- [ ] Lint/format/type checks pass
- [ ] Migrations reviewed & documented
- [ ] **Memory updated** (decisions, patterns, error→fix links)
- [ ] PR description complete; links/screenshots added
