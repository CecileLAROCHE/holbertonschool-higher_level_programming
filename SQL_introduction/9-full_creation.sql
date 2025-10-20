-- This script will create first table
CREATE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
	score INT
);

INSERT into Second_table (id, name, score)
Value 
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);