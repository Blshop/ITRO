from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Period(db.Model):
    __tablename__ = "period"
    period_id = db.Column(db.Integer, primary_key=True)
    period_desc = db.Column(db.String(20), unique=True, nullable=False)
    period_duration = db.Column(db.Integer, unique=True, nullable=False)


class PeriodSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Period
        load_instance = True
