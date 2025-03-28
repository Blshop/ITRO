from app import db
from app.models import *
from app.services.settings import get_unit
from sqlalchemy import func
import os
from flask import jsonify, json
from datetime import datetime


def add_unit_parameter(data, unit_id):
    unit = UnitSchema().dump(Unit.query.filter_by(unit_id=unit_id).first())
    data["unit"] = unit
    unit_parameter = UnitParameterSchema(session=db.session).load(data)
    db.session.add(unit_parameter)
    db.session.commit()


def get_unit_parameter(id):
    unit_parameter = (
        UnitParameter.query.join(Unit, UnitParameter.fk_unit == Unit.unit_id)
        .join(Period, UnitParameter.fk_period == Period.period_id)
        .filter(Unit.unit_id == id)
        .order_by(Period.period_duration)
        .all()
    )
    return UnitParameterSchema(many=True).dump(unit_parameter)


def print_unit_parameters(data):
    result = {}
    for unit, periods in data["unit"].items():
        if not periods:
            continue
        model_unit = Unit.query.filter_by(unit_desc=unit).first()
        unit_type = model_unit.unit_type.unit_type_desc
        result[unit] = {}
        result[unit][unit_type] = {}
        parameter_subquery = (
            UnitParameter.query.join(Unit, Unit.unit_id == UnitParameter.fk_unit)
            .join(Period, Period.period_id == UnitParameter.fk_period)
            .join(UnitType, Unit.fk_unit_type == UnitType.unit_type_id)
            .join(Parameter, Parameter.parameter_id == UnitParameter.fk_parameter)
            .join(Deviation, Deviation.deviation_id == Parameter.fk_deviation)
            .filter(Unit.unit_desc == unit)
            .with_entities(
                Parameter.parameter_desc,
                Deviation.deviation_desc,
                Unit.unit_desc,
                Period.period_desc,
            )
            .subquery()
        )
        for period in periods:
            period_parameters = (
                db.session.query(parameter_subquery).filter_by(period_desc=period).all()
            )
            if period_parameters:
                result[unit][unit_type][period] = [
                    [item[0], item[1]] for item in period_parameters
                ]
    return result


# def prepare_rest_unit_parameters(unit):
#     unit = get_unit(unit)
#     unit_parameters = (
#         Unit_parameter.query.join(Parameter)
#         .filter(Unit_parameter.unit.has(unit_id=unit.unit_id))
#         .with_entities(Parameter.parameter_desc)
#         .all()
#     )
#     unit_parameters = [p[0] for p in unit_parameters]
#     parameters = Parameter.query.filter(
#         Parameter.parameter_desc.notin_(unit_parameters)
#     ).all()
#     return parameters


# def add_unit_document(unit, document_type, period):
#     print(unit, document_type, period)
#     document_type = get_document_type(document_type)
#     unit = get_unit(unit)
#     period = get_period(period)
#     unit_document = Unit_document(unit=unit, document_type=document_type, period=period)
#     db.session.add(unit_document)
#     db.session.commit()


# def get_unit_documents(unit):
#     unit_documents = (
#         Unit_document.query.join(Unit)
#         .join(Period)
#         .join(Document_type)
#         .filter(Unit.unit_desc == unit)
#         .with_entities(
#             Document_type.document_type_desc,
#             func.aggregate_strings(Period.period_desc, ","),
#         )
#         .group_by(Document_type.document_type_desc)
#         .all()
#     )
#     output = {}
#     for unit_document in unit_documents:
#         output[unit_document[0]] = []
#         for period in unit_document[1].split(","):
#             duration = Period.query.filter_by(period_desc=period).first()
#             output[unit_document[0]].append(
#                 ",".join([duration.period_desc] * int((360 / duration.period_duration)))
#             )
#     return output


# def get_all_unit_document_types(unit):
#     unit = get_unit(unit)
#     unit_documents = (
#         Unit_document.query.join(Document_type)
#         .join(Unit)
#         .filter(unit == unit)
#         .with_entities(Document_type.document_type_desc)
#         .group_by(Document_type)
#         .all()
#     )
#     return unit_documents


def add_document(
    unit_desc,
    document_type_desc,
    period_desc,
    organization_desc,
    document_desc,
    creation_date,
    file,
    valid_year=0,
):
    print(document_desc)
    unit = Unit.query.filter(Unit.unit_desc == unit_desc).first()
    document_type = DocumentType.query.filter_by(
        document_type_desc=document_type_desc
    ).first()
    period = Period.query.filter_by(period_desc=period_desc).first()
    organization = Organization.query.filter_by(
        organization_desc=organization_desc
    ).first()
    date_object = datetime.strptime(creation_date, "%Y-%m-%d")
    if valid_year == 0:
        valid_year = date_object.year
    document_path = (
        unit_desc.replace(" ", "_") + "/" + document_type_desc.replace(" ", "_")
    )
    document_name = creation_date + ".pdf"
    path = str(valid_year) + "/" + document_path + "/"
    if not os.path.exists("all_documents/" + path):
        os.makedirs("all_documents/" + path)
    file.filename = document_name
    while True:
        if os.path.exists("all_documents/" + path + file.filename):
            file.filename = (
                os.path.splitext(
                    os.path.basename("all_documents/" + path + file.filename)
                )[0]
                + "(1)"
                + ".pdf"
            )
        else:
            break
    file.save(os.path.join("all_documents/" + path, file.filename))
    document = Document(
        unit=unit,
        document_type=document_type,
        period=period,
        organization=organization,
        document_desc=document_desc,
        date_creation=creation_date,
        year_creation=valid_year,
        document_path=path + file.filename,
    )
    db.session.add(document)
    db.session.commit()


def get_document(unit, document_type, year):
    unit = list(unit.split(","))
    document_type = list(document_type.split(","))
    documents = (
        Document.query.join(Unit, Unit.unit_id == Document.fk_unit)
        .join(DocumentType, DocumentType.document_type_id == Document.fk_document_type)
        .filter(
            Unit.unit_id.in_(unit),
            DocumentType.document_type_id.in_(document_type),
            Document.year_creation == year,
        )
        .all()
    )
    return DocumentSchema(many=True).dump(documents)


def delete_document(path):
    document = Document.query.filter_by(document_path=path).first()
    db.session.delete(document)
    db.session.commit()


def set_associacion(unit_id, document_data, organization_data):
    all_docs = (
        DocumentTypePeriod.query.join(Unit, Unit.unit_id == DocumentTypePeriod.fk_unit)
        .filter_by(unit_id=unit_id)
        .all()
    )
    for doc in all_docs:
        if doc.document_type.document_type_desc in document_data.keys():
            if (
                doc.period.period_desc
                in document_data[doc.document_type.document_type_desc]
            ):
                document_data[doc.document_type.document_type_desc].remove(
                    doc.period.period_desc
                )
            else:
                db.session.delete(doc)
                db.session.commit()

    for doc, periods in document_data.items():
        for period in periods:
            if period:
                data = {"unit": unit_id, "document_type": doc, "period": period}
                print(data)
                new_doc = DocumentTypePeriodSchema(session=db.session).load(data)
                db.session.add(new_doc)
            db.session.commit()

    all_orgs = (
        DocumentTypeOrganization.query.join(
            Unit, Unit.unit_id == DocumentTypeOrganization.fk_unit
        )
        .filter_by(unit_id=unit_id)
        .all()
    )
    for org in all_orgs:
        if org.document_type.document_type_desc in organization_data.keys():
            if (
                org.organization.organization_desc
                in organization_data[org.document_type.document_type_desc]
            ):
                organization_data[org.document_type.document_type_desc].remove(
                    org.organization.organization_desc
                )
            else:
                db.session.delete(org)
                db.session.commit()

    for doc, organizations in organization_data.items():
        for organization in organizations:
            if organization:
                data = {
                    "unit": unit_id,
                    "document_type": doc,
                    "organization": organization,
                }
                print(data)
                new_org = DocumentTypeOrganizationSchema(session=db.session).load(data)
                db.session.add(new_org)
            db.session.commit()


def get_associacion(unit_id):
    all_docs = (
        DocumentTypePeriod.query.join(Unit, Unit.unit_id == DocumentTypePeriod.fk_unit)
        .filter_by(unit_id=unit_id)
        .all()
    )
    all_orgs = (
        DocumentTypeOrganization.query.join(
            Unit, Unit.unit_id == DocumentTypeOrganization.fk_unit
        )
        .filter_by(unit_id=unit_id)
        .all()
    )
    return {
        "documents": DocumentTypePeriodSchema(many=True).dump(all_docs),
        "organizations": DocumentTypeOrganizationSchema(many=True).dump(all_orgs),
    }
