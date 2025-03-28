from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, fields


class Energy(db.Model):
    __tablename__ = "energy"
    energy_id = db.Column(db.Integer, primary_key=True)
    energy_desc = db.Column(db.String(30), unique=True)
    half_life = db.Column(db.Float, default=0)
    fk_energy_type = db.Column(
        db.Integer, db.ForeignKey("energy_type.energy_type_id"), nullable=False
    )
    energy_type = db.relationship("EnergyType", backref="energy", lazy=True)

    def __repr__(self):
        return (
            f"<Energy(energy_id={self.energy_id}, "
            f"energy_desc='{self.energy_desc}', "
            f"half_life={self.half_life}, "
            f"fk_energy_type={self.fk_energy_type})>"
        )


class EnergySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Energy
        load_instance = True

    energy_type = fields.Related(["energy_type_desc"])
