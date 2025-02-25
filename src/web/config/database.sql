BEGIN;


CREATE TABLE IF NOT EXISTS users (
    email TEXT,
    password TEXT,

    PRIMARY KEY (email)
);

COMMIT;