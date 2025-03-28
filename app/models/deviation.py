from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Deviation(db.Model):
    __tablename__ = "deviation"
    deviation_id = db.Column(db.Integer, primary_key=True)
    deviation_desc = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return f"<Deviation(deviation_id={self.deviation_id}, deviation_desc='{self.deviation_desc}')>"


class DeviationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Deviation
        load_instance = True
