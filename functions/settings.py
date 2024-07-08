from models.base_model import db
from models.settings import Deviation, Parameter, Period, Unit, Unit_parameter, Unit_type, Document_type


def add_deviation(deviation_desc):
    new_deviation = Deviation(deviation_desc=deviation_desc)
    db.session.add(new_deviation)
    db.session.commit()


def get_deviation(deviation_desc):
    deviation = Deviation.query.filter(Deviation.deviation_desc == deviation_desc).first()
    return deviation


def get_deviations():
    deviations = Deviation.query.all()
    return deviations


def update_deviation(new_deviation_desc, id):
    deviation = Deviation.query.filter(Deviation.deviation_id == id).first()
    deviation.deviation_desc = new_deviation_desc
    db.session.commit()


def add_parameter(parameter_desc, deviation_desc):
    deviation = Deviation.query.filter(
        Deviation.deviation_desc == deviation_desc
    ).first()
    new_parameter = Parameter(parameter_desc=parameter_desc, deviation=deviation)
    db.session.add(new_parameter)
    db.session.commit()


def get_parameter(parameter_desc, deviation_desc):
    parameter = Parameter.query.filter(
        Parameter.parameter_desc == parameter_desc,
        Deviation.deviation_desc == deviation_desc,
    ).first()
    return parameter


def get_parameters():
    parameters = Parameter.query.all()
    return parameters


def update_parameter(new_parameter_desc, new_deviation_desc, id):
    deviation = get_deviation(new_deviation_desc)
    parameter = Parameter.query.filter_by(parameter_id=id).first()
    parameter.parameter_desc = new_parameter_desc
    parameter.deviation = deviation
    db.session.commit()


def add_period(period_desc, period_duration):
    new_period = Period(period_desc=period_desc, period_duration=period_duration)
    db.session.add(new_period)
    db.session.commit()


def get_period(period_desc):
    period = Period.query.filter(Period.period_desc==period_desc).first()
    return period


def get_periods():
    periods = Period.query.all()
    return periods


def update_period(new_period_desc, new_period_duration, id):
    period = Period.query.filter(Period.period_id == id).first()
    period.period_desc = new_period_desc
    period.period_duration = new_period_duration
    db.session.commit()


def add_unit(unit_desc, unit_sn, unit_type_desc):
    unit_type = get_unit_type(unit_type_desc)
    new_unit = Unit(unit_desc=unit_desc, unit_sn=unit_sn, unit_type=unit_type)
    db.session.add(new_unit)
    db.session.commit()


def get_unit(unit_desc):
    unit = Unit.query.filter(Unit.unit_desc==unit_desc).first()
    return unit

def get_units():
    units = Unit.query.all()
    return units


def update_unit(new_unit_desc, new_unit_sn, id):
    unit = Unit.query.filter(Unit.unit_id == id).first()
    unit.unit_desc = new_unit_desc
    unit.unit_sn = new_unit_sn
    db.session.commit()


def add_unit_type(unit_type_desc):
    new_unit_type = Unit_type(unit_type_desc=unit_type_desc)
    db.session.add(new_unit_type)
    db.session.commit()


def get_unit_type(unit_type_desc):
    unit_type = Unit_type.query.filter(Unit_type.unit_type_desc == unit_type_desc).first()
    return unit_type


def get_unit_types():
    unit_types = Unit_type.query.all()
    return unit_types


def update_unit_type(new_unit_type, id):
    unit_type = Unit_type.query.filter(Unit_type.unit_type_id == id).first()
    unit_type.unit_type_id = new_unit_type
    db.session.commit()


def add_document_type(document_type_desc):
    new_parameter = Document_type(document_type_desc=document_type_desc)
    db.session.add(new_parameter)
    db.session.commit()


def get_document_type(document_type_desc):
    document_type = Document_type.query.filter(
        Document_type.document_type_desc == document_type_desc,
    ).first()
    return document_type


def get_document_types():
    document_types = Document_type.query.all()
    return document_types


def update_document_type(new_document_type_desc, id):
    parameter = Document_type.query.filter_by(document_type_id=id).first()
    parameter.document_type_desc = new_document_type_desc
    db.session.commit()