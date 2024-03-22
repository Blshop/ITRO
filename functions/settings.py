from models.base_model import db
from models.settings import Deviation, Parameter, Period, Unit, Unit_Parameter


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
        Parameter.fk_deviation.deviation_desc == deviation_desc,
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


def add_unit(unit_desc, unit_sn):
    new_unit = Unit(unit_desc=unit_desc, unit_sn=unit_sn)
    db.session.add(new_unit)
    db.session.commit()


def get_unit(unit_desc, unit_sn):
    unit = Unit.query.filter(Unit.unit_desc==unit_desc, Unit.unit_sn==unit_sn).first()
    return unit

def get_units():
    units = Unit.query.all()
    return units


def update_unit(new_unit_desc, new_unit_sn, id):
    unit = Unit.query.filter(Unit.unit_id == id).first()
    unit.unit_desc = new_unit_desc
    unit.unit_sn = new_unit_sn
    db.session.commit()
