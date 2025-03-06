--types of document stored in database
CREATE TABLE document_type (
    document_type_id serial PRIMARY KEY,
    document_type_desc varchar(50) UNIQUE NOT NULL
);
