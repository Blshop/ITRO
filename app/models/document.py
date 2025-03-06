from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields


class Document(db.Model):
    __tablename__ = "document"
    document_id = db.Column(db.Integer, primary_key=True)
    document_path = db.Column(db.String(100), nullable=False)
    document_desc = db.Column(db.String(50), nullable=False)
    date_creation = db.Column(db.Date, nullable=False)
    year_creation = db.Column(db.Integer, nullable=False)
    fk_unit = db.Column(db.Integer, db.ForeignKey("unit.unit_id"), nullable=False)
    fk_document_type = db.Column(
        db.Integer, db.ForeignKey("document_type.document_type_id"), nullable=False
    )
    fk_period = db.Column(db.Integer, db.ForeignKey("period.period_id"), nullable=False)
    fk_organization = db.Column(
        db.Integer, db.ForeignKey("organization.organization_id"), nullable=False
    )
    unit = db.relationship("Unit", backref="document", lazy=True)
    document_type = db.relationship("DocumentType", backref="document", lazy=True)
    period = db.relationship("Period", backref="document", lazy=True)
    organization = db.relationship("Organization", backref="document", lazy=True)


class DocumentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Document
        load_instance = True

    unit = fields.Related(["unit_desc"])
    period = fields.Related(["period_desc"])
