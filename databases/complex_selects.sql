-- Задание 1
-- Создайте новую таблицу potential customers с полями id, email, name, surname, second_name, city
-- Заполните данными таблицу.
-- Выведите имена и электронную почту потенциальных и существующих пользователей из города city 17
begin;
savepoint kek;

DROP TABLE potential_custumers;

create table potential_custumers
(
    id          serial primary key,
    email       VARCHAR(50),
    first_name  VARCHAR(50),
    surname     VARCHAR(50),
    second_name VARCHAR(50),
    city        VARCHAR(50)
);
INSERT INTO potential_custumers (email, first_name, surname, second_name, city)
VALUES ('gchasier0@barnesandnoble.com', 'Gussi', 'Chasier', 'gchasier0', 'city 16'),
       ('gfranzke1@amazon.com', 'Gregorius', 'Franzke', 'gfranzke1', 'city 19'),
       ('cbernli2@google.pl', 'Collette', 'Bernli', 'cbernli2', 'city 17'),
       ('mpears3@smugmug.com', 'Myrtle', 'Pears', 'mpears3', 'city 17'),
       ('ybernot4@stumbleupon.com', 'Ynez', 'Bernot', 'ybernot4', 'city 17'),
       ('hfrow5@opensource.org', 'Howie', 'Frow', 'hfrow5', 'city 17'),
       ('clemarchant6@youtube.com', 'Currie', 'Le Marchant', 'clemarchant6', 'city 17'),
       ('kwinchcombe7@omniture.com', 'Kathi', 'Winchcombe', 'kwinchcombe7', 'city 17'),
       ('mabrehart8@godaddy.com', 'Moyra', 'Abrehart', 'mabrehart8', 'city 19'),
       ('hbrymner9@census.gov', 'Hally', 'Brymner', 'hbrymner9', 'city 19'),
       ('lmcurea@4shared.com', 'Lonnard', 'McUre', 'lmcurea', 'city 19'),
       ('zmilierb@elpais.com', 'Zola', 'Milier', 'zmilierb', 'city 19'),
       ('jturbaynec@live.com', 'Jeremie', 'Turbayne', 'jturbaynec', 'city 19'),
       ('sterringtond@opensource.org', 'Solomon', 'Terrington', 'sterringtond', 'city 19'),
       ('scristofolinie@wikimedia.org', 'Staci', 'Cristofolini', 'scristofolinie', 'city 19'),
       ('bmcbainf@msu.edu', 'Brendan', 'McBain', 'bmcbainf', 'city 19'),
       ('erouseg@sciencedirect.com', 'Emilee', 'Rouse', 'erouseg', 'city 17'),
       ('tjeppersonh@exblog.jp', 'Thorn', 'Jepperson', 'tjeppersonh', 'city 17'),
       ('csetoni@hibu.com', 'Cedric', 'Seton', 'csetoni', 'city 17'),
       ('wfeldmesserj@umn.edu', 'Willyt', 'Feldmesser', 'wfeldmesserj', 'city 17');

SELECT potential_custumers.first_name, potential_custumers.email, users.first_name, users.email
from potential_custumers,
     users
WHERE potential_custumers.city = 'city 17'
   or users.city = 'city 17';
SELECT users.first_name               as real_customers,
       users.email                    as email,
       potential_custumers.first_name as potential_customers,
       potential_custumers.email      as email
FROM potential_custumers
         JOIN users ON potential_custumers.city = 'city 17' and users.city = 'city 17';

-- Задание 2
-- Вывести имена и электронные адреса всех users отсортированных по городам и по имени (по алфавиту)

SELECT users.first_name, users.email
FROM users
ORDER BY users.city, users.first_name;

-- Задание 3
-- Вывести наименование группы товаров, общее количество по группе товаров в порядке убывания количества

SELECT categories.category_title as title,
       SUM(products.in_stock)    as sum
FROM categories,
     products
where products.category_id = categories.category_id
GROUP BY categories.category_title
ORDER BY sum DESC;

-- Задание 4
-- 1. Вывести продукты, которые ни разу не попадали в корзину.

SELECT *
FROM products
WHERE products.product_id NOT IN (SELECT DISTINCT cart_product.products_product_id
                                  FROM cart_product);

-- 2. Вывести все продукты, которые так и не попали ни в 1 заказ. (но в корзину по

SELECT products.product_id, products.product_tittle
FROM products
         LEFT JOIN cart_product cp on products.product_id = cp.products_product_id
WHERE cp.products_product_id is null;

-- 3. Вывести топ 10 продуктов, которые добавляли в корзины чаще всего.

SELECT products.product_id, products.product_tittle, COUNT(product_id) as sum
FROM products
         JOIN cart_product cp on products.product_id = cp.products_product_id
GROUP BY product_id
ORDER BY sum DESC
LIMIT 10;

-- 4. Вывести топ 10 продуктов, которые не только добавляли в корзины, но и оформл

SELECT product_tittle, COUNT(product_id)
FROM cart_product
         JOIN orders ON cart_product.carts_cart_id = orders.carts_cart_id_id and
                        orders.order_status_order_status_id between 1 and 4
         LEFT JOIN products ON products.product_id = cart_product.products_product_id
WHERE products.product_id is not null
GROUP BY product_tittle
ORDER BY count(product_id) DESC
LIMIT 10;

-- 5. Вывести топ 5 юзеров, которые потратили больше всего денег (total в заказе).

SELECT users.first_name as name,
       users.last_name  as surname,
       SUM(o.total)     as total_spent
FROM users
         JOIN carts ON users.user_id = carts.users_user_id
         JOIN orders o on carts.carts_id = o.carts_cart_id_id
GROUP BY users.user_id
ORDER BY total_spent DESC
LIMIT 5;

-- 6. Вывести топ 5 юзеров, которые сделали больше всего заказов (кол-во заказов).

SELECT users.first_name as name,
       users.last_name  as surname,
       COUNT(o.total)   as total_orders
FROM users
         JOIN carts ON users.user_id = carts.users_user_id
         JOIN orders o on carts.carts_id = o.carts_cart_id_id
WHERE o.order_status_order_status_id between 1 and 4
GROUP BY users.user_id
ORDER BY total_orders DESC
LIMIT 5;

-- 7. Вывести топ 5 юзеров, которые создали корзины, но так и не сделали заказы.

SELECT users.first_name, users.last_name, COUNT(carts.carts_id) as carts_amount
FROM carts LEFT JOIN orders o on carts.carts_id = o.carts_cart_id_id
JOIN users ON carts.users_user_id = users.user_id
WHERE carts.carts_id is null or o.order_status_order_status_id = 5
GROUP BY users.user_id
ORDER BY carts_amount DESC
LIMIT 5;

