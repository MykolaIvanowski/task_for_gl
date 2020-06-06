# CREATE DATABASE db_task;
#
# CREATE TABLE db_task.users(
#     user_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
#     login_name NVARCHAR(40) NOT NULL,
#     password_hash BINARY(64) NOT NULL,
#     first_name NVARCHAR(40) NULL,
#     last_name NVARCHAR(40) NULL,
#
# )
#
# CREATE TABLE db_task.comments (
#   comment_id INT IDENTITY(1,1) NOT NULL,
#   user_id int NOT NULL,
# 	comment_date DATE NOT NULL,
# 	comment char,
#     FOREIGN KEY (user_id) REFERENCES db_task.user(user_id)
# );
# CREATE TABLE db_task.auth (
#   user_id int NOT NULL,
# 	auth_date DATE NOT NULL,
#   status NVARCHAR(40) NULL,
#   time_changed DATE,
#   FOREIGN KEY (user_id) REFERENCES db_task.user(user_id)
# );


# SELECT first_name
# FROM users
# WHERE
# user_id =
# (SELECT USER_ID, COUNT(user_id)
# FROM comments
# WHERE comment_date >=dateadd(day,datediff(day,0,GetDate())- 7,0)
# GROUP BY comment_date);


# UPDATE auth
# SET status, time_changed = "block", GETDATE()
# WHERE user_id =(
# SELECT users
# SET status = "block"
# WHERE (SELECT TOP 10
# FROM comments
# RIGHT JOIN users ON comments
# WHERE comment_id is null
# ));


# SELECT *
# FROM users
# exam_marks
# WHERE
# user_id =(
# SELECT user_id
# FROM auth
# WHERE DATEPART(MONTH, DATEADD(MONTH, -1, [time_changed])))
