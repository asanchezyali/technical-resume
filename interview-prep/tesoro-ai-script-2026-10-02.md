# Tesoro AI · Software Engineer (US healthcare client) · Interview script

**When:** Friday 2 Oct 2026, 9:00–9:30 COT · **Where:** Google Meet `pep-txsi-dco` · **With:** Valeria Caicedo, Research Analyst · **Language:** English

**Before 8:45:** headphones, quiet room, camera and mic tested, this file open on a second screen. One-minute answers. Keep the last ten minutes for your questions.

**Three rules**
1. Lapzo ended on 30 Sep. Say it once, in the intro, and move on.
2. Salary: ask for their range first. Only if forced: "from about four thousand dollars a month, depending on scope" (about COP 13.5M). Nothing below 13M.
3. Location: "based in Antioquia, about two hours from Medellín, moving to the city in January". Never "I live in Medellín".

---

## 1. "Tell me about yourself" (60 seconds)

> I'm a mathematician who became a software engineer. I have a master's in mathematics and I taught math and machine learning at Universidad de Antioquia for eleven years, and I've been shipping production software since 2018.
>
> For the last fourteen months I was the AI Specialist at Lapzo, an education platform. I built a Digital Professor that holds real-time voice conversations with learners, the vectorization pipelines behind course search, and an HR agent on LangGraph that answers policy questions with citations. That contract ended at the end of September, so I'm available right away.
>
> On the side I've built full products end to end, mostly Python and FastAPI with TypeScript on the front: Plixiq, AI customer support on WhatsApp, and Aluna, an AI recruitment platform. And I've worked in healthcare: a private surgical clinic commissioned VitaStock, a supply-chain system I built with their pharmacist shaping the domain model.
>
> What drew me to this role is voice plus reliability. That's exactly where I've spent my time.

## 2. "Why did the Lapzo engagement end?"

> It was a contractor engagement and it closed at the end of September. We parted on good terms; I handed over the HR agent with full documentation and said goodbye to the team properly. I'm fully available now, which is why I could take a Friday-morning call.

If she asks directly whether it was their decision: "The company ended the contract. I disagreed with the reason, but that's their call, and I'd rather talk about the work."

## 3. "What's your experience with voice infrastructure?"

> Let me be precise, because "voice" can mean two things. What I've built is voice inside a product: real-time speech-to-text with Whisper, LLM generation, and ElevenLabs synthesis, both in the Digital Professor at Lapzo and in an open-source conversational avatar I maintain, which has about 460 stars. The hard problem there was never the model; it was budgeting latency across four services, because people notice every pause in a live conversation.
>
> What I haven't built is telephony: Twilio, SIP, barge-in on phone calls. If the role is phone infrastructure, that's new ground for me and I'd say so. Which of the two is it in this case?

## 4. "How do you approach reliability?"

> With mechanisms, not adjectives. In Plixiq, WhatsApp retries webhook deliveries, so processing is idempotent and a retried delivery never duplicates a write. Anything slow runs as a background job with retries. The LLM layer sits behind LiteLLM with provider fallback, so one provider outage doesn't stop every tenant.
>
> In Aluna I built a durable pipeline on Inngest: nine checkpointed steps, three retries, and deduplication placed before quota enforcement, so a re-analysed CV reuses its cached score instead of paying for another model call.
>
> One thing I should be clear about: those systems are built and deployed, but they don't carry real customer traffic yet. I've built the mechanisms that keep a system up; I haven't yet operated one at real scale. That's the gap I want to close next.

## 5. "Tell me about your Python background."

> Eight years. FastAPI and Django mostly, async PostgreSQL, Redis, background jobs with ARQ, and LangChain and LangGraph for the agent work. At Monadical, a distributed team across Canada, the US and Latin America, I built Python backends with REST and GraphQL APIs for three years and led code reviews. More recently everything I've built alone has a FastAPI core with a Next.js front end.

## 6. "Have you worked with healthcare data or HIPAA?"

> Not HIPAA, and I won't pretend otherwise. What I have done is privacy by design under Colombian law, Ley 1581: in Aluna, consent is written in the same transaction as the candidate's data, and a revoked consent blocks any re-analysis. In VitaStock I handled clinical operations data for a surgical clinic, with roles and permissions per user type. So I understand the discipline; the specific US framework I'd need to learn.

## 7. "A lot of your recent work was solo. How do you work with teams?"

> The solo work was deliberate range, not isolation. I spent three years on Monadical's distributed team, where I led the frontend architecture and reviewed other people's code. I was code reviewer for a client's development team on an NX multi-repo. At Lapzo I worked in a product squad with a tech lead, designers and QA, and I documented blockers and decisions in ClickUp so the rest of the team could follow. Eleven years of teaching also help: explaining a system clearly is most of the job.

## 8. "How comfortable are you working in English?"

> Comfortable, as you can hear. I take weekly classes to keep sharpening it, I've worked with English-speaking teams for years, and most of my technical reading and writing is in English.

## 9. "The role is hybrid in Medellín. Does that work?"

> I'm based in Antioquia, about two hours from Medellín, and I'm moving to the city in January. Until then I can be on site a couple of days when it's planned ahead. How many days a week on site does the client expect, and where is the office?

## 10. "What are your salary expectations?"

> I'd rather hear the range you have budgeted first, so we can see quickly if it makes sense to keep going.

If she insists:

> From about four thousand dollars a month, depending on scope. If it's in pesos, roughly thirteen and a half million.

## 11. "When could you start?"

> Right away. I have no notice period.

## 12. "Do you have questions for me?" (pick four or five, logistics first)

1. Is the contract with the client directly, or with Tesoro AI?
2. What part of healthcare is the company in, and can you share its name at this stage?
3. How many days a week on site, and where is the office?
4. What's the salary range for the role, and is it in pesos or dollars?
5. When you say voice infrastructure, is it real-time telephony, or speech inside the product?
6. What are the next steps after this call, and is there a technical test?

## 13. Closing

> Thank you, Valeria. I appreciate the clarity. Talk soon.

---

## If they go off-script

- **"What are you building for fun?"** Kipux, an open-source personal-finance app in Rust with a Claude-vision receipt parser. One sentence, then back to the role.
- **"Do you have formal LLM evals?"** "I keep a regression set of real failed conversations and use escalation rate as a quality proxy. I haven't built formal offline evals or LLM-as-judge yet; that's the first thing I'd add."
- **"Kubernetes / Terraform?"** "I haven't used them. My deployments are Docker on AWS, GCP and Railway."
- **"Why healthcare?"** The VitaStock story: a clinic that ran inventory on spreadsheets, 12 modules and 5 roles, the pharmacist as domain expert, true per-patient cost through a cardex.

## After the call

Fill in `kairos/empresas/tesoro-ai.md` → "Respuestas de la llamada": contract party, client name, on-site days, range, voice type, next steps. Update `kairos/red/contactos.md` and the agenda.
