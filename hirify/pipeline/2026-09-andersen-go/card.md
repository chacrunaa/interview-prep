# andersen-go

| | |
|---|---|
| Компания | Andersen |
| Роль | Go Developer (страхование / ассистанс, cross-selling платформа) |
| Источник | Hirify, `862825`, отклик через платформу (hirify:25244) |
| Гипотеза | ? - отклик отправлен до появления режима `scan`, гипотеза не записывалась |
| Подготовлено | ? |
| Отправлено | 2026-09-28 |
| Стадия | отклик |
| Дальше | ждать реакции; учитывать, что в Andersen ушло три отклика (см. ниже) |

## Файлы

_Резюме и письмо этого отклика в репозитории не сохранились._

## Вакансия

Источник: https://hirify.me/jobs/862825-go-developer
Локация: Украина, Казахстан, Грузия, Азербайджан (`macroregion: europe`), удалённо. Язык вакансии: ru, требуется английский Upper-Intermediate+. Отклик через платформу доступен напрямую.

Заказчик - международная организация в сфере финансовых и защитных услуг. Проект - глобальная цифровая платформа для индустрии страхования и ассистанса: travel, automotive, health и assistance-сервисы.

Responsibilities:
- Building and evolving a real-time cross-selling platform, working with real-time data flows and business logic for personalized offers within an insurance context.
- Owning the backend powering multiple user-facing apps, advancing our gRPC-based microservice architecture.
- Designing and maintaining REST/gRPC APIs for integration with core insurance platforms and third-party services (risk scoring, KYC, payments).
- Working with PostgreSQL to model and managing transactional data such as policies, claims, and customer records, including audit trails.
- Implementing event-driven workflows using RabbitMQ or Kafka to handle claims events, policy updates, and notifications reliably.
- Writing and maintaining unit and integration tests, with particular attention to logic involving monetary calculations and claims/premium accuracy.
- Instrumenting services with Grafana/Prometheus to monitor critical flows and proactively catch issues before they impact users.
- Actively participating in code reviews.
- Taking a proactive role in all aspects of platform design and development, with a strong emphasis on scalability, availability, and resilience.
- Collaborating closely with Business Analysts, QA, and DevOps within an Agile/Scrum framework.
- Contributing to architectural decisions that balance flexibility for multiple consuming apps with long-term maintainability and fault tolerance.

Must-haves:
- Commercial development experience for 5+ years, including 3+ years working with Go in production environments.
- Higher education in Computer Science (software development, etc.).
- Extensive experience working with AI and the process of implementing/configuring it within a team.
- Experience of working in fintech, banking domains, and working with complex integrations.
- Strong hands-on experience, including concurrency (goroutines, channels). Proven experience designing, developing, and maintaining production-grade microservice architectures using gRPC.
- Experience with containerizing and deploying backend services.
- Strong knowledge of PostgreSQL, including schema design, query optimization, and database migrations.
- Hands-on experience with RabbitMQ or Kafka for event-driven and asynchronous communication.
- Experience designing and implementing REST APIs.
- Practical experience writing unit and integration tests for backend services.
- Experience instrumenting services with Grafana and Prometheus, including metrics collection, monitoring, and alerting.
- Experience designing scalable, highly available systems capable of handling high-throughput, real-time workloads.
- Active participation in code reviews.
- Ownership mindset with end-to-end responsibility for backend components.
- Experience working in Agile/Scrum development environments.
- Strong understanding of fault-tolerant system design, idempotency, SLA considerations, and service reliability.
- Level of English - from Upper-Intermediate and above.

Nice to have:
- Prior experience in insurance or other regulated domains; familiarity with GDPR, PCI DSS; understanding of core insurance concepts (policies, underwriting, claims lifecycle).

## Разбор

Карточка восстановлена прогоном `scan` 2026-09-30 по `applications.list`; текст подтянут через `read_vacancy`. Что уходило в отклик 28.09 - неизвестно.

- Домен: `#fintech` (страхование), тип бизнеса `#b2b2c`, тип системы `#payment-gateway` / `#identity-platform` (KYC), тип компании `#outsource` (аутсорс-вендор, 19 лет, pre-IPO)
- Требование 5+ лет общего и 3+ Go закрывается мастером без натяжки - редкий случай

### Чем закрывается рыбой

- gRPC-микросервисы, контракты, REST - b27, b19 (chi поверх net/http, grpc-go с протобафом), b26 (согласование контрактов между командами, версионирование)
- Денежная корректность, claims/premium accuracy, audit trails - b17 (минорные единицы, decimal, двойная запись, append-only журнал, ежедневная сверка), p5
- Event-driven на RabbitMQ/Kafka, надёжная доставка событий - b12, b14 (outbox, идемпотентность), p4
- Идемпотентность, SLA, fault tolerance - b14, p5, p9
- PostgreSQL: схемы, оптимизация запросов, миграции - b20, b27
- Grafana/Prometheus, алерты - b3
- Unit + integration тесты - b18
- Опыт внедрения ИИ в команде (must-have!) - b22, b25, p6 - плюс реальный раздел AI-assisted engineering
- Scalability, availability, high-throughput real-time - p9

### Не закрыто

- Страховой домен как таковой: policies, underwriting, claims lifecycle - идёт через финтех-ветку (b17, p5), прямой страховой рыбы нет
- GDPR / PCI DSS - в рыбе нет

## Пересечение

В Andersen на 2026-09-30 ушло три отклика:
- `862825` Go Developer (эта карточка), hirify:25244, 28.09
- `1071229` Go Developer (Fintech) под брендом Andersen Lab, hirify:25243, 28.09 - [2026-09-andersen-lab-fintech](../2026-09-andersen-lab-fintech/card.md)
- `1183150` Go Developer (Fintech), Worldwide, EUR 3400-5200 - в шортлисте `scan.md`, не отправлено

Вакансии `862825` и `1183150` - почти дословно один и тот же текст проекта (real-time cross-selling, страхование, gRPC, KYC/payments). То есть это одна роль, выставленная дважды.

## Рыба, ушедшая сюда

- не логировалось: отклик отправлен до появления режима, состав резюме не сохранился

## История

- 2026-09-28 - отклик отправлен через Hirify (hirify:25244)
- 2026-09-30 - карточка восстановлена прогоном `scan`, стадия проставлена по `applications.list`, найдено пересечение по компании
