# andersen-lab-fintech

| | |
|---|---|
| Компания | Andersen Lab |
| Роль | Go Developer (Fintech) - бизнес-банкинг, Казахстан |
| Источник | Hirify, `1071229`, отклик через платформу (hirify:25243) |
| Гипотеза | ? - отклик отправлен до появления режима `scan`, гипотеза не записывалась |
| Подготовлено | ? |
| Отправлено | 2026-09-28 |
| Стадия | отклик |
| Дальше | ждать реакции; в Andersen ушло три отклика, см. [andersen-go](../2026-09-andersen-go/card.md) |

## Файлы

_Резюме и письмо этого отклика в репозитории не сохранились._

## Вакансия

Источник: https://hirify.me/jobs/1071229-go-developer-fintech
Локация: Казахстан (`macroregion: cis`), формат гибридный. Язык вакансии: ru, английский Intermediate+. Грейд в карточке - **middle**. Отклик через платформу доступен напрямую.

Go Developer (Fintech)

Andersen is hiring a Go Developer (Kazakhstan) for a project building a next-generation business banking app with microservices and modern digital features. Andersen - pre-IPO software development company, 19 лет на рынке, работает с North America, Western Europe, Israel, Australia, UAE.

Проект: мобильное приложение бизнес-банкинга нового поколения на микросервисной архитектуре. Новые фичи, интеграция современных технологий, подготовка миграции корпоративных клиентов с легаси-платформы.

Responsibilities:
- Developing and maintaining microservices, including creating new microservices in Go.
- Integrating with external systems, including developing and maintaining APIs.
- Working with databases, including designing and optimizing database schemas.
- Handling containerization and orchestration.
- Ensuring code quality.
- Monitoring and logging.
- Closely collaborating with other developers, testers, and business analysts.
- Performing performance and security testing.
- Maintaining documentation.

Must-haves:
- Experience in commercial Go development for 3+ years, including participation in banking or fintech projects.
- Strong knowledge of the Go standard library: net/http, context, sync, io, encoding/json, protobuf, etc.
- Experience in developing high-load and fault-tolerant services.
- Strong command of profiling and performance optimization tools (pprof, benchmark).
- Understanding and hands-on experience with concurrency: goroutines, channels, sync primitives.
- Experience in building clean architecture and structuring code (DDD, Hexagonal, Layered Architecture).
- Experience in designing and developing REST / gRPC APIs.
- Knowledge of communication protocols and technologies: HTTP/2, WebSockets, Kafka, RabbitMQ, NATS.
- Hands-on experience with microservices architecture.
- Understanding of distributed systems principles: CAP theorem, eventual consistency, idempotency.
- Strong experience with relational and NoSQL databases: PostgreSQL, MySQL, MongoDB, Redis, Cassandra.
- Experience in query optimization, replication, sharding, and transactions.
- Knowledge of ORM frameworks and database migration tools: GORM, sqlx, migrate.
- Hands-on experience with Docker, Kubernetes, and Helm.
- Experience in setting up CI/CD pipelines: GitLab CI, GitHub Actions, Jenkins.
- Experience in implementing logging, monitoring, and alerting: Prometheus, Grafana, ELK, OpenTelemetry.
- Experience with cloud platforms: AWS, GCP, Yandex Cloud, Azure.
- Level of English - from Intermediate+ and above.

## Разбор

Карточка восстановлена прогоном `scan` 2026-09-30 по `applications.list`; текст подтянут через `read_vacancy`.

- Домен: `#fintech` (бизнес-банкинг), тип бизнеса `#b2b`, тип системы `#billing` / `#payment-gateway`, тип компании `#outsource`
- Казахстан, релокация/местное оформление - по канону направления
- Список требований - типичный «всё через запятую» от аутсорс-вендора: закрывается почти целиком, вопрос только в глубине по каждому пункту

### Чем закрывается рыбой

- Стандартная библиотека Go, конкурентность, sync-примитивы - b16, b19
- pprof, бенчмарки, профилирование - b16 (дословно: escape analysis, sync.Pool, GOMEMLIMIT, runtime/trace), b20, p9
- Чистая архитектура, DDD, Hexagonal, Layered - b15 (bounded contexts, слои, интерфейсы репозиториев в домене)
- REST/gRPC API - b27, b19
- Kafka, RabbitMQ, NATS, WebSockets - b12 (NATS JetStream детально), b8 (subscriptions поверх WebSocket), p4
- CAP, eventual consistency, идемпотентность - b14, p4, p5
- PostgreSQL, MongoDB, Redis, оптимизация запросов, транзакции - b6 (Mongo под сырые payload-ы + ClickHouse под агрегаты), b20, p7
- sqlx/migrate, миграции - b19 (pgx без ORM, goose), b27
- Docker, Kubernetes, Helm, CI/CD - b11, b27
- Prometheus, Grafana, ELK, OpenTelemetry - b3, b27
- Облака - b11 (managed-Kubernetes, S3, managed Postgres/Mongo, Terraform)
- High-load, fault-tolerant - p9

### Не закрыто

- Cassandra, sharding, replication - в рыбе нет
- GORM - в рыбе прямо противоположное: b19 говорит «pgx без ORM». Позиция осознанная, при вопросе её надо обосновывать, а не прятать
- Грейд вакансии middle при сеньорном позиционировании - расхождение вниз

## Рыба, ушедшая сюда

- не логировалось: отклик отправлен до появления режима, состав резюме не сохранился

## История

- 2026-09-28 - отклик отправлен через Hirify (hirify:25243)
- 2026-09-30 - карточка восстановлена прогоном `scan`, стадия проставлена по `applications.list`
