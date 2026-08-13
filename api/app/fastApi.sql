CREATE ROLE student_api_user
WITH LOGIN
PASSWORD 'Gfdsa@54321';

GRANT CONNECT
ON DATABASE student_db
TO student_api_user;

GRANT USAGE, CREATE
ON SCHEMA public
TO student_api_user;