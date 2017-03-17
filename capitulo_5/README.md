# Capitulo 3

## "Sentiment Analysis System"

### Prerequisitos

Antes de ejecutar el código aseguradte de haber realizado las acciones indicadas en la Wiki -> SentimentAnalysisSystem  
[Prerequisitos](https://github.com/AlexMtz/Estilos-De-Arquitectura-De-Software/wiki/SentimentAnalysisSystem)

### Ejecutar cada servicio

Para ejecutar el sistema es necesario seguir los sigiuentes pasos:  
1. Abrir terminal en Ubuntu.  
2. Clonar el repositorio:   `git clone https://github.com/AlexMtz/Estilos-De-Arquitectura-De-Software.git`  
3. Ingresar a la carpeta que descargamos:   `cd Estilos-De-Arquitectura-De-Software/`  
4. Acceder al capítulo 5:  `cd capitulo_5/`  
5. Ejecutar cliente: `python sentiment_app.py`
6. Repetir los pasos '1','3','4'
7. Ejecutar servicio de Twitter: `python twitter_mc.py`
8. Repetir los pasos '1','3','4'
9. Ejecutar servicio de análisis de texto: `python text_analysis_mc.py`
10. Repetir los pasos '1','3','4'
5. Ejecutar servicio de información: `python information_mc.py
`  

Si el simulador se ejecuto de manera correcta encontraremos lo siguiente:  
[Chapter 5](https://drive.google.com/open?id=0B1FMJsKfgRaPRnZCMDhUYkhTQms)

## Definición del API

FORMAT: 1A

HOST: http://localhost:8080/api/v1

# Sentiment API

Sentiment API es un API que permite obetener y analizar reviews 
publicados en Twitter acerca de una película o serie de Netflix para
conocer el sentimiento expresado. Además de obtener la información
acerca de esa película o serie. A continuación se detalla su 
definición.

## Servicio de Twitter [/tweets{?h}]

Obtiene los reviews más recientes publicados en Twitter acerca de una
serie o pelicula de Netflix favorita.

+ Parameters
    + h - Corresponde al nombre de usuario que utiliza la serie o película
    en Twitter.
    

### Reviews en Twitter [GET]
+ Response 200 (application/json)

        [
            {
                "review 1": "algún review en Twitter"
            }
            {
                "review 2": "otro review en Twitter"
            }
            {
                "review #": "n review de Twitter"
            }
        ]

## Servicio de análisis de texto [/text-analysis]

Analiza el sentimiento dentro de un texto escrito en lenguaje natural.

### Analizar sentimiento [POST]

+ Request (application/json)

        [
            {
                "review 1": "algún review en Twitter"
            }
            {
                "review 2": "otro review en Twitter"
            }
            {
                "review #": "n review de Twitter"
            }
        ]

+ Response 200 (application/json)

        {
            "positive": 50,
            "negative": 20,
            "neutral": 30,
            "total reviews": 100
        }

## Servicio de información [/information{?t}]

Obtiene la información general acerca de la serie o película consultada
desde las fuentes de IMDb.

+ Parameters
    + t - Corresponde al título de la película o serie de Netflix.

### Obtener información [GET]
+ Response 200 (application/json)

        {
            "Title": "Stranger Things",
            "Year": "2016–",
            "Rated": "TV-14",
            "Released": "15 Jul 2016",
            "Runtime": "55 min",
            "Genre": "Drama, Fantasy, Horror",
            "Director": "N/A",
            "Writer": "Matt Duffer, Ross Duffer",
            "Actors": "Winona Ryder, David Harbour, Finn Wolfhard, Millie Bobby Brown",
            "Plot":"In a small town where everyone knows everyone, a peculiar incident starts a chain of events that leads to the disappearance of a child - which begins to tear at the fabric of an otherwise peaceful community. Dark government agencies and seemingly malevolent supernatural forces converge on the town while a few locals begin to understand that there's more going on than meets the eye.",
            "Language": "English",
            "Country": "USA",
            "Awards": "Nominated for 2 Golden Globes. Another 4 wins & 26 nominations.",
            "Poster": "https://images-na.ssl-images-amazon.com/images/M/MV5BMjEzMDAxOTUyMV5BMl5BanBnXkFtZTgwNzAxMzYzOTE@._V1_SX300.jpg",
            "Metascore": "N/A",
            "imdbRating": "9.0",
            "imdbVotes": "264,555",
            "imdbID": "tt4574334",
            "Type": "series",
            "totalSeasons": "2",
            "Response": "True"
        }

