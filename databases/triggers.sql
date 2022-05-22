-- 1. Сравнить цену каждого продукта n с средней ценой продуктов в категории
-- продукта n. Использовать window function. Таблица результата должна
-- содержать такие колонки: category_title, product_title, price, avg.

SELECT products.product_tittle,
       product_tittle,
       price,
       AVG(price) OVER (PARTITION BY category_id) as avg
FROM products;

-- 2. Добавить 2 любых триггера и обработчика к ним.
-- Снабдить комментариями - что делают триггеры и обработчики.

-- Уменьшает количество товара в таблице продукты при обновлении корзины

CREATE OR REPLACE FUNCTION reduce_products_val()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
    UPDATE products
    SET in_stock = in_stock - 1
    WHERE products.product_id in (SELECT cart_product.products_product_id FROM cart_product WHERE cart_product.carts_cart_id = NEW.carts_id);
    RETURN NEW;
END;$$;

CREATE TRIGGER reduce_products_val_trg
  AFTER UPDATE
  ON carts
  FOR EACH ROW
  EXECUTE PROCEDURE reduce_products_val();

UPDATE carts
SET total = 250
WHERE carts_id = 47;

DROP TRIGGER IF EXISTS reduce_products_val_trg ON carts;

-- Не позволяет добавление новых пользователей из определенной страны

CREATE OR REPLACE FUNCTION country_restrict()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
    IF NEW.country = 'very aggressive country'
        then
            raise error_in_assignment;
    else
        RETURN NEW;
    end if;
END;
$$;

CREATE TRIGGER country_restrict_trg
  BEFORE INSERT
  ON users
  FOR EACH ROW
  EXECUTE PROCEDURE country_restrict();

INSERT INTO users(user_id, email, password, first_name, middle_name, last_name, is_staff, country, city, address, phone_number)
VALUES (3001, 'qwerty@gmail.com', '1388', 'Evlampiy', 'Junior', 'Petrosyan', 0, 'good country', 'city 17', 'prospect', '2204');

INSERT INTO users(user_id, email, password, first_name, middle_name, last_name, is_staff, country, city, address, phone_number)
VALUES (3002, 'qwerty@gmail.com', '1388', 'Evlampiy', 'Junior', 'Petrosyan', 0, 'very aggressive country', 'city 17', 'prospect', '2204');

DROP TRIGGER IF EXISTS country_restrict_trg ON users;