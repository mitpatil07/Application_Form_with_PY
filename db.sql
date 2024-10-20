create database ladkibahin;

Create Table Applicants(Adhar int(12) Primary Key, 
                        Name varchar(100) not null,
                        Father varchar(100) not null,
                        Contact varchar(10) not null,
                        Age int (2) not null,
                        Cast varchar(20),
                        Education varchar(20),
                        Address varchar(200) not null,
                        noofbf int(2) not null,
                        appmonth varchar(10) not null,
                        appdate date not null,
                        bankname varchar(30) not null,
                        hname varchar(100) not null,
                        acn int(20) not null, 
                        ifsc varchar(20)
                        );

CREATE TABLE details (
    appnum INT(12) PRIMARY KEY,
    Adhar INT, -- Assuming this is supposed to be a column name, not correctly specified as a foreign key
    Name VARCHAR(100) NOT NULL,
    amount INT,
    
    appmonth VARCHAR(10) NOT NULL,
    appdate DATE NOT NULL,
    bankname VARCHAR(30) NOT NULL,
    hname VARCHAR(100) NOT NULL,
    acn INT(20) NOT NULL,
    ifsc VARCHAR(20),
    status VARCHAR(10)
);




