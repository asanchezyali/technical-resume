# O3 World - AI Developer Application Answers

## Hourly rate
$63/hr

## Availability
Right away

## Booking calendar
https://cal.com/asanchezyali/full-time-opportunities

## Legally authorized to work in the country where the job is located?
No (remote from Colombia)

## Visa sponsorship required?
No

---

## Q1: Tell us about an LLM-powered application, prototype, or internal tool you've built. What was the use case, what models/tools did you use, and what parts of the solution did you personally own?

At Lapzo, I designed and built a Digital Professor system — an AI-powered platform that engages users in real-time conversations and explains educational content through interactive slides. I used LangChain and LangGraph for the conversational AI pipeline, integrated ElevenLabs API for natural text-to-speech synthesis, and built the real-time layer with Next.js, NestJS, and Firebase Realtime Database. I personally owned the architectural decisions: selecting the LLM orchestration stack, designing how voice synthesis integrates with the conversation flow, and defining the system boundaries between services. I also built the AI-powered content generator using n8n for workflow automation.

Separately, as an independent consultant, I built Plixiq (plixiq.com) — a multi-tenant SaaS platform that lets businesses deploy AI-powered WhatsApp agents. It uses LiteLLM for multi-provider LLM support with fallback, RAG for context retrieval, and an automatic escalation system that routes conversations to human agents based on configurable triggers. I designed the full architecture as a modular monolith with DDD bounded contexts. It's been in production for 3 months.

---

## Q2: Walk us through a project where you integrated an AI application with external systems or APIs (for example: HubSpot, Salesforce, internal databases, or other SaaS tools). What did you connect, what challenges came up, and how did you handle them?

For CREARIA (Colombia), I built a multi-tenant AI customer service agent that integrates with WhatsApp Cloud API, LiteLLM (connecting to multiple LLM providers like Groq and OpenAI), and MCP integrations. The system receives customer messages via WhatsApp webhooks, processes them through an LLM pipeline with RAG for business-specific context, and responds automatically. When the AI detects it cannot resolve a request, it triggers an escalation workflow that routes the conversation to the appropriate human agent based on keyword detection and role configuration.

The main challenges were: (1) managing conversation state across async WhatsApp message delivery, which I solved with Redis caching and ARQ background job processing; (2) handling multi-tenant isolation so each business client's data and agent configurations remain separate, solved through PostgreSQL row-level scoping; and (3) LLM provider reliability, addressed with LiteLLM's fallback mechanism across multiple providers.

---

## Q3: Tell us about a project where you built or supported a lightweight user interface and deployed the application for real use. What frontend tools did you use, how was it deployed, and what did you personally handle across the build and release process?

VitaStock — a medical supply chain management system I built for clinics. The frontend is Next.js with React, TypeScript, Tailwind CSS, and shadcn/ui components. I personally handled the full frontend: role-based dashboards (Admin, Pharmacist, Doctor, Operating Room, Management), procurement workflows (quotation requests, purchase orders, receptions with lot tracking), and multilingual support (ES/EN) using next-intl.

For deployment, I containerized both the FastAPI backend and Next.js frontend with Docker and deployed on Railway with CI/CD pipelines. The build process uses standard Next.js production builds. The app has been in production for 5 months serving real clinic operations, including PDF report generation for inventory and procurement documents.

---

## Q4: Please note, this is a part-time (16-20 hours per week), 3-month contract. Candidates must be able to overlap with core EST U.S. business hours.

I'm fully available for a part-time 16-20 hrs/week engagement. I'm based in Colombia (COT/EST-equivalent timezone), so I naturally overlap with core U.S. Eastern business hours. I have experience collaborating with US-based and Canadian distributed teams at Monadical and with multiple freelance clients, communicating asynchronously via Slack and participating in regular syncs. I can start right away.
