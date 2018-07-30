-- load this file with
--
-- psql -U isdb -d score -f load_income.sql

DROP TABLE IF EXISTS income;

CREATE TABLE income (
	person text,
	food_type integer,
	hundredK real,
	zeroK real,
	twentyK real,
	fourtyK real,
	sixtyK real,
	eightyK real
);

\copy income from 'csv/database_sheet - income.csv'   CSV