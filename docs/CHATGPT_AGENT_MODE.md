# ChatGPT Agent mode — using this repository

This repo is the **knowledge and policy layer** for Olga’s job-application workflow. Use it with ChatGPT **Custom GPTs**, **Projects** file context, or any “agent” surface that accepts instructions plus uploaded files.

## 1. What to paste as instructions

**Primary (short, repo-aware):** copy all of [`prompts/atlas_personalization_prompt.md`](../prompts/atlas_personalization_prompt.md).

**Optional extension (full operating policy):** append or merge [`prompts/system_master_prompt.md`](../prompts/system_master_prompt.md).

Keep both aligned with [`AGENTS.md`](../AGENTS.md) guardrails (no secrets in chat, no CAPTCHA/2FA bypass, truthful claims only).

## 2. What to attach as knowledge

Minimum useful set:

- [`knowledge/owner_profile.yaml`](../knowledge/owner_profile.yaml)
- [`knowledge/businesses/aifashionartists.yaml`](../knowledge/businesses/aifashionartists.yaml)
- [`knowledge/businesses/leadagentsstudio.yaml`](../knowledge/businesses/leadagentsstudio.yaml)
- [`knowledge/businesses/smartline.yaml`](../knowledge/businesses/smartline.yaml)
- [`knowledge/search_strategy.yaml`](../knowledge/search_strategy.yaml)
- [`knowledge/negative_filters.yaml`](../knowledge/negative_filters.yaml)
- [`knowledge/application_answers.yaml`](../knowledge/application_answers.yaml)
- [`knowledge/resumes/resume_matrix.yaml`](../knowledge/resumes/resume_matrix.yaml)

For evaluation and logging prompts, also add files under [`prompts/`](../prompts/) (e.g. `vacancy_evaluation_prompt.md`, `application_execution_checklist.md`).

## 3. Read order (matches AGENTS.md)

When the agent should “sync” with the repo brain, read in this order:

1. `docs/ARCHITECTURE_RU.md`
2. `knowledge/owner_profile.yaml`
3. `knowledge/businesses/*.yaml`
4. `knowledge/search_strategy.yaml`
5. `knowledge/negative_filters.yaml`
6. `knowledge/application_answers.yaml`
7. `knowledge/resumes/resume_matrix.yaml`
8. `schemas/application_record.schema.yaml`
9. `logs/applications.csv`

## 4. Cursor vs ChatGPT

- **Cursor:** follow root [`AGENTS.md`](../AGENTS.md) and [`.cursor/rules/job-agent.mdc`](../.cursor/rules/job-agent.mdc).
- **ChatGPT:** there is no automatic git sync; re-upload files when you change them, or point the model at this GitHub repo if your product flow allows it.

## 5. Security

Never put API keys, passwords, or session tokens in instructions or uploaded knowledge. Use local `.env` only (see [`.env.example`](../.env.example) and `docs/SECURITY_RU.md`).
