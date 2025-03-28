from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields


class UnitType(db.Model):
    __tablename__ = "unit_type"
    unit_type_id = db.Column(db.Integer, primary_key=True)
    unit_type_desc = db.Column(db.String(100), unique=True, nullable=False)
    fk_energy_type = db.Column(db.Integer, db.ForeignKey("energy_type.energy_type_id"))
    energy_type = db.relationship("EnergyType", backref="unit_type", lazy=True)

    def __repr__(self):
        return (
            f"<UnitType(unit_type_id={self.unit_type_id}, "
            f"unit_type_desc='{self.unit_type_desc}', "
            f"fk_energy_type={self.fk_energy_type})>"
        )


class UnitTypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UnitType
        load_instance = True

    energy_type = fields.Related(["energy_type_desc"])
