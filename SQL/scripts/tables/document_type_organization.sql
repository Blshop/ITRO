CREATE TABLE document_type_organization (
    document_type_organization_id serial PRIMARY KEY,
    fk_unit int REFERENCES unit (unit_id) NOT NULL,
    fk_document_type int REFERENCES document_type (document_type_id) NOT NULL,
    fk_organization int REFERENCES organization (organization_id) NOT NULL
);
