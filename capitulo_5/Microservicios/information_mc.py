# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------------------
# Archivo: information_mc.py
# Capitulo: 5 Estilo Microservicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Febrero 2017
# Descripción:
#
#   Este archivo define el rol de un microservicio. Su función general es porporcionar en un JSON la
#   información detallada acerca de una pelicula o una serie específica extraidos del sitio web
#   'https://www.imdb.com/'. La estructura del JSON está definida por el sitio de IMDB.
#   
#   
#
#                                        information_mc.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Ofrecer en un JSON   | - Se conecta con el    |
#           |     Microservicio     |    que contenga informa-|   API de IMDB.         |
#           |                       |    ción de peliculas o  | - Devuelve un JSON con |
#           |                       |    series en específico.|   datos de la serie o  |
#           |                       |                         |   pelicula en cuestión.|
#           |                       |                         | - Utiliza la ruta:     |
#           |                       |                         |   '/information'       |
#           |                       |                         |   para ofrecer el      |
#           |                       |                         |   servicio.            |
#           +-----------------------+-------------------------+------------------------+
#
#	Instrucciones de ejecución:
#		- Abrir la terminal
#		- Ejecutar el comando 'python information_mc.py'
#
#
import os
from flask import Flask
from flask import render_template
from flask import request
import urllib, json
app = Flask (__name__)

@app.route("/api/v1/information")
def get_information():
	# Método que obtiene la información de OMDB acerca de un título en particular
	# Se obtiene el parámetro 't' que contiene el título de la película o serie que se va a consultar
	title = request.args.get("t")
	# Se ocnecta con el micro servicio de OMDB a través del API que OMDB ofrece
	url_omdb = urllib.urlopen("http://www.omdbapi.com/?t="+title+"&plot=full&r=json")
	# Se lee la respuesta de OMDB
	json_omdb = url_omdb.read()
	# Se convierte en un JSON la respuesta recibida
	omdb = json.loads(json_omdb)
	# Se regresa como respuesta el JSON que se recibió del API de OMDB
	return json.dumps(omdb)

if __name__ == '__main__':
	# Se define el puerto del sistema operativo que utilizará el micro servicio
	port = int(os.environ.get('PORT', 8084))
	# Se habilita la opción de 'debug' para visualizar los errores
	app.debug = True
	# Se ejecuta el micro servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
	app.run(host='0.0.0.0', port=port)