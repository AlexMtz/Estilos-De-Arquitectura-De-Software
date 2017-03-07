# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
#-------------------------------------------------------------------------
# Archivo: text_analysis_mc.py
# Capitulo: 5 Estilo Microservicios.
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.0 Febrero 2017
# Descripción:
#
#   Este archivo define el rol de un microservicio. Su función general es porporcionar en un JSON el
#   análisis de sentimientos de un conjunto de reviews. El resultado incluye 4 datos que corresponden
#   a los reviews 'negativos', 'positivos', 'neutrales' y el 'total' de reviews analizados. El microservicio
#   realiza el análisis de sentimientos consumiendo una API proporcionada por
#   'http://text-processing.com/api/sentiment/' pasando cada uno de los reviews via 'POST' utilizando una
#   'text' que representa el review a analizar.
#
#
#
#                                       text_analysis_mc.py
#           +-----------------------+-------------------------+-------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades        |
#           +-----------------------+-------------------------+-------------------------+
#           |                       |  - Ofrecer en un JSON   | - Se conecta con una    |
#           |     Microservicio     |    que contenga el res- |   API que identifica el |
#           |                       |    ultado de los reviews|   sentimiento expresado |
#           |                       |    analizados.          |   en un review.         |
#           |                       |                         | - El sentimiento puede  |
#           |                       |                         |   ser 'positivo',       |
#           |                       |                         |   'negativo' o 'neutral'|
#           |                       |                         | - Utiliza la ruta:      |
#           |                       |                         |   '/text/analysis' para |
#           |                       |                         |   ofrecer el servicio.  |
#           |                       |                         | - Utiliza el método POST|
#           |                       |                         |   para recibir los      |
#           |                       |                         |   reviews a analizar.   |
#           |                       |                         | - Los reviews a analizar|
#           |                       |                         |   deben tener la forma: |
#           |                       |                         |   {'review #': 'texto'} |
#           +-----------------------+-------------------------+-------------------------+
#
#	Instrucciones de ejecución:
#		- Abrir la terminal
#		- Ejecutar el comando 'python text_analysis_mc.py'
#
#
import os
from flask import Flask, request
import urllib
import json
app = Flask(__name__)


@app.route("/text/analysis", methods=['POST'])
def text_analysis():
    positive = 0
    negative = 0
    neutral = 0
    total_reviews = 0
    count = 0
    json_data = {}
    input_json = request.get_json(force=True)
    for r in input_json:
        data = urllib.urlencode({"text": input_json['review ' + str(count)]})
        u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
        result = u.read()
        json_result = json.loads(result)
        count += 1
        if json_result['label'] == 'pos':
            positive += 1
        elif json_result['label'] == 'neg':
            negative += 1
        elif json_result['label'] == 'neutral':
            neutral += 1
    json_data['positive'] = str(positive)
    json_data['negative'] = str(negative)
    json_data['neutral'] = str(neutral)
    total_reviews = positive + negative + neutral
    json_data['total reviews'] = str(total_reviews)
    return json.dumps(json_data)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8082))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
