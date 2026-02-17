# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI-powered resume generator CLI that takes job descriptions and produces tailored LaTeX resumes via Claude AI (LiteLLM). Single source of truth is `data/resume-master.json`; all resume variants are generated from it.

## Commands

```bash
# Install dependencies
uv sync

# Generate resume for a single job
uv run python agent.py generate -f jobs/job.txt -o my-resume -m anthropic/claude-sonnet-4-20250514

# Interactive refinement loop (generate → review → adjust)
uv run python agent.py interactive

# Batch process all .txt/.md files in a directory
uv run python agent.py batch -d jobs/

# Compile existing .tex file
uv run python agent.py compile path/to/file.tex

# Generate complete CV (no LLM, all data included)
uv run python agent.py complete -o output-name

# Generate README.md from master data
uv run python agent.py readme

# Lint
uv run ruff check .

# Run tests
uv run pytest tests/ -v
```

## Architecture

```
Job Description + resume-master.json + templates/
        ↓
  Claude AI via LiteLLM (src/llm_handler.py)
        ↓
  Raw LaTeX output
        ↓
  pdflatex compilation (src/latex_compiler.py, runs twice for refs)
        ↓  on error → Claude auto-fix → retry (up to 3x)
        ↓
  generated/{name}.pdf
```

**Key modules:**
- `agent.py` — CLI entry point (Click). Commands: generate, interactive, batch, compile, complete, readme
- `src/llm_handler.py` — `LLMHandler` class: `generate_resume()`, `fix_latex_error()`, `adjust_resume()`. Calls Claude via `litellm.completion()`
- `src/data_loader.py` — Loads `resume-master.json`, computes skill years from `start_year`, loads templates/prompts
- `src/latex_compiler.py` — `LatexCompiler` class: runs `pdflatex` twice, captures errors, cleans aux files
- `src/latex_generator.py` — `generate_complete_cv()`: direct LaTeX from master data (no LLM)
- `src/markdown_generator.py` — `generate_readme()`: generates README.md from master data

**Data flow:** `data/resume-master.json` → data_loader (with computed years) → llm_handler (builds prompt with job desc + data + template) → Claude returns raw LaTeX → latex_compiler → PDF

**Templates:**
- `templates/example.tex` — Reference LaTeX structure (preamble, custom commands like `\resumeSubheading`)
- `templates/prompts/system_prompt.txt` — System prompt instructing Claude to output raw LaTeX only

## Code Style

- Python 3.11+, type hints on all functions
- **No docstrings** — use `#` line comments only
- Line length: 100 chars (ruff, E501 ignored)
- Linter: ruff with rules E, F, I, W
- Use `rich` for all CLI output formatting
- Use Pydantic for data validation

## LaTeX Escaping (Critical)

Always escape these characters before inserting into LaTeX: `& → \&`, `% → \%`, `$ → \$`, `# → \#`, `_ → \_`

## Git Conventions

Conventional Commits with emojis: `✨ feat:`, `🐛 fix:`, `📝 docs:`, `♻️ refactor:`, `⚡ perf:`, `✅ test:`, `🔧 chore:`

**No Co-Authored-By lines in commits.**

## CI/CD

GitHub Actions (`.github/workflows/latex.yml`) triggers on pushes to `main` that modify `data/`, `src/`, `templates/`, or the workflow file. It generates the complete CV PDF and README, then pushes them to the `technical-resume` orphan branch.

## Environment

Requires `ANTHROPIC_API_KEY` in `.env`. Optional: `LITELLM_LOG=DEBUG`, `DEFAULT_MODEL`.
