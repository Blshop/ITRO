from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields


class Parameter(db.Model):
    __tablename__ = "parameter"
    parameter_id = db.Column(db.Integer, primary_key=True)
    parameter_desc = db.Column(db.String(100), nullable=False)
    fk_deviation = db.Column(
        db.Integer, db.ForeignKey("deviation.deviation_id"), nullable=False
    )
    fk_unit_category = db.Column(
        db.Integer, db.ForeignKey("unit_category.unit_category_id"), nullable=False
    )
    deviation = db.relationship("Deviation", backref="parameter", lazy=True)
    unit_category = db.relationship("UnitCategory", backref="parameter", lazy=True)

    def __repr__(self):
        return (
            f"<Parameter(parameter_id={self.parameter_id}, "
            f"parameter_desc='{self.parameter_desc}', "
            f"fk_deviation={self.fk_deviation}, "
            f"fk_unit_category={self.fk_unit_category})>"
        )


class ParameterSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Parameter
        load_instance = True

    deviation = fields.Related(["deviation_desc"])
    unit_category = fields.Related(["unit_category_desc"])
