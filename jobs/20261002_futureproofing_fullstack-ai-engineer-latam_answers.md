# Futureproofing · Fullstack AI Software Engineer - LATAM (contract, USD 6–8k/month senior retainer) · application answers

Form: https://jobs.ashbyhq.com/futureproofing/2e49af5e-3415-46a9-ad0b-aa1516a99096/application (Ashby). Resume: `generated/AlejandroSanchezYaliAIFullStack.pdf`.
**Posting says "Based in Argentina, Brazil, or Peru".** Apply anyway and add the note below.

## Logistics (same every time)
- Legal name: Alejandro Sánchez Yalí · asanchezyali@gmail.com · [phone on file]
- LinkedIn: https://www.linkedin.com/in/asanchezyali · Site: https://asanchezyali.com · GitHub: https://github.com/asanchezyali
- Calendar: https://cal.com/asanchezyali/full-time-opportunities
- Location: Medellín, Colombia (COT, UTC-5; same as US Eastern most of the year). Fully remote.
- Work authorization: not authorized to work on-site in the US; no sponsorship required (remote contractor from Colombia)
- Availability: right away, full time
- English: B2 (upper-intermediate) on every form
- Rate: from USD 4,000/month full-time, negotiable; USD 63/hour consulting. Ask for their range first when possible.

## Note on location (put it in any free-text field)
I'm based in Colombia (UTC-5). Your posting lists Argentina, Brazil and Peru; if Colombia is an option for this engagement I'd like to be considered, otherwise please keep me in mind for the next one.

## Compensation
Senior (L5+) retainer USD 6,000–8,000/month full-time: yes. If asked for a number: 7,000.

## Why me
I build and run LLM systems end to end, not demos. Plixiq is a multi-tenant WhatsApp agent platform I architected alone: FastAPI modular monolith with 14 bounded contexts enforced in CI, a multi-provider LLM layer (Groq default, OpenAI fallback) so switching providers is a config change, RAG over tenant documents, and human escalation with full conversation context. At Lapzo I shipped an HR agent on LangGraph/FastAPI/PostgreSQL that answers policy questions with citations and executes HR requests only after human confirmation, with per-tenant isolation; I also built the content-generation pipelines (LangChain, LangGraph, n8n, Celery workers) that the platform's users rely on, and a real-time voice Digital Professor with ElevenLabs. I use Claude Code daily as my primary development workflow (1.5+ years). M.Sc. in Mathematics and 11 years teaching machine learning, so I can explain the trade-offs, not just ship them.

## Evaluation and feedback loops (they ask explicitly)
What I have: every interaction is logged with inputs, retrieved context and output; I keep a regression set built from real broken conversations and replay it before changes; escalation rate is the quality proxy I watch. What I have not built yet: formal offline evals or an LLM-as-judge pipeline. If I joined, that would be the first thing I'd set up, starting from the failure cases already logged.

Weakest point: country eligibility.
