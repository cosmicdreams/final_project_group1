-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "daily_dji" (
    "date" date   NOT NULL,
    "open" int   NOT NULL,
    "high" int   NOT NULL,
    "low" int   NOT NULL,
    "close" int   NOT NULL,
    "AdjClose" int   NOT NULL,
    "Volume" int   NOT NULL
);

CREATE TABLE "daily_weather" (
    "date" date   NOT NULL,
    "tmax" int   NOT NULL,
    "tmin" int   NOT NULL,
    "prcp" int   NOT NULL,
    "city_name" varchar   NOT NULL,
    "file_name" varchar   NOT NULL
);

CREATE TABLE "city_info" (
    "city_name" varchar   NOT NULL,
    "city_id" varchar   NOT NULL,
    "lat" int   NOT NULL,
    "lon" int   NOT NULL,
    "stn_name" varchar   NOT NULL,
    "stn_st_date" date   NOT NULL,
    "stn_ed_date" date   NOT NULL
);

ALTER TABLE "daily_dji" ADD CONSTRAINT "fk_daily_dji_date" FOREIGN KEY("date")
REFERENCES "daily_weather" ("date");

ALTER TABLE "city_info" ADD CONSTRAINT "fk_city_info_city_name" FOREIGN KEY("city_name")
REFERENCES "daily_weather" ("city_name");

