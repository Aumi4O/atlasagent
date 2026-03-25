# AGENTS.md

This repository is the operating brain for Olga's job-application agent.

## Mission
Build and maintain a private, structured system that helps Olga:
1. discover high-value opportunities,
2. evaluate fit,
3. prepare truthful, tailored application assets,
4. complete platform onboarding and job applications,
5. log every step with clean state.

## ChatGPT / Agent mode
For Custom GPTs, Projects, or other ChatGPT agent surfaces, see `docs/CHATGPT_AGENT_MODE.md` (what to paste, what to upload, read order).

## Always read first
Before changing anything, read these files in order:
1. `docs/ARCHITECTURE_RU.md`
2. `knowledge/owner_profile.yaml`
3. `knowledge/businesses/aifashionartists.yaml`
4. `knowledge/businesses/leadagentsstudio.yaml`
5. `knowledge/businesses/smartline.yaml`
6. `knowledge/search_strategy.yaml`
7. `knowledge/negative_filters.yaml`
8. `knowledge/application_answers.yaml`
9. `knowledge/resumes/resume_matrix.yaml`
10. `schemas/application_record.schema.yaml`
11. `logs/applications.csv`

## Source of truth
If there is a conflict:
1. structured YAML files beat markdown prose,
2. latest explicit user instruction beats old files,
3. logs beat assumptions.

## Hard guardrails
- Never commit secrets, passwords, API keys, or session cookies.
- Keep secrets in local `.env` only.
- Never bypass CAPTCHAs, email verification, or 2FA.
- If a workflow reaches CAPTCHA / OTP / email verification, pause and request manual completion.
- Never fabricate job history, revenue numbers, skills, or clients.
- Never apply to jobs below the minimum budget floor unless the user explicitly overrides it.
- Avoid pure software-engineering / pure Python developer roles unless the user explicitly says otherwise.
- Prefer opportunities where creative taste and AI systems overlap.
- Prefer Israeli market opportunities for AI systems, especially real-estate / construction developers.
- Log every important state transition.

## Preferred development order
1. Phase 1: discovery + scoring + logging
2. Phase 2: assisted application flows with human approval
3. Phase 3: semi-autonomous application execution
4. Phase 4: safe autonomous execution where policy and UX allow it

## Working style
- Start with plans, then implement.
- Keep code modular.
- Write small, reviewable changes.
- Use schemas for structured data.
- Update documentation when structure changes.
- If you add automation, make it resumable and idempotent.

## Browser automation rules
- Registration must use env-based credentials only.
- Save platform state in structured logs, not in prose only.
- On failure, write a resumable checkpoint.
- Use explicit selectors and stable flows.
- Record whether a submit was completed, partially completed, or blocked.
- When blocked by CAPTCHA / OTP / 2FA / verification, notify the human via Telegram: `python3 scripts/telegram_notify.py` (see `docs/TELEGRAM_ASSISTANCE.md`).

## Application quality rules
Each application should:
- match one of the allowed tracks,
- exceed budget threshold or have a strong strategic exception,
- use the correct resume version,
- use the correct narrative (fashion / systems / hybrid),
- be logged immediately after submission.

## Output expectations
When asked to implement features:
- first explain the phase,
- then propose file changes,
- then implement,
- then suggest the next smallest useful step.
