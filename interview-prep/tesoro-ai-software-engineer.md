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
- These days I build AI systems end to end. For the last fourteen months I was the AI Specialist at Lapzo, an
  education platform: I built a Digital Professor that holds real-time voice conversations with learners (LLM
  services, ElevenLabs synthesis, a real-time layer), the vectorization pipelines for course search, and an HR
  agent on LangGraph that answers policy questions with citations. That contract ended at the end of September,
  so I'm available right away.
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

## Update 1 Oct 2026 (the night before)

**Status change.** Lapzo ended on 30 Sep 2026. Say it in the intro, in one line, and move on. If asked why:

> It was a contractor engagement; it ended at the end of September. We parted on good terms and I handed the
> HR agent over with documentation. I'm fully available now, which is why I could take this call on a Friday morning.

Don't volunteer that it was their decision; don't lie if asked directly ("the company ended the contract; I
disagreed with the reason, but that's their call, and I'd rather talk about the work").

**Salary rule changed (30 Sep): ask the range first; if forced, "from USD 4,000 a month, depending on scope".**
In pesos at today's rate (TRM ~3,313) that is about COP 13.5M. The 10–16M note from 8 Sep: 10M is below the
floor, 16M is above it. Don't accept below 13M; don't anchor high.

**Location, unchanged:** "I'm based in Antioquia, about two hours from Medellín, and I'm moving to the city in
January. Until then I can be on site a couple of days when it's planned ahead." Never say "I live in Medellín".

**Logistics.** Fri 2 Oct, 9:00–9:30 COT, Google Meet pep-txsi-dco (reminder email 1 Oct 9:00). Test camera and
mic at 8:45. He is in Medellín (Airbnb in Laureles) until Saturday: good connection, quiet room, headphones.

**One new story available (optional):** Kipux, a Rust finance app with a Claude-vision receipt parser, open
source. Only if they ask what you build for fun. Not a healthcare or voice story.

## Mock interview (written 1 Oct 2026, night before). Recruiter screen, 30 minutes, English.

**V: Hi Alejandro, thanks for making the time. Could you start by telling me a bit about yourself?**
Sure. I'm a mathematician who became a software engineer. I have a master's in mathematics and I taught math and machine learning at Universidad de Antioquia for eleven years, and I've been shipping production software since 2018. For the last fourteen months I was the AI Specialist at Lapzo, an education platform: I built a Digital Professor that holds real-time voice conversations with learners, the vectorization pipelines behind course search, and an HR agent on LangGraph that answers policy questions with citations. That contract ended at the end of September, so I'm available right away. On the side I've built full products end to end, mostly Python and FastAPI with TypeScript on the front: Plixiq, AI customer support on WhatsApp, and Aluna, an AI recruitment platform. And I've worked in healthcare: a private surgical clinic commissioned VitaStock, a supply-chain system I built with their pharmacist shaping the domain model.

**V: Why did the Lapzo engagement end?**
It was a contractor engagement and it closed at the end of September. We parted on good terms; I handed over the HR agent with full documentation and said goodbye to the team properly. I'm fully available now, which is why I could take a Friday-morning call.

**V: The role involves voice infrastructure. What's your experience there?**
Let me be precise, because "voice" can mean two things. What I've built is voice inside a product: real-time speech-to-text with Whisper, LLM generation, and ElevenLabs synthesis, both in the Digital Professor at Lapzo and in an open-source conversational avatar I maintain, which has about 460 stars. The hard problem there was never the model; it was budgeting latency across four services, because people notice every pause in a live conversation. What I haven't built is telephony: Twilio, SIP, barge-in on phone calls. If the role is phone infrastructure, that's new ground for me and I'd say so. Which of the two is it in this case?

**V: It's more on the product side, with some real-time requirements. How do you approach reliability?**
With mechanisms, not adjectives. In Plixiq, WhatsApp retries webhook deliveries, so processing is idempotent and a retried delivery never duplicates a write. Anything slow runs as a background job with retries. The LLM layer sits behind LiteLLM with provider fallback, so one provider outage doesn't stop every tenant. In Aluna I built a durable pipeline on Inngest: nine checkpointed steps, three retries, and deduplication placed before quota enforcement, so a re-analysed CV reuses its cached score instead of paying for another model call. I should be clear about one thing: those systems are built and deployed, but they don't carry real customer traffic yet. I've built the mechanisms that keep a system up; I haven't yet operated one at real scale. That's the gap I want to close next.

**V: Tell me about your Python background.**
Eight years. FastAPI and Django mostly, async PostgreSQL, Redis, background jobs with ARQ, and LangChain and LangGraph for the agent work. At Monadical, a distributed team across Canada, the US and Latin America, I built Python backends with REST and GraphQL APIs for three years and led code reviews. More recently everything I've built alone has a FastAPI core with a Next.js front end.

**V: Have you worked with healthcare data or regulations like HIPAA?**
Not HIPAA, and I won't pretend otherwise. What I have done is privacy by design under Colombian law, Ley 1581: in Aluna, consent is written in the same transaction as the candidate's data, and a revoked consent blocks any re-analysis. And in VitaStock I handled clinical operations data for a surgical clinic, with roles and permissions per user type. So I understand the discipline; the specific US framework I'd need to learn.

**V: How do you work with teams, given that a lot of your recent work was solo?**
The solo work was deliberate range, not isolation. I spent three years on Monadical's distributed team, where I led the frontend architecture and reviewed other people's code. I was code reviewer for a client's development team on an NX multi-repo. At Lapzo I worked in a product squad with a tech lead, designers and QA, and I documented blockers and decisions in ClickUp so the rest of the team could follow. Eleven years of teaching also help: explaining a system clearly is most of the job.

**V: The company is US-based and the team speaks English. How comfortable are you?**
Comfortable, as you can hear. I take weekly classes to keep sharpening it, I've worked with English-speaking teams for years, and most of my technical reading and writing is in English.

**V: The position is based in Medellín with a hybrid setup. Does that work for you?**
I'm based in Antioquia, about two hours from Medellín, and I'm moving to the city in January. Until then I can be on site a couple of days when it's planned ahead. How many days a week on site does the client expect, and where is the office?

**V: What are your salary expectations?**
I'd rather hear the range you have budgeted first, so we can see quickly if it makes sense to keep going.
*(If she insists:)* From about four thousand dollars a month, depending on scope. If it's in pesos, roughly thirteen and a half million.

**V: When could you start?**
Right away. I have no notice period.

**V: Do you have questions for me?**
Yes, a few. Is the contract with the client directly, or with Tesoro AI? What part of healthcare is the company in, and can you share its name at this stage? What's the salary range for the role? And after this call, what are the next steps, and is there a technical test?

**V: Thanks, Alejandro. We'll be in touch with next steps.**
Thank you, Valeria. I appreciate the clarity. Talk soon.
