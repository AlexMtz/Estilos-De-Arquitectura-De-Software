#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------------------------
# Archivo: signos_vitales.py
# Capitulo: 3 Patrón Publica-Subscribe
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.2 Marzo 2017
# Descripción:
#
#   Ésta clase define el rol de un monitor que muestra y notifica el resultado de los eventos
#   a los operadores.
#
#   Las características de ésta clase son las siguientes:
#
#                                        signos_vitales.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |  - Es utilizado por    |
#           |                       |                         |    todas las clases    |
#           |                       |                         |    que reciben los     |
#           |        Monitor        |  - Mostrar datos a los  |    eventos.            |
#           |                       |    usuarios finales.    |  - Muestra el resulta- |
#           |                       |                         |    do de los eventos   |
#           |                       |                         |    un segundo después  |
#           |                       |                         |    de haber ocurrido.  |
#           +-----------------------+-------------------------+------------------------+
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |  - Imprime el mensa-  |
#           |   print_notification() |      String: message     |    je recibido desde  |
#           |                        |                          |    los suscriptores.  |
#           +------------------------+--------------------------+-----------------------+
#
#--------------------------------------------------------------------------------------------------

class SignosVitales:

    def print_notification(self, message):
        print(str(message))
