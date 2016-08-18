#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pika
import sys
from SignosVitales import SignosVitales


class TemperaturaManager:
    temperatura_maxima = 0
    status = ""
    values_parameters = 0

    def setUpManager(self, max):
        self.temperatura_maxima = max

    def filter_event(self, temperature):
        if temperature < self.temperatura_maxima:
            return False
        else:
            return True

    def start_consuming(self):
        self.values_parameters = sys.argv[1]
        print (self.values_parameters)
        self.create_filter()
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='adultos_mayores',
                                 type='topic')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        binding_keys = ['temperatura']
        for binding_key in binding_keys:
            channel.queue_bind(exchange='adultos_mayores',
                               queue=queue_name, routing_key=binding_key)

        print(' [*] Start monitoring. Press CTRL+C for exit monitoring')
        channel.basic_consume(self.callback,
                              queue=queue_name,
                              no_ack=True)
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        values = body.split(':')
        if self.filter_event(int(values[4])):
            self.status = "Warning: " + \
                str(values[3]) + " tiene calentura: " + str(values[4])
            monitor = SignosVitales()
            monitor.print_notification(self.status)

    def create_filter(self):
        max_value = self.values_parameters
        self.setUpManager(max_value)

test = TemperaturaManager()
test.start_consuming()
