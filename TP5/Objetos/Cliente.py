class Cliente:
    def __init__(self, estado, horaInicio, horaFin):
        self.estado = estado
        self.horaInicio = horaInicio
        self.horaFin = horaFin


    def __str__(self):
        return (
            f"Cliente(\n"
            f"  estado='{self.estado}',\n"
            f"  horaInicio={self.horaInicio},\n"
            f"  horaFin={self.horaFin},\n"

            ")"
        )
