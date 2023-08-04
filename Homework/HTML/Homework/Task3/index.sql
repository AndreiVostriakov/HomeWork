-- create
CREATE TABLE employee (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  age TEXT NOT NULL,
  address TEXT NOT NULL
);

-- insert
INSERT INTO employee (name, age, address)  VALUES ('Иван', '18', 'Москва');
INSERT INTO employee (name, age, address) VALUES ('Петр', '22', 'Иваново');
INSERT INTO employee (name, age, address) VALUES ('Анна', '35', 'Питер');
INSERT INTO employee (name, age, address) VALUES ('Юлия', '18', 'Москва');
INSERT INTO employee (name, age, address) VALUES ('Николай', '36', 'Москва');

SELECT name AS Имя_студента FROM employee WHERE address = "Москва" AND (age >= 18 AND age < 30);
