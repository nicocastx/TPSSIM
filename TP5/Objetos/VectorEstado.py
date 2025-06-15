from TP5.Objetos.Cliente import Cliente
from TP5.enums.EnumEstadoCliente import EnumEstadoCliente
from TP5.enums.EnumEstadoFernando import EnumEstadoFernando
from TP5.enums.EnumEventos import EnumEventos


class VectorEstado:
    def __init__(self, reloj=None, evento=None, proximoEvento=None, rndLlegada=None, tiempoLlegada=None,
                 horaLlegada=None, colaF=None, tiempoF=None, estadoF=None,
                 horaF=None, mesasDispL=None, rndLectura=None, cantPagLectura=None, tiempoLectura=None,
                 horaLectura=None, contadorClienteLeido=None,
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

        # Es necesario para saber cual es el siguiente cliente a ser atendido
        self.colaClientes = []

        # parametros auxiliares
        self.maximoTiempo = 0

    # todo implementar revisando la lista de clientes
    def definirNuevoTiempoSimulacion(self):
        # Filtrar los valores que no son cero
        tiempos = [t for t in [self.horaLlegada, self.horaF, self.horaLectura] if t > 0]
        # Si no hay tiempos válidos, retornar 0
        if not tiempos:
            self.maximoTiempo = 0
        else:
            self.maximoTiempo = min(tiempos)
        self.definirProximoEvento()
        return self.maximoTiempo

    # todo implementar revisando la lista de clientes
    def definirProximoEvento(self):
        if self.maximoTiempo == self.horaLlegada:
            # todo tal vez se puede plantear en otro lado? lo plantee aca porque la condicion esta se cumple tanto para el inicio como llegada
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

    def llegadaConColaFernando(self):
        self.colaF = self.colaF + 1
        for pos,cliente in enumerate(self.clientes):
            if cliente.estado == EnumEstadoCliente.CREADO.value:
                self.colaClientes.append(pos)
                cliente.estado = EnumEstadoCliente.ESPERA_ATENCION.value
                break

    def AquiNoTienenMesas(self):
        for i in self.clientes:
            if i.estado == EnumEstadoCliente.CREADO.value:
                i.estado = EnumEstadoCliente.RETIRADO.value
                break
        self.contadorClienteRetirado = self.contadorClienteRetirado + 1

    # todo deberia revisar si hay cola y si hay mesas libres
    def finAtencionFernandoConCola(self):
        pass


    def TocoLeer(self):
        pass

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
