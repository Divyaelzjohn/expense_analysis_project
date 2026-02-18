CREATE DATABASE expense_db;
USE expense_db;

CREATE TABLE expense(
  id INT PRIMARY KEY AUTO_INCREMENT,
  date DATE,
  category VARCHAR(50),
  amount DECIMAL(10,2),
  description VARCHAR(100)
);