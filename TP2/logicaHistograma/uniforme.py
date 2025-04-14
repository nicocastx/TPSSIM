import math
import random
import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from TP2.utilidades.logicaDistribuciones import logicaDistribuciones


class GenerarUniforme(tk.Toplevel):
    def __init__(self, root):
        self.logicaDistr = logicaDistribuciones()
       # self.serie = []
        self.intervalos = []

        super().__init__(root)
        numIntervalos = int(root.campos[3])
        nMuestras = int(root.campos[0])
        a = float(root.campos[1]) # Valor A
        b = float(root.campos[2]) # Valor B
        self.contadores_intervalos = 0

        self.title("Tabla de resultados")
        self.geometry("600x500")

        # Calcular la serie usando A y B

        self.serie = self.generar_listauniforme(a, b, nMuestras)

        self.intervalos = self.logicaDistr.generarIntervalos(self.serie, numIntervalos)

        print(self.intervalos)

        self.contadores_intervalos = self.logicaDistr.contadorIntervalos(self.serie, self.intervalos)

        print("contadores_intervalos: " + str(self.contadores_intervalos))

        self.crear_tabla()

    #Funcion para copiar los valores revisar ciclo for "item in items" si usar coma o punto, por defecto es punto
    def copiar_valores(self):
        self.logicaDistr.copiar_valores(self)

    @staticmethod
    def generar_listauniforme(a: float, b: float, n: int) -> list:
        """Genera una lista de n números aleatorios con distribución uniforme entre a y b."""
        if a > b:
            a, b = b, a  # Intercambia valores si están en orden incorrecto
        return [round(a + random.random() * (b - a), 4) for _ in range(n)]

    def crear_tabla(self):
        # Crear la tabla
        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ('Número de Intervalo', 'Límite Inferior', 'Límite Superior', 'Frecuencia Observada')

        # Formato de la tabla
        self.tabla.column("#0", width=0, stretch=tk.NO)
        self.tabla.column("Número de Intervalo", anchor=tk.W, width=100)
        self.tabla.column("Límite Inferior", anchor=tk.W, width=100)
        self.tabla.column("Límite Superior", anchor=tk.W, width=100)
        self.tabla.column("Frecuencia Observada", anchor=tk.W, width=100)

        # Encabezados de la tabla
        self.tabla.heading("#0", text="", anchor=tk.W)
        self.tabla.heading("Número de Intervalo", text="Número de Intervalo", anchor=tk.W)
        self.tabla.heading("Límite Inferior", text="Límite Inferior", anchor=tk.W)
        self.tabla.heading("Límite Superior", text="Límite Superior", anchor=tk.W)
        self.tabla.heading("Frecuencia Observada", text="Frecuencia Observada", anchor=tk.W)

        # Agregar datos a la tabla
        for i, intervalo in enumerate(self.intervalos):
            self.tabla.insert('', 'end', values=(
            i + 1, f"{intervalo[0]:.4f}", f"{intervalo[1]:.4f}", self.contadores_intervalos[i]))

        # Botón para copiar todos los valores
        self.boton_copiar = tk.Button(self, text="Copiar todos los valores", command=self.copiar_valores)
        self.boton_copiar.pack()

        # Botón para mostrar histograma
        self.boton_histograma = tk.Button(self, text="Ver Histograma", command=self.generar_histograma)
        self.boton_histograma.pack()

        # Agregar tabla a la ventana
        self.tabla.pack()

        # Frame para el histograma
        self.frame_histograma = tk.Frame(self)
        self.frame_histograma.pack(fill=tk.BOTH, expand=True)

        self.canvas = None  # Variable para almacenar el canvas del histograma

    def generar_histograma(self):
        """Genera y muestra el histograma en una nueva ventana de tkinter con los intervalos correctos."""
        # Crear una nueva ventana para el histograma
        ventana_histograma = tk.Toplevel(self)
        ventana_histograma.title("Histograma de Frecuencias")

        # Extraer los límites de los intervalos
        bins = [intervalo[0] for intervalo in self.intervalos]  # Primeros valores de cada intervalo
        bins.append(self.intervalos[-1][1])  # Agregar el último límite superior

        # Crear figura y eje para el histograma
        fig, ax = plt.subplots(figsize=(8, 6))  # Tamaño ajustado para caber en la ventana
        ax.hist(self.serie, bins=bins, edgecolor='black', align='mid')

        # Ajustar las etiquetas del eje X con los valores exactos de los intervalos
        ax.set_xticks(bins)
        ax.set_xticklabels([f"{b:.4f}" for b in bins], rotation=45)  # Redondeo a 4 decimales

        ax.set_title('Histograma de Frecuencias')
        ax.set_xlabel('Intervalos')
        ax.set_ylabel('Frecuencia')

        # Integrar la figura en la nueva ventana
        canvas = FigureCanvasTkAgg(fig, master=ventana_histograma)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
