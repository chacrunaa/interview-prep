# pinobyte

| | |
|---|---|
| Компания | Pinobyte |
| Роль | Go Backend Engineer, proxy infrastructure |
| Источник | hh |
| Подготовлено | 2026-09-29 |
| Отправлено | ? |
| Стадия | ? |
| Дальше | ? |

## Файлы

- [cv-en.txt](cv-en.txt)
- [cv-ru.txt](cv-ru.txt)

## Вакансия

_Исходный текст не сохранился (до переезда `for-scan-vacancy.txt` перезаписывался)._

## Разбор

Источник: `vacancies/hh/for-scan-vacancy.txt` (Pinobyte, Go Backend Engineer, proxy infrastructure)
Обработано: 2026-09-29 (`sync-resume`)

- Домен: `#network-infra` (своя proxy/egress-инфраструктура) + домены источников данных: `#ecommerce` (marketplaces), `#proptech` (real estate), `#social`
- Тип бизнеса: `#b2b` (кастомные решения по извлечению данных для заказчиков)
- Тип системы: `#data-platform` `#proxy-network`
- Тип компании: `#bootstrapped` `#startup-early` (основатели ведут компанию сами, небольшая сеньорная команда, быстрая доставка)

### Что реально ищут

Go-бэкенд под сетевой слой: proxy-протоколы, маршрутизация, обработка соединений,
распределённые микросервисы под большой трафик, разбор сетевых/распределённых инцидентов
в продакшене. Стек почти полностью совпадает с резюме (Go, gRPC, ClickHouse, Redis, Kafka,
Docker/K8s, Prometheus/Grafana) - кроме MongoDB и собственно networking.

### Закрыто резюме как есть

- Go, микросервисы, конкурентность - `bullets-bank.md` (все три компании)
- gRPC/Protobuf, снижение трафика и задержек на плохих каналах - Nedra Digital
- Большой трафик и высокая нагрузка - телеметрия до 30K измерений/сек, 100% полнота данных
- Отказоустойчивость - circuit breaker, exponential backoff, rate limiting на 14 микросервисах
- Производительность - ClickHouse (p95 с секунд до ~200 мс), PostgreSQL (N+1, keyset-пагинация)
- Observability - Prometheus/Grafana/OpenTelemetry, метрики latency/RPS/очередей
- Docker, Kubernetes, GitLab CI/CD, Redis, Kafka
- Архитектурные решения и интеграции между сервисами - dependency inversion, распил монолита

### Незакрытые требования (взято из рекомендаций Hirify + свой разбор)

- **Компьютерные сети и proxy-системы** - главный пробел, прямо назван в `recomendation-match.txt`.
  В резюме нет ни proxy-протоколов (HTTP CONNECT, SOCKS5), ни работы с соединениями/таймаутами,
  ни TLS/DNS/NAT-conntrack. Закрыто fish-bullets #2, #3, #4 + pattern #1.
- **Эксплуатация масштабной proxy/VPN/сетевой инфраструктуры** - закрыто fish-bullets #2, #4.
- **Отладка распределённых/сетевых инцидентов в продакшене** - в резюме видна только
  отказоустойчивость и метрики, без сетевой специфики. Закрыто fish-bullet #3.
- **MongoDB** - в стеке вакансии есть, в резюме нет. Закрыто fish-bullet #6.
- **SDK: разработка, упаковка, распространение** (плюс) - закрыто fish-bullet #5.
- **Node.js** (плюс) - закрыто fish-bullet #5 (тонкая обёртка над Go-SDK в npm).
- **Rust** (плюс) - прямого опыта нет и не досочиняю как продакшен: в резюме идёт уровнем
  чтения/правок, чтобы не подставляться на техинтервью.
- **Высокопроизводительные сетевые приложения** (плюс) - частично закрыто #2 (пул соединений,
  таймауты по фазам, pprof).

## Рыба, ушедшая сюда

- 2026-09-29 | pinobyte | sync-resume | domain=#network-infra,#ecommerce,#proptech,#social business=#b2b system=#data-platform,#proxy-network company=#bootstrapped,#startup-early | fish: +6 new (bank #2-#7), 0 reused | pattern: +2 new (#1 from bank #2,#3,#4; #2 from bank #5,#7) | files: vacancies/hh/pinobyte-profile.md, resume-templates/generated/pinobyte-resume.txt (ru), resume-templates/generated/pinobyte-en-resume.txt (en)

## История

- 2026-09-29 - подготовлено
