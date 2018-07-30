-- load this file with
--
-- psql -U isdb -d score -f load_totalDonationCommon.sql

DROP TABLE IF EXISTS totalDonationCommon;

CREATE TABLE totalDonationCommon (
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

\copy totalDonationCommon from 'csv/database_sheet - total_donations_common.csv'   CSV