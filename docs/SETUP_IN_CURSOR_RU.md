# Как использовать это в Cursor

## 1. Открыть проект
Открой папку репозитория в Cursor как отдельный project folder.

## 2. Проверить контекст
В корне должен лежать `AGENTS.md`.
В `.cursor/rules/` должен лежать `job-agent.mdc`.

## 3. Первое сообщение в Cursor
Вставь это:

```text
Read AGENTS.md, docs/ARCHITECTURE_RU.md, and every file in knowledge/.
Summarize the system in English for implementation.
Then propose the smallest Phase 1 architecture.
Do not write browser automation yet.
```

## 4. Второе сообщение
```text
Implement Phase 1 only:
- vacancy model
- scoring model
- application log writer
- no browser automation
- no secrets
- make everything resumable
```

## 5. Третье сообщение
```text
Implement Phase 2 only:
- proposal packet builder
- narrative selector (fashion / systems / hybrid)
- cover letter generator
- screening answer generator
- human approval gate before submit
```

## 6. Четвёртое сообщение
```text
Design Phase 3 browser automation.
Do not bypass CAPTCHA or verification.
Stop and checkpoint on OTP, email verification, or 2FA.
Use env-based secrets only.
```

## 7. Как не дать Cursor уехать в хаос
Каждый раз пиши:
- only this phase,
- no extra features,
- follow AGENTS.md,
- use knowledge files as source of truth,
- no fabricated data.

## 8. Правильный ритм работы
Лучше делать так:
1. План
2. Маленькая реализация
3. Проверка
4. Следующий маленький шаг

А не просить “сразу весь автономный агент”.
