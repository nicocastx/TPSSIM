import math
import random
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt


class Tabla(tk.Toplevel):
    def __init__(self, root):
        self.serie = []
        super().__init__(root)
        print(root.campos[0], root.campos[1])
        self.title("Tabla de resultados")
        self.geometry("500x300")

        #calcular la serie    #CODIGO ORIGINAL
        for i in range(int(root.campos[0])):
            rnd = random.random().__round__(4)
            self.serie.append(rnd)

        #calcular la serie   #ALTERNATIVA 1
        #for i in range(int(root.campos[0])):
        #    rnd = random.random()
        #    rnd = '{:.4}'.format(rnd)
        #    rnd = float(rnd)
        #    self.serie.append(rnd)

        # calcular la serie    #ALTERNATIVA 2 Creo q es mejor q la original
        #for i in range(int(root.campos[0])):
        #    rnd = random.random()
        #    rnd = self.truncar(rnd)
        #    self.serie.append(rnd)


        #aplicarformula()
        a = self.truncar(min(self.serie))
        b = self.truncar(max(self.serie))
        print("minimo: " + str(a))
        print("maximo: "+str(b))

        numIntervalos = int(root.campos[1])  # número de intervalos

        # calcular el tamaño de cada intervalo
        anchoIntervalo = self.truncar((b - a) / numIntervalos)
        print("ancho de intervalo: " + str(anchoIntervalo))

        intervalos = []

        for i in range(numIntervalos):
            inicio = self.truncar(a)
            fin = self.truncar(a + anchoIntervalo)

            if i == numIntervalos - 1:
                intervalos.append((inicio, b))  #TODO Anteriormente estaba a en lugar de inicio eso hacia q el ultimo intervalo no fuera correcto
                continue

            intervalos.append((inicio, fin))
            a = fin
        print("cantidad de intervalos: " + str(len(intervalos)))

        print(intervalos)

        # Crear tabla
        self.tabla = ttk.Treeview(self)
        self.tabla['columns'] = ('Intervalos', 'columna 2', 'Columna 3')

        # Formato de la tabla
        self.tabla.column("#0", width=0, stretch=tk.NO)
        self.tabla.column("Intervalos", anchor=tk.W, width=100)
        self.tabla.column("columna 2", anchor=tk.W, width=100)
        self.tabla.column("Columna 3", anchor=tk.W, width=100)

        # Encabezados de la tabla
        self.tabla.heading("#0", text="", anchor=tk.W)
        self.tabla.heading("Intervalos", text="Intervalos", anchor=tk.W)
        self.tabla.heading("columna 2", text="columna 2", anchor=tk.W)
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

        self.mostrar_histograma(self.serie, int(self.campos[1]))

        # Imprimir un mensaje para confirmar que los valores han sido copiados
        print("Valores copiados")

    def truncar(self, numero):
        factor = 10 ** 4
        numero_escalado = numero * factor
        numero_truncado_escalado = math.trunc(numero_escalado)
        return numero_truncado_escalado / factor

