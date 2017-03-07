# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------------------
# Archivo: dbhelper.py
# Capitulo: 5 Estilo Microservicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Febrero 2017
# Descripción:
#
#   Esun archivo auxiliar que permite realizar la conexión a la base de datos donde se almacenan
#   los reviews de la p+agina 'https://www.rottentomatoes.com/'.
#
#                                           dbhelper.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Conectar con la DB   | - Cuenta con un método |
#           |     DataManager       |    que contiene los     |   que realiza la       |
#           |                       |    reviews de la página |   conexión a la DB.    |
#           |                       |    Rotten Tomatoes.     | - Ceunta con un método |
#           |                       |                         |   que consulta todos   |
#           |                       |                         |   los reviews almacena-|
#           |                       |                         |   dos en la DB.        |
#           +-----------------------+-------------------------+------------------------+
#
#	Instrucciones de ejecución:
#		- Este archivo no se ejecuta, se utiliza dentro del microservicio de reviews_mc.py
#
#
import pymysql
import db_reviews_config
import datetime

class DBHelper:
	def connect(self, database="reviewsdb"):
		return pymysql.connect(host='localhost',
			user = db_reviews_config.db_user,
			passwd = db_reviews_config.db_password,
			db = database)

	def get_all_reviews(self):
		connection = self.connect()
		try:
			query = "SELECT content FROM reviewsdb.review;"
			with connection.cursor() as cursor:
				cursor.execute(query)
			return cursor.fetchall()
		finally:
			connection.close()