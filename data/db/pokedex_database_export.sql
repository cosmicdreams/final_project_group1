-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/UAAlwB
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

CREATE TABLE pokedex_html (
    Name varchar(50) NOT NULL Primary key,
    html text
);

CREATE TABLE pokedex_table (
    Number int NOT NULL,
    Name varchar(50) NOT NULL,
    Type varchar,
    Attack int,
    Defense int,
    HP int,
    Catch float,
    Flee float,
    Fast_Moves varchar,
    Charge_Moves varchar,
	CONSTRAINT fk_pokedex_table_Name FOREIGN KEY(Name) REFERENCES pokedex_html (Name)
);