import random

from TP5.Objetos.VectorEstado import VectorEstado
from TP5.enums.EnumEstadoFernando import EnumEstadoFernando
from TP5.enums.EnumEventos import EnumEventos


class LogicaPrincipal:

    def __init__(self, limInfLlegada, limSupLlegada, tiempoFernando, tiempo_limite, cantIteracionesMostrar, hora_desde):
        #Parametros desde interfaz
        self.limInfLlegada = 1#limInfLlegada
        self.limSupLlegada = 10#limSupLlegada
        self.tiempoFernando = 25#tiempoFernando
        self.tiempo_limite = 30#tiempo_limite
        self.cantIteracionesMostrar = 999#cantIteracionesMostrar
        self.hora_desde = 0#hora_desde

        # Parametros de la simulacion
        self.veUltimo = VectorEstado()
        self.veNuevo = VectorEstado()
        self.cadenaTabla = []

        self.tiempoSimulacion = 0
        self.cantIteraciones = 0
        #COLA CLIENTE todo pensar si en verdad hace falta xd
        self.colaClientes = []

    def simular(self):
        while self.tiempoSimulacion < self.tiempo_limite:
            #se podria optimizar pero me dio mucha paja xd
            if self.tiempoSimulacion == 0:
                self.eventoInicio()
            elif self.tiempoSimulacion > 0 and self.veUltimo.proximoEvento == EnumEventos.LLEGADA_CLIENTE.value:
                #esta linea si se repite mucho podria ir arriba del primer if
                self.veNuevo.reloj = self.tiempoSimulacion
                print("Una llegada")
                print("tiempo antes de procesar evento: " + str(self.tiempoSimulacion))
                self.eventoLlegada()
            elif self.tiempoSimulacion > 0 and self.veUltimo.proximoEvento == EnumEventos.FIN_ATENCION.value:
                print("Un fin de atencion")
                print("tiempo antes de procesar evento: " + str(self.tiempoSimulacion))
                self.eventoFinAtencion()
                self.tiempoSimulacion = self.tiempo_limite
                break
            elif self.tiempoSimulacion > 0 and self.veUltimo.proximoEvento == EnumEventos.FIN_LECTURA.value:
                print("Un fin de lectura")
                print("tiempo antes de procesar evento: " + str(self.tiempoSimulacion))
                self.eventoFinLectura()

            self.tiempoSimulacion = self.veNuevo.definirNuevoTiempoSimulacion()
            print("tiempo despues de procesar evento: " + str(self.tiempoSimulacion))
            self.veNuevo.definirProximoEvento()

            self.veUltimo = self.veNuevo

            self.rellenarTabla()


    def calcularUniforme(self, rndLlegada):
        return round(self.limInfLlegada + (rndLlegada * (self.limSupLlegada - self.limInfLlegada)), 2)

    def rellenarTabla(self):
        if self.tiempoSimulacion >= self.hora_desde and self.cantIteracionesMostrar > self.cantIteraciones:
            self.cantIteraciones += 1
            self.cadenaTabla.append(self.veNuevo.formatoFila())

    """
        Se cubre que:
        1) Se penso como si siempre fuera llegada el siguiente evento
        2) Quedan en 0 los acumuladores y varios valores
    """
    def eventoInicio(self):
        rndLlegada = round(random.random(), 2)
        valorUniforme = self.calcularUniforme(rndLlegada)

        self.veNuevo = VectorEstado(self.tiempoSimulacion, EnumEventos.INICIO.value, "", rndLlegada,
                                    valorUniforme, valorUniforme + self.tiempoSimulacion,
                                    0, self.tiempoFernando, EnumEstadoFernando.LIBRE.value, 0,
                                    10, 0, 0, 0, 0,
                                    0, 0, 0)

    """
    Se cubre que:
    1) Si hay cola, se agrega un cliente a la cola
    2) Si no hay cola, se atiende a un cliente, se cambio E de Fernando, Se cambie E de cliente
    Caso: Llegan 2 clientes y no pasa un fin de atencion, esta bugeado, lo vuelve a calcular
    """
    def eventoLlegada(self):
        self.veNuevo.evento = self.veUltimo.proximoEvento
        rndLlegada = round(random.random(), 2)
        valorUniforme = self.calcularUniforme(rndLlegada)
        self.veNuevo.rndLlegada = rndLlegada
        self.veNuevo.tiempoLlegada = valorUniforme
        self.veNuevo.horaLlegada = self.tiempoSimulacion + valorUniforme

        if self.veNuevo.colaF == 0:
            self.veNuevo.llegadaSinColaFernando()
        else:
            self.veNuevo.colaF = self.veNuevo.colaF + 1

    #todo implementar
    def eventoFinAtencion(self):
        pass

    # todo implementar
    def eventoFinLectura(self):
        pass











