-- load this file with
--
-- psql -U isdb -d score -f load_faccess.sql

DROP TABLE IF EXISTS food_access;

CREATE TABLE food_access (
	person text,
	food_type integer,
	extremely_low real,
	low real,
	normal real
);

\copy food_access from 'csv/database_sheet - access.csv'   CSV