---
name: interview
description: |
  Prepare Alejandro for a specific interview — HR screen, technical round, or system
  design. Use when given a company, a job posting, or a request like "prepárame para
  la entrevista con X" / "help me prep for this interview". Builds on the master
  playbook and tailors it to that company.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - WebFetch
  - WebSearch
---

# Interview Prep

Master playbook: `interview-prep/interview-simulation.md` — positioning, seven story
beats, HR and technical simulations, landmines, questions to ask. Read it first; do not
rewrite it. Produce a short company-specific supplement instead.

## Workflow

1. Research the company: their site, engineering blog, GitHub, the posting. Find at
   least one concrete detail he can name in the room.
2. Read the playbook and `data/resume-master.json`.
3. Write `interview-prep/<company>-<role>.md` with only what is specific to them:
   - Which of the eight stories fits their product, and why
   - The three technical areas they are most likely to probe, with his angle on each
   - Where his profile is weak against *this* posting, and the honest answer for it
   - Three questions for him to ask, tied to something real about them
   - A tailored "why this company" answer with a specific detail in it
4. Keep it under 150 lines. It is a supplement, not a second playbook.

## Rules

- Answers are spoken, so write them the way he would say them: contractions, first
  person, one idea per sentence. Beats to improvise from, never a script to recite.
- Every claim must trace to `resume-master.json` or the playbook. No invented projects
  or numbers.
- Always include at least one honest gap and the answer for it. Conceding a real
  limitation early is what buys credibility on everything else.
- His strongest technical chains: Plixiq (architecture → multi-tenant isolation → SSE vs
  WebSockets) and Aluna (two-service split → durable pipeline → dedup before quota).
- Aluna's production environment carries no real traffic yet. He must volunteer that himself,
  early and level. The architecture doc verified against a commit is the evidence that
  turns the concession into a strength. His unfair advantage is going one level below the API — pre-training,
  backprop as the chain rule over a DAG, embeddings, the JAX/Flax parallelism talk.
- Weakest areas, do not paper over them: no large-scale traffic, no formal LLM evals in
  production yet, no Kubernetes or Terraform, no tests in the public flagship repos.
