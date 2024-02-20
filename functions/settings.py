from models.base_model import db
from models.settings import Deviation, Parameter


def add_deviation(deviation_value):
    new_deviation = Deviation(deviation_desc=deviation_value)
    db.session.add(new_deviation)
    db.session.commit()


def get_deviation():
    deviations = Deviation.query.all()
    return deviations


def edit_deviation(new_deviation_desc, old_deviation_desc):
    deviation = Deviation.query.filter(
        Deviation.deviation_desc == old_deviation_desc
    ).first()
    deviation.deviation_desc = new_deviation_desc
    db.session.commit()


def add_parameter(parameter_desc, deviation_desc):
    deviation = Deviation.query.filter(
        Deviation.deviation_desc == deviation_desc
    ).first()
    new_parameter = Parameter(parameter_desc=parameter_desc, deviation=deviation)
    db.session.add(new_parameter)
    db.session.commit()


def get_parameters():
    parameters = Parameter.query.all()
    return parameters


def edit_parameter(_parameter_desc, deviation_desc):
    parameter = Parameter.query.filter(
        Parameter.parameter_id == id,
        Parameter.deviation.deviation_desc == old_deviation_desc,
    ).first()
    parameter.parameter_desc = parameter_desc
    if (
        parameter.deviation.deviation_desc != deviation_desc
        or parameter.parameter_desc != parameter_desc
    ):
        deviation = Deviation.query.filter(
            Deviation.deviation_desc == deviation_desc
        ).first()
        parameter.deviation = deviation
    db.session.commit()
