from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Deviation(db.Model):
    __tablename__ = "deviation"
    deviation_id = db.Column(db.Integer, primary_key=True)
    deviation_desc = db.Column(db.String(30), unique=True, nullable=False)


class DeviationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Deviation
        load_instance = True
