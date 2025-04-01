import math
import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from TP2.utilidades.logicaDistribuciones import logicaDistribuciones


class Tabla(tk.Toplevel):
    def __init__(self, root):
        self.logicaDistr = logicaDistribuciones()
        self.serie = []
        self.intervalos = []

        super().__init__(root)
        numIntervalos = int(root.campos[1])
        nMuestras = int(root.campos[0])

        self.title("Tabla de resultados")
        self.geometry("600x500")

        # Calcular la serie
        for i in range(nMuestras):
            rnd = random.random()
            self.serie.append(rnd)

        self.intervalos = self.logicaDistr.generarIntervalos(self.serie, numIntervalos)

        print(self.intervalos)

        contadores_intervalos = self.logicaDistr.contadorIntervalos(self.serie, self.intervalos)

        print("contadores_intervalos: " + str(contadores_intervalos))

        # Crear la tabla
        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ('Intervalos', 'Frecuencia')

        # Formato de la tabla
        self.tabla.column("#0", width=0, stretch=tk.NO)
        self.tabla.column("Intervalos", anchor=tk.W, width=150)
        self.tabla.column("Frecuencia", anchor=tk.W, width=100)

        # Encabezados de la tabla
        self.tabla.heading("#0", text="", anchor=tk.W)
        self.tabla.heading("Intervalos", text="Intervalos", anchor=tk.W)
        self.tabla.heading("Frecuencia", text="Frecuencia", anchor=tk.W)

        # Agregar datos a la tabla
        for i, intervalo in enumerate(self.intervalos):
            self.tabla.insert('', 'end', values=(f"{intervalo[0]:.4f} - {intervalo[1]:.4f}", contadores_intervalos[i]))

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
        """Genera y muestra el histograma dentro de la ventana de tkinter con los intervalos correctos."""
        # Limpiar cualquier histograma previo
        for widget in self.frame_histograma.winfo_children():
            widget.destroy()

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

        # Integrar la figura en tkinter
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame_histograma)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def copiar_valores(self):
        """Copia los valores de la tabla al portapapeles en formato tabulado."""
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

