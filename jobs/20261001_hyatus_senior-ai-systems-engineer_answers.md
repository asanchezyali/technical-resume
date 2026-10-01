# Hyatus Living (Wellfound 4746861) · Senior AI Systems Engineer · application

Applied on Wellfound on 1-oct-2026 with the profile (resume on file: AI Full Stack). Only one field: "What interests you about working for this company?"

## Note sent

Your posting describes the system I have been building for the last two years, in a different domain. Plixiq (plixiq.com) is a multi-tenant platform where AI agents handle customer support on WhatsApp: they resolve routine requests in about 2 seconds and escalate the rest to a human operator with the full conversation context. Decisions I made: a LiteLLM gateway with fallback across providers so one outage does not stop every tenant; idempotent webhook processing, because WhatsApp retries deliveries and the first version duplicated writes; frustration and keyword detection to decide when to bring in a human; ARQ background jobs with retries for everything slow; and a regression set of real broken conversations as the gate before any prompt change ships. It is built and deployed with no real users yet, so what I can show is the system, not traction. Second thing: an HR agent at Lapzo on LangGraph, FastAPI and pgvector that answers policy questions with citations and executes requests only after human confirmation. I build with coding agents every day. Side project in Rust: Kipux, a finance app with a Claude vision receipt parser (github.com/asanchezyali/kipux). More at github.com/asanchezyali. Based in Colombia, full overlap with New York. I would like to walk you through Plixiq on a call.

---
Weak point: they ask for a demo or walkthrough; the note offers a call and links, not a recorded demo. If they answer, record a 3-minute Plixiq walkthrough before the call.
