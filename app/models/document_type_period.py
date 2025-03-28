from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields


class DocumentTypePeriod(db.Model):
    __tablename__ = "document_type_period"
    document_type_period_id = db.Column(db.Integer, primary_key=True)
    fk_unit = db.Column(db.Integer, db.ForeignKey("unit.unit_id"), nullable=False)
    fk_document_type = db.Column(
        db.Integer, db.ForeignKey("document_type.document_type_id"), nullable=False
    )
    fk_period = db.Column(db.Integer, db.ForeignKey("period.period_id"), nullable=False)
    unit = db.relationship("Unit", backref="document_type_period", lazy=True)
    document_type = db.relationship(
        "DocumentType", backref="document_type_period", lazy=True
    )
    period = db.relationship("Period", backref="document_type_period", lazy=True)

    def __repr__(self):
        return (
            f"<DocumentTypePeriod("
            f"document_type_period_id={self.document_type_period_id}, "
            f"fk_unit={self.fk_unit}, "
            f"fk_document_type={self.fk_document_type}, "
            f"fk_period={self.fk_period})>"
        )


class DocumentTypePeriodSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DocumentTypePeriod
        load_instance = True

    unit = fields.Related(["unit_id"])
    document_type = fields.Related(["document_type_desc"])
    period = fields.Related(["period_desc"])
