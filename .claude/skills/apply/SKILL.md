---
name: apply
description: |
  Answer a job application form or written screening questions for Alejandro.
  Use when given application questions, a Braintrust/Wellfound/Otta form, or a request
  like "responde estas preguntas de la aplicación" / "answer this application".
  Produces a markdown file in jobs/ he can copy from.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - WebFetch
---

# Application Answers

Source of truth: `data/resume-master.json`. Past examples of tone and depth:
`jobs/20260625_braintrust_ai_agent_developer_answers.md` and
`jobs/20260318_ai_healthcare_answers.md`. Match that voice — first person, concrete,
no marketing adjectives.

## Workflow

1. Read the questions. Fetch the posting if given a URL.
2. Read `data/resume-master.json` and, if the questions are technical, the relevant
   base CV in `variants/`.
3. Write `jobs/<YYYYMMDD>_<company>_<role>_answers.md`.
4. Open with the logistics block, then one section per question in the original order.
5. Tell him at the end which answers are weakest and why.

## What lives in jobs/

`jobs/` is the archive of every application, named for him rather than for a recruiter:

- `YYYYMMDD_<company>_<role>.md` — the posting itself, saved when it arrives. Job ads disappear, and
  three weeks later an interview invitation arrives for a role nobody can re-read.
- `YYYYMMDD_<company>_<role>_answers.md` — the answers submitted with that application.

Dates lead here because this directory is chronological working memory. The recruiter-facing
filenames live in `generated/` instead, where they follow `AlejandroSanchezYali<Variant><Company>`.

Save the posting even when only answering questions. It costs one file and it is the difference
between preparing for an interview and guessing.

## Logistics block — same every time

- Legal name: Alejandro Sánchez Yalí · asanchezyali@gmail.com
- LinkedIn: https://www.linkedin.com/in/asanchezyali · Site: https://asanchezyali.com
- Calendar: https://cal.com/asanchezyali/full-time-opportunities
- Location: Colombia (COT, UTC-5) — full working day of overlap with US Eastern
- Work authorization: not authorized to work on-site in the US; no sponsorship required
- Availability: right away, full time
- Rate: ~$7,500/month full-time; $63/hour consulting. Ask for their range first when possible.

## How to answer

- Lead with the specific system, then what he personally owned, then the trade-off he chose.
  A good answer names one decision and why the alternative lost.
- Use real numbers from the JSON: 3 products in production, 10 DDD bounded contexts,
  ~40k LOC in 4 months part-time, $60-80/month infra, 12 modules and 5 roles in VitaStock,
  ~2 second responses in Plixiq, 464 stars / 110 forks, 19 PRs to Morpheus, 5 LATAM markets.
- 150-250 words for an open question. Longer reads as padding.
- Never invent a technology, a client, a headcount or a metric. If a question asks about
  something he has not done, say what he has done that is closest and be explicit about
  the gap — that answer beats a vague one.

## Recurring questions, settled answers

- **Scale**: he has built multi-tenant products with real business users, not
  high-traffic systems. Say that plainly rather than dodging.
- **Evals / LLM observability**: he logs interactions with inputs, retrieved context
  and output, keeps a regression set of real broken conversations, and uses escalation
  rate as a quality proxy. He has not built formal offline evals or LLM-as-judge yet.
  Answer with what exists plus what he would build first.
- **Team vs solo**: three years on Monadical's distributed team, code reviewer for
  a client's development team, AI Committee at Lapzo. The last two years being solo is deliberate range,
  not isolation.
- **Kubernetes / Terraform / Airflow / Spark**: he has not used them. Say so.
