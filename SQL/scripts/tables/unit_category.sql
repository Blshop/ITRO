CREATE TABLE unit_category (
    unit_category_id serial PRIMARY KEY,
    unit_category_desc varchar(100) UNIQUE NOT NULL
);
