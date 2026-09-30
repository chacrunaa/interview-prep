# go-event-driven-nats - профиль вакансии

Источник: `vacancies/hh/for-scan-vacancy.txt` (текст на английском, компания не названа).
Обработано: 2026-09-29 (`sync-resume`)

Роль: Software Engineer (Go). Высоконагруженные отказоустойчивые бэкенд-сервисы с акцентом на
событийную архитектуру, асинхронное взаимодействие сервисов и оптимизацию производительности.
Стек из TL;DR: Go-микросервисы на NATS JetStream, REST/gRPC, распределённые данные,
observability, облачная инфраструктура.

- Домен: не назван (`unspecified`) - вакансия описана только через стек и тип системы
- Тип бизнеса: `#b2b` (предположительно; продуктовая инженерная роль без признаков b2c)
- Тип системы: `#saas` `#data-platform` (распределённые данные + событийная шина)
- Тип компании: `#scaleup` (сеньорная роль, микросервисы, NATS JetStream как осознанный выбор
  вместо Kafka - типично для растущего продукта, а не для энтерпрайза)

## Закрыто резюме как есть

- Go 5+ лет коммерческой разработки (требование "5+ лет разработки, 3+ года Go" закрыто с запасом)
- Проектирование и поддержка микросервисов - 14 сервисов на Nedra, продуктовые сервисы на Carprice
- REST + gRPC/Protobuf - миграция межсервисного обмена с JSON/REST на gRPC/Protobuf
- High-load и fault tolerance - 30K измерений/сек, store-and-forward, circuit breaker,
  exponential backoff, rate limiting, идемпотентность
- PostgreSQL: схемы, индексы, транзакции, оптимизация - редизайн схем, N+1, keyset-пагинация,
  p95 1-2 c -> 300-500 мс, линтинг миграций
- Redis - кэш платных внешних API, есть в стеке всех трёх мест
- Kafka / RabbitMQ - асинхронная обработка фото на Carprice, брокеры на Nedra и Syndicate
- Docker, Kubernetes, CI/CD (GitLab CI)
- Git, культура code review - внедрял code review и тесты, покрытие критичной логики 0% -> 95%
- Observability (из TL;DR) - Prometheus, Grafana, OpenTelemetry (трейсы + метрики, OTLP)

## Незакрытые требования и чем закрыты

- **NATS JetStream** - назван в TL;DR как основной брокер, в резюме отсутствовал полностью.
  Закрыто fish-bullet #12 (durable consumers, at-least-once + дедупликация по Nats-Msg-Id,
  ack/redelivery, backpressure через MaxAckPending, retention-политики). Привязано к Nedra
  Digital: телеметрия с удалённых объектов - естественное место для стримов.
- **Event-Driven Development: event sourcing, CQRS, pub/sub, saga** - ни одного из терминов
  в резюме не было. Закрыто двумя записями: fish-bullet #13 (событийный лог как источник
  истины + проекции в read-модели, реплей - привязано к Nedra) и fish-bullet #14 (saga с
  компенсирующими шагами + transactional outbox + идемпотентные консьюмеры - привязано к
  платёжному домену Syndicate, где уже есть реальный буллет про idempotency key).
- **SOLID, DDD, Clean Architecture** - фактически эта работа в резюме есть (инверсия
  зависимостей, разделение бизнес-логики и инфраструктуры), но названа не теми словами.
  Закрыто fish-bullet #15: bounded contexts, слои domain/application/infrastructure,
  порты и адаптеры. Привязано к Syndicate.
- **Memory model, GC, escape analysis, generics** - требование про глубину языка, в резюме
  никак не отражалось. Закрыто fish-bullet #16: escape analysis и сокращение аллокаций на
  горячем пути, GOGC/GOMEMLIMIT, sync.Pool, pprof/runtime trace, дженерики в общих пакетах.
  Привязано к ingestion-сервису Nedra.
- **NoSQL (MongoDB)** - переиспользован fish-bullet #6 (сырые payload-ы в MongoDB, агрегаты
  в ClickHouse), заведён на прогоне pinobyte. Привязано к Nedra.
- **Cloud infrastructure** (из TL;DR) - переиспользован fish-bullet #11 (managed K8s, S3,
  managed PostgreSQL/MongoDB, секреты провайдера, Terraform, автоскейлинг по глубине очереди).
  Привязано к Syndicate.
- **Классы ошибок / разбор инцидентов** - переиспользован fish-bullet #3, влит в буллет про
  observability на Nedra (RED-метрики в разрезе потребителя, классификация ошибок).

## Не закрыто сознательно

- **MySQL** - вакансия допускает "PostgreSQL/MySQL", PostgreSQL закрыт полностью и с цифрами.
  Дописывать MySQL ради ключевого слова смысла нет: выгода нулевая, а на собеседовании спросят.
- **GitHub Actions** - в резюме GitLab CI, вакансия явно пишет "or equivalents". Не трогал.
