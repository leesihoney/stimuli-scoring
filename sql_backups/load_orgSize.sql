-- load this file with
--
-- psql -U isdb -d score -f load_orgSize.sql

DROP TABLE IF EXISTS organization_size;

CREATE TABLE organization_size (
	person text,
	food_type integer,
	fifty real,
	hundred real,
	fiveHundred real,
	thousand real,
	larger real
);

\copy organization_size from 'csv/database_sheet - organization_size.csv'   CSV





 