
Create data file where databases are saved
.open cat_db.db


CREATE TABLE cats (
	name TEXT,
	breed TEXT,
	age INTEGER
);


INSERT INTO cats (name, breed, age) VALUES ("Blue", "Scottish Fold", 3);
INSERT INTO cats (name, breed, age) VALUES ("Rose", "Scottish Fold", 5);
INSERT INTO cats (name, breed, age) VALUES ("Moose", "Scottish Fold", 6);
INSERT INTO cats (name, breed, age) VALUES ("Piggy", "Japanese cat", 10);
INSERT INTO cats (name, breed, age) VALUES ("Red", "Japanese cat", 11);

SELECT * FROM cats;

SELECT * FROM cats WHERE name is "Red";
SELECT * FROM cats WHERE breed IS NOT "Russian cat";
SELECT * FROM cats WHERE breed IS NOT "Russian cat" AND breed IS NOT "Pink cat";
SELECT * FROM cats WHERE age >= 6;
SELECT * FROM cats WHERE name LIKE "%tt%";