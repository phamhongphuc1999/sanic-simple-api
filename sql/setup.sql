CREATE DATABASE sanic_app;
GO

USE sanic_app;
GO

CREATE TABLE employees (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(30) NOT NULL,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(50),
)
GO

INSERT INTO employees (username, password, email)
VALUES ("Pham Hong Phuc", "1167ff3cd1af7a3845fec8883f225300b970f004417f2a765c60ffbc5fac3b75", "php@gmail.com")