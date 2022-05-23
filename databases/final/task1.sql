-- Задание 1
-- Создать бд, создать таблицы, добавить связи между таблицами, заполнить таблицу данными
-- (их нужно сгенерировать в большом количестве - для этого можно использовать последовательности,
-- собственные или встроенные функции - никаких внешних генераторов).

CREATE DATABASE car_rent;

CREATE TABLE city(
    city_id serial primary key,
    name varchar(50)
);

CREATE TABLE street(
    street_id serial primary key,
    city_id int references city(city_id),
    name varchar
);

CREATE TABLE building(
    building_id serial primary key,
    street_id int references street(street_id),
    number int
);

CREATE TABLE flat(
    flat_id serial primary key,
    building_id int references building(building_id),
    number int
);

CREATE TABLE address(
    address_id serial primary key,
    flat_id int references flat(flat_id)
);

CREATE TABLE phone(
    phone_id serial primary key,
    number int
);

CREATE TABLE customer(
    customer_id serial primary key,
    name varchar(50),
    phone_id int references phone(phone_id),
    address_id int references address(address_id)
);

CREATE TABLE branch(
    branch_id serial primary key,
    branch_number int,
    phone_id int references phone(phone_id),
    address_id int references address(address_id)
);

CREATE TABLE manufacturer(
    manufacturer_id serial primary key,
    name varchar(50)
);

CREATE TABLE car_model(
    model_id serial primary key,
    manufacturer_id int references manufacturer(manufacturer_id),
    name varchar(50)
);

CREATE TABLE car_number(
    car_number_id serial primary key,
    number int
);

CREATE TABLE car(
    car_id serial primary key,
    model_id int references car_model(model_id),
    car_number_id int references car_number(car_number_id)
);

CREATE TABLE rent(
    rent_id serial primary key,
    customer_id int references customer(customer_id),
    car_id int references car(car_id),
    branch_id int references branch(branch_id),
    price int,
    rent_start timestamp,
    rent_period int
);

insert into city (name)
select
    'city ' || i
from generate_series(1, 1000000) s(i);

insert into street (name, city_id)
select
    'street ' || i,
    i
from generate_series(1, 1000000) s(i);

CREATE OR REPLACE FUNCTION random_between(low INT ,high INT)
   RETURNS INT AS
$$
BEGIN
   RETURN floor(random()* (high-low + 1) + low);
END;
$$ language 'plpgsql' STRICT;

DROP TABLE flat CASCADE ;
do
$$
    BEGIN
        for i in 1..1000000
            loop
                insert into building(street_id, number)
                values (i, random_between(1,10000));
            end loop;
    end;
$$;

do
$$
    declare
        rec record;
    BEGIN
        for rec in select * from building
            loop
                insert into flat(building_id, number)
                values (rec.building_id, random_between(1, 1000));
            end loop;
    end;
$$;

DROP TABLE street CASCADE;

do
$$
    declare
        rec record;
    BEGIN
        for rec in select * from flat
            loop
                insert into address(flat_id)
                values (rec.flat_id);
            end loop;
    end;
$$;

DROP TABLE address CASCADE;

do
$$
    declare
        tmp int default 0;
    BEGIN
        for i in 1..1000
            loop
                tmp := random_between(1,10);
                for j in 1..6
                    loop
                    tmp := tmp * 10 + random_between(1,10);
                    end loop;
                insert into phone(number)
                values (tmp);
                tmp := 0;
            end loop;
    end;
$$;

DROP TABLE phone CASCADE;

do
$$
    declare
        phone_len int;
    BEGIN
        select count(phone.phone_id) from phone into phone_len;
        for i in 1..phone_len/2-1
            loop
                insert into customer(name, phone_id, address_id)
                values('name ' || i, i, i);
            end loop;
    end;
$$;

DROP TABLE customer CASCADE;

do
$$
    declare
        phone_len int;
    BEGIN
        select count(phone.phone_id) from phone into phone_len;
        for i in phone_len/2..phone_len
            loop
                insert into branch(branch_number, phone_id, address_id)
                values(i-499, i, i);
            end loop;
    end;
$$;

DROP TABLE branch CASCADE;

do
$$
    BEGIN
        for i in 1..100000
            loop
                insert into manufacturer(name)
                values('name ' || i);
            end loop;
    end;
$$;

DROP TABLE manufacturer CASCADE;

do
$$
    declare
        rec record;
    BEGIN
        for rec in select * from manufacturer
            loop
                insert into car_model(manufacturer_id, name)
                values(rec.manufacturer_id, 'name ' || rec.manufacturer_id);
            end loop;
    end;
$$;

DROP TABLE car_model CASCADE;

do
$$
    declare
        tmp int default 0;
    BEGIN
        for i in 1..100000
            loop
                tmp := random_between(1,10);
                for j in 1..6
                    loop
                    tmp := tmp * 10 + random_between(1,10);
                    end loop;
                insert into car_number(number)
                values (tmp) ON CONFLICT DO NOTHING;
                tmp := 0;
            end loop;
    end;
$$;

DROP TABLE car_number CASCADE;

do
$$
    declare
        car_number_len int default 0;
        car_model_len int default 0;
        rec record;
    BEGIN
        for i in 1..10000
            loop
                select count(car_model.model_id) from car_model into car_model_len;
                select count(car_number.car_number_id) from car_number into car_number_len;
                insert into car(model_id, car_number_id)
                values (random_between(1, car_model_len), random_between(1, car_number_len)) ON CONFLICT DO NOTHING;
            end loop;
    end;
$$;

DROP TABLE car CASCADE;

do
$$
    declare
        customer_id_len int default 0;
        car_id_len int default 0;
        branch_id_len int default 0;
        rent_start_gen date default '2007-02-01';
        rec record;
    BEGIN
        for i in 1..100000
            loop
                select count(customer.customer_id) from customer into customer_id_len;
                select count(car.car_id) from car into car_id_len;
                select count(branch.branch_id) from branch into branch_id_len;
                select generate_series  ( rent_start_gen::timestamp , '2022-10-31'::timestamp , '1 day'::interval) :: date into rent_start_gen;
                rent_start_gen := rent_start_gen + 1;
                insert into rent(customer_id, car_id, branch_id, price, rent_start, rent_period)
                values (
                        random_between(1, customer_id_len),
                        random_between(1, car_id_len),
                        random_between(1, branch_id_len),
                        random_between(1, 100000),
                        rent_start_gen,
                        random_between(1, 365)
                        ) ON CONFLICT DO NOTHING;
            end loop;
    end;
$$;

DROP TABLE rent CASCADE;