# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------------------
# Archivo: information_mc.py
# Capitulo: 5 Estilo Microservicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Febrero 2017
# Descripción:
#
#   Este archivo define el rol de un micro servicio. Su función general es porporcionar en un objeto JSON
#   información detallada acerca de una pelicula o una serie en particular haciendo uso del API del sitio
#   web 'https://www.imdb.com/'.
#   
#   
#
#                                        information_mc.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Ofrecer un JSON que  | - Se conecta con el    |
#           |    Micro servicio     |    contenga información |   API de IMDB.         |
#           |                       |    detallada de pelí-   | - Devuelve un JSON con |
#           |                       |    culas o series en    |   datos de la serie o  |
#           |                       |    particular.          |   pelicula en cuestión.|
#           +-----------------------+-------------------------+------------------------+
#	Ejemplo de uso: Abrir navegador e ingresar a http://localhost:8084/api/v1/information?t=matrix
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
	# Se conecta con el servicio de OMDB a través de su API que OMDB ofrece
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
