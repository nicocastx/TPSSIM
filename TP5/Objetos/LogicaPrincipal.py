import random

from TP5.Objetos.VectorEstado import VectorEstado
from TP5.enums.EnumEstadoFernando import EnumEstadoFernando
from TP5.enums.EnumEventos import EnumEventos


class LogicaPrincipal:

    def __init__(self, limInfLlegada, limSupLlegada, tiempoFernando, tiempo_limite, cantIteracionesMostrar, hora_desde):
        #Parametros desde interfaz
        self.limInfLlegada = 1#limInfLlegada
        self.limSupLlegada = 10#limSupLlegada
        self.tiempoFernando = 15#tiempoFernando
        self.tiempo_limite = 30#tiempo_limite
        self.cantIteracionesMostrar = 999#cantIteracionesMostrar
        self.hora_desde = 0#hora_desde

        # Parametros de la simulacion
        self.veUltimo = VectorEstado()
        self.veNuevo = VectorEstado()
        self.cadenaTabla = []

        self.tiempoSimulacion = 0
        self.cantIteraciones = 0
        self.rndLlegada = 0
        #COLA CLIENTE todo pensar si en verdad hace falta xd
        self.colaClientes = []

    def simular(self):
        while self.tiempoSimulacion < self.tiempo_limite:
            if self.tiempoSimulacion == 0:
                self.eventoInicio()
            elif self.tiempoSimulacion > 0 and self.veUltimo.proximoEvento == EnumEventos.LLEGADA_CLIENTE.value:
                self.veNuevo.reloj = self.tiempoSimulacion
                print("Una llegada")
                print("tiempo antes de procesar evento: " + str(self.tiempoSimulacion))
                self.eventoLlegada()
            elif self.tiempoSimulacion > 0 and self.veUltimo.proximoEvento == EnumEventos.FIN_ATENCION.value:
                print("un fin atencion")
                self.tiempoSimulacion = self.tiempo_limite
                break

            self.tiempoSimulacion = self.veNuevo.definirNuevoTiempoSimulacion()
            self.veNuevo.definirProximoEvento()

            self.veUltimo = self.veNuevo

            self.rellenarTabla()


    def calcularUniforme(self):
        return round(self.limInfLlegada + self.rndLlegada * (self.limSupLlegada - self.limInfLlegada), 4)

    def rellenarTabla(self):
        if self.tiempoSimulacion >= self.hora_desde and self.cantIteracionesMostrar > self.cantIteraciones:
            self.cantIteraciones += 1
            self.cadenaTabla.append(self.veNuevo.formatoFila())


    def eventoInicio(self):
        self.rndLlegada = round(random.random(), 4)
        valorUniforme = self.calcularUniforme()

        self.veNuevo = VectorEstado(self.tiempoSimulacion, EnumEventos.INICIO.value, "", self.rndLlegada,
                                    valorUniforme, valorUniforme + self.tiempoSimulacion,
                                    0, self.tiempoFernando, EnumEstadoFernando.LIBRE.value, 0,
                                    10, 0, 0, 0, 0,
                                    0, 0, 0)

    def eventoLlegada(self):
        self.veNuevo.evento = self.veUltimo.proximoEvento
        self.rndLlegada = round(random.random(), 4)
        valorUniforme = self.calcularUniforme()
        self.veNuevo.rndLlegada = self.rndLlegada
        self.veNuevo.tiempoLlegada = self.tiempoSimulacion
        self.veNuevo.tiempoProximaLlegada = self.tiempoSimulacion + valorUniforme

        if self.veNuevo.colaF == 0:
            self.veNuevo.llegadaSinColaFernando()
        else:
            self.veNuevo.colaF = self.veNuevo.colaF + 1









