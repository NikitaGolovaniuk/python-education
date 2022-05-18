-- Задание 1
-- Вывести:
-- 1. всех юзеров,
-- 2. все продукты,
-- 3. все статусы заказов

SELECT user_id, first_name, last_name, middle_name
from users;

SELECT product_id, product_tittle, product_description
from products;

SELECT order_id, order_status_order_status_id
from orders;

-- Задание 2
-- Вывести заказы, которые успешно доставлены и оплачены

SELECT *
from orders
WHERE order_status_order_status_id = 4;

-- Задание 3
-- Вывести:
-- (если задание можно решить несколькими способами, указывай все)
-- 1. Продукты, цена которых больше 80.00 и меньше или равно 150.00
-- 2. заказы совершенные после 01.10.2020 (поле created_at)
-- 3. заказы полученные за первое полугодие 2020 года
-- 4. подукты следующих категорий Category 7, Category 11, Category 18
-- 5. незавершенные заказы по состоянию на 31.12.2020
-- 6.Вывести все корзины, которые были созданы, но заказ так и не был оформлен.

SELECT * from products WHERE price>80 and price<=150;
SELECT * from products WHERE price between 80.01 and 150.00;

SELECT * from orders WHERE created_at > '2020.01.10';

SELECT *
from orders
WHERE created_at between '2020-01-01' and '2020-07-01';

SELECT *
from products
WHERE category_id=7 or category_id=11 or category_id=18;

SELECT *
from orders
WHERE created_at<'2020-12-31' and order_status_order_status_id between 1 and 3;

SELECT carts_id, carts_cart_id_id
from carts, orders
WHERE order_status_order_status_id=1;

-- Задание 4
-- Вывести:
-- 1. среднюю сумму всех завершенных сделок
-- 2. вывести максимальную сумму сделки за 3 квартал 2020

SELECT AVG(orders.total) as amount
from orders WHERE orders.order_status_order_status_id=4;

SELECT MAX(orders.total) as maximum
from orders WHERE orders.order_status_order_status_id=4 and orders.created_at between '2020-06-01' and '2020-09-01';

