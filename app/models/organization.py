from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Organization(db.Model):
    __tablename__ = "organization"
    organization_id = db.Column(db.Integer, primary_key=True)
    organization_desc = db.Column(db.String(100), unique=True, nullable=False)


class OrganizationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Organization
        load_instance = True
