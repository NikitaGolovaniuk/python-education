-- Задание:
-- Написать 3 представления для таблицы products; для таблиц order_status и order; для таблиц products и category.
-- Создать материализированное представление для "тяжелого" запроса на свое усмотрение.
-- Не забыть сделать запросы для примеров использования и удаления представлений.

--Для products

CREATE VIEW products_v
AS SELECT * FROM products;

DROP VIEW products_v;

SELECT * FROM products_v;

--Для таблиц order_status и order

CREATE VIEW order_status_in_human_language AS
SELECT orders.order_id, os.status_name
FROM orders
JOIN order_status os on orders.order_status_order_status_id = os.order_status_id;

DROP VIEW order_status_in_human_language;

SELECT * FROM order_status_in_human_language;

--Для таблиц products и category

CREATE VIEW products_list_v AS
SELECT products.product_tittle AS product_name,
       c.category_title AS category,
       c.category_description AS description
FROM products JOIN categories c on products.category_id = c.category_id;

DROP VIEW products_list_v;

SELECT * FROM products_list_v;

-- Создать материализированное представление для "тяжелого" запроса на свое усмотрение.

CREATE MATERIALIZED VIEW top_users_v AS
SELECT users.first_name, users.last_name, COUNT(carts.carts_id) as carts_amount
FROM carts LEFT JOIN orders o on carts.carts_id = o.carts_cart_id_id
JOIN users ON carts.users_user_id = users.user_id
WHERE carts.carts_id is null or o.order_status_order_status_id = 5
GROUP BY users.user_id
ORDER BY carts_amount DESC
LIMIT 5;

DROP MATERIALIZED VIEW top_users_v;

SELECT * FROM top_users_v;
