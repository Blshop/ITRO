from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class UnitCategory(db.Model):
    __tablename__ = "unit_category"
    unit_category_id = db.Column(db.Integer, primary_key=True)
    unit_category_desc = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return (
            f"<UnitCategory(unit_category_id={self.unit_category_id}, "
            f"unit_category_desc='{self.unit_category_desc}')>"
        )


class UnitCategorySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UnitCategory
        load_instance = True
