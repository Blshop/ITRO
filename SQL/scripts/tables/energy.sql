create table energy (
    energy_id serial primary key,
    energy_desc varchar(30) unique not null,
    half_life float default 0,
    fk_energy_type int references energy_type (energy_type_id)
);
