from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class Organization(db.Model):
    __tablename__ = "organization"
    organization_id = db.Column(db.Integer, primary_key=True)
    organization_desc = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return (
            f"<Organization(organization_id={self.organization_id}, "
            f"organization_desc='{self.organization_desc}')>"
        )


class OrganizationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Organization
        load_instance = True
