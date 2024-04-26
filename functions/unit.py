from models.base_model import db
# from models.unit import Unit_Parameter
from functions.settings import get_parameter, get_unit, get_period, get_periods
from models.settings import Unit_parameter
from models.settings import Unit, Parameter, Period


def add_unit_parameter(unit, parameter, period):
    print(unit, parameter, period)
    parameter = get_parameter(*parameter.split('*'))
    unit = get_unit(*unit.split(" SN "))
    period = get_period(period)
    unit_parameter = Unit_parameter(unit=unit, parameter=parameter, period=period)
    db.session.add(unit_parameter)
    db.session.commit()


def prepare_unit_parameters(unit):
    unit = get_unit(*unit.split(" SN "))
    all_parameters = Unit_parameter.query.filter(Unit_parameter.unit.has(unit_id=unit.unit_id))
    periods = get_periods()
    result = {}
    for period in periods:
        result[period.period_desc] = all_parameters.filter(Unit_parameter.period.has(period_desc=period.period_desc)).all()
    print(result)
    return result