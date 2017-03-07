import pymysql
import db_reviews_config

connection = pymysql.connect(host='localhost',
	user= db_reviews_config.db_user,
	passwd= db_reviews_config.db_password)
try:
	with connection.cursor() as cursor:
		sql = "CREATE DATABASE IF NOT EXISTS reviewsdb"
		cursor.execute(sql)
		sql = """CREATE TABLE IF NOT EXISTS reviewsdb.review (
		id int NOT NULL AUTO_INCREMENT,
		content VARCHAR(),
		PRIMARY KEY(id))"""
		cursor.execute(sql)
		connection.commit()
finally:
	connection.close()