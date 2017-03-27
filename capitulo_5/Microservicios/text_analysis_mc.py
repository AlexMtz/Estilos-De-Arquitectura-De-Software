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


@app.route("/api/v1/text-analysis", methods=['POST'])
def text_analysis():
    # Método que análiza el sentimiento expresado en un texto en particular
    # Se definen e inicializan las variables que contabilizarán los sentimientos 
    positive = 0
    negative = 0
    neutral = 0
    total_reviews = 0
    # Se define un contador para iterar los textos recibidos
    count = 0
    # Se define e inicializa un objeto JSON que contendrá la respuesta
    json_data = {}
    # Se lee y convierte en JSON el contenido recibido a través del método POST
    input_json = request.get_json(force=True)
    # Se itera cada texto contenido en el JSON para su análisis de sentimientos
    for r in input_json:
        # Se codifica un JSON que será enviado al API de text-processing para analizar el sentimiento
        data = urllib.urlencode({"text": input_json['review ' + str(count)]})
        # Se conecta con el API de text-processing y se envía el JSON codificado
        u = urllib.urlopen("http://text-processing.com/api/sentiment/", data)
        # Se lee el resultado del análisis
        result = u.read()
        # Se convierte en JSON el resultado leído para su contabilizar los sentimientos
        json_result = json.loads(result)
        # Se incrementa el contador para continuar con la iteración
        count += 1
        # Se contabiliza el sentimiento de acuerdo al tipo de sentimiento
        if json_result['label'] == 'pos':
            positive += 1
        elif json_result['label'] == 'neg':
            negative += 1
        elif json_result['label'] == 'neutral':
            neutral += 1
    # Se llena el JSON que contendrá la respuesta del análisis de sentimientos
    json_data['positive'] = str(positive)
    json_data['negative'] = str(negative)
    json_data['neutral'] = str(neutral)
    total_reviews = positive + negative + neutral
    json_data['total reviews'] = str(total_reviews)
    # Se devuelve el JSON que contiene la repsuesta
    return json.dumps(json_data)

if __name__ == '__main__':
    # Se define el puerto del sistema operativo que utilizará el micro servicio
    port = int(os.environ.get('PORT', 8082))
    # Se habilita la opción de 'debug' para visualizar los errores
    app.debug = True
    # Se ejecuta el micro servicio definiendo el host '0.0.0.0' para que se pueda acceder desde cualquier IP
    app.run(host='0.0.0.0', port=port)
