# TL;DR

> Формат до 2026-09-30 (старые имена файлов, без направлений). Автоматические разделы пересоберутся по новому формату при следующем прогоне `/career`.

Обновлено: 2026-09-29 | вакансий/батчей обработано: 8

## Банк
- fish-bullets-bank.md: 27/50 активных
- fish-bullets-patterns.md: 9/30 активных

## Топ-теги
- домен: #network-infra x3, #ai x2, #python x1, #php x1, #security x1, #ecommerce x2,
  #iot x1, #fintech x1, #retail x1
- бизнес: #b2b x26, #b2c x2, #marketplace x1, #internal-tools x2
- система: #data-platform x8, #saas x7, #crm x3, #proxy-network x2, #billing x1,
  #ecommerce-platform x1
- компания: #scaleup x18, #avg-product x8, #bigtech x2, #enterprise x2, #outsource x1

## Самые переиспользуемые записи
- fish-bullets-bank #7 (#nodejs #migrations #architecture #b2c #avg-product) - 6x (pinobyte, nodi, go-react-fintech, amocrm, willix, x5)
- fish-bullets-bank #6 (#databases #performance #data-platform) - 5x (pinobyte, nodi, go-event-driven-nats, amocrm, x5)
- fish-bullets-bank #11 (#cloud #devops #ci-cd #infrastructure) - 4x (nodi, go-event-driven-nats, go-react-fintech, x5)
- fish-bullets-bank #16 (#go-runtime #performance #concurrency #memory) - 4x (go-event-driven-nats, amocrm, willix, x5)
- fish-bullets-bank #3 (#networking #reliability #observability #incident-response) - 3x (pinobyte, go-event-driven-nats, x5)
- fish-bullets-bank #15 (#ddd #clean-architecture #solid #architecture) - 3x (go-event-driven-nats, go-react-fintech, x5)
- fish-bullets-bank #18 (#testing #quality #ci-cd #databases) - 3x (go-react-fintech, willix, x5)
- fish-bullets-bank #19 (#go-ecosystem #api #tooling #crm #saas) - 3x (amocrm, willix, x5)
- fish-bullets-bank #20 (#databases #performance #profiling #observability) - 3x (amocrm, willix, x5)
- fish-bullets-bank #21 (#leadership #ownership #mentoring #architecture) - 3x (amocrm, willix, x5)
- fish-bullets-bank #23 (#python #php #nodejs #fullstack #devops) - 3x (amocrm, willix, x5)
- fish-bullets-bank #5 (#sdk #tooling #nodejs #saas) - 2x (pinobyte, nodi)
- fish-bullets-bank #8 (#graphql #api #frontend #performance) - 2x (nodi, go-react-fintech)
- fish-bullets-bank #14 (#saga #outbox #distributed-transactions #payments) - 2x (go-event-driven-nats, go-react-fintech)
- fish-bullets-bank #22 (#ai #llm #tooling #quality) - 2x (amocrm, willix)
- fish-bullets-bank #24 (#teamwork #process #leadership #avg-product) - 2x (willix, x5)
- patterns #2 (#nodejs #migrations #architecture) - 2x (pinobyte, nodi)
- patterns #6 (#ai #llm #tooling #quality #saas) - 2x (amocrm, willix)
- patterns #7 (#databases #performance #profiling #observability) - 2x (amocrm, x5)
- patterns #8 (#teamwork #process #leadership #ownership #mentoring) - 2x (willix, x5)
- fish-bullets-bank #1 (#security #architecture #identity #b2b #bigtech #enterprise) - 1x (netbox)
- fish-bullets-bank #2 (#networking #proxy #performance #concurrency #network-infra) - 1x (pinobyte)
- fish-bullets-bank #4 (#networking #proxy #ecommerce #marketplace #proxy-network) - 1x (pinobyte)
- fish-bullets-bank #9 (#htmx #frontend #fullstack #internal-tools) - 1x (nodi)
- fish-bullets-bank #10 (#ai #llm #api #integration) - 1x (nodi)
- fish-bullets-bank #12 (#messaging #event-driven #nats #reliability) - 1x (go-event-driven-nats)
- fish-bullets-bank #13 (#event-sourcing #cqrs #architecture #databases) - 1x (go-event-driven-nats)
- fish-bullets-bank #17 (#fintech #payments #databases #billing) - 1x (go-react-fintech)
- fish-bullets-bank #25 (#ai #llm #tooling #testing #quality) - 1x (willix)
- fish-bullets-bank #26 (#communication #teamwork #process #microservices #enterprise) - 1x (x5)
- fish-bullets-bank #27 (#functional-scope #microservices #api #testing #ci-cd #devops) - 1x (x5-ref-from-sasha)
- patterns #1 (#network-infra #proxy-network #data-platform #networking) - 1x (pinobyte)
- patterns #3 (#graphql #htmx #frontend #fullstack) - 1x (nodi)
- patterns #4 (#event-driven #nats #cqrs #saga #reliability) - 1x (go-event-driven-nats)
- patterns #5 (#fintech #payments #billing #saga #reliability) - 1x (go-react-fintech)
- patterns #9 (#highload #performance #concurrency #microservices #scalability) - 1x (x5)

## Заметки
- 2026-09-30 - репо разделено на направления hh / hirify / linkedin, рыба у каждого своя (стартовала с общих b1-b27, p1-p9). Единственная константа в резюме - стек Go/JS; годы, компании, должности - переменные под гипотезу. Пункты ниже про «досочинять работодателей запрещено» устарели.
- Формат резюме с детальным функционалом (запрос пользователя 2026-09-29, bank #27): под каждым
  местом работы идут три блока - "Команда:" (реальные цифры из bank #24), "Функционал:" на 7-8
  повседневных задач и "Ключевые результаты:" с цифрами из bullets-bank, плюс "ИИ в работе:" с
  разбивкой по проектам (Carprice/Nedra - Copilot и чат-модели, Syndicate - Claude Code, агенты
  на тестах и обвязке). Эталон - resume-templates/generated/x5-ref-from-sasha-resume.txt.
- Сильные оси сейчас: highload-микросервисы и масштабирование (#highload, #concurrency,
  #scalability, паттерн #9), финтех/платежи (#fintech, #payments, паттерн #5), событийная
  архитектура (#event-driven, #nats, #cqrs, #saga, паттерн #4), сетевая инфраструктура/прокси
  (#network-infra, #proxy-network), фуллстек-вертикаль Go (#graphql + #htmx, паттерн #3),
  производительность данных и профилирование (#databases, #performance, #profiling, паттерн #7),
  работа с LLM в продукте и агентная разработка (#ai, #llm, паттерн #6), состав команд и
  процесс/ownership направления (#teamwork, #process, #communication, паттерн #8).
- ЯЗЫКИ, КОТОРЫХ ПОЛЬЗОВАТЕЛЬ НЕ ЗНАЕТ: Java/Spring (сказано прямо 2026-09-29) - не добавлять
  ни в резюме, ни в ответы, даже если вакансия требует. Заходить через Go-ветку требования.
- Досочинённый полиглот-бэкграунд (bank #23): Python (скрипты, pandas, автоматизация деплоя),
  PHP + MySQL в начале карьеры, Node.js Express/NestJS - всё без привязки к нанимателю,
  как "фуллстек/девопс-период до го". Держать формулировки согласованными между прогонами.
- Устойчивые привязки досочинённого опыта (держать во всех версиях резюме):
  NATS JetStream, event sourcing/CQRS, GraphQL+React/TS, MongoDB под сырые полуструктурированные
  payload-ы (агрегаты в ClickHouse) - Nedra Digital;
  saga/outbox, финансовая корректность (двойная запись, сверки), DDD/чистая архитектура,
  managed-облако/Terraform - Syndicate Group;
  testcontainers/интеграционные тесты, Node.js Express/NestJS -> Go - Carprice;
  chi/pgx/goose и набор библиотек, инструменты профилирования БД - без привязки, общий стек;
  ownership направления с нуля + менторство - Nedra Digital (телеметрия), практики ревью - Carprice.
  ВНИМАНИЕ: в nodi-resume MongoDB был привязан к Syndicate, в go-event-driven-nats и x5 - к
  Nedra. Каноничная привязка - Nedra Digital, старые версии не переписываем, новые делаем так.
- СОСТАВ КОМАНД - РЕАЛЬНЫЕ ДАННЫЕ от пользователя (2026-09-29), не досочинять и не менять:
  Syndicate Group - одна команда 7 человек на два проекта (руководитель, 3 бэкенда, 1 фронт,
  мануальный QA, бизнес-аналитик), выделенного девопса нет;
  Nedra Digital - три проекта: первый 10 месяцев соло-разработчиком (команда 9 человек),
  второй - 12 человек (3 бэкенда, 2 фронта), третий - 18 человек (6 бэкендов, 5 фронтов,
  автотестировщики, дизайнеры); Carprice - один проект, 10 человек (3 бэкенда, 3 фронта,
  бизнес/системный аналитик, 2 автотестировщика, дизайнер), бэкенд смешанный го/Node.js.
  Дубль - в fish-bullets-bank #24. С прогона x5 состав команд идёт прямо в резюме отдельной
  строкой "Команда:" под каждым местом работы - формат прижился, держать его в новых версиях.
- Хронология ИИ-инструментов (зафиксировано в willix-прогоне): Carprice 2021-2023 - ИИ нет;
  Nedra Digital 2023-2025 - GitHub Copilot + ChatGPT (автодополнение, разбор схем ClickHouse,
  тестовые данные); Syndicate Group 2026 - Claude Code, мультиагентный пайплайн ревью,
  написание тестов агентом, бойлерплейт, черновики миграций, свои скиллы.
- Постоянный пробел: трудовая история в actual-template-resume.txt начинается с июл 2021,
  поэтому требования "5+/6+/7+ лет" закрываются впритык или не закрываются вовсе - помогает
  только упоминание фуллстек/девопс-периода до Go без привязки к нанимателю. Досочинять
  работодателей запрещено. Всплывало уже трижды (nodi, go-react-fintech, x5).
- В actual-template-resume.txt в буллете Carprice остался технический артефакт:
  "Implemented authentication ... - только если реально делал, указать как именно".
  В генерируемых версиях вычищается, но стоит поправить и в оригинале.
