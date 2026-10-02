# HireLATAM · Remote AI Engineer (USD 6,500/month, US client) · application answers

Form: https://recruiterflow.com/hirelatam/jobs/1721 (Recruiterflow; the form renders in-page). Resume: **`generated/AlejandroSanchezYaliAIEngineerHireLATAM.pdf`** (tailored: summary leads with WhatsApp agents, HR agent with human confirmation, voice Digital Professor, logging and regression sets).
**Mandatory: a voice or video recording of at least 30 seconds, in English.** Without it the application is auto-rejected. Script below. Knockout questions are mandatory too; honest answers below.

## Logistics (same every time)
- Legal name: Alejandro Sánchez Yalí · asanchezyali@gmail.com · [phone on file]
- LinkedIn: https://www.linkedin.com/in/asanchezyali · Site: https://asanchezyali.com · GitHub: https://github.com/asanchezyali
- Calendar: https://cal.com/asanchezyali/full-time-opportunities
- Location: Medellín, Colombia (COT, UTC-5; same as US Eastern most of the year). Fully remote.
- Work authorization: not authorized to work on-site in the US; no sponsorship required (remote contractor from Colombia)
- Availability: right away, full time
- English: B2 (upper-intermediate) on every form
- Rate: from USD 4,000/month full-time, negotiable; USD 63/hour consulting. Ask for their range first when possible.

## Salary
Accept the fixed USD 6,500/month. Schedule Monday–Friday 9–6 LATAM hours: yes.

## Recording script (45–60 seconds, English; record on the phone, quiet room)
Hi, I'm Alejandro Sánchez Yalí, an AI engineer based in Colombia. For the last three years I've been building LLM systems that run in production, not prototypes. I architected Plixiq, a multi-tenant WhatsApp agent platform with a multi-provider LLM gateway, retrieval over each tenant's documents, and human escalation with full conversation context. At Lapzo I shipped an HR agent on LangGraph that executes requests only after human confirmation, a real-time voice professor with ElevenLabs, and the content-generation pipelines with Celery workers that the platform's users depend on. I log every interaction, keep a regression set of real failed conversations, and I'd be glad to build the automated evaluation layer on top of that. I'm available right away, full time, in LATAM hours. Thank you.

## Likely knockout questions (answer honestly)
- Production multi-agent experience with real users? → Yes: the Lapzo pipelines and HR agent (users), Plixiq (built and deployed, no customer traffic yet — say so if asked for scale).
- Streaming / low latency? → Yes: WebSocket streaming in Plixiq (~2-second responses), real-time voice with ElevenLabs in the Digital Professor, Firebase Realtime for the live layer.
- Automated evaluation frameworks / LLM-as-judge? → What I have: every interaction is logged with inputs, retrieved context and output; I keep a regression set built from real broken conversations and replay it before changes; escalation rate is the quality proxy I watch. What I have not built yet: formal offline evals or an LLM-as-judge pipeline. If I joined, that would be the first thing I'd set up, starting from the failure cases already logged.
- Observability (LangSmith, Phoenix, Arize, Datadog)? → Structured interaction logs with inputs, retrieved context, outputs, token and latency per call; I have not run LangSmith/Phoenix/Arize in production; I know what they add and would adopt one in the first weeks.
- Voice/call agents (STT/TTS/telephony)? → TTS with ElevenLabs and STT with Whisper in the Digital Professor and the open-source avatar (464 stars). No telephony (Twilio/SIP) or barge-in yet.
- English level? → B2, upper-intermediate (they ask "advanced"; apply anyway and say B2).
- Home office: dedicated workspace, fiber internet; power redundancy: answer truthfully (UPS? if not, say "planning a UPS").

## Why me (if free text)
I build and run LLM systems end to end, not demos. Plixiq is a multi-tenant WhatsApp agent platform I architected alone: FastAPI modular monolith with 14 bounded contexts enforced in CI, a multi-provider LLM layer (Groq default, OpenAI fallback) so switching providers is a config change, RAG over tenant documents, and human escalation with full conversation context. At Lapzo I shipped an HR agent on LangGraph/FastAPI/PostgreSQL that answers policy questions with citations and executes HR requests only after human confirmation, with per-tenant isolation; I also built the content-generation pipelines (LangChain, LangGraph, n8n, Celery workers) that the platform's users rely on, and a real-time voice Digital Professor with ElevenLabs. I use Claude Code daily as my primary development workflow (1.5+ years). M.Sc. in Mathematics and 11 years teaching machine learning, so I can explain the trade-offs, not just ship them.

Weakest points: "advanced English" vs his B2; no LangSmith/Arize in production; no telephony. All three are stated plainly above.
