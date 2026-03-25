# Архитектура проекта

## 1. Что это вообще такое
Это не “ещё один бот”.
Это **операционная система для job-application агента**.

У неё три слоя:

### Слой A — Knowledge Layer
Здесь агент узнаёт:
- кто такая Olga,
- какие у неё бизнесы,
- какие услуги и кейсы она продаёт,
- какие роли / проекты ей подходят,
- какие роли ей НЕ подходят,
- какие материалы использовать для подачи.

Файлы:
- `knowledge/owner_profile.yaml`
- `knowledge/businesses/*.yaml`
- `knowledge/search_strategy.yaml`
- `knowledge/negative_filters.yaml`
- `knowledge/application_answers.yaml`
- `knowledge/resumes/resume_matrix.yaml`

### Слой B — Decision Layer
Здесь агент решает:
- стоит ли идти в эту вакансию,
- по какому треку её подавать,
- какой resume использовать,
- какой angle брать в cover letter,
- нужен ли human review,
- можно ли автоматически продолжать.

Файлы:
- `prompts/system_master_prompt.md`
- `prompts/vacancy_evaluation_prompt.md`
- `prompts/application_execution_checklist.md`
- `schemas/*.yaml`

### Слой C — Execution Layer
Здесь уже живёт код:
- поиск вакансий,
- нормализация данных,
- scoring,
- логирование,
- browser automation,
- checkpoints,
- retries,
- статус заявки.

Папки:
- `src/`
- `logs/`
- `scripts/`

---

## 2. Два карьерных / бизнес-трека

### Track A — AI Fashion Artists
Использовать, когда проекту нужен:
- creative direction,
- AI visuals,
- fashion storytelling,
- luxury / beauty / brand-sensitive visual work,
- sense of aesthetics,
- editorial / campaign concepting.

### Track B — Custom AI Solutions & Systems
Использовать, когда проекту нужен:
- AI automation,
- lead qualification,
- booking flows,
- chat / voice agents,
- business workflow systems,
- custom AI applications,
- revenue / support / ops automation.

### Track C — Hybrid
Самый ценный трек.
Использовать, когда проект одновременно хочет:
- эстетическое мышление / вкус / storytelling,
- AI systems / automation / business execution.

---

## 3. Что агент должен делать по pipeline

### Step 1 — Find
Искать подходящие проекты / вакансии / запросы.

### Step 2 — Qualify
Проверять:
- бюджет,
- fit по одному из треков,
- рынок,
- насколько это pure dev role,
- насколько это strategic fit.

### Step 3 — Prepare
Выбрать:
- resume version,
- cover letter angle,
- portfolio links,
- company links,
- short answers.

### Step 4 — Register / Sign in
Если на платформе нет аккаунта:
- создать аккаунт с email из локальных secrets,
- дойти до момента, пока не требуется ручная верификация,
- сохранить статус.

### Step 5 — Apply
Пройти все шаги формы:
- profile,
- attachments,
- screening questions,
- portfolio / website links,
- final submit.

### Step 6 — Log
Сразу записать:
- platform,
- company,
- job title,
- budget,
- track,
- status,
- what was submitted,
- blockers,
- next action.

---

## 4. Главные decision rules

### Денежный фильтр
Всё ниже **$1000** по умолчанию отсекается.

### Role filter
Не брать:
- pure Python developer,
- backend-heavy engineering-first roles,
- roles where Olga is being sold mainly as a traditional programmer.

### Strategic preference
Брать в приоритет:
- проекты, где нужны и вкус, и AI,
- AI systems для простых бизнесов,
- Israel market,
- construction / real-estate developers,
- high-ticket service businesses,
- beauty / aesthetics / luxury / brand-sensitive businesses.

---

## 5. Execution modes

### Mode 1 — Research only
Ничего не отправлять.
Только собирать и ранжировать.

### Mode 2 — Assisted apply
Агент всё готовит, но перед final submit просит подтверждение.

### Mode 3 — Semi-autonomous
Агент сам доходит до почти финала и отправляет там, где нет policy-risk / verification blockers.

### Mode 4 — Autonomous
Только для уже проверенных flows и только там, где нет CAPTCHA / 2FA / ручной email verification.

---

## 6. Почему knowledge-first лучше
Потому что главная проблема обычно не “нажать submit”.
Главная проблема — чтобы агент:
- не путал бизнесы,
- не слал не тот angle,
- не шёл в плохие роли,
- не подавался дважды,
- не продавал Olga как “не того специалиста”.

---

## 7. Что сначала строить в Cursor

### Phase 1
- data model
- vacancy parser
- fit scoring
- structured logs

### Phase 2
- application packet generator
- cover letters
- screening answers
- human approval step

### Phase 3
- browser sessions
- sign-in / registration
- platform state
- resumable application runs

### Phase 4
- platform adapters
- queue
- retries
- autonomous execution on approved platforms only

---

## 8. Технический стек
Рекомендуемый стек для browser automation:
- Playwright
- structured YAML / CSV / JSON logs
- env-based secrets
- modular adapters per platform

Но этот repo умышленно начинается не с кода, а со знания и правил.

---

## 9. Дата фиксации исходных бизнес-данных
Этот starter был собран 2026-03-25.
Если сайты / offer / positioning меняются — обновляй YAML файлы в `knowledge/businesses/`.
