# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Alejandro's CV toolkit. Single source of truth is `data/resume-master.json`; five curated CVs are
derived from it — four LaTeX variants in `variants/` and the `README.md`. Tailoring for a specific
job posting is done by the Claude skills in `.claude/skills/`, not by a code generator.

## Commands

```bash
# Install dependencies
uv sync

# Compile a CV variant to PDF
uv run python agent.py compile variants/ai-fullstack.tex

# Lint
uv run ruff check .
```

## Architecture

```
data/resume-master.json          single source of truth
        |
        |  by hand, or via .claude/skills/cv
        v
variants/*.tex  +  README.md     five curated CVs
        |
        v  agent.py compile (pdflatex twice, cleans aux files)
variants/*.pdf
        |
        v  .github/workflows/latex.yml on push to main
technical-resume branch          published PDF + README
```

**Modules:**
- `agent.py` — CLI with a single command: `compile`
- `src/latex_compiler.py` — `LatexCompiler`: runs `pdflatex` twice, captures errors, cleans aux files

There is deliberately no LaTeX or Markdown generator. Selection and wording are editorial judgement,
and that judgement lives in `.claude/skills/cv/SKILL.md` so it exists in exactly one place.

## Code Style

- Python 3.11+, type hints on all functions
- **No docstrings** — use `#` line comments only
- Line length: 100 chars (ruff, E501 ignored)
- Linter: ruff with rules E, F, I, W
- Use `rich` for all CLI output formatting

## LaTeX Escaping (Critical)

Always escape these characters before inserting into LaTeX: `& → \&`, `% → \%`, `$ → \$`, `# → \#`, `_ → \_`

## Claude Skills

`.claude/skills/` holds the recurring workflows. They carry the editorial judgement that used to
live in prompt files and generator code:

- `cv` — adapt a base variant to a job posting; writes to `generated/`, never over `variants/`
- `apply` — answer application forms into `jobs/`
- `interview` — build a company-specific supplement to `interview-prep/interview-simulation.md`

Rules worth knowing before touching CV content: beginner-level skills stay out of CVs, GitHub
figures come only from `open_source.cv_highlights`, years are recomputed from `start_year` rather
than copied, and a project's `status` is checked before describing it as live.

## Git Conventions

Conventional Commits with emojis: `✨ feat:`, `🐛 fix:`, `📝 docs:`, `♻️ refactor:`, `⚡ perf:`, `✅ test:`, `🔧 chore:`

**No Co-Authored-By lines in commits.**

## CI/CD

GitHub Actions (`.github/workflows/latex.yml`) triggers on pushes to `main` that modify `variants/`,
`README.md`, or the workflow file. It compiles the variant named in `PUBLISHED_VARIANT`
(currently `ai-fullstack`) and pushes the PDF plus `README.md` to the `technical-resume` orphan branch.
Nothing is generated from the data at build time — the CI publishes files a human already reviewed.

## Environment

No API keys or `.env` required. Needs Python 3.11+ and a TeX distribution providing `pdflatex`
with the `fontawesome` package.
