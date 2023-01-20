from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Types
class Unit_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unit_type_desc = db.Column(db.String(20), unique=True, nullable=False)
    units = db.relationship("Unit", backref="unit_type")


class Period(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    period_desc = db.Column(db.String(20), unique=True, nullable=False)
    days_number = db.Column(db.Integer, nullable=False)
    quality_controls = db.relationship("Quality_control", back_populates="periods")


class Document_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    document_type_desc = db.Column(db.String(100))
    documents = db.relationship("Document", backref="document_type")


class Deviation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deviation_value = db.Column(db.String(20), unique=True)
    parameters = db.relationship("Parameter", backref="deviation")


class Equipment_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_type_desc = db.Column(db.String(20))


# class Service_type(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     service_type_desc = db.Column(db.String(20))


class Parameter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parameter_desc = db.Column(db.String(20))
    deviation_id = db.Column(db.Integer, db.ForeignKey("deviation.id"), nullable=False)
    quality_controls = db.relationship("Quality_control", back_populates="parameters")


class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unit_desc = db.Column(db.String(20), unique=True, nullable=False)
    serial_number = db.Column(db.Integer, nullable=False)
    source_type = db.Column(db.String(20), nullable=False)
    commissioning = db.Column(db.Date, nullable=True)
    unit_type_id = db.Column(db.Integer, db.ForeignKey("unit_type.id"), nullable=False)
    quality_controls = db.relationship("Quality_control", back_populates="units")


class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_desc = db.Column(db.String(20))
    serial_number = db.Column(db.Integer, nullable=False)
    unit_type_id = db.Column(db.Integer, db.ForeignKey("unit_type.id"))


class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doc_address = db.Column(db.String(20))
    doc_type_id = db.Column(db.Integer, db.ForeignKey("document_type.id"))


class Service_plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #  = db.Column(db.String(20))
    # doc_type_id = db.Column(db.Integer, db.ForeignKey("document_type.id"))


class Service_actual(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #  = db.Column(db.String(20))
    # doc_type_id = db.Column(db.Integer, db.ForeignKey("document_type.id"))


class Service_calibration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #  = db.Column(db.String(20))
    # doc_type_id = db.Column(db.Integer, db.ForeignKey("document_type.id"))


class Department_calibration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #  = db.Column(db.String(20))
    # doc_type_id = db.Column(db.Integer, db.ForeignKey("document_type.id"))


class Service_measure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #  = db.Column(db.String(20))
    # doc_type_id = db.Column(db.Integer, db.ForeignKey("document_type.id"))


class Department_measure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #  = db.Column(db.String(20))
    # doc_type_id = db.Column(db.Integer, db.ForeignKey("document_type.id"))


class Quality_control(db.Model):
    unit_id = db.Column(db.Integer, db.ForeignKey("unit.id"), primary_key=True)
    period_id = db.Column(db.Integer, db.ForeignKey("period.id"), primary_key=True)
    parameter_id = db.Column(
        db.Integer, db.ForeignKey("parameter.id"), primary_key=True
    )
    units = db.relationship("Unit", back_populates="quality_controls")
    periods = db.relationship("Period", back_populates="quality_controls")
    parameters = db.relationship("Parameter", back_populates="quality_controls")


unit_docs = db.Table(
    "unit_docs",
    db.Column("unit_id", db.Integer, primary_key=True),
    db.Column("document_id", db.Integer, primary_key=True),
)
