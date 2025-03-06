CREATE TABLE unit_parameter (
    unit_parameter_id serial PRIMARY KEY,
    fk_unit int REFERENCES unit (unit_id) NOT NULL,
    fk_parameter int REFERENCES parameter (parameter_id) NOT NULL,
    fk_period int REFERENCES period (period_id) NOT NULL
);
