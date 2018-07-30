-- load this file with
--
-- psql -U isdb -d score -f load_totalDonationUncommon.sql

DROP TABLE IF EXISTS totalDonationUncommon;

CREATE TABLE totalDonationUncommon (
	person text,
	food_type integer,
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

\copy totalDonationUncommon from 'csv/database_sheet - total_donations_uncommon.csv'   CSV