CREATE TABLE Accounts (account_ID SERIAL PRIMARY KEY, first_name VARCHAR(50), last_name VARCHAR(50), email VARCHAR(50),
 phone INTEGER, photo_URL VARCHAR(255), account_type VARCHAR(15), creation_date DATE, password VARCHAR(50), 
 location_ID REFERENCES Locations (location_ID));

CREATE TABLE Location (location_ID SERIAL PRIMARY KEY, address VARCHAR(255), latitude FLOAT, longitude FLOAT,
 city_ID REFERENCES Cities(city_ID));

CREATE TABLE City (city_ID SERIAL PRIMARY KEY, city_name VARCHAR(50), region_ID REFERENCES Region(region_ID));

CREATE TABLE Region (region_ID INTEGER, region_name VARCHAR(50));

CREATE TABLE Notifications (notification_ID SERIAL PRIMARY KEY, seen BOOLEAN, message VARCHAR(255),
 title VARCHAR(150), sent_date DATE, account_ID REFERENCES Accounts(account_ID));

CREATE TABLE Payment_Methods (payment_method_ID SERIAL PRIMARY KEY, card_Holder VARCHAR(255), card_number INTEGER, 
 expiration_date DATE, zip_code INTEGER, account_ID REFERENCES Accounts(account_ID));

CREATE TABLE Resource_Type (resource_type_ID SERIAL PRIMARY KEY, name VARCHAR(50), description VARCHAR(255));

CREATE TABLE Resources (resource_ID SERIAL PRIMARY KEY, name VARCHAR(150), price FLOAT, description VARCHAR(255), 
 quantity INTEGER, availability INTEGER, creation_date DATE, last_update DATE, account_ID REFERENCES Accounts(account_ID),
 resource_type_ID REFERENCES Resource_Type(resource_type_ID));

CREATE TABLE Resources_Requested (request_ID SERIAL PRIMARY KEY, name VARCHAR(150) description(255), quantity INTEGER,
 creation_date DATE, resource_type_ID REFERENCES Resource_Type(resource_type_ID), account_ID REFERENCES Accounts(account_ID));

CREATE TABLE Resource_Keywords (keyword_ID SERIAL PRIMARY KEY, keyword VARCHAR(15), resource_ID REFERENCES Resources(resource_ID));

CREATE TABLE Purchases (purchase_ID SERIAL PRIMARY KEY, quantity INTEGER, purchase_date DATE, purchase_price FLOAT, 
 payment_method_ID REFERENCES Payment_Methods(payment_method_ID), resource_ID REFERENCES Resources(resource_ID), 
 account_ID REFERENCES Accounts(account_ID));
