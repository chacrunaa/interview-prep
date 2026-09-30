# Resources

## Knowledge
- [PostgreSQL Tutorial — Joins Between Tables](https://www.postgresql.org/docs/current/tutorial-join.html) - официальный туториал с примерами INNER/LEFT/self-join на реальных таблицах. Use for: когда нужен канонiчный источник синтаксиса и поведения JOIN, а не пересказ.
- [PostgreSQL Docs — Table Expressions (JOIN syntax reference)](https://www.postgresql.org/docs/current/queries-table-expressions.html) - формальный справочник по всем видам JOIN, включая CROSS и условия ON/USING. Use for: точные формулировки, если нужно процитировать определение на собесе.

- [Wikipedia — Database normalization](https://en.wikipedia.org/wiki/Database_normalization) - канонические определения 1NF-BCNF с edge-case примерами. Use for: когда нужна формальная формулировка нормальной формы, а не пересказ.

## Gaps
- Нет закреплённого источника по физическим алгоритмам JOIN (Nested Loop/Hash/Merge) с картинками EXPLAIN — пока опираемся только на текстовое описание в topic_03_joins_set_operations.md.
