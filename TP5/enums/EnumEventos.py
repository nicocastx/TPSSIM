from enum import Enum

class EnumEventos(Enum):
    INICIO = "Inicio"
    LLEGADA_CLIENTE = "Llegada de Cliente"
    FIN_ATENCION = "Fin Atención"
    FIN_LECTURA = "Fin Lectura"
    RETIRO = "Retiro"