#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
import random


class SensorPresion:
    nombre = None
    id = 0

    def __init__(self, nombre):
        self.nombre = "Adulto mayor: " + nombre
        self.id = int(self.set_id())

    def set_id(self):
        return random.randint(1000, 5000)

    def get_name(self):
        return self.nombre

    def get_full_name(self):
        return '[' + str(self.id) + '] ' + str(self.nombre) + ' ' + str(self.marca)

    def start_service(self):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='direct_preasure', type='direct')
        severity = 'presion_arterial'
        presion_arterial_generada = self.simulate_data()
        mensaje = 'PA:' + str(self.id) + ':' + self.nombre + \
            ':' + str(presion_arterial_generada)
        channel.basic_publish(exchange='direct_preasure',
                              routing_key=severity, body=mensaje)
        print('[' + str(self.id) + '] ' + self.nombre +
              ': presion arterial = ' + str(presion_arterial_generada))
        connection.close()

    def simulate_data(self):
        return random.randint(int(100), int(200))
