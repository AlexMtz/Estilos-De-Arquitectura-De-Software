#!/usr/bin/env python
# -*- coding: utf-8 -*-
#--------------------------------------------------------------------------------------------------
# Archivo: simulador.py
# Capitulo: 3 Patrón Publica-Subscribe
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 2.0 Abril 2017
# Descripción:
#
#   Esta clase es el set-up del proyecto y permite simular los sensores del caso de estudio.
#
#   Las características de ésta clase son las siguientes:
#
#                                          simulador.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |  - Inicializa los sen- |
#           |                       |                         |    sores que actuarán  |
#           |                       |                         |    como publicadores.  |
#           |        set-up         |  - Iniciar el entorno   |  - Solicita al usuario |
#           |                       |    de simulación.       |    el número de adultos|
#           |                       |                         |    mayores para simular|
#           |                       |                         |    los sensores necesa-|
#           |                       |                         |    rios.               |
#           +-----------------------+-------------------------+------------------------+
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                               Métodos:
#           +-------------------------+--------------------------+-----------------------+
#           |         Nombre          |        Parámetros        |        Función        |
#           +-------------------------+--------------------------+-----------------------+
#           |                         |                          |  - Solicita al usua-  |
#           |                         |                          |    rio los valores    |
#           |     set_up_sensors()    |            N/A           |    necesarios para i- |
#           |                         |                          |    niciar la simula-  |
#           |                         |                          |    ción.              |
#           +-------------------------+--------------------------+-----------------------+
#           |                         |                          |  - Ejecuta el método  |
#           |                         |                          |    publish de cada    |
#           |     start_sensors()     |            N/A           |    sensor para iniciar|
#           |                         |                          |    la simulación.     |
#           +-------------------------+--------------------------+-----------------------+
#
#--------------------------------------------------------------------------------------------------
from dht11 import DHT11
from xiaomi_my_band import XiaomiMyBand


class Simulador:
    sensores = []
    id_inicial = 1238940

    def set_up_sensors(self):
        print('+---------------------------------------------+')
        print('|  Bienvenido al Simulador Publica-Subscribe  |')
        print('+---------------------------------------------+')
        print('')
        raw_input('presiona enter para continuar: ')
        print('+---------------------------------------------+')
        print('|        CONFIGURACIÓN DE LA SIMULACIÓN       |')
        print('+---------------------------------------------+')
        adultos_mayores = raw_input('|        número de adultos mayores: ')
        print('+---------------------------------------------+')
        raw_input('presiona enter para continuar: ')
        print('+---------------------------------------------+')
        print('|            ASIGNACIÓN DE SENSORES           |')
        print('+---------------------------------------------+')
        for x in xrange(0, int(adultos_mayores)):
            s = XiaomiMyBand(self.id_inicial)
            self.sensores.append(s)
            print('| wearable Xiaomi My Band asignado, id: ' + str(self.id_inicial))
            print('+---------------------------------------------+')
            self.id_inicial += 1
        s = DHT11(self.id_inicial)
        self.sensores.append(s)
        print('| sensor Dht11 Arduino activado, id: ' + str(self.id_inicial))
        print('+---------------------------------------------+')
        print('|             INICIANDO SIMULACIÓN            |')
        print('+---------------------------------------------+')
        raw_input('presiona enter para iniciar: ')
        self.start_sensors()

    def start_sensors(self):
        for x in xrange(0, 50):
            for s in self.sensores:
                s.publish()

if __name__ == '__main__':
    simulador = Simulador()
    simulador.set_up_sensors()
