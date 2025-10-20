-- This script will create second_table and insert multiple rows
CREATE TABLE IF NOT EXISTS Second_table (
    id INT,
    name VARCHAR(256),
	score INT
);

INSERT into Second_table (id, name, score)
VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
