from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields


class Unit(db.Model):
    __tablename__ = "unit"
    unit_id = db.Column(db.Integer, primary_key=True)
    unit_desc = db.Column(db.String(30), unique=True, nullable=False)
    unit_sn = db.Column(db.String(15))
    fk_unit_type = db.Column(
        db.Integer, db.ForeignKey("unit_type.unit_type_id"), nullable=False
    )
    fk_unit_category = db.Column(
        db.Integer, db.ForeignKey("unit_category.unit_category_id"), nullable=False
    )
    unit_type = db.relationship("UnitType", backref="Unit", lazy=True)
    unit_category = db.relationship("UnitCategory", backref="Unit", lazy=True)

    def __repr__(self):
        return (
            f"<Unit(unit_id={self.unit_id}, "
            f"unit_desc='{self.unit_desc}', "
            f"unit_sn='{self.unit_sn}', "
            f"fk_unit_type={self.fk_unit_type}, "
            f"fk_unit_category={self.fk_unit_category})>"
        )


class UnitSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Unit
        load_instance = True

    unit_type = fields.Related(["unit_type_desc"])
    unit_category = fields.Related(["unit_category_desc"])
