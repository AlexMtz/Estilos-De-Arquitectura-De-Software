#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import pika
from SensorTemperatura import SensorTemperatura
from SensorRitmoCardiaco import SensorRitmoCardiaco
from SensorPresion import SensorPresion


class SetUpSimulador:
    """
    Esta clase permite Simular los eventos en un asilo de adultos
    mayores.
    """
    sensores = []
    temperatura = 0
    ritmo_cardiaco = 0
    presion = 0

    def main(self):
        print('Bienvenido al Simulador P/S versión 1.0')
        print('Simularemos 3 tipos de eventos en adultos mayores:')
        print('Calentura, Hipertensión y Taquicardia')
        print("¿Cuántos publicadores?")
        publishers = raw_input('número entero: ')
        print("Configuremos cada uno de los publicadores")
        for x in xrange(0, int(publishers)):
            print("¿A quién se asociara éste publicador (Sensor)?")
            nombre = raw_input('nombre de la persona adulta: ')
            self.create_temperature_sensor(nombre)
            self.create_preasure_sensor(nombre)
            self.create_heart_rate_sensor(nombre)
        print("Para los consumidores, tendremos un monitor que nos indicará cuando un evento suceda")
        print("Para ello configuraremos nuestro monitor")
        print("**TEMPERATURA**")
        print('Para detectar calentura es necesario establecer')
        print('(Se recomienda utilizar un valor mínimo de 37)')
        print('¿Cuál será la temperatura máxima soportada por los adultos?')
        temperatura_maxima = raw_input('temperatura máxima: ')
        self.temperatura = int(temperatura_maxima)
        print("**RITMO CARDIACO**")
        print('Para detectar Taquicardia es necesario establecer')
        print('(Se recomienda utilizar un valor mínimo de 100)')
        print('¿Cuántos serán los latidos máximos permitidos en los adultos?')
        ritmo_maximo = raw_input('ritmo máximo: ')
        self.ritmo_cardiaco = int(ritmo_maximo)
        print("**PRESION ARTERIAL**")
        print('Para detectar Hipertensión es necesario establecer')
        print('(Se recomienda utilizar un valor mínimo de 140)')
        print('¿Cuál es la presión máxima soportada por los adultos?')
        presion_maxima = raw_input('presión máxima: ')
        self.presion = int(presion_maxima)
        print("Iniciando consumidores listo para escuchar")
        self.run_simulator()

    def create_temperature_sensor(self, nombre):
        s = SensorTemperatura(nombre)
        self.sensores.append(s)

    def create_preasure_sensor(self, nombre):
        s = SensorPresion(nombre)
        self.sensores.append(s)

    def create_heart_rate_sensor(self, nombre):
        s = SensorRitmoCardiaco(nombre)
        self.sensores.append(s)

    def run_simulator(self):
        self.start_consumers()
        self.start_publishers()

    def start_consumers(self):
        os.system(
            "gnome-terminal -e 'bash -c \"python TemperaturaManager.py 37; sleep 20 \"'")
        os.system(
            "gnome-terminal -e 'bash -c \"python RitmoCardiacoManager.py 100; sleep 20 \"'")
        os.system(
            "gnome-terminal -e 'bash -c \"python PresionManager.py 140; sleep 20 \"'")

    def start_publishers(self):
        for x in xrange(0, 1000):
            for s in self.sensores:
                s.start_service()
                time.sleep(1.0)

    def stop_simulation(self):
        for s in self.sensores:
            s.stop()

if __name__ == '__main__':
    simulador = SetUpSimulador()
    simulador.main()
