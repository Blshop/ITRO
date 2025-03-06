--Intervals for various types of checks. documents and so on
CREATE TABLE period (
    period_id serial PRIMARY KEY,
    period_desc varchar(20) UNIQUE NOT NULL,
    period_duration int UNIQUE NOT NULL
);
