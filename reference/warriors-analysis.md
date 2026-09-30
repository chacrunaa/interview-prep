# Резюме: мои версии vs warriors

> Написано до переезда 2026-09-30: пути `resume-templates/...` теперь `me/cv-en.txt`, `fish/*`, `pipeline/<вакансия>/cv-*.txt`.

Дата: 2026-09-30

**Что сравнивалось:**
- **warriors** — 13 чужих резюме (12 PDF + 1 docx из `~/Downloads/warriors`). Тексты разложены в `warriors/*.md`. У Полуяктова две версии, поэтому файлов 13 на 12 человек.
- **мои** — `resume-templates/actual-template-resume.txt` (мастер), 11 файлов в `resume-templates/generated/`, `Andrey_CV` (RU), `bullets-bank.md`, `fish-bullets-*.md`, `recomendation-match.txt`.

**Как пользоваться warriors.** Это образец формы, а не честности. Минимум у четырёх из них видны те же косяки, что и у меня (раздел 4). Копировать стоит структуру, объём и формулу буллета. Числа и «легенды» оттуда не брать.

---

## 1. Warriors в одной таблице

| # | Кто | Роль | Стр. | Слов | Компаний подробно | Стаж | Буллетов на место | LinkedIn / GitHub | Локация / TZ | Стек под каждым местом | Контекст компании |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | Artem Kuznetsov | Senior Go | 2 | 657 | 3 | 6 | 9 / 6 / 9 | + / – | Poland | + | – |
| 02 | Anatoly Poluyaktov | Senior Go | 2 | ~545 | 3 + 3–4 строкой | 10+ | **3 / 3 / 3** | + / + | GMT+1/+2 | + | + («Streaming Platform») |
| 03 | Roman Gorishny | Senior Go | 2 | 1128 | 3 | 5+ | 6 / 6 / 6 | + / + | EU / EMEA | + | + (5M MAU) |
| 04 | Ruslan Khasanshin | Senior Go/Java | 2 | 736 | 3 + 2 side | 9+ | 6 / 6 / 3 | + / + / сайт | Lisbon | – | частично |
| 05 | Dmitriy Leventsov | Java / Data | 2 | 760 | 3 | 4+ | 9 / 6 / 2 | + / – | Yerevan | – | + (абзац) |
| 06 | Maxim Konstantinov | Senior Java | 2 | 551 | 3 | 8 | 4 / 4 / 4 | + / + | GMT+2 | + | – |
| 07 | Ivan Lubchenko | Backend | 2 | 564 | 3 | 6+ | 8 / 5 / 3 | + / + | – | – | – |
| 08 | Egor Nechesov | Senior Backend | **1** | 508 | 4 | 7+ | **4 / 3 / 3 / 2** | + / + | город у каждого места | – | **+ (1 строка курсивом)** |
| 09 | Onur Karaman | DevOps/SRE | **1** | 490 | 3 | 8+ | 5 / 5 / 5 | + / – | Warsaw | – | – |
| 10 | Viktor Friin | Fullstack | 1 | 554 | 4 | 7+ | 7 / 4 / 4 | + / + | UTC+1, EU permit | + | – |
| 11 | Anon (FIXME) | Backend Node | 3 | 815 | 3 | 6 | 4 / 3 / 2 | ? | Remote | + | + |
| 12 | Yanina | GenAI | 1 | 292 | 3 | 8+ | 8 / 2 / 3 | – | Madrid | – | – |

**Медиана warriors:** 2 страницы, **~560 слов**, 3 компании подробно, 3–6 буллетов на место.

**Мои для сравнения:**

| Файл | Слов | Буллетов на место | LinkedIn / GitHub | Локация |
|---|---|---|---|---|
| actual-template-resume.txt | 909 | 6 / 6 / 5 + блок AI из 3 | – / – | – |
| go-fintech-banking-en | 761 | — | – / – | – |
| pinobyte-en | 1359 | 8 / 7 / 7 | – / – | – |
| go-event-driven-nats | 1515 | — | – / – | – |
| **x5-ref-from-sasha-en-fish** | **2054** | **8 обязанностей + 6 результатов + абзац «AI in my work»** на каждое место | – / – | – |
| Andrey_CV (RU) | 1170 | 7–8 + 6 | – / – | – |

**Медиана моих EN-версий — ~1300 слов, в 2–2,5 раза больше warriors. x5-en — почти в 4 раза.**

---

## 2. Что общего у warriors и чего нет у меня

### 2.1 Объём и структура

Порядок секций у всех один:

> Шапка → Summary 2–5 строк → (опционально Selected Impact) → Experience → Skills → Education → Languages

Своё у отдельных людей:
- Ruslan — «Writing & Speaking».
- Roman — «Selected engineering project».

**Чего у warriors нет ни у кого:**
- **Нет деления на Responsibilities и Key results.** У всех один список буллетов, где каждый буллет — результат. У меня в generated два блока: обязанности (7–8, без цифр) и результаты (6). Обязанности просто повторяют результаты другими словами и удваивают объём.
- **Нет абзаца «AI in my work» у каждого места.** У меня он есть у всех трёх мест в x5-en. Для Carprice он ещё и вредит: «GitHub Copilot for completion and a chat model… in the later part of the project» — это оправдание, а не достижение.
- **Нет отдельной секции AI из 3–4 буллетов.** У warriors AI занимает одну строку в Skills (Ruslan, Maxim) или один буллет/проект (Egor — MCP servers + Claude Code skills; Roman — «Claude Code scaffold, adopted across 10+ repos»). Твой пайплайн — сильная вещь, но сейчас AI весит почти как одно место работы. Для Senior Go выходит, что «главное в кандидате — агенты».

**Бюджет объёма, к которому стоит прийти:**
- Summary — 50–70 слов.
- Syndicate — 4–5 буллетов.
- Nedra — 5–6 буллетов.
- Carprice — 3–4 буллета.
- Skills — 7–8 строк.
- AI — один проект-буллет.
- Итого 650–750 слов, 2 страницы максимум.

### 2.2 Шапка и контакты

| | warriors | у меня |
|---|---|---|
| LinkedIn | 11 из 12 | **нет нигде** |
| GitHub / сайт | 8 из 12 | **нет** (при этом есть что показать — пайплайн ревью) |
| Локация / TZ / разрешение на работу | 11 из 12 | **нет**, только «Full-time. Remote.» |
| Почта | gmail / proton / outlook | **yandex.com** — для EN-рынка минус |
| Мессенджеры | вторичны, в конце строки | Telegram и WhatsApp основные, каждый отдельной строкой |

### 2.3 Компании: узнаваемость и контекст

У warriors работает одно из двух:
- **Узнаваемый бренд:** Zalando, Thoughtworks, Otto Group, ByteDance, Google, Viaplay, Sberbank, ABN AMRO, Wildberries, Flexport.
- **Неизвестная компания + одна строка с масштабом:**
  - «Large e-commerce platform serving **5M monthly active users**» (Roman);
  - «iGaming provider… for global operators» (Egor);
  - «platform with **117K monthly unique users**» (Ruslan).

У меня все три компании для западного рекрутера неизвестны. Контекстные строки есть, но **без масштаба**:
- Syndicate — «internal performance-marketing platforms». Внутренняя платформа без цифр читается как «маленькая».
- Nedra — «remote drilling sites». Сколько площадок, заказчиков, сколько данных в сутки — не сказано.
- Carprice — «**Leading** / **Large** AutoTech platform». Маркетинговое слово вместо цифры. Сколько сделок, городов, какой GMV?

**В x5-en компании заменены на `[Company 1..3]`.** Для обезличенного образца это нормально, но отправлять так нельзя: безымянный наниматель рушит доверие сразу.

**Количество компаний.** Три места за 5 лет — как у большинства warriors, здесь всё в порядке. Риск в другом: **Syndicate — 9 месяцев** и последнее место. У warriors минимальный срок около 1 года (Rubyroid 5 мес. у Ивана — и это читается как слабое место). В резюме объяснять не нужно, но короткий ответ «почему 9 месяцев» надо иметь заготовленным.

### 2.4 Формула буллета

Почти у всех warriors буллет устроен так:

> **глагол + что + как (1–2 техники) + число (масштаб или до→после)**

Эталоны:
- *«Reduced checkout delivery cache-hit p50 from 207 ms to 50 ms after tracing a 2-connection pool bottleneck across 77 upstream calls; introduced pooling, batched reads, and single-flight request coalescing.»* — Roman
- *«Increased load-tested PostgreSQL throughput from ~150 to ~2000 DB tx/s while keeping p99 <120 ms by optimizing indexes, transaction boundaries, and contention…»* — Egor
- *«Moved ~120 secrets from GitLab CI variables… to AWS Secrets Manager… with rotation»* — Onur

**Числа в моём мастере (доля буллетов с цифрой):**

| Место | Буллеты с числом |
|---|---|
| **Syndicate (последнее, главное)** | **1 из 6** — только p95 1–2 с → 300–500 мс |
| Nedra | 4 из 6 |
| Carprice | 4 из 5 |

Самое свежее место — самое пустое по цифрам. Что там можно было бы посчитать:
- «large volumes of production data» — сколько строк / ГБ?
- идемпотентность — какой объём операций или денег в день через неё проходит?
- линтер миграций — сколько сломанных миграций поймано?
- миграция домена — сколько сервисов, таблиц, сколько длилось переключение?

*Все эти числа — реальные, от тебя. Не досочинять.*

### 2.5 Бизнес-результат, а не только техника

Warriors почти всегда показывают **деньги, пользователей или людей**:
- «$500K+ monthly revenue» (Egor)
- «30,000 clients per year» (Maxim)
- «reducing cloud spend by $212K/year» (Poluyaktov)
- «pages per on-call shift from ~15 to ~4» (Onur)
- «4 million users daily» (Maxim)

У меня бизнес-цифр почти нет — 100+ инспекторов, 10–15K оценок в сутки, «3x меньше ручной работы диспетчеров». Главное упущение — Carprice, «reducing spend on external requests»: деньги сэкономлены, но **цифры нет**. Это самое очевидное место, куда её нужно вписать.

### 2.6 Skills

У warriors:
- 6–9 строк вида «Категория: список через запятую», без пояснений.
- Детали техник живут в буллетах опыта, а не в Skills.
- Где знания поверхностные, стоит честная пометка: «**working knowledge of** gRPC / GraphQL patterns», «**familiarity with** OpenAI API, vector search, MCP» (Roman); «Rust — reading level» (была у тебя в pinobyte, это хорошо).

У меня:
- Skills — таблица с объяснениями в скобках: «gRPC/Protobuf (migrated a 14-service system from JSON/REST)», «Prometheus, Grafana (latency, RPS, queue depth, error classes)». Это дублирует опыт и раздувает объём.
- В x5-en Skills — 35 строк, больше, чем опыт у половины warriors.
- В Skills и стеках есть технологии, которых нет ни в одном буллете. На собеседовании спросят «где и что делал»:
  - **Kafka** — есть в стеке Carprice, а в буллете написано «a message broker». Какой именно? Там же указан и RabbitMQ.
  - **Terraform** — ни одного буллета.
  - **GraphQL (gqlgen)** — ни одного буллета в мастере.
  - **saga / transactional outbox** — в Skills x5-en, в опыте не показаны.
- В `Andrey_CV` навыки идут строчными через «·» и перемешаны с практиками: «cli», «codecs», «dependency inversion», «idempotency keys». Это не навыки, а слова из буллетов.

### 2.7 Summary

**Лучшие у warriors** (Poluyaktov, Onur, Egor) — 2–5 строк:
- стаж и размер команд;
- 3–5 чисел-заголовков: «99.99%-available multi-region… 50K+ requests/sec… 10K+ events/sec… $5M+ in transactions»;
- без «я» и без объяснения, как ты думаешь.

**У меня:**
- **Мастер** — около 120 слов. Одно огромное предложение со скобками внутри скобок, плюс абзац «I work agent-first». Терпимо, но плотно и тяжело читается.
- **x5-en** — 4 абзаца, около 280 слов, повествование от первого лица:
  - «My core profile is…»
  - «REST API and gRPC are both working tools for me»
  - «On storage, PostgreSQL is the primary one»
  - «These teams had no dedicated DevOps…»

  Это текст сопроводительного письма, а не summary.
- **Andrey_CV (RU):**
  - «Кропотливо и ответственно подхожу к решению любых задач, не боюсь принимать трудные и не классические решения» — пустая фраза;
  - «В свободное время увлекаюсь изучением языков и занимаюсь спортом :)» — смайлик в резюме;
  - «**Русский** -» — уровень не заполнен.

---

## 3. Косяки и противоречия в моих материалах

### 3.1 Критично — исправить до следующей отправки

1. **Фамилия.**
   - «**KALIN / Калин**» — в мастере и в 9 из 11 generated.
   - «**Карлин**» — в `Andrey_CV` и `x5-ref-from-sasha-resume.txt`.
   - Git-пользователь и домашний каталог — karlin.

   Если настоящая фамилия Карлин, то почти все отправленные резюме подписаны неправильной фамилией. **Проверь, что ушло работодателям.**
2. **Служебный комментарий на русском внутри EN-текста:** «(OAuth2 / OIDC, JWT) - **только если реально делал, указать как именно.**»
   - `actual-template-resume.txt:104`
   - **`generated/netbox-labs-resume.txt:104`** — если эта версия уходила в NetBox Labs, её видел рекрутер.

   Там же сломано форматирование: буллет про аутентификацию склеен с предыдущим, без «-».

   Аналог у warriors — «Add relevant keywords here…» у Максима и FIXME в анонимном шаблоне. Это ровно та ошибка, которая сразу выдаёт шаблон.
3. **Разные телефоны.**
   - +7 921 981 4983 — в большинстве версий.
   - **+84 888 147 284** — в `nodi-resume.txt` и `pinobyte-en-resume.txt`.

   Если оба номера рабочие, выбери один на весь EN-рынок.
4. **Один и тот же наниматель в разных версиях — с разным стеком и разными проектами.** Это главная системная проблема, подробнее в 3.2.

### 3.2 Расхождения между версиями (эффект fish-bank)

| Утверждение | Где | Где иначе |
|---|---|---|
| Асинхронный backbone Nedra — **RabbitMQ** | мастер, x5, pinobyte | **NATS JetStream** («built the asynchronous backbone of the platform») — go-event-driven-nats |
| **MongoDB** для сырых payload-ов — в **Nedra** | x5-ru/en, go-event-driven-nats | в **Syndicate** — pinobyte-en/ru. Сам recomendation-match это признаёт: «в nodi-resume было привязано к Syndicate» |
| Syndicate — «egress-сервис, HTTP CONNECT/SOCKS5, **tens of thousands of concurrent connections**, ротация исходящих адресов, обход anti-automation» | pinobyte-en/ru | Больше нигде. В мастере Syndicate — платежи и реестр аккаунтов |
| Carprice — «Shipped a thin Node.js wrapper (**npm package**)» | pinobyte, nodi | Больше нигде |
| Nedra — «SDK generated from proto… private module proxy» | pinobyte-en | Больше нигде |
| Headline | «Networking, Proxy Infrastructure» / «Full Stack, GraphQL, **HTMX**» / «Event-Driven» / «Fintech» | Одни и те же три места работы |

**Почему это опасно.** У одного из warriors — Полуяктова — это видно прямо. Две его версии за одним именем и контактами:
- «Earlier experience»: в одной **Group-IB, Google, Anabar**, в другой **Sellics, Google, Sekoia.io, Anabar**;
- даты Google и Anabar сдвинуты;
- магистратура — то «Computer security 2019–2021», то «Software Engineering 2018–2020».

Две такие версии на одном рекрутинговом рынке или в одной ATS рекрутеры сопоставят сразу. С 11 версиями и банком из 50 досочинённых буллетов у тебя тот же риск: **LinkedIn будет один, а резюме — одиннадцать разных**.

### 3.3 Логические дыры, за которые зацепится интервьюер

- **«Migrated inter-service communication from JSON/REST to gRPC/Protobuf, reducing traffic and latency over constrained links to remote sites».** Межсервисный трафик идёт внутри платформы, а узкий канал — от буровой до приёма. Спросят: «gRPC между сервисами в ДЦ помог узкому каналу на буровой — как?»
- **«100% data completeness».** Абсолютная цифра сразу вызывает вопрос «как измеряли?». У warriors — 99.9 / 99.99 и конкретный способ сверки.
- **Senior в заголовке, «Go Developer» во всех должностях.** У warriors должность и заголовок совпадают. Либо в должностях писать то, что реально было, но в EN-форме («Backend Engineer (Go)»), либо не ставить «Senior» в заголовок без опоры. «**Led** the migration…» при наличии руководителя в команде из 7 — тоже место для вопроса.
- **«Backend engineer with 5+ years… full-stack before that» + «PHP (early full-stack period)» в x5-en.** До июля 2021 нет ни одного места работы. Если «до этого» было, это пробел в хронологии. Если не было — утверждение без опоры. Warriors такое выносят в «Freelance + pet projects (since 2019)» с датами (Viktor) или не пишут вовсе.
- **Nedra: «Increased team delivery speed by 20–30%».** Диапазон без способа измерения. У Ивана так же («40–60%», «20–30%», «30–50%») — такие диапазоны у warriors как раз выглядят самыми подозрительными.
- **Carprice: Kafka и RabbitMQ в стеке, но «a message broker» в буллете.** Слово-заглушка там, где должно быть имя технологии.

### 3.4 AI-слоп и маркеры сгенерированного текста

У warriors буллеты сухие: глагол, объект, цифра. Не пишет так даже Viktor, у которого есть своя вода («My experience helps to get maximal profit for the company»).

Что у меня читается как текст от LLM:
- **Риторика «не X, а Y»:**
  - «so the process improves, **not just** the code»;
  - «debug network incidents in production **rather than** guess about them»;
  - «found **instead of** being called "flaky network"»;
  - «graceful degradation **instead of** failure»;
  - «**turned** extracting a module into a service **into a mechanical step**».
- **Эссе о себе:**
  - «My focus is correctness and operability»;
  - «I work agent-first»;
  - «REST API and gRPC are both working tools for me»;
  - «design, contracts and the final review stay under my own control» — в мастере эта мысль повторена **трижды** (summary, skills, AI-секция).
- **Однотипные хвосты «, so …» / «, making …» / «- …» почти в каждом буллете.**
- **Список-перечисление вместо результата:**
  - «escape analysis on decoding buffers, sync.Pool for batch buffers, GOMEMLIMIT set to the container limit, bottlenecks found with pprof and runtime/trace». Здесь нет ни одного «было → стало». Сколько сняли по памяти, по p99, по GC pause?

  Roman делает то же, но с цифрой: «Scaled order-search concurrency from 10 to 30 workers and diagnosed/fixed the data race exposed under higher parallel load».

### 3.5 Процессные косяки репозитория

- **Одиннадцать generated-версий против одного мастера.** Факты расползаются (см. 3.2). У warriors один человек — одна версия. Даже Полуяктов с двумя версиями — это проблема, а не образец.
- **Мастер содержит черновые хвосты:** русский комментарий, склеенный буллет. Мастер — источник истины, в нём мусора быть не должно.
- **`Andrey_CV` (RU) и `actual-template-resume.txt` расходятся:**
  - фамилия;
  - в RU есть блоки «Функционал» и «Команда», в EN-мастере нет;
  - в RU брокер Carprice — «брокер сообщений», в EN-стеке — Kafka и RabbitMQ.

---

## 4. Где warriors сами ошибаются (не копировать)

| Кто | Косяк |
|---|---|
| Poluyaktov | Две версии с разной ранней историей и образованием (см. 3.2) |
| Ivan Lubchenko | Бакалавр **Aug 2020 – May 2024** и магистр 2024–2025 при full-time Software Engineer с **April 2020**; «reducing security incidents to zero»; Skills — около 80 пунктов, включая Vue, Next.js, Hanami, Sinatra |
| Maxim Konstantinov | «8 → 2.5 minutes (**a 56% reduction**)» — на самом деле 69%, арифметика не сходится; «Add relevant keywords here separated by spaces» осталось в тексте; абзац ACHIEVEMENT — чистая вода |
| Anon (rez-english-v4) | FIXME в шапке, 3 страницы, Skills-суп из 70+ пунктов, «6 лет, 7 мес» по-русски внутри EN, Tech Stack повторяется построчно |
| Viktor Friin | «My experience helps to get maximal profit for the company», Skills со словами «Math», «UI, UX» |
| Roman Gorishny | 1128 слов, «Senior Go capability highlights» дублирует Skills, «Certification **targets**» (цели, а не сертификаты) |
| Yanina | «improving cost per token in 5 times», «Jun 2020s» — нет вычитки |

**Лучшие образцы под Go/Backend EN:**
- **Структура и summary** — Poluyaktov (сама форма, не содержание).
- **Плотность и одна страница** — Egor Nechesov.
- **Правдоподобные цифры с «~»** — Onur Karaman.
- **Честность и Go-платформа** (observability на 25 сервисов, Renovate, govulncheck) — Ruslan Khasanshin.
- **Глубина Go-специфики** — Roman Gorishny. Брать формулу буллета, но не объём.

---

## 5. Что делать: план по шагам

1. **Исправить критичное из 3.1:** фамилия, русский комментарий в мастере и netbox, один телефон.
2. **Завести одну «fact sheet» на каждого нанимателя** — стек, брокер, хранилища, числа. Все версии должны с ней совпадать. Ответить себе один раз и навсегда:
   - брокер Nedra — RabbitMQ или NATS?
   - MongoDB — в Nedra или в Syndicate?
   - был ли egress/proxy?
   - Kafka в Carprice — где и зачем?
3. **Собрать один EN-мастер на 650–750 слов**, вариации по вакансиям ограничить:
   - headline (в пределах одной оси, без «HTMX» и «Proxy»);
   - summary;
   - порядок буллетов;
   - порядок строк в Skills.

   **Не менять:** факты, стек и проекты у нанимателя.
4. **Структура:**
   ```
   ANDREY KARLIN
   Senior Backend Engineer (Go) · 5+ yrs · Distributed Systems, Data Ingestion, Payments
   City, Country · UTC+X · open to remote/relocation · email@gmail · linkedin · github · telegram

   SUMMARY (3–4 строки, 3–4 числа, без "I")

   EXPERIENCE
   Company — одна строка контекста С МАСШТАБОМ          Mon YYYY – Mon YYYY
   Backend Engineer (Go)
   - 4–6 буллетов: глагол + что + как + число
   Stack: одна строка

   SKILLS (7–8 строк "Категория: a, b, c", без пояснений в скобках)
   EDUCATION / LANGUAGES
   ```
   AI — **одна строка в Skills + один буллет или проект со ссылкой на GitHub**, если пайплайн можно показать. У Ruslan статья на Medium и Habr работает сильнее любого абзаца про agent-first.
5. **Добрать реальные числа для Syndicate** (2.4) и бизнес-цифры для Carprice и Nedra (2.3, 2.5). Каждое число должно выдерживать вопрос «как измеряли».
6. **Вычистить слоп (3.4).** Проверка одна: если фразу можно вставить в резюме любого бэкендера — вычеркнуть.
7. **Пересчитать Skills.** Всё, чего нет в буллетах, либо убрать, либо пометить «working knowledge» (Terraform, GraphQL, saga).
8. **Подготовить устные ответы:** 9 месяцев в Syndicate, «Senior» при должности Go Developer, что было до июля 2021.

### Пример переписывания (Syndicate, мастер)

Было — 6 буллетов, число только в одном. Стало — 4 буллета по формуле. Вместо `[..]` подставить реальные числа, придумывать их нельзя:

- Cut ad-account registry p95 from 1–2 s to 300–500 ms by removing N+1 queries, batching reads and switching to keyset pagination in PostgreSQL.
- Implemented idempotency keys at API and storage level for payment operations (~[N] ops/day), eliminating duplicate execution on client and provider retries.
- Migrated a core domain to a new data model across [N] services and [N] tables; moved [N]M production rows with a Go CLI tool (validation, quarantine of invalid records, safe re-run) with zero loss.
- Added migration linting and pre-push hooks to CI, stopping [N] broken migrations from reaching deployment in [period].

---

## Индекс файлов warriors

- [01 Artem Kuznetsov — Senior Go](warriors/01-artem-kuznetsov-go.md)
- [02a Anatoly Poluyaktov — Senior Go, v1](warriors/02a-anatoly-poluyaktov-go-v1.md)
- [02b Anatoly Poluyaktov — Senior Go, v2](warriors/02b-anatoly-poluyaktov-go-v2.md)
- [03 Roman Gorishny — Senior Go](warriors/03-roman-gorishny-go.md)
- [04 Ruslan Khasanshin — Senior Go/Java](warriors/04-ruslan-khasanshin-go-java.md)
- [05 Dmitriy Leventsov — Java / Data](warriors/05-dmitriy-leventsov-java.md)
- [06 Maxim Konstantinov — Senior Java](warriors/06-maxim-konstantinov-java.md)
- [07 Ivan Lubchenko — Backend](warriors/07-ivan-lubchenko-backend.md)
- [08 Egor Nechesov — Senior Backend TS](warriors/08-egor-nechesov-backend-ts.md)
- [09 Onur Karaman — DevOps/SRE](warriors/09-onur-karaman-devops.md)
- [10 Viktor Friin — Fullstack](warriors/10-viktor-friin-fullstack.md)
- [11 Anon — Backend Node (шаблон с FIXME)](warriors/11-anon-backend-node-template.md)
- [12 Yanina — GenAI](warriors/12-yanina-genai.md)
