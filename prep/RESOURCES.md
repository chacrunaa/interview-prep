# Resources

## Knowledge
- [PostgreSQL Tutorial — Joins Between Tables](https://www.postgresql.org/docs/current/tutorial-join.html) - официальный туториал с примерами INNER/LEFT/self-join на реальных таблицах. Use for: когда нужен канонiчный источник синтаксиса и поведения JOIN, а не пересказ.
- [PostgreSQL Docs — Table Expressions (JOIN syntax reference)](https://www.postgresql.org/docs/current/queries-table-expressions.html) - формальный справочник по всем видам JOIN, включая CROSS и условия ON/USING. Use for: точные формулировки, если нужно процитировать определение на собесе.

- [Wikipedia — Database normalization](https://en.wikipedia.org/wiki/Database_normalization) - канонические определения 1NF-BCNF с edge-case примерами. Use for: когда нужна формальная формулировка нормальной формы, а не пересказ.

- [PostgreSQL Docs — Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html) - официальное описание уровней изоляции, поведения Read Committed при конкурентном UPDATE и ошибок сериализации. Use for: сверка, что именно происходит в PostgreSQL, а не в общем учебнике.
- [PostgreSQL Docs — Serialization Failure Handling](https://www.postgresql.org/docs/current/mvcc-serialization-failure-handling.html) - какие коды (40001, 40P01) означают «повтори транзакцию» и почему повторять надо всю транзакцию вместе с логикой решения. Use for: вопросы про retry транзакций и отличие ошибки сериализации от конфликта версии.
- [PgBouncer — Features](https://www.pgbouncer.org/features.html) - режимы session/transaction/statement и таблица, какие возможности PostgreSQL работают в каждом. Use for: что ломается в transaction pooling.
- [PgBouncer — Configuration](https://www.pgbouncer.org/config.html) - pool_mode, max_prepared_statements (1.21+). Use for: точные имена параметров.
- [pgx — QueryExecMode](https://pkg.go.dev/github.com/jackc/pgx/v5#QueryExecMode) - режимы выполнения запросов и кэш prepared statements. Use for: pgx за PgBouncer.
- [PostgreSQL Docs — MVCC Introduction](https://www.postgresql.org/docs/current/mvcc-intro.html) - что такое MVCC в PostgreSQL и почему чтение не блокирует запись. Use for: короткое официальное определение.
- [PostgreSQL Docs — System Columns](https://www.postgresql.org/docs/current/ddl-system-columns.html) - xmin, xmax, ctid. Use for: показать версии строк руками.
- [PostgreSQL Docs — Routine Vacuuming](https://www.postgresql.org/docs/current/routine-vacuuming.html) - VACUUM, autovacuum, VACUUM FULL, wraparound. Use for: вопросы про bloat и долгие транзакции.
- [PostgreSQL Docs — Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) - чтение плана: узлы JOIN, rows, loops, Batches, EXPLAIN ANALYZE и BUFFERS. Use for: как анализировать медленный запрос и JOIN.
- [PostgreSQL Docs — Statistics Used by the Planner](https://www.postgresql.org/docs/current/planner-stats.html) - откуда планировщик берёт оценки строк, ANALYZE, CREATE STATISTICS. Use for: почему выбран не тот алгоритм JOIN.
- [PostgreSQL Docs — Sorting Rows (ORDER BY)](https://www.postgresql.org/docs/current/queries-order.html) - ASC/DESC, NULLS FIRST/LAST, порядок без ORDER BY не гарантирован. Use for: вопросы про сортировку и стабильную пагинацию.

- [PostgreSQL Docs — Explicit Locking](https://www.postgresql.org/docs/current/explicit-locking.html) - режимы блокировки строк (FOR UPDATE / NO KEY UPDATE / SHARE), NOWAIT, SKIP LOCKED, deadlock. Use for: точные формулировки про блокировки в PostgreSQL.
- [PostgreSQL Docs — Returning Data from Modified Rows](https://www.postgresql.org/docs/current/dml-returning.html) - RETURNING у INSERT/UPDATE/DELETE. Use for: когда нужно и атомарно изменить строку, и получить значение в код без отдельного SELECT.

- [Хабр — Что нужно знать об архитектуре ClickHouse](https://habr.com/ru/post/509540/) - разбор устройства ClickHouse, указан как дополнительный материал в банке (`db/column/clickhouse.md`). Use for: когда нужна механика колоночного хранения глубже, чем «хранит по колонкам».
- [highload.today — Колоночные БД](https://highload.today/kolonochnye-bazy-dannykh/) - обзор колоночных баз и их сценариев, тоже из списка банка. Use for: формулировки про OLTP/OLAP на понятном языке.
- [PostgreSQL Docs — Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) - PRIMARY KEY, UNIQUE, FOREIGN KEY, CHECK, синтаксис REFERENCES и режимы ON DELETE / ON UPDATE. Use for: точные формулировки про связи и целостность, когда в банке только список ограничений без деталей.
- [Google SRE Book — Monitoring Distributed Systems](https://sre.google/sre-book/monitoring-distributed-systems/) - четыре золотых сигнала (latency, traffic, errors, saturation), почему важны перцентили, а не среднее. Use for: терминология нагрузки и латентности.
- [Prometheus — функция rate()](https://prometheus.io/docs/prometheus/latest/querying/functions/#rate) - средняя скорость роста счётчика за окно. Use for: как получить RPS из счётчика запросов.
- [PostgreSQL — pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html) - статистика по запросам: calls, total_exec_time, mean_exec_time. Use for: найти, какие запросы суммарно съедают время базы.
- [Prometheus — histograms and summaries](https://prometheus.io/docs/practices/histograms/) - гистограммы, _sum и _count, перцентили. Use for: время ответов по эндпоинтам и доля времени.

## Gaps
- В банке вопросов нет материала про блокировки строк в PostgreSQL (только MySQL в `mysql/concurency.md`), опираемся на официальную документацию.
- Нет официальной документации ClickHouse в ресурсах: про разреженный индекс и гранулы пока опираемся на `db/column/clickhouse.md` и статьи с Хабра. Стоит найти и закрепить страницу из clickhouse.com/docs.
- В банке вопросов нет материала про пулы соединений и PgBouncer (только упоминание в integration/topic_07), опираемся на документацию PgBouncer и pgx.
- В банке вопросов нет разбора RPS/DAU/перцентилей и арифметики нагрузки (только упоминания масштаба в `architecture/topic_07_highload_caching.md`), опираемся на SRE Book, документацию Prometheus и `prep/sd/load-math-questions.md`.
