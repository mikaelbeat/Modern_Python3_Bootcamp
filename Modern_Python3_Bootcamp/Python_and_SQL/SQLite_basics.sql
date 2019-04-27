
Create data file where databases are saved
.open cat_db.db


CREATE TABLE cats (
	name TEXT.
	breed TEXT,
	age INTEGER
);


INSERT INTO cats (name, breed, age) VALUES ("Blue", "Scottish Fold", 3);
INSERT INTO cats (name, breed, age) VALUES ("Rose", "Italian cat", 5);
INSERT INTO cats (name, breed, age) VALUES ("Moose", "Canadian cat", 6);
INSERT INTO cats (name, breed, age) VALUES ("Piggy", "Pink cat", 10);
INSERT INTO cats (name, breed, age) VALUES ("Red", "Russian cat", 11);

SELECT * FROM cats;

SELECT * FROM cats WHERE name is "Red";
SELECT * FROM cats WHERE breed IS NOT "Russian cat";


360 -> 4:06