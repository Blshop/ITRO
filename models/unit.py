from models.base_model import db


class Unit_parameter(db.Model):
    unit_parameter_id = db.Column(db.Integer, primary_key=True)
    fk_unit = db.Column(
        db.Integer, db.ForeignKey("unit.unit_id"), primary_key=True, nullable=False
    )
    fk_parameter = db.Column(
        db.Integer,
        db.ForeignKey("parameter.parameter_id"),
        primary_key=True,
        nullable=False,
    )
    fk_period = db.Column(
        db.Integer, db.ForeignKey("period.period_id"), primary_key=True, nullable=False
    )
    unit = db.relationship("Unit", back_populates="unit_parameter")
    parameter = db.relationship("Parameter", back_populates="unit_parameter")
    period = db.relationship("Period", back_populates="unit_parameter")


class Unit_document(db.Model):
    unit_document_id = db.Column(db.Integer, primary_key=True)
    fk_unit = db.Column(
        db.Integer, db.ForeignKey("unit.unit_id"), primary_key=True, nullable=False
    )
    fk_document_type = db.Column(
        db.Integer,
        db.ForeignKey("document_type.document_type_id"),
        primary_key=True,
        nullable=False,
    )
    fk_period = db.Column(
        db.Integer, db.ForeignKey("period.period_id"), primary_key=True, nullable=False
    )
    unit = db.relationship("Unit", back_populates="unit_document")
    document_type = db.relationship("Document_type", back_populates="unit_document")
    period = db.relationship("Period", back_populates="unit_document")


class Document(db.Model):
    document_id = db.Column(db.Integer, primary_key=True)
    document_path = db.Column(db.String(100), unique=True, nullable=False)
    document_desc = db.Column(db.String(50), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    valid_year = db.Column(db.Integer, nullable=False)
    fk_unit = db.Column(
        db.Integer, db.ForeignKey("unit.unit_id"), primary_key=True, nullable=False
    )
    fk_period = db.Column(
        db.Integer, db.ForeignKey("period.period_id"), primary_key=True, nullable=False
    )
    fk_document_type = db.Column(
        db.Integer,
        db.ForeignKey("document_type.document_type_id"),
        primary_key=True,
        nullable=False,
    )
    unit = db.relationship("Unit", back_populates="document")
    document_type = db.relationship("Document_type", back_populates="document")
    period = db.relationship("Period", back_populates="document")
