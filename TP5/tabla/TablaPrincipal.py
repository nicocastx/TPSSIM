import tkinter as tk
import tksheet


class TablaPrincipal(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=10, pady=10)

        # Configurar estilo para la última fila
        self.sheet = tksheet.Sheet(self,
                                 show_x_scrollbar=True,
                                 show_y_scrollbar=True)
        
        # Definir el estilo para la última fila
        self.sheet.change_theme("light blue")
        self.sheet.highlight_columns(columns=[], bg="#f0f0f0", fg="black")
        self.sheet.highlight_rows(rows=[], bg="#f0f0f0", fg="black")
        
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
            "Proximo evento",
            "RND Llegada",
            "Tiempo Llegada",
            "Hora Llegada",
            "Cola Fernando",
            "Tiempo atencion",
            "Estado",
            "Hora Fin Atencion",
            "Mesas disponibles",
            "RND paginas",
            "Cantidad Paginas",
            "Tiempo de lectura",
            "Hora Fin lectura",
            "Cantidad de leídos",
            "Cantidad de retirados",
            "Cantidad de atendidos", #
            "T. Acum lectura",
            "T. Lectura promedio",
            "% de retirados" #
        ]

        self.sheet.headers(encabezados)

    def set_datos(self, data):
        headers_fijos = self.sheet.headers()[:21]
        self.sheet.headers(headers_fijos)
        self.sheet.set_sheet_data([])

        # Encontrar el número máximo de columnas en los datos
        max_columns = max(len(row) for row in data) if data else 0

        # Si no hay suficientes columnas para los clientes, agregar las que faltan
        if max_columns > len(self.sheet.headers()):
            # Calcular cuántos clientes nuevos hay
            num_clientes = (max_columns - 21) // 3  # 18 columnas fijas iniciales

            # Agregar columnas para los clientes que faltan
            for i in range(len(self.sheet.headers()) - 21, num_clientes + 1):  # +1 porque i empieza en 1
                if i > 0:  # Evitar cliente 0
                    self.add_cliente_columna(f"Cliente {i}", ["Estado", "Inicio", "Fin Lectura"])

        # Asegurarse de que todas las filas tengan el mismo número de columnas
        headers_count = len(self.sheet.headers())
        for row in data:
            while len(row) < headers_count:
                row.append("")  # Rellenar con cadenas vacías

            # Truncar filas que tengan más columnas que los encabezados
            row = row[:headers_count]

        # Configurar los datos
        self.sheet.set_sheet_data(data)
        
        # Resaltar la última fila
        self.resaltar_ultima_fila()
        
        # Asegurarse de que la tabla se redibuje correctamente
        self.sheet.refresh()

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

    def resaltar_ultima_fila(self):
        """Resalta solo la última fila de la tabla"""
        data = self.sheet.get_sheet_data()
        if not data:
            return

        ultima_fila = len(data) - 1

        # Quitar resaltado de todas las filas excepto la última
        filas_a_limpiar = list(range(len(data)))
        filas_a_limpiar.remove(ultima_fila)
        self.sheet.highlight_rows(rows=filas_a_limpiar, bg="#f0f0f0", fg="black")

        # Resaltar la última fila
        self.sheet.highlight_rows(rows=[ultima_fila], bg="#ffeb3b", fg="black")
