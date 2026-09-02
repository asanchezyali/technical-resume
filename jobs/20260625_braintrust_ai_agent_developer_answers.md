# Braintrust (Industry Genome) - AI Agent Developer Application Answers

## Personal information
- **Legal first name:** Alejandro
- **Legal last name:** Sánchez Yalí
- **Email:** asanchezyali@gmail.com
- **LinkedIn profile URL:** https://www.linkedin.com/in/asanchezyali
- **Website:** https://asanchezyali.com

## Are you okay with the posted pay rate? (budget $6,000 – $8,000/mo)
$7,500/mo  _(adjust to your preference — mid-to-high of the posted range)_

## Do you meet the timezone requirement (overlap 3-4 hrs EST/EDT)?
Yes

## When are you available to start?
Right away

## Add your booking calendar URL
https://cal.com/asanchezyali/full-time-opportunities

## Are you legally authorized to work in the country where the job is located?
No (working remotely from Colombia)

## Will you now or in the future require visa sponsorship?
No

## Resume
Attach: generated/AlejandroSanchezYaliAIEngineer.pdf (or your latest AI Engineer PDF)

---

## Q1: Describe an AI-powered application or product that you personally built and deployed for real-world commercial use. Provide links to relevant work.

I built and deployed **Plixiq** (https://plixiq.com) — a multi-tenant SaaS platform that lets businesses deploy AI-powered WhatsApp agents with automatic human escalation. It's been in production for 3 months serving real business clients.

I personally owned the full architecture and implementation. The backend is a modular monolith in Python/FastAPI structured with DDD bounded contexts (Identity, AgentConfig, Conversation, Escalation, Messaging) and an event-driven design. Each incoming WhatsApp message flows through an LLM pipeline with RAG for business-specific context; when the agent can't confidently resolve a request, an escalation workflow routes the conversation to a human operator. I integrated multiple LLM providers through LiteLLM (with fallback), built real-time conversation monitoring over SSE, role-based access control, background job processing with ARQ, Redis caching, and async PostgreSQL with migrations. The frontend is Next.js + React + TypeScript. Deployed with Docker on Railway with CI/CD.

The same core was deployed for **CREARIA (Colombia)** as a customer-service agent integrating WhatsApp Cloud API, LiteLLM, RAG, and MCP integrations.

Other relevant, publicly available work:
- **Digital Human — interactive AI avatar** (464★, 110 forks): https://github.com/asanchezyali/talking-avatar-with-ai — conversational AI with OpenAI GPT, Whisper, and ElevenLabs, real-time lip-sync, Three.js/React Three Fiber.
- **Morpheus — AI image generation platform** (open source, 19 PRs contributed): https://github.com/Monadical-SAS/Morpheus
- Technical writeup on building digital humans with LLMs: https://monadical.com/posts/build-a-digital-human-with-large-language-models.html

---

## Q2: Which LLM providers and APIs have you worked with (OpenAI, Anthropic, Gemini, etc.)? Describe a project where you integrated an LLM into a workflow or product.

I've worked with **OpenAI** (GPT models, Whisper), **Anthropic Claude** (including daily professional use of Claude Code for 1.5+ years), and a range of providers via **LiteLLM**, which I use to route across providers (OpenAI, Anthropic, Groq, and others) with fallback. I've also worked with OpenAI's Whisper for speech-to-text and ElevenLabs for text-to-speech, plus orchestration frameworks LangChain and LangGraph, and RAG and MCP for context and tool integration.

At **Lapzo**, I designed and built a **Digital Professor** system — an AI platform that holds real-time conversations with learners and explains course content through interactive slides. I used LangChain and LangGraph for the conversational pipeline, integrated ElevenLabs for natural voice synthesis, and built the real-time layer with Next.js, NestJS, and Firebase Realtime Database. I owned the architectural decisions: choosing the LLM orchestration stack, designing how voice synthesis plugs into the conversation flow, and defining the boundaries between the LLM, voice, and real-time services. I also built an AI-powered content generator using LangChain and n8n for workflow automation.

---

## Q3: This role requires work across backend, database, APIs, and frontend. Which of the following have you worked with professionally, and for how long? (Python, JavaScript/TypeScript, React/Next.js, PostgreSQL/Supabase, REST APIs/Webhooks)

All of them, professionally and in production:
- **Python** — 8+ years (Django, FastAPI, Flask; AI/ML and backend)
- **JavaScript/TypeScript** — 6+ years (Node.js, NestJS, Express)
- **React / Next.js** — React 7+ years, Next.js 6+ years
- **PostgreSQL** — 6+ years (async PostgreSQL with migrations on recent projects); also MongoDB, MySQL, Firebase, Redis
- **REST APIs / Webhooks** — 6+ years building RESTful APIs (also GraphQL); webhook-driven integrations including WhatsApp Cloud API and Stripe

I've delivered full-stack products end-to-end across all four layers — e.g., Plixiq and VitaStock (a medical supply-chain platform, 5 months in production) both span FastAPI backends, PostgreSQL, REST APIs/webhooks, and Next.js frontends that I built myself.

---

## Q4: This role requires full-time commitment and at least 4 hours of overlap with US Eastern Time. What country/time zone are you located in, and are you available for this schedule?

I'm based in **Colombia (COT, UTC-5)**, which is aligned with US Eastern Time year-round, so I comfortably overlap a full working day with EST/EDT — well beyond the required 4 hours. I'm available for a full-time, 40 hrs/week commitment and can start right away. I have years of experience working with US- and Canada-based distributed teams (Monadical) and multiple international freelance clients, collaborating async over Slack and in regular syncs.

---

## Q5: Have you built or maintained multi-step automated workflows (N8N, Zapier, Airflow, custom pipelines, etc.)? Briefly describe the most complex workflow you've implemented.

Yes — both with **n8n** and with **custom pipelines**.

At Lapzo I used n8n to automate an AI-powered educational content-generation pipeline, chaining LLM calls (LangChain/LangGraph) with content-processing and delivery steps.

My most complex workflow is the **WhatsApp AI agent pipeline** behind Plixiq/CREARIA, which I built as a custom event-driven system. A single customer message triggers a multi-step flow: webhook ingestion → tenant resolution and auth → conversation-state hydration from Redis → RAG context retrieval → LLM inference via LiteLLM (with provider fallback) → tool/MCP calls when needed → response generation → and a conditional **escalation branch** that, when the agent detects it can't resolve the request, routes the conversation to the right human operator based on configurable triggers. The hard parts were managing conversation state across asynchronous WhatsApp delivery (solved with Redis + ARQ background jobs), keeping multi-tenant data isolated (PostgreSQL row-level scoping), and provider reliability (LiteLLM fallback). It's been running in production for 3 months.
