CREATE DATABASE IF NOT EXISTS studentdb;

USE studentdb;

CREATE TABLE IF NOT EXISTS students (

    id INT AUTO_INCREMENT PRIMARY KEY,

    name VARCHAR(100) NOT NULL,

    email VARCHAR(100) UNIQUE,

    course VARCHAR(100)

);

INSERT INTO students(name,email,course)

VALUES

('Rahul','rahul@gmail.com','Docker'),

('Priya','priya@gmail.com','Kubernetes'),

('Amit','amit@gmail.com','AWS'),

('Sneha','sneha@gmail.com','Linux'),

('John','john@gmail.com','DevOps');