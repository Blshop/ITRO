from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields


class DocumentTypeOrganization(db.Model):
    __tablename__ = "document_type_organization"
    document_type_organization_id = db.Column(db.Integer, primary_key=True)
    fk_unit = db.Column(db.Integer, db.ForeignKey("unit.unit_id"), nullable=False)
    fk_document_type = db.Column(
        db.Integer, db.ForeignKey("document_type.document_type_id"), nullable=False
    )
    fk_organization = db.Column(
        db.Integer, db.ForeignKey("organization.organization_id"), nullable=False
    )
    unit = db.relationship("Unit", backref="document_type_organization", lazy=True)
    document_type = db.relationship(
        "DocumentType", backref="document_type_organization", lazy=True
    )
    organization = db.relationship(
        "Organization", backref="document_type_organization", lazy=True
    )

    def __repr__(self):
        return (
            f"<DocumentTypeOrganization("
            f"document_type_organization_id={self.document_type_organization_id}, "
            f"fk_unit={self.fk_unit}, "
            f"fk_document_type={self.fk_document_type}, "
            f"fk_organization={self.fk_organization})>"
        )


class DocumentTypeOrganizationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DocumentTypeOrganization
        load_instance = True

    unit = fields.Related(["unit_id"])
    document_type = fields.Related(["document_type_desc"])
    organization = fields.Related(["organization_desc"])
