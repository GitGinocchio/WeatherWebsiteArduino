BEGIN;


CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    email TEXT,
    password TEXT,

    PRIMARY KEY (email)
);

COMMIT;