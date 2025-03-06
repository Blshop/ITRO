--Parameters of units required to be checked regularly
CREATE TABLE parameter (
    parameter_id serial PRIMARY KEY,
    parameter_desc varchar(100) NOT NULL,
    fk_deviation int REFERENCES deviation (deviation_id) NOT NULL,
    fk_unit_category int REFERENCES unit_category (unit_category_id) NOT NULL,
    UNIQUE (parameter_desc, fk_deviation, fk_unit_category)
);
