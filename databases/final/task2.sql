-- Задание 2
-- Придумать 3 различных запроса SELECT с осмысленным использованием разных видов JOIN.
-- Используя explain добавить только необходимые индексы для уменьшения стоимости (cost) запросов.

-- Все пользователи из определенного города

-- только индекс этот существенно влияет
CREATE INDEX city_name_idx ON city(name);
DROP INDEX city_name_idx;
EXPLAIN analyse SELECT customer.name, c.name FROM customer join address a on a.address_id = customer.address_id
    join flat f on a.flat_id = f.flat_id
    join building b on f.building_id = b.building_id
    join street s on b.street_id = s.street_id
    left join city c on c.name = 'city 17' WHERE c.city_id is not null;

-- 10 vip клиентов с телефонами

CREATE INDEX phone_id_idx ON phone(phone_id);
CREATE INDEX rent_customer_id_idx ON rent(customer_id);

SELECT rent.customer_id, rent.price, p.number
FROM rent
JOIN customer c on rent.customer_id = c.customer_id
JOIN phone p on p.phone_id = c.phone_id
LIMIT 10;

-- Топ 10 арендуемых моделей
CREATE INDEX c_car_id_idx ON car(car_id);
CREATE INDEX c_car_id_idx ON rent(car_id);

EXPLAIN ANALYSE SELECT count(rent.car_id) as rate,
       rent.car_id
       FROM rent join car c on c.car_id = rent.car_id
GROUP BY c.car_id, rent.car_id
ORDER BY rate DESC
LIMIT 10;
