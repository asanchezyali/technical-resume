# TaskRabbit (Braintrust job 17885) · Senior Software Engineer (Fullstack), Tasker & Supply · answers

Posting: `jobs/20261001_taskrabbit_senior-fullstack-tasker-supply.md`. Variant: Senior Full Stack (no AI component in the posting).

## Logistics
- Hourly rate: **$67** (preset; client budget $60–90)
- Timezone requirement (3–4 h overlap with Pacific): **Yes** (Colombia is UTC-5; a full Pacific morning overlaps)
- Available to start: **Right away**
- Booking calendar: https://cal.com/asanchezyali/full-time-opportunities
- Legally authorized to work in the country where the job is located: **Yes** (work from anywhere; working from Colombia)
- Visa sponsorship: **No**
- Resume: generated/AlejandroSanchezYaliSeniorFullStack.pdf

## Q1 — Years of TypeScript across frontend and backend; stacks

Six years of TypeScript on both sides, within eight years of engineering. At Monadical (2021–2024, distributed team across Canada, the US and Latin America) I built and maintained full stack applications: React and Next.js frontends in TypeScript, Node.js and Express services, and Python backends on Django and FastAPI exposing REST and GraphQL APIs. I led the frontend architecture there, including the component library and the testing strategy with Vitest and Jest. At Lapzo (2025–2026) I made the architectural decisions for an educational platform and implemented its real-time features with Next.js, NestJS and Firebase Realtime Database. As an independent engineer I shipped three products end to end: Plixiq and VitaStock on FastAPI plus Next.js and TypeScript with PostgreSQL, and Aluna on Next.js 15 with TypeScript, FastAPI, Inngest and Upstash Redis. The recurring decision across all of them is the one your posting names: what belongs in the client and what belongs in the API, and keeping the contract between them typed from end to end.

## Q2 — BFF architectures or REST APIs for mobile/web clients

I have built REST APIs that serve web clients on every product I have shipped, and I have not built a BFF for a native mobile app, so I will describe what is closest. In Plixiq, a multi-tenant platform for WhatsApp support agents, the FastAPI backend serves a Next.js dashboard and also acts as the integration layer in front of the WhatsApp Cloud API: inbound webhooks with idempotent processing, outbound messages, Redis caching, ARQ background jobs and role-based access across tenants. The domain is split into ten DDD bounded contexts whose boundaries are enforced by a lint rule in CI. In VitaStock, a surgical supply chain system commissioned by a clinic, the FastAPI API backs twelve modules and five user roles in a Next.js frontend. At Lapzo the backend was NestJS, with Firebase Realtime Database for the real-time layer consumed by the Next.js client. The shape of the work in your migration, aggregating backend endpoints into a client-specific contract and keeping it strictly typed, is what I do in the API layer of these products; the mobile client would be new to me.

## Q3 — GraphQL (Apollo) and migrating away from GraphQL to REST

I designed and implemented GraphQL APIs alongside REST ones at Monadical, in Python backends consumed by React and Next.js clients, so I know the schema, resolver and client-cache side well enough to read a legacy GraphQL layer and understand what each query actually depends on. I have not taken part in a migration away from GraphQL to REST, and I would rather say that plainly than stretch it. The migration work I have done is of a similar kind: moving a course-embedding pipeline out of n8n into a service at Lapzo, and refactoring legacy codebases for consulting clients, where the method is the same one I would apply here, inventory the callers, define the new contract with types, move consumers one at a time behind the new endpoint, and delete the old path only when nothing reaches it.

## Q4 — TanStack Query / data fetching and caching libraries

My frontend state and data layers have used Zustand and Redux with a typed fetch layer, validated with Zod at the boundary; I have not used TanStack Query in production yet. The caching and invalidation decisions I have made sit mostly on the server. In Plixiq, Redis caches per-tenant configuration and conversation state, and webhook processing is idempotent so a retried delivery never duplicates a write. In Aluna, a durable CV-analysis pipeline on Inngest runs nine checkpointed steps with retries, and deduplication is placed before quota enforcement so a re-analysed CV reuses its cached score instead of paying for another model call. The rules I would carry into a TanStack Query refactor are the ones that mattered there: one key scheme per resource, invalidation tied to the mutation that changes the data rather than to timers, and cached values typed by the same contract as the endpoint so a stale shape fails at compile time.

## Q5 — How you ensure code quality across the stack

Tests first where the logic is non-trivial: at Monadical I led the frontend testing strategy with Vitest, Jest and React Testing Library under TDD, and on the Python side the API and domain layers carry unit tests that run in GitHub Actions on every pull request. Code review is the second gate; I led reviews on the Monadical team and acted as code reviewer for a client's development team on an NX multi-repo, where I also designed the database architecture. Architecture is enforced by tooling rather than by memory: in Plixiq the ten bounded contexts have a lint rule in CI that fails the build if one imports from another's internals, which keeps a one-person codebase honest. Design documents precede any change that crosses a boundary, and I write them to be read by the next engineer, not to be filed; eleven years of teaching made that habit permanent.

---
Weakest answers: Q3 and Q4, because the data has no GraphQL→REST migration and no TanStack Query, and the posting lists both. Both are honest and pivot to the closest real work; if he prefers not to flag the TanStack gap in Q4, delete the clause "I have not used TanStack Query in production yet". React Native and Rails are absent too and not asked directly.
