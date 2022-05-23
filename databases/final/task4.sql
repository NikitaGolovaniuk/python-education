-- Задание 4
-- Создать 3 функции (одна из них должна возвращать таблицу, одна из них должна использовать циклы, одна из них должна использовать курсор).

-- возвращает таблицу с диапазоном номеров

create or replace function return_table(a int, b int)
    returns table(
        name varchar,
        phone_id int
                 )
as
$$
    begin
        RETURN QUERY SELECT
            customer.name,
            cast(p.number as integer)
        FROM
            customer join phone p on p.phone_id = customer.phone_id
        WHERE
            p.phone_id between a and b;
    end;
$$
language 'plpgsql';

SELECT * FROM
return_table(1, 1000000);


-- Возвращает таблицу с диапазоном цен, используя циклы

CREATE OR REPLACE FUNCTION get_rent_price_diapason (a int, b int)
    RETURNS TABLE (
        tbl_price int
) AS $$
DECLARE
    rec record;
BEGIN
    FOR rec IN(SELECT
                rent.price
                FROM rent
                WHERE price between a and b)
    LOOP
        tbl_price := rec.price;
        RETURN NEXT;
    END LOOP;
END; $$
LANGUAGE 'plpgsql';

SELECT * from
get_rent_price_diapason(250, 10000);
DROP FUNCTION get_rent_price_diapason;

-- Использует курсоры
-- Удаляет строку из таблицы rent если в ней есть null

create or replace function purge_all_null_rows()
returns boolean
as
$$
DECLARE
   curs1 refcursor;
   rec record;
BEGIN
   OPEN curs1 FOR SELECT * FROM rent ORDER BY rent_start FOR UPDATE;
   DELETE FROM rent WHERE rent_start is null;
   LOOP
      FETCH curs1 INTO rec;
      EXIT WHEN NOT FOUND;
      RAISE NOTICE 'ROW:%',rec.rent_start;
   END LOOP;
   CLOSE curs1;
   return true;
END
$$
language 'plpgsql' VOLATILE;

DROP FUNCTION purge_all_null_rows();

SELECT * from purge_all_null_rows();