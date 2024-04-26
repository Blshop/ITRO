CREATE TABLE deviation(
	deviation_id serial PRIMARY KEY,
	deviation_desc varchar(30) UNIQUE NOT NULL
);


CREATE TABLE "parameter"(
	parameter_id serial PRIMARY KEY,
	parameter_desc varchar(100) NOT NULL,
	fk_deviation int REFERENCES deviation(deviation_id),
	UNIQUE (parameter_desc, fk_deviation)
);


CREATE TABLE unit_type(
	unit_type_id serial PRIMARY KEY,
	unit_type_desc varchar(100) UNIQUE NOT NULL
);


CREATE TABLE unit(
	unit_id serial PRIMARY KEY,
	unit_desc varchar(30) NOT NULL,
	unit_sn varchar(15) NOT NULL,
	fk_unit_type int REFERENCES unit_type(unit_type_id) NOT NULL,
	UNIQUE (unit_desc, unit_sn)
);


CREATE TABLE "period"(
	period_id serial PRIMARY KEY,
	period_desc varchar(20) UNIQUE NOT NULL,
	period_duration int NOT NULL
);


CREATE TABLE unit_parameter(
	unit_parameter_id serial PRIMARY KEY,
	fk_unit int REFERENCES unit(unit_id) NOT NULL,
	fk_parameter int REFERENCES "parameter"(parameter_id) NOT NULL,
	fk_period int REFERENCES "period"(period_id) NOT NULL
);

