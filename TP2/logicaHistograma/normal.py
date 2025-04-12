import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from TP2.utilidades.logicaDistribuciones import logicaDistribuciones

class TablaNormal(tk.Toplevel):
    def __init__(self, parent, numIntervalos, nMuestras, media, desviacion):
        super().__init__(parent)
        self.logicaDistr = logicaDistribuciones()
        self.serie = []
        self.numIntervalos = numIntervalos
        self.nMuestras = nMuestras
        self.media = media
        self.desviacion = desviacion

        self.title("Tabla de resultados (Distribución Normal)")
        self.geometry("500x300")

        # Generación de números normales
        for _ in range(nMuestras):
            valor = random.gauss(self.media, self.desviacion)
            self.serie.append(valor)

        self.intervalos = self.logicaDistr.generarIntervalos(self.serie, numIntervalos)
        self.contadores_intervalos = self.logicaDistr.contadorIntervalos(self.serie, self.intervalos)

        self.crear_tabla()

    def crear_tabla(self):
        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ('Número de Intervalo', 'Límite Inferior', 'Límite Superior', 'Frecuencia Observada')

        self.tabla.column("#0", width=0, stretch=tk.NO)
        self.tabla.column("Número de Intervalo", anchor=tk.W, width=100)
        self.tabla.column("Límite Inferior", anchor=tk.W, width=100)
        self.tabla.column("Límite Superior", anchor=tk.W, width=100)
        self.tabla.column("Frecuencia Observada", anchor=tk.W, width=100)

        self.tabla.heading("#0", text="", anchor=tk.W)
        self.tabla.heading("Número de Intervalo", text="Número de Intervalo", anchor=tk.W)
        self.tabla.heading("Límite Inferior", text="Límite Inferior", anchor=tk.W)
        self.tabla.heading("Límite Superior", text="Límite Superior", anchor=tk.W)
        self.tabla.heading("Frecuencia Observada", text="Frecuencia Observada", anchor=tk.W)

        for i, intervalo in enumerate(self.intervalos):
            self.tabla.insert('', 'end', values=(
                i + 1, f"{intervalo[0]:.4f}", f"{intervalo[1]:.4f}", self.contadores_intervalos[i]))

        self.boton_copiar = tk.Button(self, text="Copiar todos los valores", command=self.copiar_valores)
        self.boton_copiar.pack()

        self.boton_histograma = tk.Button(self, text="Ver Histograma", command=self.generar_histograma)
        self.boton_histograma.pack()

        self.tabla.pack()
        self.frame_histograma = tk.Frame(self)
        self.frame_histograma.pack(fill=tk.BOTH, expand=True)
        self.canvas = None

    def generar_histograma(self):
        ventana_histograma = tk.Toplevel(self)
        ventana_histograma.title("Histograma de Frecuencias")

        bins = [intervalo[0] for intervalo in self.intervalos]
        bins.append(self.intervalos[-1][1])

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.hist(self.serie, bins=bins, edgecolor='black', align='mid')

        ax.set_xticks(bins)
        ax.set_xticklabels([f"{b:.4f}" for b in bins], rotation=45)

        ax.set_title('Histograma de Frecuencias')
        ax.set_xlabel('Intervalos')
        ax.set_ylabel('Frecuencia')

        canvas = FigureCanvasTkAgg(fig, master=ventana_histograma)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def copiar_valores(self):
        items = self.tabla.get_children()
        valores = [self.tabla.item(item, 'values') for item in items]
        csv_data = ['\t'.join(self.tabla['columns'])] + ['\t'.join(map(str, fila)) for fila in valores]
        self.clipboard_clear()
        self.clipboard_append('\n'.join(csv_data))
        print("Valores copiados")
