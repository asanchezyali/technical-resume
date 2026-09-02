---
name: cv
description: |
  Adapt Alejandro's CV to a specific job posting, starting from one of the four
  base variants. Use when given a job description, a job URL, or a request like
  "hazme un CV para esta oferta" / "adapt my CV for this role". Also use to update
  the base variants themselves when new data lands in resume-master.json.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - WebFetch
---

# CV Builder

Single source of truth: `data/resume-master.json`. Never invent anything that is not in it.

## The four base variants

Each is a self-contained, hand-curated `.tex` file in `variants/`. They are artifacts, not
generated output — read the closest one, adapt it, and save the result to `generated/`.
Never overwrite a file in `variants/` while tailoring for a posting.

| File | Use when the posting says | Leads with |
|---|---|---|
| `variants/ai-engineer.tex` | AI Engineer, LLM Engineer, ML Engineer, Applied AI, AI Platform | Plixiq, Aluna, LLM architecture, PyCon talk, M.Sc. Mathematics |
| `variants/ai-fullstack.tex` | AI Full Stack, Full Stack + AI, AI Product Engineer | The three products end to end: FastAPI + Next.js + LLM |
| `variants/product-engineer.tex` | Product Engineer, Founding Engineer, 0→1, early-stage startup | Products shipped alone, decisions, delivery speed |
| `variants/senior-fullstack.tex` | Senior/Staff Full Stack, Backend, no AI component | Monadical team years, architecture, code review, mentoring |

If a posting straddles two, pick the one matching the **title**, then pull one or two
bullets from the other. Do not blend them into something that reads like neither.

`README.md` at the repo root is the **fifth CV** — the public, web-shaped one, and the only one
people find without being sent it. It gets the same editorial standard as the four variants: no
beginner-level skills, no bullet dumps, no unreviewed regeneration. When the data changes in a way
that matters, update it by hand like any other variant.

## Where each CV lives

- `variants/` — few, stable, maintained. Positioning, not postings. Never written to while
  tailoring; treat them as read-only during a `/cv` run.
- `generated/` — recruiter-facing PDFs. Filenames follow
  `AlejandroSanchezYali<Variant><Company>` — e.g. `AlejandroSanchezYaliAIEngineerACME.pdf`. This is
  the name that shows up in someone's inbox, so it carries his name and the role, never a date or a
  slug. The four base PDFs live here without a company suffix, rebuilt with `agent.py build`.

**When to add a fifth variant:** only when the same adaptation has been made three times. Two
adaptations are a coincidence; three is a role type worth maintaining. Until then, adapt.

**Why not more variants:** they do not update themselves. Every new product or metric in
`resume-master.json` means reviewing each variant by hand. Four is a maintainable number; eight
becomes a set of CVs that quietly go stale.

**Rebuilding the base PDFs:** `uv run python agent.py build` compiles all four variants into
`generated/` under their recruiter-facing names. Use it to preview a change or to produce a
company-suffixed CV. Do not commit the four base PDFs by hand — CI recompiles and commits them, and
a locally built PDF differs by a few bytes across TeX versions.

**Syncing after a data change:** when `resume-master.json` changes materially — a new project, a
corrected metric, a status change — review all five CVs (the four variants plus `README.md`) in
one pass rather than fixing whichever one is next needed. Report which ones you changed and which
you deliberately left alone.

## Workflow

1. Read the job description. If given a URL, fetch it.
2. Name the variant you picked and why, in one line, before writing anything.
3. Read that `.tex` and `data/resume-master.json`.
4. Adapt — and adapting means **reordering and swapping in bullets that already exist in the
   JSON**, plus rewriting the summary for this role. Nothing else.
5. Write to `generated/AlejandroSanchezYali<Variant><Company>.tex` — Variant is one of AIEngineer,
   AIFullStack, ProductEngineer, SeniorFullStack; Company is the company name in PascalCase with no
   spaces or punctuation.
6. Compile: `uv run python agent.py compile generated/<name>.tex` — the PDF lands beside it under
   the same name.
7. If it fails, read the error, fix the LaTeX, recompile. Escaping is the usual culprit.
8. Report: variant used, what changed, what the posting asked for that he does not have.

## Honesty rules — non-negotiable

- Never add a technology, a role, a metric or a year that is not in `resume-master.json`.
- If the posting requires something he lacks (Go, Kubernetes, Terraform, Airflow, Spark),
  leave it unaddressed. Do not imply it. Tell him about the gap in your report instead.
- Only use GitHub numbers from `open_source.cv_highlights`. Everything in
  `open_source.excluded_from_cv` is off-limits, and the reasons are written there.
- Star counts and rankings drift — if they were verified more than ~3 months ago
  (`open_source.last_verified`), re-check with `open_source.verify_command` before using them.
- Recompute years, never copy them from a `.tex`. Engineering started **Aug 2018** and teaching
  **Jan 2010**; skills carry `start_year`. A CV written last year is already stale by one.
- Check each project's `status` field before describing it. Not everything is live: Aluna is
  built and verified end to end but its production environment carries no real traffic yet.
  Marketing copy on a product's own website may describe the business, not the software.

## How to write a bullet

Decision or outcome first, number inside, technology last. Not "Built X using Y".

- Bad: "Built a multi-tenant SaaS platform using Python, FastAPI and LiteLLM"
- Good: "Sole architect and engineer of a multi-tenant SaaS that resolves customer inquiries
  in ~2 seconds and escalates the rest with full context — Python/FastAPI, LiteLLM, PostgreSQL"

Every job should carry at least one bullet showing an architectural decision and its
trade-off, because that is what separates him from a candidate with the same stack list.

## Facts worth having in mind

- 8+ years engineering (since Aug 2018) plus 11 years teaching ML and mathematics.
- M.Sc. Mathematics, Universidad de Antioquia. PyCon Colombia 2024 speaker (JAX/Flax).
- Three products live and owned end to end: Plixiq, Aluna, VitaStock.
- 464★ / 110 forks on the open-source conversational AI avatar.
- Colombia, UTC-5, full-day overlap with US Eastern. No sponsorship needed.
- Rate anchors: ~$7,500/month full-time, $63/hour consulting.

## Known gaps — do not paper over them

No Kubernetes, Terraform, Airflow, dbt or Spark. No large-scale traffic numbers. No formal
LLM evaluation or observability tooling in production yet. Rust and Solidity are beginner
level. When a posting centers on any of these, say so in your report rather than stretching
the wording.
