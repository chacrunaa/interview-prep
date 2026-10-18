-- Стенд к уроку 0014 «Как ускорить JOIN». Страница с заданиями: 0014-join-performance.html
-- Загрузка в psql:  \i /lab/0014-join-performance.sql   (около 30 секунд)
-- Можно запускать повторно: всё пересоздаётся с нуля.

DROP TABLE IF EXISTS order_items, orders, customers, imports, products CASCADE;

-- 100 000 клиентов
CREATE TABLE customers (
    id    int PRIMARY KEY,
    name  text NOT NULL,
    email text NOT NULL
);
INSERT INTO customers
SELECT g, 'Клиент ' || g, 'user' || g || '@mail.test'
FROM generate_series(1, 100000) g;

-- 500 000 заказов: у нечётных клиентов по 10 заказов, у чётных - ни одного.
CREATE TABLE orders (
    id          int PRIMARY KEY,
    customer_id int NOT NULL REFERENCES customers(id),
    amount      int NOT NULL,
    created_at  timestamptz NOT NULL
);
INSERT INTO orders
SELECT g,
       (g % 50000) * 2 + 1,
       (random() * 10000)::int,
       now() - (g || ' minutes')::interval
FROM generate_series(1, 500000) g;
CREATE INDEX orders_customer_id_idx ON orders (customer_id);

-- 2 000 000 позиций, по 4 на заказ.
-- Внешний ключ на orders есть, а ИНДЕКСА на order_id НЕТ - так задумано (шаг 1).
CREATE TABLE order_items (
    id       bigint PRIMARY KEY,
    order_id int NOT NULL REFERENCES orders(id),
    sku      text NOT NULL,
    qty      int NOT NULL
);
INSERT INTO order_items
SELECT g, (g - 1) / 4 + 1, 'SKU-' || (g % 1000), 1 + g % 5
FROM generate_series(1, 2000000) g;

-- Справочник товаров: 1000 строк, индекса по sku нет (шаг 3).
CREATE TABLE products (
    sku   text NOT NULL,
    title text NOT NULL
);
INSERT INTO products
SELECT 'SKU-' || g, 'Товар ' || g FROM generate_series(0, 999) g;

-- Таблица импорта: пока 1000 строк, все со статусом 'done'.
-- Autovacuum выключен, чтобы он не обновил статистику за тебя (шаг 3).
CREATE TABLE imports (
    id     serial PRIMARY KEY,
    sku    text NOT NULL,
    status text NOT NULL
) WITH (autovacuum_enabled = false);
INSERT INTO imports (sku, status)
SELECT 'SKU-' || (g % 1000), 'done' FROM generate_series(1, 1000) g;

VACUUM ANALYZE customers, orders, order_items, products, imports;
