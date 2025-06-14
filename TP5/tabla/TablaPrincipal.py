import tkinter as tk
import tksheet


class TablaPrincipal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=10, pady=10)

        self.sheet = tksheet.Sheet(self,
                                   show_x_scrollbar=True,
                                   show_y_scrollbar=True)

        self.sheet.enable_bindings(
            "single_select",  # seleccionar una celda
            "row_select",
            "column_select",
            "arrowkeys",
            "right_click_popup_menu",
            "rc_select",
            "copy",
            "paste",
            "delete",
            "undo"
        )

        self.sheet.grid(row=0, column=0, sticky="nswe")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        encabezados = [
            "Reloj",
            "Evento",
            "RND Fernando",
            "Tiempo Llegada",
            "Hora",
            "Cola Fernando",
            "Tiempo atencion",
            "Estado",
            "HoraFin At",
            "Mesas disponibles",
            "RND Lectura",
            "Q pag",
            "Tiempo de lectura",
            "Fin lectura",
            "C Cliente",
            "C clientes Retiran",
            "TLP"
        ]

        self.sheet.headers(encabezados)

    def set_datos(self, data):
        self.sheet.set_sheet_data(data)

    def get_sheet(self):
        return self.sheet

    def add_fila(self, fila):
        """Agrega una nueva fila al final de la tabla"""
        datos_actuales = self.sheet.get_sheet_data()
        datos_actuales.append(fila)
        self.sheet.set_sheet_data(datos_actuales)

    def add_columna(self, nombre_columna):
        """Agrega una nueva columna a la derecha de la tabla"""

        headers_actuales = self.sheet.headers()
        headers_actuales.append(nombre_columna)
        self.sheet.headers(headers_actuales)

        # Asegurarse de que los datos existentes tengan el mismo número de columnas
        datos_actuales = self.sheet.get_sheet_data()
        for fila in datos_actuales:
            if len(fila) < len(headers_actuales):
                fila.append("")  # Rellenar con valor vacío si es necesario
        self.sheet.set_sheet_data(datos_actuales)

    def add_cliente_columna(self, nombre_principal, subcolumnas):
        """
        Crea un grupo de columnas con un encabezado principal que las abarca.
        Ejemplo de uso:
        add_cliente_columna("Cliente 1", ["Estado", "Hora Inicio", "Hora Fin"])
        """
        # Obtener los datos actuales
        headers_actuales = self.sheet.headers()
        datos_actuales = self.sheet.get_sheet_data()

        # Guardar la posición inicial de las nuevas columnas
        indice_inicio = len(headers_actuales)

        # Agregar los encabezados de las subcolumnas con el formato "Cliente 1 - Estado"
        for subcol in subcolumnas:
            headers_actuales.append(f"{nombre_principal} - {subcol}")

        # Actualizar los encabezados
        self.sheet.headers(headers_actuales)

        # Ajustar los datos existentes
        for fila in datos_actuales:
            # Agregar celdas vacías para las subcolumnas
            fila.extend([""] * len(subcolumnas))

        # Actualizar los datos
        self.sheet.set_sheet_data(datos_actuales)

        # Ajustar el ancho de las columnas para mejor visualización
        self.sheet.set_all_column_widths(120)  # Un poco más ancho para los encabezados largos

        # Retornar los índices de las subcolumnas para referencia futura
        return {f"{nombre_principal} - {subcol}": indice_inicio + i
                for i, subcol in enumerate(subcolumnas)}
