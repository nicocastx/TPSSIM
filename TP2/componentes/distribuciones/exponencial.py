# exponencial.py

import tkinter as tk
from TP2.logicaHistograma.exponencial import TablaExponencial

class Ventana_Exponencial:
    def __init__(self, parent):
        self.parent = parent
        self.root = tk.Toplevel(parent)
        self.tamanio_muestra_entry = None
        self.mu_entry = None
        self.intervalos_entry = None

        self.root.title("Distribución Exponencial")
        self.mostrar_valores()

    def get_parametros(self):
        # Obtener valores de los campos
        try:
            campos = [
                int(self.tamanio_muestra_entry.get()),  # nMuestras
                int(self.intervalos_entry.get()),  # numIntervalos
                float(self.mu_entry.get())  # mu
            ]

            # Validar parámetros
            if campos[2] <= 0:
                raise ValueError("μ debe ser positivo")

            # Crear ventana de resultados
            self.crear_tabla(campos)

        except ValueError as e:
            print("Error:", e)

    def crear_tabla(self, campos):
        numIntervalos = campos[1]
        nMuestras = campos[0]
        mu = campos[2]
        TablaExponencial(self.root, numIntervalos, nMuestras, mu)


    def abrir_ventana(self):
        self.root = tk.Toplevel(self.parent)  # Usar Toplevel en lugar de Tk
        self.root.title("Distribución Exponencial para n muestras")
        self.mostrar_valores()

    def mostrar_valores(self):

        muestra_label = tk.Label(self.root, text="Ingresa la cantidad de muestras a simular: ")
        muestra_label.grid(row=0, column=0, sticky="w")
        self.tamanio_muestra_entry = tk.Entry(self.root, text="Ingresa el tamaño de la muestra")
        self.tamanio_muestra_entry.grid(row=0, column=1)

        mu_label = tk.Label(self.root, text="Ingresa el valor de mu (media): ")
        mu_label.grid(row=1, column=0, sticky="w")
        self.mu_entry = tk.Entry(self.root)
        self.mu_entry.grid(row=1, column=1)

        intervalos_label = tk.Label(self.root, text="Ingresa el numero de intervalos: ")
        intervalos_label.grid(row=3, column=0, sticky="w")
        self.intervalos_entry = tk.StringVar(self.root)
        self.intervalos_entry.set("10")
        opciones = ["10", "15", "20", "30"]

        for opcionIntervalo in opciones:
            tk.Radiobutton(self.root, text= opcionIntervalo, variable=self.intervalos_entry, value=opcionIntervalo).grid()

        # Botón para generar tabla
        boton = tk.Button(
            self.root,
            text="Generar tabla",
            command=self.get_parametros  # Conectado a get_parametros
        )
        boton.grid(row=10, column=0, columnspan=2)