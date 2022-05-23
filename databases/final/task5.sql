-- Задание 5
-- Написать 2 любые хранимые процедуры. В них использовать транзакции для insert, update, delete.

-- проверяем чтобы номер был от 5 до 8 цифр

CREATE PROCEDURE insert_phone(phone_id_f int, number_f int)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO phone (phone_id, number) VALUES (phone_id_f, number_f);
            IF number_f between 100000 and 99999999 then
                COMMIT;
            ELSE
                ROLLBACK;
    END IF;
END;
$$;

DROP PROCEDURE insert_phone(phone_id_f int, number_f int);
CALL insert_phone(1001, 23213132);

CREATE PROCEDURE delete_customer(cus_id int)
LANGUAGE plpgsql
AS $$
BEGIN
    DELETE FROM customer WHERE customer_id = cus_id;
            IF cus_id is not null then
                COMMIT;
            ELSE
                ROLLBACK;
    END IF;
END;
$$;

DROP PROCEDURE delete_customer(cus_id int);
CALL delete_customer(15);
