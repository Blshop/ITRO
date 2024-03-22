from models.base_model import db
from models.unit import Unit_Parameter
from functions.settings import get_parameter, get_unit, get_period


def add_unit_parameter(unit, parameter, period):
    parameter = get_parameter(parameter.split(' '))
    unit = get_unit(unit.split(" "))
    period = get_period(period)
    unit_parameter = Unit_Parameter(unit, parameter, period)
    db.session.add(unit_parameter)
    db.commit()

