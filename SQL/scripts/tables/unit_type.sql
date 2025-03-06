CREATE TABLE unit_type (
    unit_type_id serial PRIMARY KEY,
    unit_type_desc varchar(100) UNIQUE NOT NULL,
    fk_energy_type int REFERENCES energy_type (energy_type_id)
);
