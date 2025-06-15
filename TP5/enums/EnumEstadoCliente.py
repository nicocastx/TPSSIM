from enum import Enum

class EnumEstadoCliente(Enum):
    CREADO = ""
    ESPERA_ATENCION = "Esperando Atencion"
    EN_ATENCION = "Siendo atendido"
    SENTADO_MESA = "Sentado en Mesa"
    DESTRUIDO = "Destruído"
    RETIRADO = "Retirado"