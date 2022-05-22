-- Задание:
-- 1. Создать функцию, которая сетит shipping_total = 0 в таблице order, если город юзера равен x (аргумент функции),
--     и возвращает сумму всех заказов для поля shipping_total. Использовать IF clause.

create or replace function set_shipping_total_if_usercity_is_x(x varchar)
    returns int
    language plpgsql
as
$$
declare
    rec                record;
    shipping_total_sum int default 0;
begin
    for rec in
        select users.city, o.order_id, shipping_total
        from users
                 join carts c on users.user_id = c.users_user_id
                 join orders o on c.carts_id = o.carts_cart_id_id
        LOOP
            IF rec.city = x then
                shipping_total_sum := shipping_total_sum + rec.shipping_total;
                update orders
                set shipping_total = 0
                where order_id = rec.order_id;
            end if;
        end loop;
    return shipping_total_sum;
end;
$$;

DROP FUNCTION set_shipping_total_if_usercity_is_x(x varchar);
select set_shipping_total_if_usercity_is_x('city 17');

-- 2. Написать 3 любые (НО осмысленные) хранимые процедуры с использованием условий,
--     циклов и транзакций. Дать комментарии что делает каждая процедура.

-- Добавляет уникальный заказ

create or replace procedure add_new_unique_order(order_id int,
                                                 carts_cart_id_id int,
                                                 order_status_order_status_id int,
                                                 shipping_total int,
                                                 total int,
                                                 created_at timestamp,
                                                 updated_at timestamp)
    language plpgsql
as
$$
declare
    rec  record;
    flag boolean default true;
begin
    for rec in
        select * from orders
        loop
            if rec.order_id = order_id or
               rec.carts_cart_id_id = carts_cart_id_id or
               rec.order_status_order_status_id = order_status_order_status_id or
               rec.shipping_total = shipping_total or
               rec.total = total or
               rec.created_at = created_at or
               rec.updated_at = updated_at
            then
                flag := false;
            end if;
        end loop;
    if flag = true then
        INSERT INTO orders
        VALUES (order_id, carts_cart_id_id, order_status_order_status_id, shipping_total, total, created_at,
                updated_at);
    else
        rollback;
    end if;
end;
$$;

call add_new_unique_order(
        1501, 1501, 6, 61, 1571, '1997-11-20 00:00:00.00', '1998-11-20 00:00:00.00'
    );

DROP PROCEDURE add_new_unique_order;

delete
from orders
WHERE orders.order_id = 1501;

-- Удаляет всех пользователей из выбранной страны

create or replace procedure delete_country(name varchar)
language plpgsql
as
$$
declare
    rec record;
    tmp_val record;
begin
    for rec in select * from users join carts c on users.user_id = c.users_user_id
        join orders o on c.carts_id = o.carts_cart_id_id
    loop
        if rec.country = name then
            delete from orders where orders.carts_cart_id_id = rec.carts_cart_id_id;
            delete from cart_product where cart_product.carts_cart_id = rec.carts_id;
            delete from carts where carts.users_user_id = rec.user_id;
            delete from users where users.country = name;
            commit;
        else
            rollback;
        end if;
    end loop;
end;
$$;

DROP PROCEDURE delete_country;

call delete_country('country 502');
delete from users where city = 'country 500';

select users.country from users;

-- меняет цены всех продуктов в заданном диапазоне на %, где .5 - 50%, а 1.5 - 150%

create or replace procedure show_products(min int, max int, persents float)
language plpgsql
as
$$
    declare
        rec record;
begin
    for rec in select * from products
    loop
        if rec.price between min and max then
            commit;
            update products set
            price = price * persents
            where price = rec.price;
            commit;
        else
            rollback;
        end if;
    end loop;
end;
$$;

DROP PROCEDURE show_products;
call show_products(200, 500, .5);
