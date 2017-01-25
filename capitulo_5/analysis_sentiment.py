# -*- coding: utf-8 -*-
#!/usr/bin/env python
#-------------------------------------------------------------------------
# Archivo: sentiment_analisis.py
# Capitulo: 5 Estilo Microservicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Enero 2017
# Descripción:
#
#   Ésta archivo define el rol de un microservicio. 
#   Se conecta con la url http://www.sentiment140.com/api/bulkClassifyJson para valorar el 
#   sentimiento del contenido de los tweets.
#
#
#                                        analysis_sentiment.py
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
import json
import urllib2
from flask import request

from flask import Flask
app = Flask(__name__)

URL_SENTIMENT140 = "http://www.sentiment140.com/api/bulkClassifyJson"
#data = {'data': [{'text': '?Que tiene Indiana de #Sobrenatural? Eerie Indiana es una serie de #TV de los 90, y hoy @netflix la revive con... https://t.co/AhFYq0Mjg3', 'id': 824310765310111744, 'language': 'es', 'query': '@Stranger_Things'}, {'text': 'Que cosa! @Stranger_Things \n\nhttps://t.co/voNWA1UaS4', 'id': 824307551546249216, 'language': 'es', 'query': '@Stranger_Things'}, {'text': '@indiehoy @Stranger_Things @DaiFerrada en tu cara', 'id': 824298885489262601, 'language': 'es', 'query': '@Stranger_Things'}, {'text': 'RT @StrangerESP11: #StrangerThings Este domingo se celebraran los premios del Sindicato de Actores donde @Stranger_Things esta nominada a 2...', 'id': 824297952004997121, 'language': 'es', 'query': '@Stranger_Things'}, {'text': 'RT @StrangerESP11: @GuaridaDel7Arte @movistarseries Y recordad que participa Barb de @Stranger_Things!! https://t.co/RrytIciz3i', 'id': 824294907426852866, 'language': 'es', 'query': '@Stranger_Things'}, {'text': '@GuaridaDel7Arte @movistarseries Y recordad que participa Barb de @Stranger_Things!! https://t.co/RrytIciz3i', 'id': 824294722583822340, 'language': 'es', 'query': '@Stranger_Things'}, {'text': 'RT @Stranger_Things: A universal badass. https://t.co/yTsgTmb8c3', 'id': 824290949278957568, 'language': 'es', 'query': '@Stranger_Things'}, {'text': 'RT @OrfeoFM: #LaManana | Arriba la @milliebbrown La joven protagonista de @Stranger_Things debuto como modelo para @CalvinKlein https://t.c...', 'id': 824282895334473730, 'language': 'es', 'query': '@Stranger_Things'}, {'text': '#LaManana | Arriba la @milliebbrown La joven protagonista de @Stranger_Things debuto como modelo para @CalvinKlein https://t.co/YFhQNnikwW', 'id': 824281184440090624, 'language': 'es', 'query': '@Stranger_Things'}, {'text': 'RT @paolo_valdivia: !POR FIN! @Stranger_Things muestra su primer teaser trailer de la segunda temporada. https://t.co/9FOrIl3C4H \n\n#Strang...', 'id': 824276801103036416, 'language': 'es', 'query': '@Stranger_Things'}]}

@app.route("/analysis")
def index():
    negative_tweets = 0
    positive_tweets = 0 
    data = data = request.args.get("data")
    req = urllib2.Request(URL_SENTIMENT140)
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, str(data))
    json_response = json.loads(response.read())
    for j in json_response["data"]:
        if int(j["polarity"]) == 0:
            negative_tweets += 1
        elif int(j["polarity"]) == 4:
            positive_tweets += 1
    print "Positive Tweets: " + str(positive_tweets)
    print "Negative Tweets: " + str(negative_tweets)
    result = {"Positive Tweets" : positive_tweets, "Negative Tweets" : negative_tweets}
    return str(result)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
