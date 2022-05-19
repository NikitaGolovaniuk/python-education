-- Задание:
-- Использовать транзакции для insert, update, delete на 3х таблицах.
-- Предоставить разнообразные примеры включая возврат к savepoints.


-- TABLE_1 - USERS

-- Добавляем пользователя, если коллизия - можем откатиться до сейвпоинта SP1
BEGIN;
SAVEPOINT SP1;
INSERT INTO users(user_id, email, password, first_name, middle_name, last_name, is_staff, country, city, address, phone_number)
VALUES (3001, 'qwerty@gmail.com', '1388', 'Evlampiy', 'Junior', 'Petrosyan', 0, 'country 17', 'city 17', 'prospect', '2204');
ROLLBACK TO SAVEPOINT SP1;
COMMIT;
END;

-- Меняем столбец middle_name, если перепутали id - можем откатиться до сейвпоинта SP2
BEGIN;
SAVEPOINT SP2;
UPDATE users
SET middle_name = 'MIDDLEMAN'
WHERE user_id = 3001;
ROLLBACK TO SAVEPOINT SP2;
COMMIT;
END;

-- Удаляем строку по id - можем откатиться до сейвпоинта SP3
BEGIN;
SAVEPOINT SP3;
DELETE FROM users
WHERE user_id = 3001;
ROLLBACK TO SAVEPOINT SP3;
COMMIT;
END;

-- TABLE_2 - order_status
-- Добавляем новый статус когда кто-то потерял заказ
BEGIN;
SAVEPOINT SP1;
INSERT INTO order_status(order_status_id, status_name)
VALUES (6, 'Lost');
ROLLBACK TO SAVEPOINT SP1;
COMMIT;
END;

-- Когда нашли заказ SP2
BEGIN;
SAVEPOINT SP2;
UPDATE order_status
SET status_name = 'Found'
WHERE order_status_id = 6;
ROLLBACK TO SAVEPOINT SP2;
COMMIT;
END;

-- Удаляем статус по id - можем откатиться до сейвпоинта SP3
BEGIN;
SAVEPOINT SP3;
DELETE FROM order_status
WHERE order_status_id = 6;
ROLLBACK TO SAVEPOINT SP3;
COMMIT;
END;

-- TABLE_3 - categories
-- Добавляем новую категорию
BEGIN;
SAVEPOINT SP1;
INSERT INTO categories(category_id, category_title, category_description)
VALUES (21, 'Category 21', 'Category 21 description');
ROLLBACK TO SAVEPOINT SP1;
COMMIT;
END;

-- Определяем ее как пиццу
BEGIN;
SAVEPOINT SP2;
UPDATE categories
SET category_title = 'pizza'
WHERE category_id = 21;
ROLLBACK TO SAVEPOINT SP2;
COMMIT;
END;

-- Удаляем категорию по id - никакой больше пиццы, можем откатиться до сейвпоинта SP3
BEGIN;
SAVEPOINT SP3;
DELETE FROM categories
WHERE category_id = 21;
ROLLBACK TO SAVEPOINT SP3;
COMMIT;
END;