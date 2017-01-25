# -*- coding: utf-8 -*-
#!/usr/bin/env python
#-------------------------------------------------------------------------
# Archivo: twitter_microservice.py
# Capitulo: 5 Estilo Microservicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Enero 2017
# Descripción:
#
#   Ésta archivo define el rol de un microservicio. Sus características son las siguientes:
#   Tema incluido en los Tweets publicados @Stranger_Things.
#   Límite de tweets por consulta 1000.
#   El lenguaje de los Tweets publicados español
#
#   Para ejecutar éste servicio, recuerda que antes debes de dirigirte a https://dev.twitter.com/, crear
#   una aplicación (con algún nombre representativo) y obtener las siguientes claves:
#      - Consumer Key = "xxXxxXxXXxXXxXxXxxXxxXXXx"
#      - Consumer Secret = "xXXXXxXXXXXXXxXxXXxXxXXXXXXxxxxXXXxXXXXxXXXXxxXXxx"
#      - Access Token = "XXXXXXXXXXXXXXXXXX-xXXXXXxXXXxxXXXXXXXxXxxXXXXXXXx"
#      - Access Token Secret = "xXXXxxxXXXxXxXxXXxXXXXXXxxxxxXxXxXXxxxXxXXxxX"
#
#                                        twitter_miscroservice.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Ofrecer un servicio  |                        |
#           |     Microservicio     |                         |                        |
#           |                       |                         |                        |
#           |                       |                         |                        |
#           |                       |                         |                        |
#           |                       |                         |                        |
#           |                       |                         |                        |
#           |                       |                         |                        |
#           |                       |                         |                        |
#           |                       |                         |                        |
#           |                       |                         |                        |
#           +-----------------------+-------------------------+------------------------+

from tweepy import OAuthHandler
import tweepy
import json
from unidecode import unidecode

from flask import Flask
app = Flask(__name__)


@app.route("/twetter_messages")
def index():
    CKEY = "qmAcwSrXXuNBc3rYuoKmsCYNe"
    CSECRET = "cXL1Ln9YVPC4RnCfE0rFe6Q8BLPcwuu7F4aAGS2m2L35ecT7xn"
    ATOKEN = "715041734372298752-tZTVZ9aXHUfr4DHDAUTtGecHRIMPG2f"
    ATOKENSECRET = "fYHUsibHPJj1v1bGOyWBX0FQtrpvzTh2d3XbtlUtVSmtD"
    TOPIC = "@Stranger_Things"
    LANGUAGE = 'es'
    LIMIT = 1000

    auth = OAuthHandler(CKEY, CSECRET)
    auth.set_access_token(ATOKEN, ATOKENSECRET)
    api = tweepy.API(auth)
    tweets = []

    for tweet in tweepy.Cursor(api.search,
                               q=TOPIC,
                               result_type='recent',
                               include_entities=True,
                               lang=LANGUAGE).items(LIMIT):
        aux = {"text": unidecode(tweet.text.replace(
            '"', '')), "language": LANGUAGE,  "query": TOPIC, "id": tweet.id}
        tweets.append(aux)

    result = { "data" : tweets }
    return str(result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
