from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields


class UnitParameter(db.Model):
    __tablename__ = "unit_parameter"
    unit_parameter_id = db.Column(db.Integer, primary_key=True)
    fk_unit = db.Column(db.Integer, db.ForeignKey("unit.unit_id"), nullable=False)
    fk_parameter = db.Column(
        db.Integer,
        db.ForeignKey("parameter.parameter_id"),
        nullable=False,
    )
    fk_period = db.Column(db.Integer, db.ForeignKey("period.period_id"), nullable=False)
    parameter = db.relationship("Parameter", backref="unit_parameter", lazy=True)
    period = db.relationship("Period", backref="unit_parameter", lazy=True)
    unit = db.relationship("Unit", backref="unit_parameter", lazy=True)

    def __repr__(self):
        return (
            f"<UnitParameter(unit_parameter_id={self.unit_parameter_id}, "
            f"fk_unit={self.fk_unit}, "
            f"fk_parameter={self.fk_parameter}, "
            f"fk_period={self.fk_period})>"
        )


class UnitParameterSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UnitParameter
        load_instance = True

    parameter = fields.Related(["parameter_desc"])
    period = fields.Related(["period_desc"])
    unit = fields.Related(["unit_desc"])
