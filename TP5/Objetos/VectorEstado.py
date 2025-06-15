from TP5.Objetos.Cliente import Cliente
from TP5.enums.EnumEstadoCliente import EnumEstadoCliente
from TP5.enums.EnumEstadoFernando import EnumEstadoFernando
from TP5.enums.EnumEventos import EnumEventos


class VectorEstado:
    def __init__(self, reloj=None, evento=None, proximoEvento=None, rndLlegada=None, tiempoLlegada=None, horaLlegada=None, colaF=None, tiempoF=None, estadoF=None,
                 horaF=None, mesasDispL=None, rndLectura=None, cantPagLectura=None, tiempoLectura=None, horaLectura=None, contadorClienteLeido=None,
                 contadorClienteRetirado=None, tlp=None):
        self.reloj = reloj
        self.evento = evento
        self.proximoEvento = proximoEvento
        self.rndLlegada = rndLlegada
        self.tiempoLlegada = tiempoLlegada
        self.horaLlegada = horaLlegada
        self.colaF = colaF
        self.tiempoF = tiempoF
        self.estadoF = estadoF
        self.horaF = horaF
        self.mesasDispL = mesasDispL
        self.rndLectura = rndLectura
        self.cantPagLectura = cantPagLectura
        self.tiempoLectura = tiempoLectura
        self.horaLectura = horaLectura
        self.contadorClienteLeido = contadorClienteLeido
        self.contadorClienteRetirado = contadorClienteRetirado
        self.tlp = tlp
        self.clientes = []

        #parametros auxiliares
        self.maximoTiempo = 0

    def definirNuevoTiempoSimulacion(self):
        self.maximoTiempo = max(self.horaLlegada, self.horaF, self.horaLectura)
        return self.maximoTiempo

    def definirProximoEvento(self):
        if self.maximoTiempo == self.horaLlegada:
            #todo tal vez se puede plantear en otro lado?
            self.clientes.append(Cliente(EnumEstadoCliente.CREADO.value, 0, 0, 0))
            self.proximoEvento = EnumEventos.LLEGADA_CLIENTE.value
        elif self.maximoTiempo == self.horaF:
            self.proximoEvento = EnumEventos.FIN_ATENCION.value
        elif self.maximoTiempo == self.horaLectura:
            self.proximoEvento = EnumEventos.FIN_LECTURA.value

    def llegadaSinColaFernando(self):
        self.estadoF = EnumEstadoFernando.OCUPADO.value
        self.horaF = self.reloj + self.tiempoF
        for i in self.clientes:
            if i.estado == EnumEstadoCliente.CREADO.value:
                i.estado = EnumEstadoCliente.EN_ATENCION.value
                break

    def formatoFila(self):
        fila = [
            self.reloj,
            self.evento,
            self.proximoEvento,
            self.rndLlegada,
            self.tiempoLlegada,
            self.horaLlegada,
            self.colaF,
            self.tiempoF,
            self.estadoF,
            self.horaF,
            self.mesasDispL,
            self.rndLectura,
            self.cantPagLectura,
            self.tiempoLectura,
            self.horaLectura,
            self.contadorClienteLeido,
            self.contadorClienteRetirado,
            self.tlp
        ]

        # Agregar los atributos de cada cliente a la fila
        for cliente in self.clientes:
            fila.extend([
                cliente.estado,
                cliente.horaInicio,
                cliente.horaFin,
                cliente.tiempoLectura
            ])

        return fila

    def __str__(self):
        return (
            f"VectorEstado(\n"
            f"  reloj={self.reloj},\n"
            f"  evento='{self.evento}',\n"
            f"  proximoEvento='{self.proximoEvento}',\n"
            f"  rndLlegada={self.rndLlegada},\n"
            f"  tiempoLlegada={self.tiempoLlegada},\n"
            f"  horaLlegada={self.horaLlegada},\n"
            f"  colaF={self.colaF},\n"
            f"  tiempoF={self.tiempoF},\n"
            f"  estadoF='{self.estadoF}',\n"
            f"  horaF={self.horaF},\n"
            f"  mesasDispL={self.mesasDispL},\n"
            f"  rndLectura={self.rndLectura},\n"
            f"  cantPagLectura={self.cantPagLectura},\n"
            f"  tiempoLectura={self.tiempoLectura},\n"
            f"  horaLectura={self.horaLectura},\n"
            f"  contadorClienteLeido={self.contadorClienteLeido},\n"
            f"  contadorClienteRetirado={self.contadorClienteRetirado},\n"
            f"  tlp={self.tlp},\n"
            f"  clientes=[{', '.join(str(c) for c in self.clientes)}]\n"
            ")"
        )
