-- load this file with
--
-- psql -U isdb -d score -f load_poverty.sql

DROP TABLE IF EXISTS poverty;

CREATE TABLE poverty (
	person text,
	food_type integer,
	zero real,
	ten real,
	twenty real,
	thirty real,
	forty real,
	fifty real,
	sixty real
);

\copy poverty from 'csv/database_sheet - poverty.csv'   CSV