COPY "deviation"(deviation_id, deviation_desc)
FROM 'C:\projects\ITRO\SQL\data\raw_data\deviation.csv'
DELIMITER ','
CSV HEADER;
SELECT setval(pg_get_serial_sequence('deviation', 'deviation_id'), (SELECT MAX(deviation_id) FROM "deviation") + 1);

COPY "document_type"(document_type_id, document_type_desc)
FROM 'C:\projects\ITRO\SQL\data\raw_data\document_type.csv'
DELIMITER ','
CSV HEADER;
SELECT setval(pg_get_serial_sequence('document_type', 'document_type_id'), (SELECT MAX(document_type_id) FROM "document_type") + 1);

COPY "energy_type"(energy_type_id, energy_type_desc)
FROM 'C:\projects\ITRO\SQL\data\raw_data\energy_type.csv'
DELIMITER ','
CSV HEADER;
SELECT setval(pg_get_serial_sequence('energy_type', 'energy_type_id'), (SELECT MAX(energy_type_id) FROM "energy_type") + 1);

COPY "period"(period_id, period_desc, period_duration)
FROM 'C:\projects\ITRO\SQL\data\raw_data\period.csv'
DELIMITER ','
CSV HEADER;
SELECT setval(pg_get_serial_sequence('period', 'period_id'), (SELECT MAX(period_id) FROM "period") + 1);

COPY "unit_category"(unit_category_id, unit_category_desc)
FROM 'C:\projects\ITRO\SQL\data\raw_data\unit_category.csv'
DELIMITER ','
CSV HEADER;
SELECT setval(pg_get_serial_sequence('unit_category', 'unit_category_id'), (SELECT MAX(unit_category_id) FROM "unit_category") + 1);

COPY "unit_type"(unit_type_id, unit_type_desc, fk_energy_type)
FROM 'C:\projects\ITRO\SQL\data\raw_data\unit_type.csv'
DELIMITER ','
CSV HEADER;
SELECT setval(pg_get_serial_sequence('unit_type', 'unit_type_id'), (SELECT MAX(unit_type_id) FROM "unit_type") + 1);

COPY "energy"(energy_id, energy_desc, half_life,fk_energy_type)
FROM 'C:\projects\ITRO\SQL\data\raw_data\energy.csv'
DELIMITER ','
CSV HEADER;
SELECT setval(pg_get_serial_sequence('energy', 'energy_id'), (SELECT MAX(energy_id) FROM "energy") + 1);

COPY "unit"(unit_id, unit_desc, unit_sn, fk_unit_type, fk_unit_category)
FROM 'C:\projects\ITRO\SQL\data\raw_data\unit.csv'
DELIMITER ','
CSV HEADER;
SELECT setval(pg_get_serial_sequence('unit', 'unit_id'), (SELECT MAX(unit_id) FROM "unit") + 1);

COPY "parameter"(parameter_id, parameter_desc, fk_deviation, fk_unit_category)
FROM 'C:\projects\ITRO\SQL\data\raw_data\parameter.csv'
DELIMITER ','
CSV HEADER;
SELECT setval(pg_get_serial_sequence('parameter', 'parameter_id'), (SELECT MAX(parameter_id) FROM "parameter") + 1);

COPY "unit_parameter"(unit_parameter_id, fk_unit, fk_parameter, fk_period)
FROM 'C:\projects\ITRO\SQL\data\raw_data\unit_parameter.csv'
DELIMITER ','
CSV HEADER;
SELECT setval(pg_get_serial_sequence('unit_parameter', 'unit_parameter_id'), (SELECT MAX(unit_parameter_id) FROM "unit_parameter") + 1);

COPY "organization"(organization_id, organization_desc)
FROM 'C:\projects\ITRO\SQL\data\raw_data\organization.csv'
DELIMITER ','
CSV HEADER;
SELECT setval(pg_get_serial_sequence('organization', 'organization_id'), (SELECT MAX(organization_id) FROM "organization") + 1);





