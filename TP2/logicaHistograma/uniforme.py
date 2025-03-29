import tkinter as tk
from tkinter import ttk

class Tabla(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        print(root.campos[0], root.campos[1])
        self.title("Tabla de resultados")
        self.geometry("500x300")

        # Crear tabla
        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ('Columna 1', 'Columna 2', 'Columna 3')

        # Formato de la tabla
        self.tabla.column("#0", width=0, stretch=tk.NO)
        self.tabla.column("Columna 1", anchor=tk.W, width=100)
        self.tabla.column("Columna 2", anchor=tk.W, width=100)
        self.tabla.column("Columna 3", anchor=tk.W, width=100)

        # Encabezados de la tabla
        self.tabla.heading("#0", text="", anchor=tk.W)
        self.tabla.heading("Columna 1", text="Columna 1", anchor=tk.W)
        self.tabla.heading("Columna 2", text="Columna 2", anchor=tk.W)
        self.tabla.heading("Columna 3", text="Columna 3", anchor=tk.W)

        # Agregar datos a la tabla (por ejemplo, puedes agregar datos aquí)
        for i in range(10):
            self.tabla.insert('', 'end', values=(f'Dato {i}', f'Dato {i+1}', f'Dato {i+2}'))

        # Botón para copiar todos los valores
        self.boton_copiar = tk.Button(self, text="Copiar todos los valores", command=self.copiar_valores)
        self.boton_copiar.pack()

        # Agregar tabla a la ventana
        self.tabla.pack()

    def copiar_valores(self):
        # Obtener la lista de ítems de la tabla
        items = self.tabla.get_children()

        # Crear una lista para almacenar los valores
        valores = []

        # Recorrer la lista de ítems y obtener los valores
        for item in items:
            valores.append(self.tabla.item(item, 'values'))

        # Formatear los valores en formato CSV con tabulación
        csv_data = []
        csv_data.append('\t'.join(self.tabla['columns']))  # Agregar los nombres de las columnas
        for fila in valores:
            csv_data.append('\t'.join(map(str, fila)))

        # Unir las filas con saltos de línea
        csv_data = '\n'.join(csv_data)

        # Copiar los datos a la clipboard
        self.clipboard_clear()
        self.clipboard_append(csv_data)

        # Imprimir un mensaje para confirmar que los valores han sido copiados
        print("Valores copiados")