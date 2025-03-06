--Deviation determines how much parameter can deviate from set value
CREATE TABLE deviation (
    deviation_id serial PRIMARY KEY,
    deviation_desc varchar(30) UNIQUE NOT NULL
);
