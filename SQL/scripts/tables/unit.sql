CREATE TABLE unit (
    unit_id serial PRIMARY KEY,
    unit_desc varchar(30) NOT NULL,
    unit_sn varchar(15),
    fk_unit_type int REFERENCES unit_type (unit_type_id) NOT NULL,
    fk_unit_category int REFERENCES unit_category (unit_category_id),
    UNIQUE (unit_desc, unit_sn)
);
