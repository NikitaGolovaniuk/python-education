-- Задание:
-- Придумать 3 сложных запроса с использованием 2 и более таблиц, которые можно оптимизировать с помощью индекса (проверять стоит ли оптимизировать запрос оператором explain) и оптимизировать их
-- используя индекс. Результат проверять также операторами explain, analyze. Желательно в финальный SQL-файл вставить вывод планировщика в виде комментариев.
--
-- Все запросы включить в итоговый SQL-файл.

SET enable_indexscan TO ON;
SET enable_seqscan TO OFF;

begin;
savepoint SP1;

CREATE INDEX orders_carts_cart_id_id_idx ON orders(carts_cart_id_id);
CREATE INDEX carts_users_user_id_idx ON carts(users_user_id);

DROP INDEX IF EXISTS orders_carts_cart_id_id_idx;
DROP INDEX IF EXISTS carts_users_user_id_idx;

EXPLAIN ANALYSE
SELECT *
FROM users
         JOIN carts c on users.user_id = c.users_user_id
         JOIN orders o on c.carts_id = o.carts_cart_id_id;

ROLLBACK TO SAVEPOINT SP1;
COMMIT;
END;

-- Default

-- Hash Join  (cost=10000000296.06..10000000331.94 rows=1500 width=216) (actual time=133.589..133.999 rows=1500 loops=1)
--   Hash Cond: (c.users_user_id = users.user_id)
--   ->  Hash Join  (cost=10000000105.28..10000000137.23 rows=1500 width=67) (actual time=0.304..0.519 rows=1500 loops=1)
--         Hash Cond: (o.carts_cart_id_id = c.carts_id)
--         ->  Seq Scan on orders o  (cost=10000000000.00..10000000028.00 rows=1500 width=39) (actual time=0.006..0.063 rows=1500 loops=1)
--         ->  Hash  (cost=80.28..80.28 rows=2000 width=28) (actual time=0.289..0.290 rows=2000 loops=1)
--               Buckets: 2048  Batches: 1  Memory Usage: 141kB
--               ->  Index Scan using carts_carts_id_idx on carts c  (cost=0.28..80.28 rows=2000 width=28) (actual time=0.011..0.185 rows=2000 loops=1)
--   ->  Hash  (cost=153.28..153.28 rows=3000 width=149) (actual time=133.254..133.254 rows=3000 loops=1)
--         Buckets: 4096  Batches: 1  Memory Usage: 510kB
--         ->  Index Scan using users_user_id_idx on users  (cost=0.28..153.28 rows=3000 width=149) (actual time=0.014..0.291 rows=3000 loops=1)
-- Planning Time: 0.224 ms
-- JIT:
--   Functions: 17
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"
-- "  Timing: Generation 2.403 ms, Inlining 1.674 ms, Optimization 90.116 ms, Emission 40.867 ms, Total 135.060 ms"
-- Execution Time: 136.557 ms

-- INDEXING

-- Hash Join  (cost=86.09..320.59 rows=1500 width=216) (actual time=0.639..2.232 rows=1500 loops=1)
--   Hash Cond: (c.carts_id = o.carts_cart_id_id)
--   ->  Merge Join  (cost=0.56..212.56 rows=2000 width=177) (actual time=0.042..1.286 rows=2000 loops=1)
--         Merge Cond: (users.user_id = c.users_user_id)
--         ->  Index Scan using users_user_id_idx on users  (cost=0.28..153.28 rows=3000 width=149) (actual time=0.012..0.455 rows=2001 loops=1)
--         ->  Index Scan using carts_users_user_id_idx on carts c  (cost=0.28..80.28 rows=2000 width=28) (actual time=0.009..0.252 rows=2000 loops=1)
--   ->  Hash  (cost=66.78..66.78 rows=1500 width=39) (actual time=0.577..0.578 rows=1500 loops=1)
--         Buckets: 2048  Batches: 1  Memory Usage: 122kB
--         ->  Index Scan using orders_carts_cart_id_id_idx on orders o  (cost=0.28..66.78 rows=1500 width=39) (actual time=0.008..0.343 rows=1500 loops=1)
-- Planning Time: 0.820 ms
-- Execution Time: 2.361 ms

begin;
savepoint SP2;

CREATE INDEX orders_carts_cart_id_id_idx ON orders(carts_cart_id_id);
CREATE INDEX carts_users_user_id_idx ON carts(users_user_id);
CREATE INDEX orders_total_idx ON orders(total);
CREATE INDEX users_user_id_idx ON users(user_id);
DROP INDEX IF EXISTS orders_carts_cart_id_id_idx;
DROP INDEX IF EXISTS carts_users_user_id_idx;
DROP INDEX IF EXISTS orders_total_idx;
DROP INDEX IF EXISTS users_user_id_idx;

EXPLAIN ANALYSE SELECT users.first_name as name,
       users.last_name  as surname,
       SUM(o.total)     as total_spent
FROM users
         JOIN carts ON users.user_id = carts.users_user_id
         JOIN orders o on carts.carts_id = o.carts_cart_id_id
GROUP BY users.user_id
ORDER BY total_spent DESC
LIMIT 5;

ROLLBACK TO SAVEPOINT SP2;

COMMIT;
END;

--DEFAULT

-- Limit  (cost=10000045410.13..10000045410.14 rows=5 width=67) (actual time=260.081..260.083 rows=5 loops=1)
--   ->  Sort  (cost=10000045410.13..10000045413.88 rows=1500 width=67) (actual time=158.028..158.030 rows=5 loops=1)
--         Sort Key: (sum(o.total)) DESC
--         Sort Method: top-N heapsort  Memory: 25kB
--         ->  GroupAggregate  (cost=10000000190.22..10000045385.22 rows=1500 width=67) (actual time=0.650..157.740 rows=1500 loops=1)
--               Group Key: users.user_id
--               ->  Nested Loop  (cost=10000000190.22..10000045358.97 rows=1500 width=41) (actual time=0.358..156.981 rows=1500 loops=1)
--                     Join Filter: (carts.carts_id = o.carts_cart_id_id)
--                     Rows Removed by Join Filter: 2998500
--                     ->  Merge Join  (cost=190.22..327.22 rows=2000 width=39) (actual time=0.347..1.135 rows=2000 loops=1)
--                           Merge Cond: (users.user_id = carts.users_user_id)
--                           ->  Index Scan using users_user_id_idx on users  (cost=0.28..153.28 rows=3000 width=35) (actual time=0.015..0.321 rows=2001 loops=1)
--                           ->  Sort  (cost=189.94..194.94 rows=2000 width=8) (actual time=0.326..0.416 rows=2000 loops=1)
--                                 Sort Key: carts.users_user_id
--                                 Sort Method: quicksort  Memory: 142kB
--                                 ->  Index Scan using carts_carts_id_idx on carts  (cost=0.28..80.28 rows=2000 width=8) (actual time=0.006..0.193 rows=2000 loops=1)
--                     ->  Materialize  (cost=10000000000.00..10000000035.50 rows=1500 width=10) (actual time=0.000..0.037 rows=1500 loops=2000)
--                           ->  Seq Scan on orders o  (cost=10000000000.00..10000000028.00 rows=1500 width=10) (actual time=0.007..0.089 rows=1500 loops=1)
-- Planning Time: 0.174 ms
-- JIT:
--   Functions: 19
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"
-- "  Timing: Generation 1.043 ms, Inlining 4.392 ms, Optimization 62.887 ms, Emission 34.620 ms, Total 102.942 ms"
-- Execution Time: 261.226 ms

-- INDEXED

-- Limit  (cost=371.75..371.76 rows=5 width=67) (actual time=2.552..2.557 rows=5 loops=1)
--   ->  Sort  (cost=371.75..375.50 rows=1500 width=67) (actual time=2.550..2.553 rows=5 loops=1)
--         Sort Key: (sum(o.total)) DESC
--         Sort Method: top-N heapsort  Memory: 25kB
--         ->  HashAggregate  (cost=328.09..346.84 rows=1500 width=67) (actual time=1.877..2.295 rows=1500 loops=1)
--               Group Key: users.user_id
--               Batches: 1  Memory Usage: 833kB
--               ->  Hash Join  (cost=86.09..320.59 rows=1500 width=41) (actual time=0.287..1.334 rows=1500 loops=1)
--                     Hash Cond: (carts.carts_id = o.carts_cart_id_id)
--                     ->  Merge Join  (cost=0.56..212.56 rows=2000 width=39) (actual time=0.011..0.830 rows=2000 loops=1)
--                           Merge Cond: (users.user_id = carts.users_user_id)
--                           ->  Index Scan using users_user_id_idx on users  (cost=0.28..153.28 rows=3000 width=35) (actual time=0.004..0.254 rows=2001 loops=1)
--                           ->  Index Scan using carts_users_user_id_idx on carts  (cost=0.28..80.28 rows=2000 width=8) (actual time=0.004..0.214 rows=2000 loops=1)
--                     ->  Hash  (cost=66.78..66.78 rows=1500 width=10) (actual time=0.272..0.273 rows=1500 loops=1)
--                           Buckets: 2048  Batches: 1  Memory Usage: 81kB
--                           ->  Index Scan using orders_carts_cart_id_id_idx on orders o  (cost=0.28..66.78 rows=1500 width=10) (actual time=0.003..0.164 rows=1500 loops=1)
-- Planning Time: 0.442 ms
-- Execution Time: 2.603 ms

SET work_mem TO '0.5MB';

CREATE INDEX orders_carts_cart_id_id_idx ON orders(carts_cart_id_id);
CREATE INDEX users_user_id_idx ON users(user_id);
CREATE INDEX carts_users_user_id_idx ON carts(users_user_id);
CREATE INDEX carts_carts_id_idx ON carts(carts_id);
CREATE INDEX orders_order_status_order_status_id_idx ON orders(order_status_order_status_id);

DROP INDEX IF EXISTS orders_carts_cart_id_id_idx;
DROP INDEX IF EXISTS users_user_id_idx;
DROP INDEX IF EXISTS carts_users_user_id_idx;
DROP INDEX IF EXISTS carts_carts_id_idx;
DROP INDEX IF EXISTS order_status_order_status_id_idx;

EXPLAIN ANALYSE SELECT users.first_name, users.last_name, COUNT(carts.carts_id) as carts_amount
FROM carts LEFT JOIN orders o on carts.carts_id = o.carts_cart_id_id
JOIN users ON carts.users_user_id = users.user_id
WHERE carts.carts_id is null or o.order_status_order_status_id = 5
GROUP BY users.user_id
ORDER BY carts_amount DESC
LIMIT 5;

--DEFAULT

-- Limit  (cost=10000000293.01..10000000293.02 rows=5 width=43) (actual time=109.023..109.026 rows=5 loops=1)
--   ->  Sort  (cost=10000000293.01..10000000293.92 rows=364 width=43) (actual time=0.900..0.901 rows=5 loops=1)
--         Sort Key: (count(carts.carts_id)) DESC
--         Sort Method: top-N heapsort  Memory: 25kB
--         ->  GroupAggregate  (cost=10000000169.04..10000000286.96 rows=364 width=43) (actual time=0.562..0.857 rows=273 loops=1)
--               Group Key: users.user_id
--               ->  Merge Join  (cost=10000000169.04..10000000281.50 rows=364 width=39) (actual time=0.555..0.788 rows=273 loops=1)
--                     Merge Cond: (carts.users_user_id = users.user_id)
--                     ->  Sort  (cost=10000000168.76..10000000169.67 rows=364 width=8) (actual time=0.547..0.556 rows=273 loops=1)
--                           Sort Key: carts.users_user_id
--                           Sort Method: quicksort  Memory: 37kB
--                           ->  Hash Left Join  (cost=10000000047.03..10000000153.28 rows=364 width=8) (actual time=0.219..0.526 rows=273 loops=1)
--                                 Hash Cond: (carts.carts_id = o.carts_cart_id_id)
--                                 Filter: ((carts.carts_id IS NULL) OR (o.order_status_order_status_id = 5))
--                                 Rows Removed by Filter: 1727
--                                 ->  Index Scan using carts_carts_id_idx on carts  (cost=0.28..80.28 rows=2000 width=8) (actual time=0.015..0.176 rows=2000 loops=1)
--                                 ->  Hash  (cost=10000000028.00..10000000028.00 rows=1500 width=8) (actual time=0.198..0.198 rows=1500 loops=1)
--                                       Buckets: 2048  Batches: 1  Memory Usage: 75kB
--                                       ->  Seq Scan on orders o  (cost=10000000000.00..10000000028.00 rows=1500 width=8) (actual time=0.008..0.095 rows=1500 loops=1)
--                     ->  Index Scan using users_pkey on users  (cost=0.28..153.28 rows=3000 width=35) (actual time=0.005..0.151 rows=1500 loops=1)
-- Planning Time: 0.306 ms
-- JIT:
--   Functions: 24
-- "  Options: Inlining true, Optimization true, Expressions true, Deforming true"
-- "  Timing: Generation 2.578 ms, Inlining 6.392 ms, Optimization 66.319 ms, Emission 35.304 ms, Total 110.593 ms"
-- Execution Time: 111.689 ms

--INDEXED

-- Limit  (cost=314.29..314.30 rows=5 width=43) (actual time=0.930..0.931 rows=5 loops=1)
--   ->  Sort  (cost=314.29..315.20 rows=364 width=43) (actual time=0.929..0.930 rows=5 loops=1)
--         Sort Key: (count(carts.carts_id)) DESC
--         Sort Method: top-N heapsort  Memory: 25kB
--         ->  GroupAggregate  (cost=190.32..308.24 rows=364 width=43) (actual time=0.581..0.891 rows=273 loops=1)
--               Group Key: users.user_id
--               ->  Merge Join  (cost=190.32..302.78 rows=364 width=39) (actual time=0.575..0.817 rows=273 loops=1)
--                     Merge Cond: (carts.users_user_id = users.user_id)
--                     ->  Sort  (cost=190.04..190.95 rows=364 width=8) (actual time=0.571..0.579 rows=273 loops=1)
--                           Sort Key: carts.users_user_id
--                           Sort Method: quicksort  Memory: 37kB
--                           ->  Merge Left Join  (cost=0.56..174.56 rows=364 width=8) (actual time=0.011..0.548 rows=273 loops=1)
--                                 Merge Cond: (carts.carts_id = o.carts_cart_id_id)
--                                 Filter: ((carts.carts_id IS NULL) OR (o.order_status_order_status_id = 5))
--                                 Rows Removed by Filter: 1727
--                                 ->  Index Scan using carts_pkey on carts  (cost=0.28..80.28 rows=2000 width=8) (actual time=0.005..0.170 rows=2000 loops=1)
--                                 ->  Index Scan using orders_carts_cart_id_id_idx on orders o  (cost=0.28..66.78 rows=1500 width=8) (actual time=0.003..0.136 rows=1500 loops=1)
--                     ->  Index Scan using users_user_id_idx on users  (cost=0.28..153.28 rows=3000 width=35) (actual time=0.003..0.141 rows=1500 loops=1)
-- Planning Time: 0.383 ms
-- Execution Time: 0.962 ms
