# Master Data Structure

`data/resume-master.json` is the single source of truth. Everything else — the four CV variants in
`variants/`, the README, application answers, interview prep — is derived from it by hand or by a
Claude skill, never by a code generator.

## Root object

```json
{
  "personal":  { },
  "skills":    { },
  "experience":[ ],
  "projects":  [ ],
  "open_source": { },
  "blog_posts":[ ],
  "talks":     [ ],
  "education": [ ],
  "summary_templates": { }
}
```

## `skills`

Grouped by category (`languages`, `frontend`, `backend`, `ai_ml`, `databases`, `cloud_devops`,
`testing`, `software_engineering`, `mathematics`, `blockchain`, `data_engineering`, `automation`,
`build_tools`, `soft_skills`). Each entry:

```json
{
  "name": "Python",
  "years": 8,
  "level": "beginner | intermediate | advanced | expert",
  "categories": ["backend", "ai"],
  "display": "Python (8+ years)",
  "start_year": 2018
}
```

`years` is derived from `start_year`; treat `start_year` as the fact and recompute rather than
trusting a stale `years`. **Skills at `beginner` level stay in the data for honesty but are kept off
CVs** — listing them dilutes the advanced signal.

## `experience`

```json
{
  "id": "lapzo-2025",
  "title": "AI Specialist",
  "company": "Lapzo",
  "location": "Remote, Mexico",
  "start_date": "2025-08-01",
  "end_date": null,
  "date_range": "Aug 2025 -- Present",
  "categories": ["ai", "leadership"],
  "technologies": ["Python", "LangChain"],
  "highlights": [{ "text": "...", "categories": ["ai", "architecture"] }]
}
```

`highlights[].categories` is what makes tailoring possible: a variant selects the bullets whose
categories overlap the target role, rather than reordering by hand every time.

## `projects`

Same shape as experience, plus:

| Field | Meaning |
|---|---|
| `role` | What he actually did — `"Sole architect and engineer"`, `"Lead Engineer"` |
| `status` | **Read this before describing a project.** Not everything is live. |
| `scale` | Verifiable size, e.g. `"336 source files, 26 tables, 11 external providers"` |
| `duration` / `date_range` | How long it took; short durations on large systems are evidence of delivery speed |
| `engagement` | How the work was contracted, when it is not a plain employment relationship |
| `stars` | GitHub stars, for open-source projects only. Verify before reuse |

⚠️ A product's marketing website may describe the **business**, not the software. Aluna's site cites
results from a recruitment operation; its software carries no production traffic yet, which is what
`status` records.

## `open_source`

GitHub and GitRanks metrics, with the editorial judgement attached:

- `cv_highlights` — the only strings that may appear on a CV
- `excluded_from_cv` — claims that are technically true but misleading, each with the reason
- `last_verified` / `verify_command` — star counts drift; re-check before reuse
- `profile`, `rankings`, `top_repositories`, `contributions` — the raw numbers

## `summary_templates`

Per-role summary paragraphs used as a starting point. The years figure inside them is written by
hand — the first engineering role started **August 2018**, so the number is 8+ and grows.

## Changing the data

1. Edit `data/resume-master.json`.
2. Decide whether any of the five CVs (`variants/*.tex` and `README.md`) should change — they do not
   update themselves, on purpose. A CV should not change without someone reading it.
3. Recompile what you touched: `uv run python agent.py compile variants/<name>.tex`.
