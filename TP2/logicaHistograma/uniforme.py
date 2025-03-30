import math
import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

from TP2.utilidades.logicaDistribuciones import logicaDistribuciones


class Tabla(tk.Toplevel):
    def __init__(self, root):
        self.logicaDistr = logicaDistribuciones()
        self.serie = []

        super().__init__(root)
        numIntervalos = int(root.campos[1])
        nMuestras = int(root.campos[0])


        self.title("Tabla de resultados")
        self.geometry("500x300")

        #calcular la serie
        for i in range(nMuestras):
            rnd = random.random()
            self.serie.append(rnd)

        intervalos = self.logicaDistr.generarIntervalos(self.serie, numIntervalos)

        print(intervalos)

        contadores_intervalos = self.logicaDistr.contadorIntervalos(self.serie, intervalos)

        print("contadores_intervalos: " + str(contadores_intervalos))

        # Crear la tabla
        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ('Intervalos', 'Frecuencia')

        # Formato de la tabla
        self.tabla.column("#0", width=0, stretch=tk.NO)
        self.tabla.column("Intervalos", anchor=tk.W, width=100)
        self.tabla.column("Frecuencia", anchor=tk.W, width=100)

        # Encabezados de la tabla
        self.tabla.heading("#0", text="", anchor=tk.W)
        self.tabla.heading("Intervalos", text="Intervalos", anchor=tk.W)
        self.tabla.heading("Frecuencia", text="Frecuencia", anchor=tk.W)

        # Agregar datos a la tabla
        for i, intervalo in enumerate(intervalos):
            self.tabla.insert('', 'end', values=(f"{intervalo[0]} - {intervalo[1]}", contadores_intervalos[i]))

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



