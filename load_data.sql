-- load this file with
--
-- psql -U isdb -d score -f load_data.sql

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

DROP TABLE IF EXISTS food_access;

CREATE TABLE food_access (
	person text,
	food_type integer,
	extremely_low real,
	low real,
	normal real
);

\copy food_access from 'csv/database_sheet - access.csv'   CSV

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