from models.models import db
from sqlalchemy import func


def get_unit(id):
    unit = Unit.query.filter_by(id=id).first()
    return unit


def gather_info(data):
    result = []
    for id, periods in data.items():
        unit = get_unit(id)
        unit = {
            "unit_type": unit.unit_type.unit_type_desc,
            "unit": unit.unit_desc,
            "serial": unit.serial_number,
        }
        param = []

        for period in periods:
            per = {}
            per["period"] = period
            parameters = (
                Quality_control.query.join(Unit, Period, Parameter)
                .filter(Unit.id == id, Period.period_desc == period)
                .all()
            )
            per["data"] = []
            for parameter in parameters:
                per["data"].append(parameter.parameters.parameter_desc)
            param.append(per)
        result.append((unit, param))
    return result


def menu():
    sq = db.session.query(Unit_type.unit_type_desc, Unit).join(Unit).subquery()
    print(db.session.query(sq).all())
    units = (
        db.session.query(sq.c.unit_type_desc, func.count(sq.c.unit_type_desc))
        .group_by(sq.c.unit_type_desc)
        .all()
    )
    print(units)
    result = {}
    for unit in units:
        result[unit[0]] = [
            (x[0], x[1])
            for x in db.session.query(sq.c.unit_desc, sq.c.id)
            .filter(sq.c.unit_type_desc == unit[0])
            .all()
        ]
    print(result)
    return result
