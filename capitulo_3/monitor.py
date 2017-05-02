#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------------------------
# Archivo: monitor.py
# Capitulo: 3 Estilo Publica-Subscribe
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.2 Abril 2017
# Descripción:
#
#   Ésta clase define el rol de un monitor que muestra y notifica el resultado de los eventos
#   a los usuarios finales.
#
#   Las características de ésta clase son las siguientes:
#
#                                            monitor.py
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
#           |  print_notification()  |  - datetime: fecha en que|  - Imprime el mensa-  |
#           |                        |     se envió el mensaje. |    je recibido.       |
#           |                        |  - id: identificador del |                       |
#           |                        |     dispositivo que      |                       |
#           |                        |     envió el mensaje.    |                       |
#           |                        |  - value: valor extremo  |                       |
#           |                        |     que se desea notifi- |                       |
#           |                        |     car.                 |                       |
#           |                        |  - name_param: signo vi- |                       |
#           |                        |     tal que se desea no- |                       |
#           +------------------------+--------------------------+-----------------------+
#           |   format_datetime()    |  - datetime: fecha que se|  - Formatea la fecha  |
#           |                        |     formateará.          |    en que se recibió  |
#           |                        |                          |    el mensaje.        |
#           +------------------------+--------------------------+-----------------------+
#
#--------------------------------------------------------------------------------------------------

class Monitor:

    def print_notification(self, datetime, id, value, name_param, model):
    	print "  ---------------------------------------------------"
        print "    ADVERTENCIA"
        print "  ---------------------------------------------------"
        print "    Se ha detectado un incremento de " + str(name_param) + " (" + str(value) + ")" + " a las " + str(self.format_datetime(datetime)) + " en el adulto mayor que utiliza el dispositivo " + str(model) + ":" + str(id)
        print ""
        print ""

    def format_datetime(self, datetime):
    	values_datetime = datetime.split(':')
    	f_datetime = values_datetime[3] + ":" + values_datetime[4] + " del " + values_datetime[0] + "/" + values_datetime[1] + "/" + values_datetime[2]
    	return f_datetime
