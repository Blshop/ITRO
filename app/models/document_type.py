from app import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


class DocumentType(db.Model):
    __tablename__ = "document_type"
    document_type_id = db.Column(db.Integer, primary_key=True)
    document_type_desc = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f"<DocumentType(document_type_id={self.document_type_id}, document_type_desc='{self.document_type_desc}')>"


class DocumentTypeSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DocumentType
        load_instance = True
