-- load this file with
--
-- psql -U isdb -d score -f load_lastDonation.sql

DROP TABLE IF EXISTS lastDonation;

CREATE TABLE lastDonation (
	person text,
	food_type integer,
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
	twelve real,
	never real
);

\copy lastDonation from 'csv/database_sheet - last_donation.csv'   CSV