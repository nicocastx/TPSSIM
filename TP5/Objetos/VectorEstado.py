
class VectorEstado:
    def __init__(self, reloj, evento, rndLlegada, tiempoLlegada, horaLlegada, colaF, tiempoF, estadoF, horaF, mesasDispL, rndL, cantPagL, tiempoL, horaL, contadorClienteLeido, contadorClienteRetirado, tpl):
        self.reloj = reloj
        self.evento = evento
        self.rndLlegada = rndLlegada
        self.tiempoLlegada = tiempoLlegada
        self.horaLlegada = horaLlegada
        self.colaF = colaF
        self.tiempoF = tiempoF
        self.estadoF = estadoF
        self.horaF = horaF
        self.mesasDispL = mesasDispL
        self.rndL = rndL
        self.cantPagL = cantPagL
        self.tiempoL = tiempoL
        self.horaL = horaL
        self.contadorClienteLeido = contadorClienteLeido
        self.contadorClienteRetirado = contadorClienteRetirado
        self.tpl = tpl

