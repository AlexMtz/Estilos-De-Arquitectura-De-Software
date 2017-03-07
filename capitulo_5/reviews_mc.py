# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------------------
# Archivo: reviews_mc.py
# Capitulo: 5 Estilo Microservicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Febrero 2017
# Descripción:
#
#   Este archivo define el rol de un microservicio. Su función general es porporcionar en un JSON un
#   conjunto de reviews almacenados en una base de datos. Los reviews en la base de datos fueron
#   extraidos del sitio web 'https://www.rottentomatoes.com/'. La estructura del JSON es la siguiente
#   'review #' : 'review text' 
#	donde: 
#		# -> corresponde al número de review
#		review text -> corresponde al texto de ese review en particular
#   
#   
#
#                                           reviews_mc.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Ofrecer en un JSON   | - Se conecta con una   |
#           |     Microservicio     |    que contenga reviews |   DB que tiene almace- |
#           |                       |    publicados en la     |   nados los reviews de |
#           |                       |    página de Rotten     |   la serie.            |
#           |                       |    Tomatoes.            | - Genera un JSON con la|
#           |                       |                         |   siguiente estructura:|
#           |                       |                         |   {                    |
#           |                       |                         |    'review #' : 'texto'|
#           |                       |                         |   }                    |
#           |                       |                         | - Utiliza la ruta:     |
#           |                       |                         |   '/db/reviews' para   |
#           |                       |                         |   ofrecer el servicio. |
#           +-----------------------+-------------------------+------------------------+
#
#	Instrucciones de ejecución:
#		- Abrir la terminal
#		- Ejecutar el comando 'python reviews_mc.py'
#
#
import os
from dbhelper import DBHelper
from flask import Flask
from flask import render_template
import json
app = Flask (__name__)

@app.route("/db/reviews")
def db_reviews():
	DB = DBHelper()
	reviews = DB.get_all_reviews()
	json_data = {}
	count = 0
	for r in reviews:
		review_text = str(reviews[count]) + ""
		review_text = review_text.replace("(\"","")
		review_text = review_text.replace("('","")
		review_text = review_text.replace("',)","")
		review_text = review_text.replace("\",)","")
		json_data['review ' + str(count)] = str(review_text)
		count += 1
	return json.dumps(json_data)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8081))
	app.debug = True
	app.run(host='0.0.0.0', port=port)