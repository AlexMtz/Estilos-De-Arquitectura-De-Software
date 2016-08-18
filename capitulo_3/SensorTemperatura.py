#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import pika


class SensorTemperatura():
    nombre = None
    id = 0

    def __init__(self, nombre):
        self.nombre = "Guest: " + nombre
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
        channel.exchange_declare(exchange='adultos_mayores', type='topic')
        routing_key = 'temperatura'
        temperatura_generada = self.simulate_data()
        mensaje = 'TM:' + str(self.id) + ':' + self.nombre + \
            ':' + str(temperatura_generada)
        channel.basic_publish(exchange='adultos_mayores',
                              routing_key=routing_key, body=mensaje)
        print('[' + str(self.id) + '] ' + self.nombre +
              ':' + str(temperatura_generada))
        connection.close()

    def simulate_data(self):
        return random.randint(int(0), int(100))
