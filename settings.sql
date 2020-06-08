DROP DATABASE IF EXISTS scribble;
DROP USER IF EXISTS scribbleuser;

CREATE DATABASE scribble;
CREATE USER scribbleuser
WITH PASSWORD 'scribble';
GRANT ALL PRIVILEGES ON DATABASE scribble TO scribbleuser;