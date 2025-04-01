import math
import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

from TP2.utilidades.logicaDistribuciones import logicaDistribuciones

class TablaExponencial(tk.Toplevel):
    def __init__(self, parent, numIntervalos, nMuestras, mu):
        super().__init__(parent)
        self.logicaDistr = logicaDistribuciones()
        self.serie = []
        self.numIntervalos = numIntervalos
        self.nMuestras = nMuestras
        self.mu = mu

        self.title("Tabla de resultados (Distribución Exponencial)")
        self.geometry("500x300")

        upper_limit = 1 - math.exp(-1 / self.mu)


        # Generación de números exponenciales ACOTADOS [0, 1)
        for _ in range(nMuestras):
            rnd = random.random() * upper_limit  # RND escalado
            x = -self.mu * math.log(1 - rnd)
            self.serie.append(x)


        intervalos = self.logicaDistr.generarIntervalos(self.serie, numIntervalos)
        contadores_intervalos = self.logicaDistr.contadorIntervalos(self.serie, intervalos)

        print("Intervalos:", intervalos)
        print("Frecuencias:", contadores_intervalos)

        # Crear la tabla
        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ('Intervalos', 'Frecuencia')

        self.tabla.column("#0", width=0, stretch=tk.NO)
        self.tabla.column("Intervalos", anchor=tk.W, width=100)
        self.tabla.column("Frecuencia", anchor=tk.W, width=100)

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

        # Añadir botón para histograma
        self.boton_histograma = tk.Button(
            self,
            text="Mostrar Histograma",
            command=self.mostrar_histograma
        )
        self.boton_histograma.pack()

    def mostrar_histograma(self):
        plt.hist(self.serie, bins=self.numIntervalos, density=True)
        plt.title(f'Histograma Exponencial (μ={self.mu})')
        plt.xlabel('Valores')
        plt.ylabel('Frecuencia')
        plt.show()

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
        csv_data.append('\t'.join(self.tabla['columns']))
        for fila in valores:
            csv_data.append('\t'.join(map(str, fila)))

        # Unir las filas con saltos de línea
        csv_data = '\n'.join(csv_data)

        self.clipboard_clear()
        self.clipboard_append('\n'.join(csv_data))

        # Imprimir un mensaje para confirmar que los valores han sido copiados
        print("Valores copiados")
