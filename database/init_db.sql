CREATE DATABASE second_project;

\c second_project;

CREATE TABLE Users (
        domain_id       SERIAL PRIMARY KEY,
        user_id         INT NOT NULL,
        domain_name     TEXT
);

CREATE TABLE Records (
        record_id       SERIAL PRIMARY KEY,
        domain_id       INT,
        record_type     TEXT,
        record          TEXT,
        ttl             INT NOT NULL,
        CONSTRAINT domain_exists FOREIGN KEY (domain_id) REFERENCES Users (domain_id) ON DELETE CASCADE
);
