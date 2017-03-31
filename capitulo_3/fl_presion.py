#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------------------------
# Archivo: fl_presion.py
# Capitulo: 3 Patrón Publica-Suscribe
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.5.2 Marzo 2017
# Descripción:
#
#   Ésta clase define el rol de un suscriptor, componente interesado en recibir los mensajes.
#   Las características de ésta clase son las siguientes:
#
#                                        fl_presion.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |  - Recibir mensajes     |  - Se suscribe a la    |
#           |      Suscriptor       |  - Notificar al         |    cola de 'direct     |
#           |                       |    monitor.             |    preasure'.          |
#           |                       |  - Filtrar valores      |  - Define un rango en  |
#           |                       |    de presion arterial. |    el que la presión   |
#           |                       |                         |    tiene valores vá-   |
#           |                       |                         |    lidos.              |
#           |                       |                         |  - Notifica al monitor |
#           |                       |                         |    después después de  |
#           |                       |                         |    recibir el mensaje. |
#           +-----------------------+-------------------------+------------------------+
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |  - Establece el valor |
#           |    set_up_manager()    |      int: sistolica      |    máximo permitido   |
#           |                        |                          |    de la presión      |
#           |                        |                          |    arterial sistólica.|
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |  - Lee los argumentos |
#           |                        |                          |    con los que se e-  |
#           |                        |                          |    jecuta el programa |
#           |                        |                          |    para establecer el |
#           |                        |                          |    valor máximo que   |
#           |                        |                          |    puede tomar la     |
#           |                        |                          |    presión sistólica. |
#           |   start_consuming()    |          None            |  - Realiza la conexi- |
#           |                        |                          |    ón con el servidor |
#           |                        |                          |    de RabbitMQ local. |
#           |                        |                          |  - Declara el tipo de |
#           |                        |                          |    intercambio y a    |
#           |                        |                          |    que cola se va a   |
#           |                        |                          |    subscribir.        |
#           |                        |                          |  - Comienza a esperar |
#           |                        |                          |    los eventos.       |
#           +------------------------+--------------------------+-----------------------+
#           |                        |   ch: propio de Rabbit   |  - Contiene la lógica |
#           |                        | method: propio de Rabbit |    de negocio.        |
#           |       callback()       |   properties: propio de  |  - Se manda llamar    |
#           |                        |         RabbitMQ         |    cuando un evento   |
#           |                        |       String: body       |    ocurre.            |
#           +------------------------+--------------------------+-----------------------+
#
#           Nota: "propio de Rabbit" implica que se utilizan de manera interna para realizar
#            la recepcion de datos, para éste ejemplo no hubo necesidad de utilizarlos
#            y para evitar la sobrecarga de información se han omitido sus detalles.
#            Para más información acerca del funcionamiento interno de RabbitMQ puedes
#            visitar: https://www.rabbitmq.com/
#            
#
#--------------------------------------------------------------------------------------------------


import pika
import sys
from signos_vitales import SignosVitales

class FlPresion:
    presion_sistolica = 0
    values_parameters = []

    def set_up_manager(self, sistolica):
        self.presion_sistolica = sistolica

    def start_consuming(self):
        self.values_parameters = sys.argv[1]
        self.set_up_manager(self.values_parameters)
        #   +--------------------------------------------------------------------------------------+
        #   | La siguiente linea permite realizar la conexión con el servidor que aloja a RabbitMQ |
        #   +--------------------------------------------------------------------------------------+
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        channel = connection.channel()
        #   +----------------------------------------------------------------------------------------+
        #   | La siguiente linea permite definir el tipo de intercambio y de que cola recibirá datos |
        #   +----------------------------------------------------------------------------------------+
        channel.exchange_declare(exchange='direct_preasure',
                                 type='direct')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        severity = 'presion_arterial'
        #   +----------------------------------------------------------------------------+
        #   | La siguiente linea permite realizar la conexión con la cola que se definio |
        #   +----------------------------------------------------------------------------+
        channel.queue_bind(exchange='direct_preasure',
                            queue=queue_name, routing_key=severity)
        print(' [*] Inicio de monitoreo de presión arterial. Presiona CTRL+C para finalizar el monitoreo')
        #   +----------------------------------------------------------------------------------------+
        #   | La siguiente linea permite definir las acciones que se realizarán al ocurrir un método |
        #   +----------------------------------------------------------------------------------------+
        channel.basic_consume(self.callback,
                              queue=queue_name,
                              no_ack=True)
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        values = body.split(':')
        event = int(values[3])
        if event > int(self.presion_sistolica):
            monitor = SignosVitales()
            monitor.print_notification('+----------+-----------------------+----------+')
            monitor.print_notification('|   ' + str(values[3]) + '   |   TIENE HIPERTENSIÓN  |   ' + str(values[2]) + '   |')
            monitor.print_notification('+----------+-----------------------+----------+')
            monitor.print_notification('')
            monitor.print_notification('')

test = FlPresion()
test.start_consuming()
