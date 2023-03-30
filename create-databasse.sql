CREATE DATABASE marketbackend;

CREATE USER market_admin WITH PASSWORD 'trytoguessthis';

GRANT ALL PRIVILEGES ON DATABASE marketbackend TO market_admin;     
