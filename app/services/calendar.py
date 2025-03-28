from app import db
from app.models import *
from app.services.settings import get_unit
from sqlalchemy import func
import os
from flask import jsonify, json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


def get_unit_doc(unit_desc):
    docs = (
        DocumentTypePeriod.query.join(Unit, Unit.unit_id == DocumentTypePeriod.fk_unit)
        .filter_by(unit_desc=unit_desc)
        .all()
    )
    return DocumentTypePeriodSchema(many=True).dump(docs)


def get_org_doc(doc_desc, unit_desc):
    print(doc_desc, unit_desc)
    periods = (
        DocumentTypePeriod.query.join(
            DocumentType,
            DocumentType.document_type_id == DocumentTypePeriod.fk_document_type,
        )
        .join(Unit, Unit.unit_id == DocumentTypePeriod.fk_unit)
        .filter(
            DocumentType.document_type_desc == doc_desc, Unit.unit_desc == unit_desc
        )
        .all()
    )

    orgs = (
        DocumentTypeOrganization.query.join(
            DocumentType,
            DocumentType.document_type_id == DocumentTypeOrganization.fk_document_type,
        )
        .join(Unit, Unit.unit_id == DocumentTypeOrganization.fk_unit)
        .filter(
            DocumentType.document_type_desc == doc_desc, Unit.unit_desc == unit_desc
        )
        .all()
    )

    return {
        "periods": DocumentTypePeriodSchema(many=True).dump(periods),
        "organizations": DocumentTypeOrganizationSchema(many=True).dump(orgs),
    }


def alerts():
    all_units = Unit.query.all()
    result = []
    for unit in all_units:
        required_docs = (
            DocumentTypePeriod.query.join(
                Unit, Unit.unit_id == DocumentTypePeriod.fk_unit
            )
            .join(Period, Period.period_id == DocumentTypePeriod.fk_period)
            .filter(Unit.unit_desc == unit.unit_desc, Period.period_duration > 30)
            .all()
        )
        for doc in required_docs:
            required_doc = (
                Document.query.join(
                    DocumentType,
                    DocumentType.document_type_id == Document.fk_document_type,
                )
                .join(Period, Period.period_id == Document.fk_period)
                .join(Unit, Unit.unit_id == Document.fk_unit)
                .filter(
                    DocumentType.document_type_desc
                    == doc.document_type.document_type_desc,
                    Unit.unit_desc == unit.unit_desc,
                    Period.period_duration >= doc.period.period_duration,
                )
                .with_entities(Document.date_creation)
                .order_by(Document.date_creation.desc())
                .first()
            )
            message = ""
            current_date = datetime.now().date()

            if required_doc:
                month = doc.period.period_duration // 30
                next_date = required_doc.date_creation + relativedelta(months=month)
                diff_date = next_date - current_date
                print(current_date, next_date, diff_date)
                if diff_date > timedelta(days=10):
                    message = "OK"
                elif diff_date <= timedelta(days=10) and diff_date >= timedelta(days=0):
                    message = "waiting"
                elif diff_date <= timedelta(days=0) and diff_date >= timedelta(
                    days=-10
                ):
                    message = "warning"
                else:
                    message = "error"
                if message != "OK":
                    result.append(
                        [
                            unit.unit_desc,
                            doc.document_type.document_type_desc,
                            doc.period.period_desc,
                            message,
                        ]
                    )
    return result
