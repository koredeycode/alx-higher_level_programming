-- create a mysql server user
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_i_pwd';
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;