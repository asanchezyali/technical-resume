# MGT (Braintrust job 17740) · AI Automation Engineer (Agentic AI, remote US/Canada/LATAM) · answers

Posting: https://app.usebraintrust.com/jobs/17740/ · $90–100/hr · 1099 full-time, 40 h/wk · 3-month term, extension likely · US business-hours overlap · invited by client. Saved in `jobs/20261001_mgt_ai-automation-engineer.md`.

## Logistics
- Hourly rate: **$90** (bottom of the client's budget; maximises the chance of the intro call; the term is 3 months)
- Timezone requirement (full day overlap MST–EST): **Yes** (Colombia is UTC-5, same as US Eastern)
- Available to start: **Right away**
- Booking calendar: https://cal.com/asanchezyali/full-time-opportunities
- Legally authorized to work in the country where the job is located: **Yes** (the posting is open to LATAM; working from Colombia) — *his call: the previous Braintrust application answered "No" for a US-only role*
- Visa sponsorship: **No**
- Resume: generated/AlejandroSanchezYaliAIEngineer.pdf (already on the Braintrust profile)

## Q1 — Experience building and delivering AI/agentic automation end-to-end, development through production

The most complete example is the HR agent I built this year at Lapzo, a learning platform. It answers employees' questions about company policy with citations and executes HR requests (certificates, absences, document requests) with a human-confirmation step before anything is written. I owned it from the technical plan to staging: LangGraph for the agent graph, FastAPI, PostgreSQL with pgvector for retrieval over policy documents, a tool catalogue with a uniform result contract, per-tenant isolation enforced at the data layer, SSE streaming, and an internal htmx panel with a test bench so non-engineers could try it before the product UI existed. It is deployed in QA and staging with a runbook and a handover document; the only pieces still pending were decisions owned by product and an upstream HR data service that did not exist yet.

Before that, Plixiq: a multi-tenant platform that runs AI agents on WhatsApp with automatic escalation to a human, built and deployed on Railway. And Aluna, an AI recruitment platform where I built a durable CV-analysis pipeline on Inngest (checkpointed steps, retries, deduplication before quota) and one screening engine serving WhatsApp, web and email.

I build with Claude Code daily and have for over a year, on these same production codebases.

## Q2 — Taking ownership of an existing or partially completed build and driving it through completion

Aluna. I joined as lead engineer when it was a partially built recruitment product with an early codebase, no pipeline for CV analysis and no QA process. In three months I restructured it into two services (Next.js 15 front end, stateless FastAPI backend), built the durable analysis pipeline on Inngest, added multi-model routing through LiteLLM, and set up a PR-per-issue workflow with a QA engineer so every change had a test report. The last stretch was closing the eleven open PRs for the 1.0.0 release while running weekly reviews with the founder. Outcome: a working product the founder is now taking into commercial meetings, with the CV pipeline, the WhatsApp screening assistant and the reporting dashboard shipped and documented.

A second case: at Lapzo I inherited the course-vectorization system, which had been bolted together in n8n. I migrated it to a dedicated VM, moved the embeddings pipeline into the platform itself, and it now powers the Express-courses feature.

## Q3 — Working directly with clients or non-technical stakeholders

Most of my consulting is with founders and operations people, not engineers. With the founder of Aluna, a staffing-agency product, we ran a weekly call where I showed working features, not slides; when he came back from sales meetings with requests, I turned them into issues with a cost estimate and we decided together what went into the week. When QA found more issues than we could close, I told him the same day and we cut scope instead of slipping silently.

At Lapzo I wrote the technical plan for the HR agent as a one-page-per-section document with every open decision marked as a question for product, with the deadline it blocked. That document is what the team is using now to retake the project.

What I have learned the hard way: say the uncomfortable thing early and in writing. The costliest delay I have had was waiting for a product decision I had not escalated with a date.

## Q4 — 40 h/week for 3 months with US overlap

Yes. I am available full time starting now, for the three-month term and beyond if it is extended. I am in Colombia (UTC-5), so I overlap the full US Eastern day and most of the Pacific day. I have no other full-time commitment.

## Q5 — Client-facing and stakeholder experience in the resume

It is there under Independent Software & AI Consultant (2024–present): lead engineer for Aluna working directly with the founder, the WhatsApp support agent for CREARIA, and code review and architecture for a client's development team. Happy to add detail if useful.

## One gap, stated plainly
I have not deployed to Azure Container Apps or Function Apps. My deployments are Docker on AWS, GCP and Railway, and I have used Azure Cognitive Services. Containers, secrets, triggers and scaling are the same problem with a different console; I expect to be productive on Azure within the first week, and I say so rather than let it surprise anyone.

---
Weakest answers: Q5 is a formality. Q1 should mention the Azure gap only if the form has no better place for it; here it is at the end so he can paste it into Q1 or leave it out.
