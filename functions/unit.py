from models.base_model import db
from functions.settings import (
    get_parameter,
    get_unit,
    get_period,
    get_periods,
    get_document_type,
)
from models.settings import (
    Unit,
    Parameter,
    Unit_document,
    Document_type,
    Period,
    Unit_parameter,
    Document,
    Deviation,
)
from sqlalchemy import func
import os


def add_unit_parameter(unit, parameter, period):
    parameter = get_parameter(*parameter.split("*"))
    unit = get_unit(*unit.split(" SN "))
    period = get_period(period)
    unit_parameter = Unit_parameter(unit=unit, parameter=parameter, period=period)
    db.session.add(unit_parameter)
    db.session.commit()


def prepare_unit_parameters(unit):
    unit = get_unit(unit)
    all_parameters = Unit_parameter.query.filter(
        Unit_parameter.unit.has(unit_id=unit.unit_id)
    )
    periods = get_periods()
    result = {}
    for period in periods:
        result[period.period_desc] = all_parameters.filter(
            Unit_parameter.period.has(period_desc=period.period_desc)
        ).all()
    return result


def prepare_rest_unit_parameters(unit):
    unit = get_unit(unit)
    unit_parameters = (
        Unit_parameter.query.join(Parameter)
        .filter(Unit_parameter.unit.has(unit_id=unit.unit_id))
        .with_entities(Parameter.parameter_desc)
        .all()
    )
    unit_parameters = [p[0] for p in unit_parameters]
    parameters = Parameter.query.filter(
        Parameter.parameter_desc.notin_(unit_parameters)
    ).all()
    return parameters


def add_unit_document(unit, document_type, period):
    print(unit, document_type, period)
    document_type = get_document_type(document_type)
    unit = get_unit(unit)
    period = get_period(period)
    unit_document = Unit_document(unit=unit, document_type=document_type, period=period)
    db.session.add(unit_document)
    db.session.commit()


def get_unit_documents(unit):
    unit_documents = (
        Unit_document.query.join(Unit)
        .join(Period)
        .join(Document_type)
        .filter(Unit.unit_desc == unit)
        .with_entities(
            Document_type.document_type_desc,
            func.aggregate_strings(Period.period_desc, ","),
        )
        .group_by(Document_type.document_type_desc)
        .all()
    )
    output = {}
    for unit_document in unit_documents:
        output[unit_document[0]] = []
        for period in unit_document[1].split(","):
            duration = Period.query.filter_by(period_desc=period).first()
            output[unit_document[0]].append(
                ",".join([duration.period_desc] * int((360 / duration.period_duration)))
            )
    return output


def get_all_unit_document_types(unit):
    unit = get_unit(unit)
    unit_documents = (
        Unit_document.query.join(Document_type)
        .join(Unit)
        .filter(unit == unit)
        .with_entities(Document_type.document_type_desc)
        .group_by(Document_type)
        .all()
    )
    return unit_documents


def add_document(
    unit, document_type, period, document_desc, creation_date, valid_year, file
):
    unit = get_unit(unit)
    document_type = get_document_type(document_type)
    period = get_period(period)
    path = (
        str(valid_year)
        + "/"
        + unit.unit_desc.replace(" ", "_")
        + "/"
        + document_type.document_type_desc.replace(" ", "_")
    )
    if not os.path.exists("all_documents/" + path):
        os.makedirs("all_documents/" + path)
    file.filename = creation_date + "_" + document_desc + ".pdf"
    file.save(os.path.join(("all_documents/" + path), file.filename))
    document = Document(
        unit=unit,
        document_type=document_type,
        period=period,
        document_desc=document_desc,
        creation_date=creation_date,
        valid_year=valid_year,
        document_path=path + "/" + file.filename,
    )
    db.session.add(document)
    db.session.commit()


def get_documents(unit, year):
    types = Document_type.query.all()
    periods = Period.query.all()
    result = {}
    for type in types:
        result[type.document_type_desc] = {}
        for period in periods:
            result[type.document_type_desc][period.period_desc] = (
                Document.query.join(Unit, Unit.unit_id == Document.fk_unit)
                .join(
                    Document_type,
                    Document_type.document_type_id == Document.fk_document_type,
                )
                .join(Period, Period.period_id == Document.fk_period)
                .filter(
                    Unit.unit_desc == unit, Period.period_desc == period.period_desc
                )
                .filter(Document_type.document_type_desc == type.document_type_desc)
                .filter(Document.valid_year == year)
                .order_by(Period.period_duration.desc(), Document.creation_date.desc())
                .all()
            )
    print(result)
    return result


def print_period_parameters(data):
    output = {}
    for period, units in data.items():
        if period not in output.keys():
            output[period] = []
        for unit in units:
            full_unit = get_unit(unit)
            unit_parameter = (
                Unit.query.join(Unit_parameter, Unit.unit_id == Unit_parameter.fk_unit)
                .join(Period, Unit_parameter.fk_period == Period.period_id)
                .join(Parameter, Parameter.parameter_id == Unit_parameter.fk_parameter)
                .join(Deviation, Deviation.deviation_id == Parameter.fk_deviation)
                .filter(Period.period_desc == period, Unit.unit_desc == unit)
                .with_entities(Parameter.parameter_desc, Deviation.deviation_desc)
                .all()
            )
            if unit_parameter:
                output[period].append({full_unit: unit_parameter})
    return output


def prepare_docs_for_calendar(year):
    all_docs = (
        Document.query.join(Period, Period.period_id == Document.fk_period)
        .filter(Document.valid_year == year)
        .all()
    )
    result = {}
    for doc in all_docs:
        result[str(doc.creation_date)] = [doc.unit.unit_desc, doc.period.period_desc]
    return result


def documents_per_unit(unit, document_type, year):
    """
    Returns all documents fo a giver unit and year

    Parameters:
        unit: (int) needed unit id
        document_type
        year: (integer)
    """
    types = Document_type.query.all()
    periods = Period.query.all()
    result = {}
    for type in types:
        result[type.document_type_desc] = {}
        for period in periods:
            result[type.document_type_desc][period.period_desc] = (
                Document.query.join(Unit, Unit.unit_id == Document.fk_unit)
                .join(
                    Document_type,
                    Document_type.document_type_id == Document.fk_document_type,
                )
                .join(Period, Period.period_id == Document.fk_period)
                .filter(
                    Unit.unit_desc == unit, Period.period_desc == period.period_desc
                )
                .filter(Document_type.document_type_desc == type.document_type_desc)
                .filter(Document.valid_year == year)
                .order_by(Period.period_duration.desc(), Document.creation_date.desc())
                .all()
            )
    print(result)
    return result
