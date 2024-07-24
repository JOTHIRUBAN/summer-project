
/*Query for user table Schema*/
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(120) NOT NULL
);

Create table feed(
	user_id int,
	keyword varchar(50),
	feed_date date
);
