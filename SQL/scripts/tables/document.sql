CREATE TABLE document (
    document_id serial PRIMARY KEY,
    document_path varchar(100),
    document_desc varchar(50),
    date_creation date,
    year_creation int,
    fk_unit int REFERENCES unit (unit_id) NOT NULL,
    fk_document_type int REFERENCES document_type (document_type_id) NOT NULL,
    fk_period int REFERENCES period (period_id) NOT NULL,
    fk_organization int REFERENCES organization (organization_id) NOT NULL
);
