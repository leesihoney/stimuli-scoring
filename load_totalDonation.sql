-- load this file with
--
-- psql -U isdb -d score -f load_totalDonation.sql

DROP TABLE IF EXISTS totalDonation;

CREATE TABLE totalDonation (
	person text,
	zero real,
	one real,
	two real,
	three real,
	four real,
	five real,
	six real,
	seven real,
	eight real,
	nine real,
	ten real,
	eleven real,
	twelve real
);

\copy totalDonation from 'csv/database_sheet - total_donations_all types.csv'   CSV