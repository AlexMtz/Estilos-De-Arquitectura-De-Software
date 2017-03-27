# -*- coding: utf-8 -*-
#!/usr/bin/env python
#----------------------------------------------------------------------------------------------------------------
# Archivo: twitter_mc.py
# Capitulo: 5 Estilo Microservicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Febrero 2017
# Descripción:
#
#   Este archivo define el rol de un microservicio. Su función general es conectarse con el API
#   de Twitter para obtener comentarios actuales acerca de la serie Stranger Things. 
#   La estructura del JSON es la siguiente 'review #' : 'comment text'
#   donde: 
#       # -> corresponde al número de review
#       commnet text -> corresponde al comentario extraido desde Twitter
#
#                                           twitter_mc.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Ofrecer en un JSON   | - Se conecta con la red|
#           |     Microservicio     |    que contenga comenta-|   social de Twitter.   |
#           |                       |    rios publicados en la| - Genera un JSON con la|
#           |                       |    página de Twitter.   |   siguiente estructura:|
#           |                       |                         |   {                    |
#           |                       |                         |    'review #' : 'texto'|
#           |                       |                         |   }                    |
#           |                       |                         | - Utiliza la ruta:     |
#           |                       |                         |   '/tweets'            |
#           |                       |                         |   para ofrecer el      |
#           |                       |                         |   servicio.            |
#           |                       |                         | - El hashtag a analizar|
#           |                       |                         |   es el siguiente:     |
#           |                       |                         |   @Stranger_Things.    |
#           +-----------------------+-------------------------+------------------------+
#
#   Instrucciones de ejecución:
#       - Contar con una cuenta de Twitter.
#       - Dirigirse a https://dev.twitter.com/
#       - Obtener un consumer key, consumer secret, access token y access token secret como la siguiente estructura:
#           -> Consumer Key = "xxXxxXxXXxXXxXxXxxXxxXXXx"
#           -> Consumer Secret = "xXXXXxXXXXXXXxXxXXxXxXXXXXXxxxxXXXxXXXXxXXXXxxXXxx"
#           -> Access Token = "XXXXXXXXXXXXXXXXXX-xXXXXXxXXXxxXXXXXXXxXxxXXXXXXXx"
#           -> Access Token Secret = "xXXXxxxXXXxXxXxXXxXXXXXXxxxxxXxXxXXxxxXxXXxxX"
#       - Ingresar las credenciales en el archivo.
#       - Abrir la terminal
#       - Ejecutar el comando 'python twitter_mc.py'
#
#
from tweepy import OAuthHandler
import tweepy
import json
from unidecode import unidecode
from flask import request
import os

from flask import Flask
app = Flask(__name__)

@app.route("/api/v1/tweets")
def get_tweets():
    # Método que obtiene los tuits relacionados con una película o serie en particular
    # Se definen las claves y token's necesarios para conectar y utilizar el API de Twitter 
    CKEY = "qmAcwSrXXuNBc3rYuoKmsCYNe"
    CSECRET = "cXL1Ln9YVPC4RnCfE0rFe6Q8BLPcwuu7F4aAGS2m2L35ecT7xn"
    ATOKEN = "715041734372298752-tZTVZ9aXHUfr4DHDAUTtGecHRIMPG2f"
    ATOKENSECRET = "fYHUsibHPJj1v1bGOyWBX0FQtrpvzTh2d3XbtlUtVSmtD"
    # Se lee el parámetro 'u' que contiene el nombre de usuario de Twitter del cual se obtendrán los tuits
    TOPIC = request.args.get("u")
    # Se define el lenguaje de los tuits que serán consultados
    LANGUAGE = 'es'
    # Se define el'número de tuits límite para consultar
    LIMIT = 10
    # Se define e inicializa el autenticador con las claves y token's para hacer uso del API de Twitter
    auth = OAuthHandler(CKEY, CSECRET)
    auth.set_access_token(ATOKEN, ATOKENSECRET)
    # Se autentica en el API para su uso posterior
    api = tweepy.API(auth)
    # Se define e inicializa el JSON que contendrá los tuits
    json_result = {}
    # Se define e inicializa un contador para definir el número de tuit obtenido
    count = 0
    # Se itera cada tuit obtenido para formar el JSON de la respuesta
    for tweet in tweepy.Cursor(api.search,
                               q=TOPIC,
                               result_type='recent',
                               include_entities=True,
                               lang=LANGUAGE).items(LIMIT):
        # Se llena uno a uno el JSON de la repsuesta con los mensajes incluidos en cada tuit relacionado con el usuario
        json_result['review ' + str(count)] = str(unidecode(tweet.text.replace(
            '"', '')))
        # Se incrementa el contador para continuar con la iteración
        count += 1
    # Se devuelve el JSON de la respuesta con los tuits obtenidos
    return json.dumps(json_result)

if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el micro servicio
    port = int(os.environ.get('PORT', 8083))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el micro servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)
