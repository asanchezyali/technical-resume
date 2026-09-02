# Interview Simulation & Prep — Alejandro Sánchez Yalí

> Built from `data/resume-master.json`, asanchezyali.com, your Medium stories, your GitHub (live API) and your GitRanks profile.
> Everything here is meant to be *said out loud*, not read. If a sentence feels like a résumé bullet in your mouth, cut it.

---

## 0. How to use this file

1. **Read Section 1 and 2 once.** That's your positioning and your numbers. Know them cold.
2. **Memorize the beats, not the words.** Section 3 gives each story as a 5-beat skeleton. If you memorize sentences you will sound like a press release; if you memorize beats you'll sound like a person who was there.
3. **Practice out loud with a timer.** HR answers: 60–90 seconds. Technical answers: 2–3 minutes, then stop and ask "want me to go deeper on any part of that?"
4. **The `🎯 Coach` notes** tell you *why* the answer is shaped that way and where interviewers usually push.

---

## 1. Your positioning — the one thing they should remember

> **"I'm a mathematician who became a product engineer. I spent 11 years teaching math and ML at a university, then 8 years shipping production software — and for the last two years I've been building LLM products end to end, mostly alone. I'm the person who can own a system from the architecture decision down to the deploy."**

Three pillars you keep returning to, no matter the question:

| Pillar | Evidence you can name in one breath |
|---|---|
| **I ship whole products, alone** | Plixiq (~40k LOC in 4 months part-time, in production), Aluna (336 files, 26 tables, 11 providers, in 3 months), VitaStock (5 months in production in real clinics) |
| **I make architecture decisions and defend them** | Modular monolith with 10 DDD bounded contexts enforced in CI; SSE over WebSockets; dedup before quota so a re-analysis costs nothing; one conversation engine across three transports |
| **I think in structure because of the math** | M.Sc. Mathematics, category theory / linear algebra / probability; PyCon talk on JAX+Flax parallelism; essays on neural nets as DAGs of differentiable programs |

**Your differentiator sentence** (use it when they ask "why you?"):
> "Most people are either the AI person or the product person. I've been on both sides — I taught the math, and I've shipped the SaaS. That means when an LLM feature fails I can tell whether it's a prompt problem, a retrieval problem, a data problem, or an architecture problem, and I don't need three people to find out."

---

## 2. Fact sheet — the verified numbers

Use these. They're checked against live sources today.

**Career**
- 8+ years professional software engineering (since 2018), 16 years of technical work counting teaching.
- Professor, Universidad de Antioquia — Jan 2010 → Oct 2021 (11 years): ML, Data Science, Mathematics; built the AI/ML elective curriculum for the Mathematics Institute.
- BCFort (Medellín), Full Stack Engineer, Aug 2018 → Oct 2020 — blockchain/Web3, Ethereum, Hyperledger, NFT marketplaces.
- Monadical (remote, Canada/US), Full Stack Engineer, Apr 2021 → Aug 2024 — 3+ years on a distributed international team.
- Independent IT Consultant, Aug 2024 → present.
- AI Specialist, Lapzo (remote, Mexico), Aug 2025 → present — lead member of the AI Committee.

**Education**
- M.Sc. Mathematics, Universidad de Antioquia (2010–2013).
- B.Sc. Teaching Mathematics and Physics, Universidad de Antioquia (2004–2009).

**Products owned end to end**
- **Plixiq** — plixiq.com. AI customer support on WhatsApp. ~40k lines to a near-complete MVP in 4 months part-time, ~2 second responses, 10 DDD bounded contexts enforced by a CI lint rule, $60–80/month infra. In production.
- **Aluna** — aluna.works. AI recruitment platform for staffing agencies. Lead engineer, Jun 2026 → present (**3 months**). 336 source files across 4 packages, 26 tables, 11 external providers. Two services: Next.js 15 owns all domain state, a stateless FastAPI service owns model calls and the WhatsApp channel. ⚠️ **Production is provisioned but carries no real traffic yet — say this before they ask.**
- **VitaStock** — vitastock.piagents.dev. Surgical supply chain for private clinics in Colombia. 12 modules, 5 roles, lot tracking with expiry alerts, per-patient cost cardex, read-only AI assistant in Spanish. 5 months in production.

**GitHub (live, verified)**
- `talking-avatar-with-ai` (Digital Human): **464 stars, 110 forks**. (Résumé corrected from 320 → 464.)
- `ai-avatar` (Zippy): 27 stars.
- 36 public repos, 43 followers, account since 2017.
- **GitRanks: Global rank "Master 2", persona "Creator", #78,775 globally. Top 4.9% of ranked profiles for own projects (486 stars across ranked repos); top 2.4% for open-source contributions.**
- Contributions: 19 PRs to `Monadical-SAS/Morpheus`, 1 PR to `timlrx/tailwind-nextjs-starter-blog`.

⚠️ **Two accuracy fixes — now applied to `data/resume-master.json`, but know the reasoning:**
1. Your résumé listed **Morpheus at 150★**. The repo is actually at **29★**, now corrected — a curious interviewer clicks the link, and a number that doesn't match is the single fastest way to lose credibility on everything else you said. Talk about Morpheus for *what you built* (FastAPI + React + Stable Diffusion, 19 PRs), not for stars.
2. The GitRanks "contributed to repos with 10.6K stars" line is mostly one PR to a popular blog template. **Don't lean on it.** If asked, say plainly: "that ranking counts a one-line PR to a popular template — the number I'd actually stand behind is the 464 stars on the digital human project, which is mine."

**Writing & speaking**
- PyCon Colombia 2024: *"Scaling Learning Models: Parallelism Strategies in JAX with Flax"* — https://www.youtube.com/watch?v=m4hP1soE414
- Essays: *Pre-training: the idea behind every LLM*; *Zero-Shot Text Classification*; *Cryptography: The Fundamental Pillar of Blockchain*; *Neural Networks as DAGs of Parameterized Computational Programs*; *Revolutionizing Animation: Building Digital Humans with LLMs* (published on Monadical's blog).
- Hosts a weekly study group in Spanish on math, software engineering and AI.
- Site tagline: *"Mathematics × Code × AI — exploring the edges of what's computable."*

**Logistics**
- Colombia, UTC-5 → full-day overlap with US Eastern year-round.
- Remote-native since 2021. No visa sponsorship needed; not authorized to work on-site in the US.
- Calendar: https://cal.com/asanchezyali/full-time-opportunities

---

## 3. Story bank — eight stories, as beats

Learn the beats. Improvise the words. Each one should land in 90 seconds and survive three follow-up questions.

### Story A — "The modular monolith" (architecture judgment)
1. **Situation.** Plixiq: businesses want AI agents on WhatsApp, but they can't staff support 24/7. I was building it essentially alone, part-time.
2. **Tension.** The clean answer was microservices — ten separate domains, Identity, AgentConfig, Conversation, Escalation, Messaging. The honest answer was that one person cannot operate ten services.
3. **Decision.** Modular monolith: one deployable, ten bounded contexts, and — the part I care about — **the boundaries are enforced by a lint rule in CI.** A rule you don't enforce is a suggestion.
4. **Result.** ~40k lines, near-complete MVP in four months part-time, in production, running at $60–80/month because the cost scales with LLM usage, not infrastructure.
5. **Lesson.** I optimize for the team that exists, not the team on the org chart. And I make the architecture defend itself, because I know future-me will be in a hurry.
> 🎯 Coach: this is your best story for senior/staff roles. The CI-enforced boundaries detail is what separates you from someone who just read a blog post about DDD. Expect: *"how do you migrate out of the monolith later?"* → answer: the bounded contexts are already the seams; extraction means replacing an in-process call with an HTTP or queue call, and the event-driven design means several of them already talk asynchronously.

### Story B — "LiteLLM, or how I refused to marry a provider" (technical foresight)
1. Every LLM product I've built has outlived at least one provider decision.
2. So in Plixiq I never call OpenAI or Groq directly — everything goes through LiteLLM, defaulting to Groq for latency and cost, falling back to OpenAI.
3. Switching providers is a config change, not a refactor. When a provider had trouble, the fallback absorbed it and nobody in the product noticed.
4. Same pattern in the resume generator I built for myself — the model is a CLI flag.
5. Lesson: with a field moving this fast, the durable engineering decision isn't *which model*, it's *where the seam goes.*
> 🎯 Coach: great answer to "how do you keep up with how fast AI moves?" Don't say "I read a lot." Say "I architect so that being wrong is cheap."

### Story C — "The Digital Human" (the thing people actually clicked on)
1. At Monadical I wanted to see if a browser could hold a real conversation with a face attached.
2. Built it: OpenAI GPT for the reasoning, Whisper for speech-to-text, ElevenLabs for the voice, Rhubarb for lip-sync, Three.js and React Three Fiber for the 3D avatar — with real-time processing so the mouth matches the audio.
3. Open-sourced it. It's at **464 stars and 110 forks**, and I wrote the technical piece on Monadical's blog explaining how to build one.
4. The hard part wasn't the LLM — it was latency budgeting across four services, because a human notices a 400ms pause in a conversation and forgives none of it.
5. Lesson: in AI products the model is rarely the bottleneck. The plumbing is.
> 🎯 Coach: lead with the latency insight, not the star count. Mention the stars once, casually, then move on — the number does the bragging so you don't have to.

### Story D — "From the classroom to the codebase" (your origin story)
1. I taught mathematics and ML at Universidad de Antioquia for 11 years — I built the AI/ML elective curriculum for the Mathematics Institute.
2. What I loved was the moment a hard idea becomes obvious to someone. What frustrated me was that it stopped at the whiteboard.
3. So I started building — blockchain platforms at BCFort, then full-stack at Monadical — and I never stopped teaching. I still run a weekly study group in Spanish, I gave a PyCon talk on JAX and Flax parallelism, and I write long essays about pre-training and differentiable programming.
4. The teaching didn't go away; it turned into code review, mentoring, and design docs.
5. Lesson: I explain systems for a living either way. Now the explanations compile.
> 🎯 Coach: this is your "tell me about yourself" spine and the answer to "why the career change." Never frame it as leaving academia because it failed. Frame it as the same drive finding a bigger surface.

### Story E — "VitaStock and the boring domain" (product maturity)
1. Clinics manage surgical supplies in spreadsheets. Getting it wrong means a surgery starts without an implant.
2. I built VitaStock: FastAPI + async PostgreSQL, clean architecture with DDD, five real roles (Admin, Pharmacist, Doctor, Operating Room, Management), full procurement flow — quotation requests → purchase orders → receptions — with lot tracking and controlled storage.
3. Next.js frontend, bilingual ES/EN, PDF reports, Docker on Railway with CI/CD.
4. **Five months in production in real clinic operations.**
5. Lesson: the interesting engineering was the domain modeling, not the tech. Roles and lot tracking are where the real complexity lives, and I got that by sitting with the pharmacist, not by reading a spec.
> 🎯 Coach: use this whenever the interviewer's product is unglamorous (fintech ops, logistics, healthcare, internal tools). It proves you don't only chase shiny AI.

### Story F — "Agentic development, honestly" (how you actually work)
1. I've used Claude Code as my daily driver for about a year and a half, on live production projects.
2. What that means concretely: I use it to decompose problems and surface edge cases, and then I review the output like I'd review a junior's PR — because it *is* like a junior's PR: fast, confident, and occasionally wrong in a way that only shows up in production.
3. The unlock was pairing it with hard architectural guardrails. On Plixiq the CI-enforced module boundaries are what let me move fast with AI without the codebase turning to mush.
4. Result: I ship end-to-end features in a fraction of the time, and the review discipline is what keeps the quality.
5. Lesson: AI raised my throughput, so taste and review became the scarce resources, not typing.
> 🎯 Coach: expect skepticism here from senior engineers. Your credibility move is naming a failure — have one ready: a time the generated code compiled, passed tests, and was still wrong, and how your review caught it. Never say "AI writes my code." Say "I direct it and I own the output."

### Story G — "Nineteen PRs and a code review culture" (collaboration)
1. At Monadical I worked three-plus years on a distributed team across Canada, the US and Latin America — async by default.
2. I contributed 19 PRs to Morpheus, our open-source AI image platform (Python/FastAPI + React + Stable Diffusion), led the frontend architecture and component library, and pushed testing discipline — Vitest, Jest, TDD.
3. Later, as a consultant at ROCKET CODE, I was the code reviewer for their team and designed the database architecture for their orbit-control workflow platform in an NX multi-repo with Screaming Architecture.
4. I mentor. It's the part of teaching I got to keep.
5. Lesson: I've never believed the reviewer's job is to find mistakes. It's to make the next person's version easier to write.
> 🎯 Coach: this counters the biggest risk in your profile — "he's been solo for two years, can he work in a team?" Get this story out early and unprompted in HR rounds.

---

### Story H — "Aluna in three months" (delivery speed and honest engineering)
1. **Situation.** A staffing agency wanted AI to do the filtering — score the CVs, interview the candidates — without taking the hiring decision away from the recruiter.
2. **What I built, in three months.** 336 source files across 4 packages, 26 tables, 11 external providers. Two services with one responsibility each: a Next.js 15 app that owns all domain state and is the only thing that writes to Postgres, and a stateless FastAPI service that owns model calls and the WhatsApp channel and doesn't even know what a vacancy is.
3. **The decision I'd defend hardest.** The CV analysis is a durable Inngest pipeline — nine checkpointed steps, three retries — and deduplication runs *before* quota enforcement. Re-analysing an unchanged CV reuses the cached score: no model call, no plan quota consumed. Reverse those two and you're billing customers for work you didn't do.
4. **The one that saved the most code.** One conversational screening engine serving three transports — WhatsApp, signed-link web chat, and email. The transport changes; the conversation doesn't.
5. **The honest part.** Production is provisioned but carries no real traffic yet. I say that first, not last. What I can defend is every decision inside it, and I wrote the architecture documentation verified line by line against a specific commit, with a section stating what I couldn't verify.
> 🎯 Coach: this is your delivery-speed story and your integrity story at once. Pair the number with Plixiq's — 40k lines in 4 months, 336 files in 3 months — and you have answered "how fast do you ship?" without anyone having to take your word for it. Always volunteer the empty-production fact yourself; conceding it first is what makes the rest credible.

---

## 4. HR / behavioral interview — full simulation

*(Interviewer lines are marked **Q**. Speak your answers; don't read them.)*

---

**Q1. Tell me about yourself.**

> "I'm a software engineer with a mathematics background — and the order matters, because I did the math first. I have an M.Sc. in Mathematics and I taught machine learning and math at Universidad de Antioquia for about eleven years, including building the AI/ML elective curriculum for the Mathematics Institute.
>
> I moved into industry in 2018, starting with blockchain platforms at BCFort in Medellín, then three-plus years at Monadical, a distributed company across Canada and the US, doing full-stack Python and TypeScript and integrating LLMs into production apps. For the last two years I've been consulting independently and, since last August, working as an AI Specialist at Lapzo, where I'm on the AI committee that sets how the company builds with AI.
>
> The thread through all of it is that I like owning a system end to end. My most recent product, Plixiq, is a multi-tenant SaaS that lets businesses run AI agents on WhatsApp — I designed the architecture, wrote the backend and the frontend, and it's been running in production for months. That's the kind of ownership I'm looking for next, ideally with a team I can also teach and learn from, because the teaching part never really left me."

> 🎯 Coach: 75 seconds. Three moves — where you come from, what you've done, what you want. End on what you want, so the conversation opens instead of closing.

---

**Q2. Why are you looking to leave / why now?**

> "Consulting has been great for range — I've made architecture decisions across maybe six or seven products in two years, in healthcare, education, customer support, sports club management. What it doesn't give me is depth over time. I keep handing off systems right at the point where they'd start getting interesting: the second year, when you find out which of your decisions actually held up.
>
> I also miss having colleagues. I've done the solo-builder thing thoroughly enough to know I'm good at it and that I don't want it to be permanent. I want a team where I'm reviewing other people's code and having mine reviewed."

> 🎯 Coach: never criticize a client or employer. "I want depth and colleagues" is honest, flattering to them, and unfalsifiable.

---

**Q3. Tell me about a time you failed or made a bad technical call.**

> "At BCFort, early on, I over-invested in the blockchain layer for a platform where most of the actual value was ordinary analytics. I was excited about smart contracts and I designed the system around them — and we spent weeks on on-chain patterns for data that never needed to be on-chain. It made the system harder to change and slower to demo.
>
> What I took from it: I now ask 'what's the smallest piece of this that actually needs the exotic technology?' before I design anything. You can see the same instinct in Plixiq — I chose Server-Sent Events instead of WebSockets because the traffic is basically one-way, server to dashboard. WebSockets would have been more impressive and strictly worse."

> 🎯 Coach: a real failure, a real cost, a specific behavior change, and evidence the change stuck. The SSE callback is what makes it land — it proves the lesson wasn't rhetorical.

---

**Q4. Tell me about a conflict with a teammate or a client.**

> "At ROCKET CODE I was reviewing for a team that was moving fast on a workflow-automation platform. One developer kept opening large PRs that mixed a feature with refactors across the whole repo — genuinely good work, impossible to review honestly.
>
> I'd been leaving comments and it wasn't landing, so I stopped commenting and asked for a call. I said something like: I'm not blocking you on style, I'm blocking myself — I can't give you a real review on 900 lines that touch four contexts, so I'm either rubber-stamping it or holding you up for days, and both are bad for you. We agreed to split refactors into their own PRs.
>
> The thing that worked wasn't the rule. It was moving out of the comment thread into a conversation, and framing it as my problem rather than his mistake."

> 🎯 Coach: shows judgment about *medium* (text → voice), which senior interviewers notice. Keep the other person sympathetic — never make your conflict story about someone incompetent.

---

**Q5. How do you handle working remotely and staying aligned?**

> "I've been fully remote since 2021 — three years at Monadical across Canada, the US and Latin America, then international clients. A few habits: I'm in Colombia at UTC-5, so I overlap a full working day with US Eastern, and I protect that overlap for anything that needs a human. Everything else I write down. If a decision happened in a call, it isn't real until it's in a doc or a PR description.
>
> The failure mode of remote isn't laziness, it's silence. So I over-communicate status, and when I'm blocked I say so within hours, not days."

---

**Q6. What's your biggest weakness?**

> "I go too deep on foundations before I need to. It's the mathematician in me — my instinct is to understand the whole structure before I touch anything, and there are days when the job just needs the endpoint shipped.
>
> What I do about it: I timebox the understanding. I'll give myself a bounded window to explore, then commit to the simplest thing that works and leave a note about what I'd revisit. Consulting helped a lot with this, honestly — when you're billing someone, the difference between 'elegant' and 'done' gets very concrete."

> 🎯 Coach: a real weakness with a real cost and a real mitigation. Avoid "I'm a perfectionist" framing; the "when you're billing someone" line makes it credible.

---

**Q7. You've done a lot of things — blockchain, teaching, full-stack, AI. Isn't that scattered?**

> "I'd say it's sequential, not scattered. Each one was three or more years, and each one fed the next. The math is why I can read an ML paper. The blockchain years are why I think about cryptography and trust boundaries. The teaching is why I can explain a design to a non-technical stakeholder without condescending to them.
>
> And I'm not spread thin now: everything I've built in the last two years has been LLM-powered products with a Python backend and a TypeScript frontend. That's the center of gravity."

> 🎯 Coach: name the pattern for them. Interviewers who see a varied résumé are looking for whether *you* can articulate the thread. If you can, variety becomes range.

---

**Q8. Where do you see yourself in three to five years?**

> "Technically deep, with scope. I don't want to leave code — I want to be the person who owns an important system and grows the people around it. Some companies call that staff engineer, some call it tech lead. The part I care about is that I'm still designing and still teaching.
>
> Concretely, for AI products I'd want to go from 'we integrated an LLM' to 'we have real evaluation, real observability, and we know why quality changed last Tuesday.' That's the maturity gap in most AI products right now, including some of mine."

---

**Q9. What kind of environment do you do your best work in?**

> "Small teams with real ownership and written decisions. I do well when I'm handed a problem rather than a ticket — tell me what the business needs and let me come back with two options and a recommendation. I've done that with clients repeatedly: run the design session, translate what they said into an architecture, name the trade-off, pick one.
>
> What doesn't suit me is an environment where the architecture is decided in a meeting I'm not in and handed down as a list of tasks."

---

**Q10. Why this company / why this role?**

> *(Template — fill in per company, and always cite something specific: their product, their engineering blog, their open source.)*
>
> "Two reasons. The first is the problem — [specific thing about their product], which is close to what I built at [Plixiq / VitaStock / Lapzo], so I'd be productive early instead of spending a quarter learning the domain. The second is the stage: you're at the point where the AI features need to become a real system with evaluation and observability rather than a set of prompts, and that transition is exactly what I've been doing."

> 🎯 Coach: never answer this generically. If you can't name one specific thing about them, you haven't prepared enough — and they can always tell.

---

**Q11. What are your salary expectations?**

> "I'm currently targeting the equivalent of around $7,500 a month for a full-time remote role, and I've worked at roughly $63 an hour on consulting engagements. But I'd rather hear the range you've budgeted for this role — if the work and the team are right, I'm flexible within a reasonable band."

> 🎯 Coach: give a number only after you've asked once for theirs. If they push first: "what range do you have budgeted?" Then anchor at or slightly above the midpoint. Your consulting rate is a legitimate floor — use it as a fact, not a threat.

---

**Q12. What questions do you have for us?** → See Section 7. Always have at least three. Never zero.

---

## 5. Technical interview — full simulation

### 5.1 AI / LLM engineering

---

**Q. Walk me through an LLM system you built end to end.**

> "Plixiq. A business connects its WhatsApp number, uploads its knowledge — policies, catalog, FAQs — and gets an agent that handles the routine questions and escalates the rest to a human without losing the thread.
>
> The flow: a message hits a WhatsApp Cloud API webhook. I acknowledge it immediately and push the work onto a background queue — ARQ over Redis — because WhatsApp's webhook has a timeout and LLM calls don't respect anyone's timeout. The worker loads conversation state, does retrieval against that tenant's knowledge for context, and calls the model through LiteLLM, which defaults to Groq and falls back to OpenAI. If the agent can't resolve it confidently, or a trigger fires, an escalation moves the conversation to a human operator with the full history intact. Meanwhile the operator dashboard is getting live updates over Server-Sent Events.
>
> Backend is Python 3.12 with FastAPI and SQLModel over Postgres. Frontend is Next.js and TypeScript, using Effect for typed error handling. It's on Railway with GitHub Actions.
>
> The two decisions I'd defend hardest: everything scopes to an Organization tenant at the data layer, so multi-tenant isolation isn't something you have to remember to do; and the LLM is behind a gateway, so the model is a configuration detail."

**Follow-up: How do you handle multi-tenant isolation, concretely?**
> "Every domain entity carries the organization scope, and queries are scoped at the repository layer rather than in each endpoint — so isolation is structural, not a thing an individual developer can forget. Agent configuration and knowledge are per-organization too, so one tenant's retrieval can't reach another's documents. If I were hardening it further, the next step is Postgres row-level security so the database enforces it even if the application layer has a bug."

**Follow-up: Why not WebSockets for the dashboard?**
> "Because the traffic is one-way — server to dashboard. SSE gives me that over plain HTTP: it reconnects on its own, it goes through proxies without special handling, and there's no connection state to operate. WebSockets would have bought me a channel back to the server that I don't use, and cost me operational complexity. If the product needed bidirectional real-time — collaborative editing, say — I'd switch."

> 🎯 Coach: this three-question chain is the most likely deep dive you'll get. Practice it as one unit. Note the shape of every answer: decision → reason → *and here's what would make me choose differently.* That last part is what makes you sound senior.

---

**Q. How do you evaluate an LLM feature? How do you know it's good?**

> "Honestly? This is the part of the industry — mine included — that's least mature, so let me tell you what I do and where I'd want to go.
>
> What I do today: I keep a set of real conversations that broke, turn them into a regression set, and run changes against it before shipping. I log every interaction with the inputs, retrieved context, and output, so when something's wrong I can tell whether it was retrieval or generation. And the escalation path is itself a signal — the rate at which the agent hands off to a human is a proxy for quality that a business actually feels.
>
> Where I'd want to go: proper offline evals with graded rubrics, an LLM-as-judge with a human-labeled calibration set so I know the judge itself is trustworthy, and online metrics — resolution rate, escalation rate, time to resolution — segmented by tenant, because averages hide the tenant whose experience is terrible.
>
> What I do have closer to that in Aluna is instrumentation rather than evaluation, and I'd call it that honestly: usage events per model call, audit logs, and an explicit status reason written whenever the pipeline skips or fails a candidate — so a silent failure becomes a visible one. That's the foundation evals sit on, but it isn't evals.
>
> The general principle is the same as any ML system: you cannot improve what you don't measure, and vibes-based prompt tuning stops working the moment you have more than one customer."

> 🎯 Coach: this is the highest-signal question in AI interviews right now and most candidates bluff it. Your "here's what I do, here's the gap, here's the plan" structure is stronger than a fake-complete answer. Rehearse it.

---

**Q. Explain RAG. When would you not use it?**

> "RAG is retrieval plus generation: instead of hoping the model memorized your data, you fetch the relevant pieces at query time and put them in the context, and the model's job becomes reading comprehension rather than recall. Practically: chunk the source, embed the chunks, index them, embed the query, retrieve the top-k by similarity — often with a reranker, and often hybrid with keyword search because pure vector search is bad at exact identifiers like SKUs or error codes.
>
> When I wouldn't use it: when the knowledge is small enough to just fit in the context window — retrieval infrastructure you don't need is pure liability. When the task is reasoning rather than lookup, retrieval adds noise. When the answer needs to be exact and structured, a SQL query against the real database beats a similarity search over prose — in VitaStock, 'how many units of this lot are left' should never go near an embedding. And when the data changes every few seconds, your index is a lie."

**Follow-up: How would you improve a RAG system that's returning irrelevant chunks?**
> "In order of cheapness: look at the actual failures first — I'd read fifty bad ones before touching anything. Then chunking, because it's usually chunking: chunks that split a table in half, or chunks too small to carry meaning. Then hybrid retrieval so exact terms have a path. Then a reranker over a wider top-k. Then query rewriting, since users don't phrase questions the way documents phrase answers. Metadata filtering — by tenant, by document type, by date — usually beats anything clever. Fine-tuning embeddings is last, because it's the most expensive thing on the list and rarely the actual problem."

---

**Q. You use Claude Code daily. Doesn't that hurt code quality?**

> "It can, and I've seen it. The failure mode is real: the code compiles, the tests pass, and it's still wrong — usually because it solved the problem I described rather than the problem I had, or it quietly duplicated logic that already existed somewhere else in the codebase.
>
> Two things keep it honest. First, I review everything like a PR from a fast, confident junior — I read the diff, not the summary. Second, and this matters more: architectural guardrails the machine can't argue with. On Plixiq the module boundaries are enforced by a lint rule in CI, so no matter how enthusiastic the generated code is, it can't reach across a bounded context. That's the real insight for me — AI-assisted development is safe in proportion to how much of your architecture is *enforced* rather than *documented*.
>
> Net effect after a year and a half: I ship end-to-end features much faster, and the scarce resource moved from typing to judgment."

> 🎯 Coach: never be defensive here. Concede the risk in the first sentence — it buys you the rest of the answer.

---

**Q. What's actually happening in pre-training? (You wrote about this.)**

> "At its core it's next-token prediction at scale — you show the model an enormous corpus and train it to predict what comes next, and the loss is cross-entropy over the vocabulary. The interesting claim is that this apparently trivial objective forces the model to learn structure, because predicting the next token well eventually requires syntax, then facts, then something that behaves like reasoning. Compression and understanding start to look like the same thing.
>
> Then there's the practical layer: the objective is simple, the engineering isn't. Data curation and deduplication drive quality more than architecture does at this point, and the whole thing is a parallelism problem — which is what my PyCon talk was about, parallelism strategies in JAX with Flax: data parallel, model parallel, sharding, and how you split when the model no longer fits on one device.
>
> I also like framing a network as a DAG of parameterized differentiable programs — I wrote an essay on that. Once you see it that way, 'training' is just applying the chain rule over a graph, and architectures stop looking like magic and start looking like composition."

> 🎯 Coach: this is your unfair advantage — most application engineers can't go one level below the API. Don't dump it unprompted, but when the door opens, walk through it. The category-theory-flavored "composition" framing is distinctively yours.

---

**Q. How do you make an LLM pipeline durable — and cheap?**

> "In Aluna the CV analysis is a durable function: nine checkpointed steps with three retries, and steps that already completed don't re-run when a later one fails. That matters because the model call is the expensive step, and a naive retry pays for it twice.
>
> The ordering decision I care about most is that deduplication runs *before* quota enforcement. If someone re-analyses a CV whose inputs haven't changed, it reuses the cached score — no model call, and no plan quota consumed. Getting that order backwards means charging a customer for work you didn't do.
>
> There are four early exits: revoked consent, already analysed, quota exhausted, and a failure that stamps the process with a reason. The failure mode I designed against is the silent one — a candidate sitting there unscored with nothing on screen explaining why. In my experience that's what actually costs you trust in production, not the loud errors."

> 🎯 Coach: this is a strong answer for any AI-infrastructure role. The dedup-before-quota detail is the kind of thing only someone who actually shipped it would say.

---

**Q. You use several model providers. How do you decide which model does what?**

> "In Aluna every agent has a deliberately chosen default. Gemini reads documents and drafts — CV analysis, job posts, the narrated sections of the client report. Claude handles conversation: Sonnet for the screening bot, Haiku for the vacancy assistant where latency matters more than depth.
>
> It all goes through LiteLLM, and the model is overridable per agent at runtime from the database, with an environment variable as fallback. So which model runs is a configuration decision, not a code change — same principle as the provider fallback in Plixiq.
>
> The reasoning is that these aren't the same task. Document extraction rewards a model that's cheap and reliable at structure; a conversation rewards one that holds tone and context across turns. Using one model for everything means overpaying on the easy half of your workload."

---

**Q. When would you fine-tune instead of prompting or RAG?**

> "Prompting first, RAG when the issue is missing knowledge, fine-tuning when the issue is missing *behavior*. If the model doesn't know your data, fine-tuning is the wrong tool — you'll bake in a snapshot that's stale next month. If the model knows the material but won't produce the format, tone, or task shape you need consistently, or if you're paying for a huge prompt on every single call and want to distill it into a smaller cheaper model, that's fine-tuning's actual case.
>
> The other honest reason is latency and cost at volume: a small fine-tuned model that does one narrow thing can beat a large general one on both, and for a high-traffic classification step that trade is often worth it."

---

### 5.2 Backend & architecture

---

**Q. Clean architecture, DDD, SOLID — do you actually use them or do they just live on your résumé?**

> "I use a subset, deliberately. The parts that pay for themselves: bounded contexts, because they give you names for where things belong and a reason to say no; dependency inversion, because it's what makes the database and the LLM provider swappable; and keeping domain logic free of framework imports, so tests don't need infrastructure.
>
> The parts I skip: ceremony. I don't write a mapper between four layers for a CRUD endpoint. In VitaStock the procurement flow — quotations, purchase orders, receptions, lot tracking — has real invariants, so it gets real domain modeling. The settings page does not.
>
> The concrete version of 'do you really use it' is the CI lint rule on Plixiq's module boundaries. That's not a philosophy, that's a build failure."

---

**Q. Design a rate limiter for a multi-tenant API.**

> "Let me ask two things first: are we limiting per tenant, per user, or per endpoint — and is this protecting our infrastructure or enforcing a billing plan? They lead to different designs.
>
> Assume per-tenant plan enforcement. I'd use a sliding-window counter in Redis keyed by tenant and window, incremented atomically — a Lua script or the atomic increment-with-expiry pattern — so concurrent requests can't race past the limit. Fixed windows are simpler but let a tenant burst double at the boundary; a token bucket is nicer when you *want* to allow bursts, which for API plans you usually do. So: token bucket in Redis, refill rate from the plan, checked in middleware before the handler.
>
> On exceeding: 429 with `Retry-After`, plus `X-RateLimit-Remaining` so good clients can self-regulate. Failure mode matters — if Redis is down, I fail open for a paid API, because rejecting paying customers to protect a counter is worse than briefly over-serving. I'd log it loudly.
>
> Scaling: Redis is a single point of coordination, which is fine until it isn't. At that scale you go to local token buckets per instance with a fraction of the budget, plus periodic reconciliation — you trade exactness for availability."

> 🎯 Coach: the shape here is the point — clarify, propose, name the failure mode, name the scaling limit. Do this even when you know the answer instantly.

---

**Q. Your Postgres query got slow in production. Walk me through it.**

> "First, I'd establish whether it's *the query* or *the load*, because the fix is completely different. Then `EXPLAIN ANALYZE` on the real data — not on my laptop's data, where everything is fast and nothing is representative.
>
> What I'm looking for: sequential scans on big tables where I expected an index; a row estimate wildly off the actual, which usually means stale statistics or a correlation the planner can't see; and nested loops over large sets. Then the usual suspects in application code — N+1 queries are the single most common cause I've hit, especially with an ORM, and the fix is eager loading rather than cleverness. In Django I've written custom ORM extensions for exactly this class of problem.
>
> After that: the right index, and ideally a covering index so it's an index-only scan; check for lock contention if it's intermittent rather than constant; and only then consider denormalizing or caching. I try to resist caching as a first move — a cache in front of a bad query means you now have a bad query *and* an invalidation problem."

---

**Q. How do you handle background jobs and failure?**

> "On Plixiq it's ARQ over Redis. The rules I hold to: the webhook handler does almost nothing — validate, persist, enqueue, return 200 fast, because the platform will retry you if you're slow and now you have duplicates. Jobs are idempotent, keyed by the source message ID, so a retry can't send a customer the same answer twice. Retries are exponential with a cap, and anything that exhausts them goes to a dead-letter place a human can actually see — a queue nobody looks at is a data loss mechanism with extra steps.
>
> And LLM calls specifically need timeouts and a fallback provider, because the tail latency on model APIs is genuinely bad and 'it'll finish eventually' is not a strategy when there's a customer staring at WhatsApp."

---

### 5.3 System design round — "Design an AI customer-support agent for 500 businesses"

> 🎯 Coach: you have lived this exact problem. Resist the urge to answer instantly — walk them through the structure. Suggested 35-minute shape:

**Minutes 0–5, requirements.** Ask, don't assume: How many messages per business per day? Is voice in scope or text only? How fast must a human be able to take over? What's the data isolation requirement — is this regulated? Do businesses self-serve, or do we onboard them? *State your assumptions out loud and write them down.*

**Minutes 5–12, high level.** Channel adapters (WhatsApp first, but keep the interface generic) → ingestion API that acknowledges fast and enqueues → worker pool → conversation service holding state → retrieval over per-tenant knowledge → LLM gateway with multi-provider fallback → escalation service → operator dashboard over SSE. Postgres for durable state, Redis for cache and queue, object storage for uploaded documents.

**Minutes 12–22, go deep where they push.** Your strongest depth areas, in order: tenant isolation (scope at the repository layer, RLS as the hardening step), provider abstraction and fallback, escalation with full context handoff, idempotency on webhook retries.

**Minutes 22–30, scale and failure.** 500 tenants is not a scale problem, it's an *isolation and noisy-neighbor* problem — per-tenant rate limits and queue fairness so one busy tenant can't starve the rest. What happens when the LLM provider degrades: fallback, then a graceful "a human will be with you shortly" rather than a hallucinated answer. Cost control: cache retrieval, cap context size, route easy intents to a cheap model.

**Minutes 30–35, what you'd measure.** Escalation rate, resolution rate, p95 latency, cost per conversation per tenant, and a regression set of real broken conversations run on every deploy.

**Say this near the end — it's a senior signal:**
> "If it were a small team, I'd build this as a modular monolith with hard internal boundaries rather than services, and extract only what actually needs independent scaling — realistically the workers, first. I've built it that way and the boundaries held because CI enforced them."

---

### 5.4 Frontend

**Q. You've done React for seven years. What have you changed your mind about?**

> "Global state. I used to reach for Redux by default, and I've watched a lot of applications turn most of their server data into global client state and then spend their lives keeping it in sync. Now my first question is 'is this actually client state?' — most of it is server cache, and it belongs in something built for that. What's left over is genuinely small and Zustand handles it.
>
> The second thing is types at the boundary. I validate at the edge with Zod, and lately on the Plixiq frontend I've used Effect for typed error handling — so the failure paths are in the type system rather than in a try/catch someone forgot to write. Coming from math, I find it hard to unsee: if the type doesn't rule out the bad state, the bad state will happen."

**Q. How do you approach performance in a Next.js app?**

> "Measure first — I don't optimize from intuition, I've been wrong too often. Then the usual hierarchy: don't ship what you don't need (bundle analysis, dynamic imports for heavy things like the Three.js scenes in the digital human project), render on the server where the data is, and be careful about what forces a component into the client. Images and fonts are the boring ones that produce most of the actual score improvement. Then memoization *last*, because premature `useMemo` everywhere makes code worse and measurably helps less than people think."

---

### 5.5 Math / ML fundamentals — your home turf

**Q. Explain gradient descent and why it works.**

> "You have a loss surface over parameters. The gradient points in the direction of steepest increase, so you step against it, scaled by a learning rate. That's it — the whole thing is first-order local information used repeatedly.
>
> Why it works in practice for networks, when the loss is wildly non-convex, is more interesting: in very high dimensions the problem isn't local minima the way the 2D picture suggests — most critical points are saddles, and stochastic noise from mini-batching helps you escape them. The noise isn't a defect of SGD, it's part of why it works.
>
> And backpropagation is just the chain rule applied efficiently over the computation graph — which is why I like describing a network as a DAG of parameterized differentiable programs. Once you frame it that way, autodiff isn't a framework feature, it's the obvious consequence of the structure."

**Q. Explain the bias-variance trade-off to a non-technical stakeholder.**

> "I'd say: imagine studying for an exam. Bias is a student who learned one oversimplified rule and applies it to everything — consistently wrong, in the same way, every time. Variance is a student who memorized last year's exam perfectly and is helpless when the questions change. You want the one who learned the actual pattern. In model terms, we control that with more data, with regularization, and by testing on questions the model has never seen — which is what a validation set is."

> 🎯 Coach: eleven years of teaching is your moat on questions like this. Interviewers remember the candidate who could explain something clearly far longer than the one who recited a definition. Use an analogy every single time you're asked to explain a concept.

**Q. What's a vector embedding, really?**

> "A learned map from things to points in a space, where the geometry means something — the training objective forces items used in similar ways to land near each other, so distance becomes a proxy for similarity. That's the whole trick behind retrieval. The caveat I'd add: 'similar' means similar *according to the training objective*, which is why off-the-shelf embeddings are decent at topical similarity and bad at exact identifiers. That's why I use hybrid search — the embedding will happily tell you that part number A-4471 is close to A-4477."

---

### 5.6 Live coding round — how to narrate

You have HackerRank practice in your repos; the risk isn't the algorithm, it's going silent. Rules:

1. **Restate the problem in your own words** and confirm before typing. Ask about input size and edge cases — empty, single element, duplicates, negatives.
2. **Say the brute force out loud first**, with its complexity, then improve it. "The naive version is O(n²) because I'd compare every pair — I can get that to O(n) with a hash map if I trade space."
3. **Type in small runnable steps.** Never write forty lines and then run.
4. **Talk while you think.** If you're stuck, say what you're considering — silence reads as not knowing; narrated uncertainty reads as thinking.
5. **When it works, immediately state complexity, then a test case that would break it.** Volunteering your own weakness is the highest-trust move in a coding round.
6. **Your Python is your strongest language** — use it unless the role is explicitly TypeScript.

---

## 6. Hard questions and landmines

**"You don't have a computer science degree."**
> "That's true — my degrees are in mathematics, and I taught ML and math for eleven years before moving into industry. In practice the gap that matters would be things like operating systems and compilers, and where I've needed them I've gone and learned them — I've done systems work in C and I'm learning Rust. What the math degree gave me instead is the part people usually find harder to acquire: I can read the papers, I understand the linear algebra and probability under the models, and I'm comfortable with abstraction. Eight years of production systems covered the rest."

**"Your recent work is mostly solo. Can you work in a team?"**
> "The last two years are consulting, yes — but before that I spent three-plus years at Monadical on a distributed team across three countries, leading frontend architecture, reviewing code, and mentoring. And even as a consultant I've been the code reviewer for ROCKET CODE's team and I'm on Lapzo's AI committee, which is fundamentally a group-alignment job — standardizing how a whole organization builds with AI. Solo work sharpened my ownership. It didn't replace my collaboration."

**"Rust — beginner. Why is it on your résumé?"**
> "Because it's honest — it's listed at the level I'm actually at. I've been learning it for about two years on side projects, including a small chatbot. I'd be productive in it in weeks, not days, and I'd want review from someone who knows it well. I'd rather tell you that now than discover it in the first sprint."

> 🎯 Coach: this answer builds enormous trust. Calibrated self-assessment is rarer than skill.

**"Morpheus has 29 stars, not 150."** *(Corrected in the résumé, so this shouldn't come up. If an old PDF is in play:)*
> "You're right — that number was stale in an older version of my résumé. What I'd stand behind on Morpheus is the work: I contributed 19 PRs to it, on the FastAPI backend, the ML model integration and the React frontend. The starred project that's actually mine is the digital human, at 464."

**"Aluna's production environment is empty. Nobody has actually used it."**
> "That's right, and I'd rather say it than have you discover it. Production is provisioned but carries no real traffic yet — everything has been verified end to end in development. What I can defend is every decision inside the system, and I wrote its architecture documentation verified line by line against a specific commit, including an explicit section on what I couldn't verify. If you want to judge my engineering rather than my luck with launches, that document is the best thing I can hand you."

> 🎯 Coach: volunteer this before anyone asks. Conceding a real limitation first is what makes everything else you say credible — and the documentation detail turns the concession into evidence.

**"Why should we hire you over someone with FAANG experience?"**
> "If you need someone who's operated at a scale I haven't, hire them — I've built products with hundreds of users and tenants, not hundreds of millions. What I bring instead is range and ownership: I can take a vague business problem, design the system, build both halves of it, deploy it, and keep it alive, without four handoffs. For a team where the constraint is 'we need this shipped and shipped well,' that's usually worth more than scale experience you won't use for two years."

**Salary, if pushed for a number first:** see Q11 in Section 4. Ask for their range once, then anchor. Your data points: **$7,500/month** targeted full-time, **$63/hour** consulting.

---

## 7. Questions you ask them

Pick three or four per interview. They're chosen to make *you* look senior and to actually protect you from a bad job.

**For the hiring manager**
1. "What does the first ninety days look like — what would I have shipped if this went well?"
2. "How do architecture decisions get made here? Is there a design doc culture, or is it decided in the PR?"
3. "What's the thing about this codebase that everyone complains about?" *(The answer tells you more than anything on their careers page.)*

**For the engineers**
4. "How do you evaluate your AI features today? Do you have an eval set, or is it still judgment calls?" *(You'll instantly know their maturity — and it sets you up as the person who could build it.)*
5. "What's your code review culture like — how long does a PR usually sit?"
6. "Where does the on-call pain come from?"

**For the AI/product side**
7. "Are you tied to a single model provider, or is there an abstraction layer? How would you switch if you had to?"
8. "How do you decide when a feature should be an LLM feature versus deterministic code?"

**About you in the role**
9. "What's the gap between where the team is now and where you need it to be — and where would I fit in closing it?"
10. "How do you work with people outside your main timezone? I'm at UTC-5, which overlaps a full day with US Eastern, but I want to know what the norms are."

---

## 8. Closing lines

**End of an HR screen:**
> "This sounds like the right shape of problem for me. Just to be direct about logistics — I'm in Colombia at UTC-5, so I overlap a full working day with US Eastern, I'm available to start right away, and I don't need sponsorship. What are the next steps?"

**End of a technical round:**
> "I enjoyed that — especially the [specific part]. If it's useful, the closest thing I've built to what you described is Plixiq, and I'm happy to walk anyone through the architecture in more detail or share the write-up."

**If you don't know something:**
> "I haven't used that. Here's the closest thing I have used and how I'd expect it to map — tell me where that intuition breaks."

Never bluff. You have enough real depth that admitting one gap costs you nothing and buys credibility on everything else.

---

## 9. Practice plan

**Drill 1 — the 60-second self-intro.** Record yourself. Listen back. Cut every clause that doesn't carry information. Repeat until it's boring to you; that's when it's ready.

**Drill 2 — story beats without notes.** For each of the eight stories in Section 3, say the five beats from memory. Don't write the words down — if you can hit the beats, the words will come, and they'll come out sounding like you.

**Drill 3 — the Plixiq deep dive.** Three follow-ups deep, out loud: architecture → tenant isolation → SSE vs WebSockets. This is your most likely technical conversation. Own it completely.

**Drill 3b — the Aluna deep dive.** Two follow-ups deep: two-service split → why dedup runs before quota. Then say the empty-production line out loud until it comes out level, not apologetic.

**Drill 4 — explain it to a stakeholder.** Take RAG, embeddings, and fine-tuning, and explain each in 45 seconds with an analogy and no jargon. You taught for eleven years; this is free points, but only if you practice it in English out loud.

**Drill 5 — the uncomfortable five.** No degree in CS. Solo for two years. Rust beginner. Salary. Why leaving. Say each answer once a day until it stops feeling defensive.

**Before every interview, 10 minutes:**
- [ ] Read the company's engineering blog or GitHub; find one specific thing to reference.
- [ ] Re-read Section 1 and your three pillars.
- [ ] Pick which of the eight stories fits this company's product.
- [ ] Pick your three questions from Section 7.
- [ ] Have open in tabs: plixiq.com, aluna.works, vitastock.piagents.dev, github.com/asanchezyali/talking-avatar-with-ai, your PyCon talk.
- [ ] Pick the base CV you sent them (`variants/`) and re-read it — they will ask about a bullet in it.

**Housekeeping before you send another application:**
- [x] ~~Fix Morpheus stars in `data/resume-master.json`~~ — done (150 → 29).
- [x] ~~Update Digital Human stars~~ — done (320 → 464). Also corrected in `jobs/20260625_braintrust_ai_agent_developer_answers.md`.
- [x] ~~Add the Plixiq case study link to your materials~~ — done; it is in the `cv` skill's fact list.
- [x] ~~Build the base CVs~~ — done: four in `variants/`, all two pages.
- [ ] Add a LICENSE, a test suite and CI to `talking-avatar-with-ai` (464★, currently has none) and answer its 3 open issues.
- [ ] Build an eval harness for Plixiq or Aluna. It is the single gap that would most change how you interview.
- [ ] Keep the Aluna architecture PDF ready to send — it is your strongest work sample.
