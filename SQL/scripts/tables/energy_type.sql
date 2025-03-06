CREATE TABLE energy_type (
    energy_type_id serial PRIMARY KEY,
    energy_type_desc varchar(30) UNIQUE NOT NULL
);
