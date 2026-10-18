# reference

Чужое знание, только для чтения. Три экспорта Telegram-топиков сообщества АйТи Красавчика (одна супергруппа, id 2110672971, разные форум-топики), разбор каждого и база чужих резюме.

Сырьё чатов и `warriors/` - в `.gitignore` (чужие личные данные, ~27 МБ). Разборы `*-analysis/` лежат в git, их служебные `_work/` - нет.

## Чаты и разборы

| Топик | Сырьё | Сообщений | Период | Разбор | Главный файл |
|---|---|---|---|---|---|
| «Резюме» (прожарка) | `roast-chat/` | 5 023 | 2023-12 … 2026-09 | `roast-analysis/` | `rules.md` - 151 правило, `canon-*.md` по направлениям |
| «LinkedIn блокировки» | `linkedin-bans-chat/` | 1 941 | 2025-02 … 2026-10 | `linkedin-bans-analysis/` | `SETUP.md` - пошаговый заход в LinkedIn, 210 правил |
| «Налоги, ИП, платежи, контракты» | `taxes-chat/` | 9 435 | 2024-01 … 2026-10 | `taxes-analysis/` | `OFFER-PLAYBOOK.md` - этап оффера, 439 правил |

Рядом с каждым разбором лежит промпт, по которому он сделан: `roast-analysis-PROMPT.md`, `linkedin-bans-analysis-PROMPT.md`, `taxes-analysis-PROMPT.md`. Новый экспорт того же топика разбирается тем же промптом.

## Чем пользоваться

- **Резюме и профиль по содержанию** - `roast-analysis/canon-hh.md`, `canon-hirify.md`, `canon-linkedin.md`, цифры объёма в `volume.md`, полный свод в `rules.md`.
- **Аккаунт LinkedIn: завести, не словить бан, разбаниться** - `linkedin-bans-analysis/SETUP.md`, под ним `rules.md`, `BAN-TRIGGERS.md`, `RECOVERY.md`, `canon-profile-safety.md` (черновик для канона направления).
- **Оффер: как оформиться и получать деньги** - `taxes-analysis/OFFER-PLAYBOOK.md`, под ним `jurisdictions.md` (страновая матрица), `banking.md` (счета и банки), `payments.md` (маршруты денег), `contracts.md` (что смотреть в договоре), `risks.md` (ФНС, валютный контроль, работодатель).
- **Чужие резюме как образец формы** - `warriors/` + `warriors-analysis.md`.

## Курс Балуна по System Design

`balun-sd/` - платный курс, целиком в `.gitignore`. По нему учит скилл `teach-sd`.

- `raw/00-05/` - распакованные уроки (PDF слайдов, видео, ДЗ). Видео есть у уроков 1, 3, 5. У урока 2 и 4 видео нет, у урока 5 нет слайдов. `raw/notes-*` - два архива чужих конспектов.
- `text/NN-slides.md` - дословный текст каждого слайда со ссылкой на PNG (`slides/NN/`), `NN-slides.raw.md` - сырой текстовый слой PDF. `NN-transcript.md` - расшифровка видео, `NN-homework.md` - ДЗ, `notes-*.md` и `ns*-slides.raw.md` - конспекты.
- `map/course-map.md` - карта курса: урок → тема → подтема, ключевые идеи, слайды, таймкоды. Порядок обучения в `teach-sd` задаёт она.
- `site/` - Docusaurus по карте: `cd reference/balun-sd/site && npm start` → http://localhost:3000.

Пересборка: `python3 -I reference/_tools/balun/extract_slides.py --pdf <pdf> --lesson NN --out reference/balun-sd` (сырой текст и PNG), `reference/_tools/balun/transcribe.sh <mp4> <out> <NN>` (mlx-whisper из `~/.venvs/whisper`), `python3 -I reference/_tools/balun/build_site.py reference/balun-sd` (страницы сайта из карты и текстов).

## Прочее

- `_tools/build_corpus.py` - собирает корпус из экспорта: `messages.json`, куски по ~50 К символов, выжимка сообщений эталона.
  `python3 reference/_tools/build_corpus.py --chat reference/<slug>-chat --root <id топика> --work reference/<slug>-analysis/_work`
- `_tools/validate_theses.py` - проверяет тезисы агентов (цитата дословна, id существует) и собирает `theses.jsonl`.
  `python3 reference/_tools/validate_theses.py --work reference/<slug>-analysis/_work --schema bans|taxes all`

## Границы

Разборы пишут только в свою папку `*-analysis/`. Переносить выводы в `hh/`, `hirify/`, `linkedin/` - решение пользователя: каноны направлений он правит сам, здесь лежат только черновики (`canon-*.md`).

Это пересказ чужого опыта, а не инструкция и не консультация. У правил есть окно дат; то, что работало в 2024, в 2026 может быть мертво.
