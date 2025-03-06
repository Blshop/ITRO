from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class EnergyType(db.Model):
    __tablename__ = "energy_type"
    energy_type_id = db.Column(db.Integer, primary_key=True)
    energy_type_desc = db.Column(db.String(30), unique=True, nullable=False)


class EnergyTypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EnergyType
        load_instance = True
