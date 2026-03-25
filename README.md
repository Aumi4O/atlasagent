# Atlas Agent (`atlasagent`)

Публичный репозиторий: [github.com/Aumi4O/atlasagent](https://github.com/Aumi4O/atlasagent).

Это **starter-repo** для Cursor, GitHub и **режима агента в ChatGPT**, чтобы собрать “мозг” агента, который:
- ищет высокооплачиваемые проекты,
- понимает два направления бизнеса,
- готовит материалы для подачи,
- регистрирует аккаунты на платформах,
- проходит подачу заявки максимально автономно,
- и аккуратно логирует всё, что уже было сделано.

## Главное
Этот репозиторий специально сделан как **knowledge-first**:
сначала знание, правила, фильтры и логи, потом — код.

Так агент не “галлюцинирует”, а работает по твоим данным.

### ChatGPT / Agent mode (кратко)

1. В **Instructions** (или системный контекст агента) вставь содержимое `prompts/atlas_personalization_prompt.md`. При необходимости добавь `prompts/system_master_prompt.md` как расширение политики.
2. Загрузи в знания агента ключевые файлы из `knowledge/` и при необходимости `AGENTS.md` (порядок чтения — внутри `AGENTS.md`).
3. Подробный чеклист: [docs/CHATGPT_AGENT_MODE.md](docs/CHATGPT_AGENT_MODE.md).

## Два направления
1. **AI Fashion Artists**  
   Портфолио / creative direction / AI visual storytelling.

2. **Lead Agents Studio / SmartLine**  
   Custom AI solutions, AI systems, revenue apps, voice/chat/follow-up systems, AI booking and qualification flows.

## Основные фильтры поиска
- Не рассматривать проекты **ниже $1000**.
- Не идти в **pure developer / pure Python** роли, где нужен классический инженер как основной профиль.
- Приоритет — проекты, где сочетаются:
  - вкус / creative direction / brand sense,
  - AI automation / AI systems,
  - работа с реальным бизнес-результатом.
- Для AI systems отдельно таргетировать:
  - **израильский рынок**,
  - **construction / real-estate developers**,
  - простые бизнесы, которым реально можно внедрить AI automation.

## Что дальше делать в Cursor
1. Открой этот репозиторий в Cursor.
2. Убедись, что файл `AGENTS.md` лежит в корне.
3. Убедись, что правила есть в `.cursor/rules/`.
4. Дай Cursor первое задание:

```text
Read AGENTS.md, docs/ARCHITECTURE_RU.md, and all files in knowledge/.
Do not write code yet.
First produce a concrete implementation plan for Phase 1 only:
job discovery, scoring, and application logging.
```

5. Потом второе:

```text
Implement Phase 1 only.
No browser automation yet.
Use the schemas and prompts already in the repo.
```

6. Потом третье:

```text
Implement Phase 2:
assisted browser application flows with mandatory human approval before final submit.
```

## Очень важно про безопасность
- **Не коммить реальные пароли и токены в GitHub.**
- Используй `.env` локально.
- Если пароль, который был отправлен в чат, реально рабочий и используется где-то ещё — **лучше сменить его**.
- На CAPTCHA / 2FA / email verification агент должен **останавливаться и просить ручное действие**, а не пытаться обходить ограничения.

## Быстрый GitHub flow

### Вариант 1 — через GitHub веб-интерфейс
1. Создай **private repository**.
2. Не добавляй автоматически лишние файлы, если будешь пушить этот starter как существующий проект.
3. Залей содержимое этой папки.

### Вариант 2 — через CLI
```bash
cd atlas
git init
git add .
git commit -m "Initial Atlas Agent repo"
git branch -M main
git remote add origin https://github.com/Aumi4O/atlasagent.git
git push -u origin main
```

## Что уже предзаполнено
- профайл владельца,
- описание бизнесов,
- стратегия поиска,
- фильтры,
- шаблоны cover letter,
- master prompt для агента,
- схема логирования заявок,
- инструкция для Cursor.

## Что тебе надо дописать вручную
- точные resume versions,
- банкинг / billing / legal details, если нужны,
- реальные platform-specific ответы,
- список платформ, где ты точно хочешь работать,
- реальные credentials — только локально, в `.env`, не в git.

