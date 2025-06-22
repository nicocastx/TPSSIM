import random

from TP5.Objetos.VectorEstado import VectorEstado
from TP5.enums.EnumEstadoFernando import EnumEstadoFernando
from TP5.enums.EnumEventos import EnumEventos


class LogicaPrincipal:

    def __init__(self, limInfLlegada, limSupLlegada, tiempoFernando, tiempo_limite, cantIteracionesMostrar, hora_desde,
                 k_primer, k_segundo, k_tercero):
        #Parametros desde interfaz
        self.limInfLlegada = 1#limInfLlegada
        self.limSupLlegada = 10#limSupLlegada
        self.tiempoFernando = 15#tiempoFernando
        self.tiempo_limite = 80#tiempo_limite
        self.cantIteracionesMostrar = 0#cantIteracionesMostrar
        self.hora_desde = 0#hora_desde

        # Parametros de la simulacion
        self.mesasDisponibles = 10
        self.limitesCantPaginas = [10, 40]
        self.veUltimo = VectorEstado()
        self.veNuevo = VectorEstado()
        self.cadenaTabla = []


        #tiempo de lectura
        self.k_primer_intervalo = k_primer
        self.k_segundo_intervalo = k_segundo
        self.k_tercer_intervalo = k_tercero

        # self.tiempoLecturaPagina = 3

        self.tiempoSimulacion = 0
        self.cantIteraciones = 0


    def simular(self):
        while self.tiempoSimulacion < self.tiempo_limite:
            self.veNuevo.evento = self.veUltimo.proximoEvento
            self.veNuevo.reloj = self.tiempoSimulacion
            #se podria optimizar pero me dio mucha paja xd
            if self.tiempoSimulacion == 0:
                self.eventoInicio()
            elif self.tiempoSimulacion > 0 and self.veUltimo.proximoEvento == EnumEventos.LLEGADA_CLIENTE.value:
                #esta linea si se repite mucho podria ir arriba del primer if
                print("Una llegada")
                print("tiempo antes de procesar evento: " + str(self.tiempoSimulacion))
                self.eventoLlegada()
            elif self.tiempoSimulacion > 0 and self.veUltimo.proximoEvento == EnumEventos.FIN_ATENCION.value:
                print("Un fin de atencion")
                print("tiempo antes de procesar evento: " + str(self.tiempoSimulacion))
                self.eventoFinAtencion()
            elif self.tiempoSimulacion > 0 and self.veUltimo.proximoEvento == EnumEventos.FIN_LECTURA.value:
                print("Un fin de lectura")
                print("tiempo antes de procesar evento: " + str(self.tiempoSimulacion))
                self.eventoFinLectura()
                self.tiempoSimulacion = self.tiempo_limite
                break

            self.tiempoSimulacion = self.veNuevo.definirNuevoTiempoSimulacion()
            print("tiempo despues de procesar evento: " + str(self.tiempoSimulacion))

            self.veUltimo = self.veNuevo

            self.rellenarTabla()

        self.cadenaTabla.append(self.veUltimo.formatoFila())


    def calcularUniforme(self, rndLlegada, limInf, limSup):
        return round(limInf + (rndLlegada * (limSup - limInf)), 2)

    def rellenarTabla(self):
        #todo se podria implementar una flag, y asi evitar en caso de mostrar todas, mostrar el ultimo 2 veces
        if self.hora_desde == 0 and self.cantIteracionesMostrar == 0:
            self.cadenaTabla.append(self.veNuevo.formatoFila())
        elif self.tiempoSimulacion >= self.hora_desde and self.cantIteracionesMostrar > self.cantIteraciones:
            self.cantIteraciones += 1
            self.cadenaTabla.append(self.veNuevo.formatoFila())

    """
        Se cubre que:
        1) Se penso como si siempre fuera llegada el siguiente evento
        2) Quedan en 0 los acumuladores y varios valores
    """
    def eventoInicio(self):
        rndLlegada = round(random.random(), 2)
        valorUniforme = self.calcularUniforme(rndLlegada, self.limInfLlegada, self.limSupLlegada)

        self.veNuevo = VectorEstado(self.tiempoSimulacion, EnumEventos.INICIO.value, "", rndLlegada,
                                    valorUniforme, valorUniforme + self.tiempoSimulacion,
                                    0, self.tiempoFernando, EnumEstadoFernando.LIBRE.value, 0,
                                    self.mesasDisponibles, 0, 0, 0, 0,
                                    0, 0, 0)

    """
    Se cubre que:
    1) Si hay cola, se agrega un cliente a la cola
    2) Si no hay cola, se atiende a un cliente, se cambio E de Fernando, Se cambie E de cliente
    y mas giladas que me olvide
    """
    def eventoLlegada(self):
        rndLlegada = round(random.random(), 2)
        valorUniforme = self.calcularUniforme(rndLlegada, self.limInfLlegada, self.limSupLlegada)
        self.veNuevo.rndLlegada = rndLlegada
        self.veNuevo.tiempoLlegada = valorUniforme
        self.veNuevo.horaLlegada = self.veNuevo.reloj + valorUniforme

        if self.veNuevo.colaF == 0 and self.veNuevo.estadoF == EnumEstadoFernando.LIBRE.value and self.veNuevo.mesasDispL > 0:
            self.veNuevo.llegadaSinColaFernando()
        elif self.veNuevo.mesasDispL == 0:
            self.veNuevo.aquiNoTienenMesas()
        else:
            self.veNuevo.llegadaConColaFernando()

    #todo implementar, y ver de como implementar aqui el Euler, actualmente no anda porque falta la logica de maximo tiempo y definir siguiente evento
    """"
    Deberia:
    1) Calcular el rnd de lectura
    2) Calcular el tiempo finde lectura
    3) cambiar estado fernando si no hay cola
    4) cambiar estado fernando si hay cola
    5) cambiar estado cliente a sentado en mesa
    """
    def eventoFinAtencion(self):
        #todo ocurre lo mismo con fin atencion y lectura, podria hacer metodo resetearRandoms() algo asi para el nuevo VE
        self.veNuevo.rndLlegada = 0
        self.veNuevo.tiempoLlegada = 0

        # Calculo de tiempo lectura
        self.veNuevo.rndLectura = round(random.random(), 2)
        self.veNuevo.cantPagLectura = self.calcularUniforme(self.veNuevo.rndLectura, self.limitesCantPaginas[0], self.limitesCantPaginas[1])
        # todo implementar calculo tiempo lectura Euler, no implemente esto en VE porque no se como quedara con el euler implementado
        self.veNuevo.k = self.calcular_k()
        self.veNuevo.tiempoLectura = self.veNuevo.k / 5 * 10
        self.veNuevo.horaLectura = self.veNuevo.tiempoLectura + self.veNuevo.reloj

        # Cambio estado cliente
        self.veNuevo.tocoLeer()

        if self.veNuevo.colaF == 0:
            self.veNuevo.estadoF = EnumEstadoFernando.LIBRE.value
        else:
            self.veNuevo.finAtencionFernandoConCola()




    # todo implementar
    def eventoFinLectura(self):
        pass

    def calcular_k(self):
        #todo: se debe poder ingresar el valor de k para cada intervalo de páginas
        if self.veNuevo.cantPagLectura < 20:
            return self.k_primer_intervalo
        elif self.veNuevo.cantPagLectura < 30:
            return self.k_segundo_intervalo
        else:
            return self.k_tercer_intervalo
