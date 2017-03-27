# Micro servicios
En esta carpeta se definen los micro servicios utilizados en el capítulo 5. La especificación de cada micro servicio se realizó utilizando blueprint de Apiary.
La especificación de cada micro servicio es la siguiente:
## Text Analysis Microservice
+----------------------------------------------------------------------------------------+
FORMAT: 1A
HOST: 212.237.6.240:8082

# Analysis API

Api que permite evaluar el sentimiento en un texto específico.

## Text Analysis Microservice [/api/v1/text-analysis]

### Sentiment Analysis [POST]

+ Request (application/json)

        {
            "review 0": "Some text",
            "review 1": "Some text",
            "review n": "Some text"
        }

+ Response 200 (application/json)

        {
            "positive": "0",
            "negative": "10",
            "neutral": "5",
            "total reviews": "15"
        }
+----------------------------------------------------------------------------------------+
