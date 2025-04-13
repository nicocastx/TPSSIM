import tkinter as tk


# def abrir_ventanaNormal(self): esto para menu.py
#     Ventana_Normal()

from TP2.logicaHistograma.normal import TablaNormal

import tkinter as tk
from tkinter import messagebox

class Ventana_Normal:
    def __init__(self):
        self.root = None

        self.mu_entry = None
        self.sigma_entry = None
        self.tamanio_muestra_entry = None
        self.intervalos_var = None

        self.abrir_ventana()

    def get_parametros(self):
        try:
            # Obtener los valores desde los campos correctos
            mu = float(self.mu_entry.get())
            sigma = float(self.sigma_entry.get())
            n = int(self.tamanio_muestra_entry.get())
            intervalos = int(self.intervalos_entry.get())

            if sigma <= 0:
                messagebox.showerror("Error", "La desviación estándar (σ) debe ser mayor a 0.")
                return

            if n < 1 or n > 1000000:
                messagebox.showerror("Error", "La cantidad de muestras debe estar entre 1 y 1.000.000.")
                return

        except ValueError:
            messagebox.showerror("Error", "Todos los campos deben contener valores numéricos válidos.")
            return

        # Si está todo bien, pasamos a la lógica
        TablaNormal(self.root, intervalos, n, mu, sigma)
        print("n:",n,"mu:",mu,"sigma:",sigma,"intervalos:", intervalos)

    def abrir_ventana(self):
        self.root = tk.Tk()
        self.root.title("Distribución normal para n muestras")
        self.mostrar_valores()
        self.root.mainloop()

    def mostrar_valores(self):

        muestra_label = tk.Label(self.root, text="Ingresa la cantidad de muestras a simular: ")
        muestra_label.grid(row=0, column=0, sticky="w")
        self.tamanio_muestra_entry = tk.Entry(self.root, text="Ingresa el tamaño de la muestra")
        self.tamanio_muestra_entry.grid(row=0, column=1)

        mu_label = tk.Label(self.root, text="Ingresa el valor de mu (media): ")
        mu_label.grid(row=1, column=0, sticky="w")
        self.mu_entry = tk.Entry(self.root)
        self.mu_entry.grid(row=1, column=1)

        sigma_label = tk.Label(self.root, text="Ingresa el valor de sigma (desviacion): ")
        sigma_label.grid(row=2, column=0, sticky="w")
        self.sigma_entry = tk.Entry(self.root)
        self.sigma_entry.grid(row=2, column=1)

        intervalos_label = tk.Label(self.root, text="Ingresa el numero de intervalos: ")
        intervalos_label.grid(row=3, column=0, sticky="w")
        self.intervalos_entry = tk.StringVar(self.root)
        self.intervalos_entry.set("10")
        opciones = ["10", "15", "20", "30"]
        for opcionIntervalo in opciones:
            tk.Radiobutton(self.root, text= opcionIntervalo, variable=self.intervalos_entry, value=opcionIntervalo).grid()

        # Toma los valores y los pasa a la función lógica
        boton = tk.Button(self.root, text="Armar tabla", command=self.get_parametros)
        boton.grid(row=10, column=0)
