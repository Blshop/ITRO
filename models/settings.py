from models.base_model import db

class Unit_parameter(db.Model):
    unit_parameter_id = db.Column(db.Integer, primary_key=True)
    fk_unit = db.Column(db.Integer, db.ForeignKey("unit.unit_id"), primary_key=True, nullable=False)
    fk_parameter = db.Column(db.Integer, db.ForeignKey("parameter.parameter_id"),primary_key=True, nullable=False)
    fk_period = db.Column(db.Integer, db.ForeignKey("period.period_id"), primary_key=True, nullable=False)
    unit = db.relationship("Unit", back_populates='unit_parameter')
    parameter = db.relationship("Parameter", back_populates='unit_parameter')
    period = db.relationship("Period", back_populates='unit_parameter')
    


class Deviation(db.Model):
    deviation_id = db.Column(db.Integer, primary_key=True)
    deviation_desc = db.Column(db.String(15), unique=True)
    parameters = db.relationship("Parameter", backref="deviation")


class Parameter(db.Model):
    parameter_id = db.Column(db.Integer, primary_key=True)
    parameter_desc = db.Column(db.String(20))
    fk_deviation = db.Column(
        db.Integer, db.ForeignKey("deviation.deviation_id"), nullable=False
    )
    unit_parameter = db.relationship("Unit_parameter", back_populates='parameter')


class Period(db.Model):
    period_id = db.Column(db.Integer, primary_key=True)
    period_desc = db.Column(db.String(10), unique=True, nullable=False)
    period_duration = db.Column(db.Integer, unique=True, nullable=False)
    unit_parameter = db.relationship("Unit_parameter", back_populates='period')


class Unit(db.Model):
    unit_id = db.Column(db.Integer, primary_key=True)
    unit_desc = db.Column(db.String(20), unique=True, nullable=False)
    unit_sn = db.Column(db.Integer, unique=True, nullable=False)
    unit_parameter = db.relationship("Unit_parameter", back_populates='unit')
    fk_unit_type = db.Column(
        db.Integer, db.ForeignKey("unit_type.unit_type_id"), nullable=False
    )

class Unit_type(db.Model):
    unit_type_id = db.Column(db.Integer, primary_key=True)
    unit_type_desc = db.Column(db.String(30), unique=True)
    units = db.relationship("Unit", backref="unit_type")