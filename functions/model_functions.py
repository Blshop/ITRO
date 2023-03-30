from models import (
    db,
    Unit_type,
    Period,
    Deviation,
    Document_type,
    Source_type,
    Parameter,
    Source_energy,
    Quality_control,
    Unit,
    Equipment_type,
)

# unit_types functions
def add_unit_type(unit_type):
    new_unit_type = Unit_type(unit_type_desc=unit_type)
    db.session.add(new_unit_type)
    db.session.commit()


def get_unit_type():
    unit_types = Unit_type.query.all()
    return unit_types


def edit_unit_type(new_unit_type, id):
    unit_type = Unit_type.query.filter(Unit_type.id == id).first()
    unit_type.unit_type_desc = new_unit_type
    db.session.commit()


# period functions
def add_period(period_desc, days_number):
    new_period = Period(period_desc=period_desc, days_number=days_number)
    db.session.add(new_period)
    db.session.commit()


def get_period():
    periods = Period.query.order_by(Period.days_number.asc()).all()
    return periods


def edit_period(period_desc, days_number, id):
    period = Period.query.filter(Period.id == id).first()
    period.period_desc = period_desc
    period.days_number = days_number
    db.session.commit()


# deviation functions
def add_deviation(deviation_value):
    new_deviation = Deviation(deviation_value=deviation_value)
    db.session.add(new_deviation)
    db.session.commit()


def get_deviation():
    deviations = Deviation.query.all()
    return deviations


def edit_deviation(deviation_value, id):
    deviation = Deviation.query.filter(Deviation.id == id).first()
    deviation.deviation_value = deviation_value
    db.session.commit()


# document_types functions
def add_document_type(document_type):
    new_document_type = Document_type(document_type_desc=document_type)
    db.session.add(new_document_type)
    db.session.commit()


def get_document_type():
    document_types = Document_type.query.all()
    return document_types


def edit_document_type(new_document_type, id):
    document_type = Document_type.query.filter(Document_type.id == id).first()
    document_type.document_type_desc = new_document_type
    db.session.commit()


# source_types functions
def add_source_type(source_type):
    new_source_type = Source_type(source_type_desc=source_type)
    db.session.add(new_source_type)
    db.session.commit()


def get_source_type():
    source_types = Source_type.query.all()
    return source_types


def edit_source_type(new_source_type, id):
    source_type = Source_type.query.filter(Source_type.id == id).first()
    source_type.source_type_desc = new_source_type
    db.session.commit()


# parameter functions
def add_parameter(parameter_desc, deviation_value):
    deviation = Deviation.query.filter(
        Deviation.deviation_value == deviation_value
    ).first()
    new_parameter = Parameter(parameter_desc=parameter_desc, deviation=deviation)
    db.session.add(new_parameter)
    db.session.commit()


def get_parameters():
    parameters = Parameter.query.all()
    return parameters


def edit_parameter(parameter_desc, deviation_value, id):
    parameter = Parameter.query.filter(Parameter.id == id).first()
    parameter.parameter_desc = parameter_desc
    if parameter.deviation.deviation_value != deviation_value:
        deviation = Deviation.query.filter(
            Deviation.deviation_value == deviation_value
        ).first()
        parameter.deviation = deviation
    db.session.commit()


# source_energy functions
def add_source_energy(source_energy_desc, source_type):
    source_type = Source_type.query.filter(
        Source_type.source_type_desc == source_type
    ).first()
    new_source_energy = Parameter(
        source_energy_desc=source_energy_desc, source_type=source_type
    )
    db.session.add(new_source_energy)
    db.session.commit()


def get_source_energies():
    source_energies = Source_energy.query.all()
    return source_energies


def edit_source_energy(parameter_desc, source_type, id):
    parameter = Source_energy.query.filter(Source_energy.id == id).first()
    parameter.parameter_desc = parameter_desc
    if parameter.deviation.deviation_value != source_type:
        deviation = Source_type.query.filter(
            Source_type.source_type_desc == source_type
        ).first()
        parameter.deviation = deviation
    db.session.commit()


# unit functions
def add_unit(unit_desc, serial_number, unit_type_desc):
    unit_type = Unit_type.query.filter(
        Unit_type.unit_type_desc == unit_type_desc
    ).first()
    new_unit = Unit(
        unit_desc=unit_desc, serial_number=serial_number, unit_type=unit_type
    )
    db.session.add(new_unit)
    db.session.commit()


def get_unit():
    units = Unit.query.all()
    return units


def edit_unit(unit_desc, serial_number, unit_type_desc, id):
    unit = Unit.query.filter(Unit.id == id).first()
    unit.unit_desc = unit_desc
    unit.serial_number = serial_number
    if unit.unit_type != unit_type_desc:
        unit_type = Unit_type.query.filter(
            Unit_type.unit_type_desc == unit_type_desc
        ).first()
        unit.unit_type = unit_type
    db.session.commit()


# quality_control functions
def set_quality_control(parameter_desc, period_desc, id):
    period = Period.query.filter(Period.period_desc == period_desc).first()
    parameter = Parameter.query.filter(
        Parameter.parameter_desc == parameter_desc
    ).first()
    unit = Unit.query.filter(Unit.id == id).first()
    new_quaity_control = Quality_control(
        units=unit, parameters=parameter, periods=period
    )
    db.session.add(new_quaity_control)
    db.session.commit()


def get_quality_control(id):
    periods = (
        x
        for x, in Quality_control.query.join(Unit, Period)
        .filter(Unit.id == id)
        .with_entities(Period.period_desc)
        .distinct()
        .all()
    )
    unit_control = {}
    for period in periods:
        parameters = (
            Quality_control.query.join(Unit, Period, Parameter)
            .filter(Unit.id == id, Period.period_desc == period)
            .with_entities(Parameter.parameter_desc)
            .all()
        )
        unit_control[period] = enumerate([x for x, in parameters])

    return unit_control


def get_protocols():
    units = Unit.query.all()
    table = {}
    for unit in units:
        table[unit.unit_desc] = [
            unit.id,
            [
                x
                for x, in Quality_control.query.join(Unit, Period)
                .filter(Unit.unit_desc == unit.unit_desc)
                .with_entities(Period.period_desc)
                .distinct()
                .all()
            ],
        ]
    return table


def gather_info(id, period):
    unit = Unit.query.filter(Unit.id == id).first()
    params = (
        Quality_control.query.join(Unit, Period, Parameter)
        .filter(Unit.id == id, Period.id == period)
        .all()
    )
    params = [x.parameters.parameter_desc for x in params]
    info = {"name": unit.unit_desc, "serial": unit.serial_number, "parameters": params}
    return info


# equipment_type functions
def add_equipment_type(equipment_type_desc):
    new_equipment_types = Equipment_type(equipment_type_desc=equipment_type_desc)
    db.session.add(new_equipment_types)
    db.session.commit()


def get_equipment_type():
    equipment_types = Equipment_type.query.all()
    return equipment_types
