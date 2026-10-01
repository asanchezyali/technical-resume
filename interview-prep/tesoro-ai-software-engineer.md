# Tesoro AI → US healthcare company · Software Engineer

Supplement to `interview-simulation.md`. Friday 2 Oct 2026, 9:00–9:30 (UTC-5), Google Meet, in English.
First screen with Tesoro AI, a Medellín recruiting firm that places LatAm engineers with North American
startups. The client is confidential. What Valeria wrote on 8 Sep: Python-heavy codebase, AI-enabled
products, reliability, voice infrastructure, healthcare.

A 30-minute recruiter screen isn't a technical round. They're checking three things: your English holds,
the story is clear, and the logistics fit. Keep answers to about a minute. Spend the last ten minutes on your questions.

## 60-second intro (beats, not a script)

- I'm a mathematician who became a software engineer. I taught math and machine learning at Universidad de
  Antioquia for eleven years, and I've been shipping production software since 2018.
- These days I build AI systems end to end. At Lapzo I'm the AI Specialist: I built a Digital Professor that
  holds real-time voice conversations with learners, with LLM services, ElevenLabs synthesis and a real-time layer.
- On the side I've led and built full products: Aluna, an AI recruitment platform, and Plixiq, AI customer
  support on WhatsApp. Mostly Python and FastAPI, with TypeScript on the front.
- Healthcare isn't new to me either. A private surgical clinic commissioned VitaStock, a supply-chain system.
  I built it, and their pharmacist shaped the domain model.
- What drew me to this role is voice plus reliability. That's exactly where I've spent my time.

## Three stories, tied to what they asked for

**1. Voice, real time → Lapzo Digital Professor** (playbook Story C for the latency angle)
- S: Lapzo wanted a professor learners could actually talk to, explaining course content on interactive slides.
- T: I owned the architecture: LLM services, ElevenLabs voice synthesis and the real-time communication layer.
- A: Next.js and NestJS with Firebase Realtime Database for the live channel. ElevenLabs for speech.
- R: Don't claim it has real users: it doesn't. What does run with real users at Lapzo is the AI content-generation
  pipeline (LangChain, LangGraph, n8n). If they ask about production, name that one.
- Lesson, from the open-source avatar (464★): the model is rarely the bottleneck. It's the latency budget
  across services, because people notice every pause in a conversation.

**2. Reliability → Aluna's durable pipeline** (Story H)
- S: A staffing agency needed every CV scored by a model, and the whole run couldn't die on a single failure.
- A: A durable Inngest pipeline with nine checkpointed steps and three retries. Deduplication runs *before* quota
  enforcement, so re-analysing an unchanged CV reuses the cached score and costs nothing.
- Say it first: production is provisioned, but it doesn't carry real traffic yet. What you can defend is every
  decision, plus an architecture doc verified line by line against a commit.

**3. Conversational AI with a safety valve → the WhatsApp agent** (Plixiq, Story A or B)
- AI agents answer routine questions in about two seconds and hand off to a human with the full context.
  Escalation triggers on frustration or keyword detection.
- LiteLLM sits in front of the providers: Groq by default, OpenAI as fallback. Switching is a config change.
- Healthcare angle: the escalation path is the part you'd design first, because some conversations shouldn't stay with a bot.
- Same honesty: built and deployed, no real customer traffic yet.

## What they'll likely probe, and your angle

| Area | Your angle |
|---|---|
| Voice infrastructure | Your voice work is synthesis and speech-to-text inside a product (ElevenLabs, Whisper), not telephony. Ask which one they mean before claiming anything |
| Reliability | Retries, checkpoints, idempotent webhook processing, provider fallback. Give concrete mechanisms, not adjectives |
| Python backend | 8+ years. FastAPI, Django, async PostgreSQL, Redis, ARQ background jobs |

## Honest gaps for this posting

- **No large-scale traffic.** "I've built the mechanisms that keep a system up, and I haven't yet operated one at
  real scale. That's the gap I want to close next."
- **No telephony or SIP.** If voice means phone infrastructure, say so plainly and point to the latency work.
- **No HIPAA experience.** Say that you've handled privacy by design under Colombian law, Ley 1581, in Aluna:
  consent written in the same transaction and a revoked consent blocking re-analysis. It isn't HIPAA, and you shouldn't imply it is.
- **No formal LLM evals in production.** Only if it comes up.

## Why this company

You don't know the client's name yet, so don't pretend to. Keep it to the work: "Voice, Python, and reliability in
healthcare is the overlap of the three things I've been building: real-time voice at Lapzo, durable pipelines,
and a clinical system with a pharmacist. It's rare to find a role that asks for all three."

## Questions to ask (pick four or five, logistics first)

1. Is the contract with the client directly, or with Tesoro AI?
2. What part of healthcare is the company in, and can you share its name?
3. How many days a week on site, and where is the office?
4. What's the salary range for the role?
5. When you say voice infrastructure, is it real-time telephony, or speech inside the product?
6. What are the next steps after this call, and is there a technical test?
