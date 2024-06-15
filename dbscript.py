import sqlite3

connection = sqlite3.connect("testdata.db")

connection.execute(
'''CREATE TABLE FARMER
(
PHONE VARCHAR(10) PRIMARY KEY NOT NULL,
NAME VARCHAR(50) NOT NULL, 
PASSWORD VARCHAR(20) NOT NULL,
LOCATION VARCHAR(100)
);''')

connection.execute(
'''CREATE TABLE EXPERT
(
PHONE VARCHAR(10) PRIMARY KEY NOT NULL,
NAME VARCHAR(50) NOT NULL, 
EMAIL VARCHAR(50) NOT NULL,
PASSWORD VARCHAR(20) NOT NULL,
LOCATION VARCHAR(100) NOT NULL
);''')