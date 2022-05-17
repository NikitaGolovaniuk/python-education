CREATE DATABASE shop;
CREATE TABLE Categories(
    category_id serial primary key,
    category_title varchar(255),
    category_description text
);

CREATE TABLE Products(
    product_id serial primary key,
    product_tittle varchar(255),
    product_description text,
    in_stock int,
    price float,
    slug varchar(45),
    category_id int references Categories(category_id)
);

CREATE TABLE Users(
    user_id serial primary key,
    email varchar(255),
    password varchar(255),
    first_name varchar(255),
    middle_name varchar(255),
    last_name varchar(255),
    is_staff int,
    country varchar(255),
    city varchar(255),
    address text
);

CREATE TABLE Carts(
    carts_id serial primary key,
    Users_user_id int references Users(user_id),
    subtotal decimal,
    total decimal,
    timestamp timestamp(2)
);

CREATE TABLE Cart_product(
    carts_cart_id int references Carts(carts_id),
    products_product_id int references Products(product_id)
);

CREATE TABLE Order_status(
    order_status_id serial primary key,
    status_name varchar(255)
);

CREATE TABLE Orders(
    order_id serial primary key,
    carts_cart_id_id int references Carts(carts_id),
    order_status_order_status_id int references Order_status(order_status_id),
    shipping_total decimal,
    total decimal,
    created_at timestamp(2),
    updated_at timestamp(2)
);

COPY users from '/usr/src/users.csv' WITH (format csv);
COPY carts from '/usr/src/carts.csv' WITH (format csv);
COPY categories from '/usr/src/categories.csv' WITH (format csv);
COPY products from '/usr/src/products.csv' WITH (format csv);
COPY cart_product from '/usr/src/cart_products.csv' WITH (format csv);
COPY order_status from '/usr/src/order_statuses.csv' WITH (format csv);
COPY orders from '/usr/src/orders.csv' WITH (format csv);

ALTER TABLE users add column phone_number int;
ALTER TABLE users alter column phone_number type varchar;

UPDATE products SET price = price * 2;


