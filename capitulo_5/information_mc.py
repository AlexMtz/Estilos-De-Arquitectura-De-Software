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

@app.route("/information")
def get_information():
	title = request.args.get("t")
	# Conectar con el microservicio de OMDB
	url_omdb = urllib.urlopen("http://www.omdbapi.com/?t="+title+"&plot=full&r=json")
	# Leer la respuesta de OMDB
	json_omdb = url_omdb.read()
	# Convertir en json la respuesta
	omdb = json.loads(json_omdb)
	return json.dumps(omdb)

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8084))
	app.debug = True
	app.run(host='0.0.0.0', port=port)