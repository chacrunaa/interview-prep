# nodi

| | |
|---|---|
| Компания | Nodi |
| Роль | Senior Full Stack Engineer (Go + HTMX) |
| Источник | Hirify, `1154961`, отклик залогирован вручную (tracker:373017) |
| Гипотеза | ? - не записывалась |
| Подготовлено | 2026-09-29 |
| Отправлено | 2026-09-29 |
| Стадия | отклик |
| Дальше | **вероятный тупик:** вакансия только для Латинской Америки, см. «Блокер» ниже |

## Файлы

- [cv-en.txt](cv-en.txt)

## Блокер

Текст вакансии подтянут прогоном `scan` 2026-09-30 - через полтора дня после отклика. В нём обнаружилось то, чего не было в рекомендациях Hirify, по которым собиралось резюме:

- **удалёнка только внутри Колумбии, Коста-Рики, Перу или Бразилии** (`macroregion: latam`, города Богота, Медельин, Лима, Сан-Паулу);
- 6+ лет опыта - тот же пробел, что фиксировался при подготовке;
- Azure «strongly preferred», а в резюме закрывалось абстрактным managed-облаком (b11);
- Templ, Alpine.js, Tailwind рядом с HTMX - в рыбе (b9) только html/template + HTMX.

Локация - жёсткое требование, снять его рыбой нельзя. Если ответа нет - переводи в `тишина`.

## Вакансия

Источник: https://hirify.me/jobs/1154961-senior-fullstack-go-htmx
Локация: удалённо внутри Колумбии, Коста-Рики, Перу или Бразилии. Вилка: USD 3400-5100 в месяц. Язык: en, английский B2.

Company: Nodi develops software solutions involving cloud technologies, modern engineering practices, and AI-enabled applications.

What you will do:
- Design, build, test, and maintain scalable production applications and backend services in Go.
- Develop REST and GraphQL APIs, including schemas, queries, mutations, and resolvers.
- Design MongoDB data models and queries with attention to performance, scalability, and maintainability.
- Build server-rendered interfaces with HTMX and Templ, using Tailwind CSS and Alpine.js for responsive and accessible experiences.
- Apply testing, code reviews, debugging, CI/CD, Docker, and cloud deployment practices across the software lifecycle.
- Integrate AI capabilities into enterprise applications and apply AI-assisted development practices for coding, testing, documentation, and troubleshooting.

Requirements:
- 6+ years of software development experience with strong hands-on expertise in Go.
- Experience designing REST and GraphQL APIs, MongoDB schemas and queries, and server-driven UIs with HTMX.
- Experience with Templ, Alpine.js, Tailwind CSS, automated testing, Docker, CI/CD, code reviews, and debugging.
- Hands-on experience deploying and supporting cloud applications with Azure, AWS, or GCP; Azure experience is strongly preferred.
- Knowledge of AI-assisted development, large language models, prompt engineering, retrieval-augmented generation, AI governance, and responsible AI.
- Strong problem-solving, communication, and collaboration skills in Agile, cross-functional product teams.

Nice to have:
- Experience with GitHub Copilot, Claude, ChatGPT, or comparable AI-enabled engineering tools.
- Experience with agentic AI patterns, distributed systems, and event-driven architectures.
- Experience optimizing Go applications for latency, throughput, scalability, and resilience.
- Familiarity with production DevOps and observability practices.

## Разбор

Источник: `resume-templates/recomendation-match.txt` (рекомендации Hirify от 2026-09-29 04:06).
Текста самой вакансии на момент прогона не было: `vacancies/hh/for-scan-vacancy.txt` всё ещё
содержал Pinobyte. Оси определены по TL;DR из рекомендаций - при появлении полного текста
вакансии профиль стоит уточнить.
Обработано: 2026-09-29 (`sync-resume`)

Роль: Senior Full Stack Engineer (Go + HTMX). Backend-сервисы и API, server-rendered
интерфейсы, производительные модели данных, встраивание AI-возможностей, оптимизация
распределённых приложений, поддержка продакшена через CI/CD и observability.

- Домен: не определён по рекомендациям (`unspecified`); по стеку - продуктовая разработка с AI-функциональностью `#ai`
- Тип бизнеса: `#b2b` (предположительно, по формату "scalable backend services + internal/product UI")
- Тип системы: `#saas` `#internal-tools`
- Тип компании: `#startup-growth` / `#avg-product` (сеньорная роль с полной вертикалью от БД до UI)

### Закрыто резюме как есть

- Go, микросервисы, распределённые системы, конкурентность - все три компании
- Производительные модели данных - редизайн схем и контрактов (Syndicate), ClickHouse
  (партиционирование, materialized views, кодеки), PostgreSQL (N+1, батчинг, keyset-пагинация)
- Оптимизация распределённых приложений - circuit breaker, бэкофф, rate limiting на 14 сервисах,
  миграция на gRPC/Protobuf
- Поддержка продакшена: CI/CD - GitLab CI, линтинг миграций, pre-push хуки;
  observability - Prometheus, Grafana, OpenTelemetry (трейсы + метрики через OTLP)
- Тестирование - unit и интеграционные тесты, покрытие критичной логики 0% -> 95%

### Незакрытые требования и чем закрыты

- **GraphQL** - прямо назван в рекомендациях как причина возможного отсева. Закрыто
  fish-bullet #8: GraphQL-схема на gqlgen для аналитических дашбордов, dataloader против N+1,
  subscriptions на живые показатели. В резюме привязано к Nedra Digital вместе с фронтендом
  (React + TypeScript + Apollo Client, типы генерируются из схемы) - по прямому указанию
  пользователя 2026-09-29.
- **HTMX / server-rendered UI** - второй названный пробел. Закрыто fish-bullet #9:
  внутренние админки на html/template + HTMX (hx-get/hx-post с HTML-фрагментами, hx-trigger
  на поллинг долгих операций, hx-swap). В резюме привязано к Syndicate Group (внутренние
  платформы - естественное место для админок).
- **MongoDB** - закрыто переиспользованием fish-bullet #6 (сырые payload-ы в MongoDB,
  агрегаты в ClickHouse), уже заведён на прогоне pinobyte.
- **Встраивание AI-возможностей в продукт** - закрыто fish-bullet #10: вызовы LLM за отдельным
  интерфейсом, очередь с ретраями, валидация ответов по схеме, кэш по хэшу промпта, стриминг,
  лимиты по токенам и стоимости. Плюс уже реальный раздел AI-assisted engineering (Claude Code,
  мульти-агентный review-пайплайн) - он остаётся в резюме как есть.
- **Cloud technologies** - в резюме были только Docker/K8s/GitLab CI без облака.
  Закрыто fish-bullet #11: managed-Kubernetes, S3, managed Mongo/Postgres, секреты провайдера,
  Terraform, автоскейлинг воркеров по глубине очереди.
- **Node.js** (в стеке роли как full stack) - переиспользованы fish-bullets #5 и #7
  (npm-обёртка над Go-SDK; миграция Express/NestJS -> Go на Carprice).

### Не закрыто сознательно

- **6+ лет опыта.** В `actual-template-resume.txt` трудовая история начинается с июл 2021
  (Carprice), это ~5 лет 2 месяца. Дотянуть до 6+ можно только добавив более раннего
  работодателя - это запрещено жёстким ограничением скилла (проверяемый факт, риск на
  бэкграунд-чеке). В резюме вместо этого усилена вертикаль опыта: "5+ лет коммерческого Go
  поверх фуллстек-работы на Node.js/JS, откуда я в Go и пришёл". Если в HH/профиле есть
  места работы до 2021 года - добавь их в `actual-template-resume.txt`, и пробел закроется
  сам собой на следующем прогоне.

## Рыба, ушедшая сюда

- 2026-09-29 | nodi | sync-resume | domain=unspecified,#ai business=#b2b system=#saas,#internal-tools company=#startup-growth,#avg-product | fish: +4 new (bank #8-#11), 3 reused (bank #5, #6, #7) | pattern: +1 new (#3 from bank #8, #9), 1 reused (#2) | files: vacancies/hh/nodi-profile.md, resume-templates/generated/nodi-resume.txt (en) | прим.: вакансия текстом не приходила, работал по recomendation-match.txt (Hirify); GraphQL+фронтенд привязан к Nedra Digital по указанию пользователя; требование 6+ лет опыта не закрыто (нет работодателей до 2021 в actual-template-resume.txt)

## История

- 2026-09-29 - подготовлено
- 2026-09-29 - отклик залогирован в трекере Hirify (tracker:373017, стадия Applied)
- 2026-09-30 - прогон `scan`: стадия проставлена по `applications.list`, подтянут исходный текст вакансии, найден блокер по локации (только LATAM)
