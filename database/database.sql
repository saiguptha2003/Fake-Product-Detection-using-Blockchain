
create database cpd;
use cpd;
create table users(email varchar(40) not null primary key, pass varchar(40) not null,roleofuser varchar(16) not null);
select * from users;

create table product(product_id int not null primary key,
product_name varchar(30),rrole varchar(30),_status varchar(30),
_source varchar(30), destination varchar(30),remarks varchar(50));


use cpd;
CREATE TABLE suppliers (
    email VARCHAR(255) PRIMARY KEY,
    remarks VARCHAR(255),
    password VARCHAR(20),
    address VARCHAR(255)
);

CREATE TABLE distributors (
    email VARCHAR(255) PRIMARY KEY,
    remarks VARCHAR(255),
    password VARCHAR(20),
    address VARCHAR(255)
);

CREATE TABLE wholesalers (
    email VARCHAR(255) PRIMARY KEY,
    remarks VARCHAR(255),
    password VARCHAR(20),
    address VARCHAR(255)
);

CREATE TABLE retailers (
    email VARCHAR(255) PRIMARY KEY,
    remarks VARCHAR(255),
    password VARCHAR(20),
    address VARCHAR(255)
);

CREATE TABLE customer (
    email VARCHAR(255) PRIMARY KEY,
    remarks VARCHAR(255),
    password VARCHAR(20),
    address VARCHAR(255)
);
use cpd;
select * from distributors;