from app import db
from app.models import *


def add_deviation(data):
    deviation_shema = DeviationSchema(session=db.session).load(data)
    db.session.add(deviation_shema)
    db.session.commit()


def get_deviation(id=None):
    if id == None:
        deviation = Deviation.query.all()
    else:
        deviation = Deviation.query.filter_by(deviation_id=id).first()
    return DeviationSchema(many=True).dump(deviation)


def add_unit_category(data):
    unit_category_schema = UnitCategorySchema(session=db.session).load(data)
    db.session.add(unit_category_schema)
    db.session.commit()


def get_unit_category(id=None):
    if id == None:
        unit_category = UnitCategory.query.all()
    else:
        unit_category = UnitCategory.query.filter_by(unit_category_id=id)
    return UnitCategorySchema(many=True).dump(unit_category)


def add_parameter(data, filter):
    unit_category = UnitCategorySchema().dump(
        UnitCategory.query.filter_by(unit_category_desc=filter).first()
    )
    data["unit_category"] = unit_category
    parameterSchema = ParameterSchema(session=db.session).load(data)
    db.session.add(parameterSchema)
    db.session.commit()


def get_parameter(filter=None):
    if filter == None:
        parameter = Parameter.query.order_by(Parameter.parameter_desc).all()
    else:
        parameter = (
            Parameter.query.join(
                UnitCategory,
                UnitCategory.unit_category_id == Parameter.fk_unit_category,
            )
            .filter(UnitCategory.unit_category_desc == filter)
            .all()
        )
    return ParameterSchema(many=True).dump(parameter)


def add_period(data):
    periodSchema = PeriodSchema(session=db.session).load(data)
    db.session.add(periodSchema)
    db.session.commit()


def get_period(id=None):
    if id == None:
        period = Period.query.order_by(Period.period_duration).all()
    else:
        period = Period.query.filter_by(period_id=id).first()
    return PeriodSchema(many=True).dump(period)


def add_energy_type(data):
    energy_type_schema = EnergyTypeSchema(session=db.session).load(data)
    db.session.add(energy_type_schema)
    db.session.commit()


def get_energy_type(id=None):
    if id == None:
        energy_type = EnergyType.query.all()
    else:
        energy_type = EnergyType.query.filter_by(energy_type_id=id).first()
    return EnergyTypeSchema(many=True).dump(energy_type)


def add_energy(data):
    energy_schema = EnergySchema(session=db.session).load(data)
    db.session.add(energy_schema)
    db.session.commit()


def get_energy(id=None):
    if id == None:
        energy = Energy.query.all()
    else:
        energy = Energy.query.filter_by(energy_id=id).first()
    return EnergySchema(many=True).dump(energy)


def add_unit_type(data):
    unit_type_schema = UnitTypeSchema(session=db.session).load(data)
    db.session.add(unit_type_schema)
    db.session.commit()


def get_unit_type(id=None):
    if id == None:
        unit_type = UnitType.query.all()
    else:
        unit_type = UnitType.query.filter_by(unit_type_id=id).first()
    return UnitTypeSchema(many=True).dump(unit_type)


def add_unit(data):
    unit = UnitSchema(session=db.session).load(data)
    db.session.add(unit)
    db.session.commit()


def get_unit(filter=None):
    if filter == None:
        unit = Unit.query.all()
    else:
        unit = (
            Unit.query.join(
                UnitCategory, UnitCategory.unit_category_id == Unit.fk_unit_category
            )
            .filter(UnitCategory.unit_category_desc == filter)
            .all()
        )
    return UnitSchema(many=True).dump(unit)


def add_document_type(data):
    document_type_shema = DocumentTypeSchema(session=db.session).load(data)
    db.session.add(document_type_shema)
    db.session.commit()


def get_document_type(id=None):
    if id == None:
        document_type = DocumentType.query.all()
    else:
        document_type = Deviation.query.filter_by(document_type_id=id).first()
    return DocumentTypeSchema(many=True).dump(document_type)


def add_organization(data):
    organization_shema = OrganizationSchema(session=db.session).load(data)
    db.session.add(organization_shema)
    db.session.commit()


def get_organization(id=None):
    if id == None:
        organization = Organization.query.all()
    else:
        organization = Organization.query.filter_by(organization_id=id).first()
    return OrganizationSchema(many=True).dump(organization)
