# Alejandro Sánchez Yalí

**AI Full Stack Engineer · Mathematician**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-asanchezyali-blue?logo=linkedin)](https://www.linkedin.com/in/asanchezyali)
[![GitHub](https://img.shields.io/badge/GitHub-asanchezyali-black?logo=github)](https://github.com/asanchezyali)
[![Website](https://img.shields.io/badge/Website-asanchezyali.com-green)](https://asanchezyali.com)
[![Email](https://img.shields.io/badge/Email-asanchezyali%40gmail.com-red?logo=gmail)](mailto:asanchezyali@gmail.com)
[![Schedule](https://img.shields.io/badge/Schedule-Book%20a%20Call-orange)](https://cal.com/asanchezyali/full-time-opportunities)

I spent eleven years teaching mathematics and machine learning at Universidad de Antioquia, then eight
building production software. For the last two years I have been designing and shipping LLM-powered
products end to end — architecture, backend, frontend and deploy — mostly on my own.

Based in Colombia (UTC-5), which overlaps a full working day with US Eastern.

---

## Products

**[Plixiq](https://plixiq.com) — AI customer support on WhatsApp**
Multi-tenant SaaS where AI agents resolve routine inquiries in about two seconds and escalate the rest
to human operators with the full conversation intact. Sole architect and engineer: a modular monolith
with 10 DDD bounded contexts whose boundaries are enforced by a lint rule in CI, and a multi-provider
LLM layer through LiteLLM so switching providers is a configuration change. ~40,000 lines to a
near-complete MVP in four months part-time, running at $60–80/month.
`Python` `FastAPI` `LiteLLM` `RAG` `PostgreSQL` `Redis` `ARQ` `Next.js` `SSE`

**[Aluna](https://www.aluna.works) — AI recruitment platform for staffing agencies**
CVs are scored automatically, an agent interviews candidates over WhatsApp or web chat, and the
recruiter gets a shortlist and a client-ready report. Lead engineer; built in three months: 336 source
files across 4 packages, 26 tables, 11 external providers. Two services with one responsibility each —
a Next.js 15 application that owns all domain state, and a stateless FastAPI service that owns model
calls and the WhatsApp channel.
`Next.js 15` `FastAPI` `LiteLLM` `Inngest` `Claude` `Gemini` `PostgreSQL` `WhatsApp Cloud API`

**[VitaStock](https://vitastock.piagents.dev) — surgical supply chain for private clinics**
Twelve modules and five roles replacing spreadsheet-based inventory and procurement in Colombian
surgical clinics. Surgery scheduling with supply baskets and real-time consumption tracking, lot-level
traceability with expiry alerts, and true per-patient cost through a cardex. Five months in production.
`Python` `FastAPI` `Next.js` `TypeScript` `PostgreSQL` `Docker` `Railway`

---

## Experience

**AI Specialist** · Lapzo · Remote, Mexico · *Aug 2025 – Present*
- Lead member of the AI Committee, standardising how the organisation builds with AI
- Designed and built a Digital Professor that converses with learners in real time and teaches through interactive slides
- Owned the architecture connecting LLM services, voice synthesis and the real-time communication layer

**Independent Software & AI Consultant** · Remote · *Aug 2024 – Present*
- Lead engineer of Aluna; built a multi-tenant AI customer service agent for CREARIA on WhatsApp Cloud API, LiteLLM, RAG and MCP
- Led technical design sessions with clients, turning business requirements into architectures and naming the trade-off behind each decision
- Designed the database architecture for a client's workflow automation platform and served as code reviewer for their development team

**Full Stack Engineer** · Monadical · Remote, Canada/US · *Apr 2021 – Aug 2024*
- Three years on a distributed team across Canada, the US and Latin America
- Built full stack applications in Python (Django, FastAPI) and TypeScript (React, Next.js), with REST and GraphQL APIs
- Led frontend architecture and testing strategy (Vitest, Jest, TDD); reviewed code and mentored engineers

**Full Stack Engineer** · BCFort · Medellín, Colombia · *Aug 2018 – Oct 2020*
- Designed system architecture for blockchain and analytics platforms: smart contract patterns, data models, service boundaries
- Built decentralised applications and NFT marketplaces with React, Web3.js, Ethereum and Hyperledger

**Professor of Mathematics & Machine Learning** · Universidad de Antioquia · *Jan 2010 – Oct 2021*
- Taught Machine Learning, Data Science and Mathematics with Python, NumPy, Pandas, TensorFlow and PyTorch
- Built the AI/ML elective curriculum for the Mathematics Institute and mentored student research

---

## Technical Skills

| | |
|---|---|
| **Languages** | Python (8+ years), TypeScript (6+ years), JavaScript (6+ years), SQL |
| **AI & LLMs** | LangChain, LangGraph, LiteLLM, RAG, MCP, OpenAI API, Whisper, ElevenLabs, agentic development |
| **ML & Mathematics** | PyTorch, TensorFlow, Scikit-learn, JAX, Flax, NumPy, Pandas, linear algebra, probability, statistical inference |
| **Backend** | FastAPI, Django, Django REST Framework, Flask, NestJS, Node.js, Express, REST, GraphQL, microservices |
| **Frontend** | React.js (7+ years), Next.js (6+ years), Tailwind CSS, Shadcn UI, Redux, Zustand, Zod, Three.js |
| **Data & Infrastructure** | PostgreSQL, Redis, MongoDB, MySQL, Docker, AWS, GCP, GitHub Actions, CI/CD |
| **Engineering** | Clean architecture, DDD, SOLID, modular monolith, TDD, Vitest, Jest, code review |

---

## Open Source

- **[talking-avatar-with-ai](https://github.com/asanchezyali/talking-avatar-with-ai)** — 464 stars, 110 forks.
  Open-source conversational AI avatar: OpenAI GPT, Whisper, ElevenLabs, Rhubarb lip-sync, Three.js
- **[Monadical-SAS/Morpheus](https://github.com/Monadical-SAS/Morpheus)** — 19 pull requests.
  Open-source AI image generation platform: FastAPI, React, Stable Diffusion
- 486 GitHub stars across own open-source projects — top 4.9% of ranked GitHub profiles

---

## Talks & Writing

- **[Scaling Learning Models: Parallelism Strategies in JAX with Flax](https://www.youtube.com/watch?v=m4hP1soE414)** — PyCon Colombia, 2024
- [Building Plixiq: a multi-tenant WhatsApp AI support platform](https://asanchezyali.com) — architecture case study
- [Pre-training: the idea behind every LLM](https://asanchezyali.com)
- [Neural Networks as DAGs of Parameterized Computational Programs](https://www.asanchezyali.com/blog/en/differentiable-programming/20240923DifferentiablePrograms)
- [Revolutionizing Animation: Building Digital Humans with LLMs](https://monadical.com/posts/build-a-digital-human-with-large-language-models.html)

I also host a weekly study group in Spanish on mathematics, software engineering and AI.

---

## Education

**M.Sc. in Mathematics** · Universidad de Antioquia · 2010 – 2013
**B.Sc. in Teaching Mathematics and Physics** · Universidad de Antioquia · 2004 – 2009

---

## About this repository

`data/resume-master.json` is the single source of truth. `variants/` holds four curated CVs —
AI Engineer, AI Full Stack, Product Engineer and Senior Full Stack — each a self-contained LaTeX
file compiled with `uv run python agent.py compile variants/<name>.tex`. The AI Full Stack variant
is published as a PDF on the [`technical-resume`](../../tree/technical-resume) branch.

---

## Let's Connect

I'm open to full-time remote roles in AI and full stack engineering.

[Schedule a call](https://cal.com/asanchezyali/full-time-opportunities) ·
[LinkedIn](https://www.linkedin.com/in/asanchezyali) ·
[Website](https://asanchezyali.com) ·
asanchezyali@gmail.com
