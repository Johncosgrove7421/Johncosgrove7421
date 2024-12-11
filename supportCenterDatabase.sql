
CREATE DATABASE supportCenter;

USE supportCenter;

CREATE TABLE employees (
    ID INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
    Role VARCHAR(50) NOT NULL
);

CREATE TABLE devices (
    ID INT PRIMARY KEY,
    Type VARCHAR(50) NOT NULL,
    Version VARCHAR(50) NOT NULL,
    CheckedOutTo INT,
    Location VARCHAR(50) NOT NULL,
    FOREIGN KEY (CheckedOutTo) REFERENCES employees(ID)
);

CREATE TABLE offices (
    Office VARCHAR(50) PRIMARY KEY,
    Capacity INT NOT NULL,
    NetworkID INT NOT NULL
);
