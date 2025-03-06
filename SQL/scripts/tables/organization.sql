CREATE TABLE organization (
    organization_id serial PRIMARY KEY,
    organization_desc varchar(100) UNIQUE NOT NULL
)
