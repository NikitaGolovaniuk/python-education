-- Задание 3
-- Создать 3 представления (1 из них должно быть материализированным и хранить данные от "тяжелого" запроса).

-- Топ 20 городов тратящих больше всего на аренду машин

CREATE MATERIALIZED VIEW most_costly_rents_by_city AS
SELECT c2.name, sum(rent.price) as city_spend
FROM rent
JOIN customer c on rent.customer_id = c.customer_id
JOIN phone p on p.phone_id = c.phone_id
JOIN address a on a.address_id = c.address_id
JOIN flat f on a.flat_id = f.flat_id
JOIN building b on b.building_id = f.building_id
JOIN street s on b.street_id = s.street_id
JOIN city c2 on c2.city_id = s.city_id
GROUP BY c2.name
ORDER BY city_spend DESC
LIMIT 20;

SELECT * FROM most_costly_rents_by_city;
DROP MATERIALIZED VIEW most_costly_rents_by_city;

-- 10 самых дорогих аренд с телефонами vip клиентов.

CREATE VIEW ten_costly_rents AS
SELECT rent.customer_id, rent.price, p.number
FROM rent
JOIN customer c on rent.customer_id = c.customer_id
JOIN phone p on p.phone_id = c.phone_id
ORDER BY rent.price DESC
LIMIT 10;

SELECT * FROM ten_costly_rents;
DROP VIEW ten_costly_rents;

-- Вывести полные адреса всех филиалов

CREATE VIEW show_branches_by_cities AS
SELECT branch.branch_number,
       c.name as city,
       s.name as street,
       b.number as building,
       f.number as flat
FROM branch JOIN address a on a.address_id = branch.address_id
JOIN flat f on a.flat_id = f.flat_id
JOIN building b on b.building_id = f.building_id
JOIN street s on b.street_id = s.street_id
JOIN city c on c.city_id = s.city_id
ORDER BY c.city_id;


SELECT * FROM show_branches_by_cities;
DROP VIEW show_branches_by_cities;
