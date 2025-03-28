CREATE TABLE document_type_period (
    document_type_period_id serial PRIMARY KEY,
    fk_unit int REFERENCES unit (unit_id) NOT NULL,
    fk_document_type int REFERENCES document_type (document_type_id) NOT NULL,
    fk_period int REFERENCES period (period_id) NOT NULL
);
