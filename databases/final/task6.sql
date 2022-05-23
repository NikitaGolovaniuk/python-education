-- Задание 6
-- Добавить 2 триггера (один из них ДО операции по изменению данных, второй после) и функции или процедуры-обработчики к ним.

-- Проверка чтобы нельзя было установить больше 365 дней аренды

CREATE OR REPLACE FUNCTION rent_period_check()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
    if new.rent_period > 365 then
        raise error_in_assignment;
    else
        return NEW;
    end if;
END;
$$;

CREATE TRIGGER rent_period_check_trg
  BEFORE UPDATE
  ON rent
  FOR EACH ROW
  EXECUTE PROCEDURE rent_period_check();

UPDATE rent
SET rent_period = 366
WHERE rent.rent_id = 1;

DROP TRIGGER IF EXISTS rent_period_check_trg ON rent;


-- Сразу устанавливает текущую дату начала аренды

CREATE OR REPLACE FUNCTION rent_date_start()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
  AS
$$
BEGIN
    update rent
    set rent_start = now()
    WHERE rent.rent_id = new.rent_id;
    RETURN NEW;
END;
$$;

CREATE TRIGGER rent_date_start_trg
  AFTER UPDATE
  ON rent
  FOR EACH ROW
  WHEN ( pg_trigger_depth() < 1 )
  EXECUTE PROCEDURE rent_date_start();

UPDATE rent
SET rent_period = 12
WHERE rent.rent_id = 3;

DROP FUNCTION rent_date_start();
DROP TRIGGER IF EXISTS rent_date_start_trg ON rent;
