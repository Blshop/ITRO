--All SQL required for databse creation

--Deviation determines how much parameter can deviate from set value
CREATE TABLE deviation(
	deviation_id serial PRIMARY KEY,
	deviation_desc varchar(30) UNIQUE NOT NULL
);

--Parameters of units required to be checked regularly
CREATE TABLE "parameter"(
	parameter_id serial PRIMARY KEY,
	parameter_desc varchar(100) NOT NULL,
	fk_deviation int REFERENCES deviation(deviation_id),
	UNIQUE (parameter_desc, fk_deviation)
);

--type of units used in patients treatments
CREATE TABLE unit_type(
	unit_type_id serial PRIMARY KEY,
	unit_type_desc varchar(100) UNIQUE NOT NULL
);


--Units use to treat patients
--correct unit_desc unique constraint
CREATE TABLE unit(
	unit_id serial PRIMARY KEY,
	unit_desc varchar(30) NOT NULL,
	unit_sn varchar(15) NOT NULL,
	fk_unit_type int REFERENCES unit_type(unit_type_id) NOT NULL,
	UNIQUE (unit_desc, unit_sn)
);

--Intervals for various types of checks. documents and so on
--add period_duration unique constraint
CREATE TABLE "period"(
	period_id serial PRIMARY KEY,
	period_desc varchar(20) UNIQUE NOT NULL,
	period_duration int NOT NULL
);

--association of units and parameters to check at agiven period
--add unique constraint
CREATE TABLE unit_parameter(
	unit_parameter_id serial PRIMARY KEY,
	fk_unit int REFERENCES unit(unit_id) NOT NULL,
	fk_parameter int REFERENCES "parameter"(parameter_id) NOT NULL,
	fk_period int REFERENCES "period"(period_id) NOT NULL
);

--types of document stored in database
CREATE TABLE document_type(
	document_type_id serial PRIMARY KEY,
	document_type_desc varchar(50) UNIQUE NOT NULL
);

--documents to check progress per unit during a year 
CREATE TABLE unit_document_check(
	unit_document_check_id serial PRIMARY KEY,
	fk_document_type int REFERENCES document_type(document_type_id) NOT NULL,
	fk_unit int REFERENCES unit(unit_id) NOT NULL,
	fk_period int REFERENCES "period"(period_id) NOT NULL
	UNIQUE(fk_document_type, fk_unit, fk_period)
);


CREATE TABLE "document"(
	document_id serial PRIMARY KEY,
	document_path varchar(100) UNIQUE,
	document_desc varchar(50),
	creation_date date,
	valid_year int,
	fk_unit int REFERENCES unit(unit_id) NOT NULL,
	fk_document_type int REFERENCES document_type(document_type_id) NOT NULL,
	fk_period int REFERENCES "period"(period_id) NOT NULL
);




DROP TABLE "document" 


