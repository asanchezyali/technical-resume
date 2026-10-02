# Trust Wallet · Lead AI Engineer (LLM & Agents) · Remote - Global · application answers

Form: https://jobs.ashbyhq.com/trust-wallet/87c32867-4e32-473c-b818-8eae0306f46a/application (Ashby). Resume: **`generated/AlejandroSanchezYaliAIEngineerTrustWallet.pdf`** (tailored: summary adds the two BCFort blockchain years and the reliability vocabulary of the posting).
Posted 2-oct-2026. Requirements that do not match: **Golang** (not in his data) and **LLM features with 10,000+ active users**. Both go stated plainly.

## Logistics (same every time)
- Legal name: Alejandro Sánchez Yalí · asanchezyali@gmail.com · [phone on file]
- LinkedIn: https://www.linkedin.com/in/asanchezyali · Site: https://asanchezyali.com · GitHub: https://github.com/asanchezyali
- Calendar: https://cal.com/asanchezyali/full-time-opportunities
- Location: Medellín, Colombia (COT, UTC-5; same as US Eastern most of the year). Fully remote.
- Work authorization: not authorized to work on-site in the US; no sponsorship required (remote contractor from Colombia)
- Availability: right away, full time
- English: B2 (upper-intermediate) on every form
- Rate: from USD 4,000/month full-time, negotiable; USD 63/hour consulting. Ask for their range first when possible.

## Why me
I build and run LLM systems end to end, not demos. Plixiq is a multi-tenant WhatsApp agent platform I architected alone: FastAPI modular monolith with 14 bounded contexts enforced in CI, a multi-provider LLM layer (Groq default, OpenAI fallback) so switching providers is a config change, RAG over tenant documents, and human escalation with full conversation context. At Lapzo I shipped an HR agent on LangGraph/FastAPI/PostgreSQL that answers policy questions with citations and executes HR requests only after human confirmation, with per-tenant isolation; I also built the content-generation pipelines (LangChain, LangGraph, n8n, Celery workers) that the platform's users rely on, and a real-time voice Digital Professor with ElevenLabs. I use Claude Code daily as my primary development workflow (1.5+ years). M.Sc. in Mathematics and 11 years teaching machine learning, so I can explain the trade-offs, not just ship them.

The posting asks for two years of Web3: at BCFort (2018–2020) I designed the architecture of blockchain and analytics platforms on Ethereum and Hyperledger, including NFT marketplaces and smart-contract patterns, with Python/Django, Node.js and Web3.js.

## On Go
I have not written Go professionally. My backends are Python (FastAPI, Django, Celery) and TypeScript (Node, NestJS), and I write Rust on a personal project. Go is a small language and I would be productive in weeks, but I will not claim it today.

## On "10,000+ active users"
The LLM features with real users I own are the Lapzo content-generation pipelines and the course assistant. My own products (Plixiq, Aluna) are built and deployed but are not yet carrying real traffic. I'd rather be clear about that than oversell it.

## Evaluation discipline
What I have: every interaction is logged with inputs, retrieved context and output; I keep a regression set built from real broken conversations and replay it before changes; escalation rate is the quality proxy I watch. What I have not built yet: formal offline evals or an LLM-as-judge pipeline. If I joined, that would be the first thing I'd set up, starting from the failure cases already logged.

Weakest points: Go, user scale, and "Lead" title. Still worth sending: the agent/RAG/reliability scope is exactly what he does.
