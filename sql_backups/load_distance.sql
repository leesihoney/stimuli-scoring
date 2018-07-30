-- load this file with
--
-- psql -U isdb -d score -f load_distance.sql

DROP TABLE IF EXISTS distance;

CREATE TABLE distance (
	person text,
	food_type integer,
	fifteen real,
	thirty real,
	fourtyFive real,
	sixty real
);

\copy distance from 'csv/database_sheet - distance.csv'   CSV