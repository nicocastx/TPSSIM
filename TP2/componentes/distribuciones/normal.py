import tkinter as tk
from tkinter import messagebox

# def abrir_ventanaNormal(self): esto para menu.py
#     Ventana_Normal()

from TP2.logicaHistograma.normal import TablaNormal

import tkinter as tk


class Ventana_Normal:
    def __init__(self):
        self.window = None
        self.tamanio_muestra_entry = None
        self.mu_entry = None
        self.sigma_entry = None
        self.intervalos_entry = None
        

    def get_parametros(self):
        try:
            tamanio_muestra = int(self.tamanio_muestra_entry.get())
            media = float(self.mu_entry.get())
            desviacion = float(self.sigma_entry.get())
            intervalos = int(self.intervalos_entry.get())

            if tamanio_muestra <= 0 or tamanio_muestra > 1000000:
                messagebox.showerror("Error", "El número debe estar entre 1 y 1.000.000.")
                return

            if media <= 0:
                messagebox.showerror("Error", "El valor de media debe ser positivo.")
                return
            if desviacion <= 0:
                messagebox.showerror(title="Error", message="El valor de la desviación debe ser positivo")

            # ✅ Abrir la ventana de tabla con los datos
            TablaNormal(self.window, intervalos, tamanio_muestra, media, desviacion)

        except ValueError:
            print("Por favor, ingresa valores válidos.")



    def abrir_ventana(self):
        self.window = tk.Tk()
        self.window.title("Distribución normal para n muestras")
        self.mostrar_valores()
        self.window.mainloop()

    def mostrar_valores(self):

        muestra_label = tk.Label(self.window, text="Ingresa la cantidad de muestras a simular: ")
        muestra_label.pack()
        self.tamanio_muestra_entry = tk.Entry(self.window)
        self.tamanio_muestra_entry.pack()

        mu_label = tk.Label(self.window, text="Ingresa el valor de mu (media): ")
        mu_label.pack()
        self.mu_entry = (tk.Entry(self.window))
        self.mu_entry.pack()

        sigma_label = tk.Label(self.window, text="Ingresa el valor de sigma (desviacion): ")
        sigma_label.pack()
        self.sigma_entry = (tk.Entry(self.window))
        self.sigma_entry.pack()

        intervalos_label = tk.Label(self.window, text="Ingresa el numero de intervalos: ")
        intervalos_label.pack()
        self.intervalos_entry = tk.StringVar(self.window)
        self.intervalos_entry.set("10")
        opciones = ["10", "15", "20", "30"]
        for opcionIntervalo in opciones:
            tk.Radiobutton(self.window, text= opcionIntervalo, variable=self.intervalos_entry, value=opcionIntervalo).pack()

        # Toma los valores y los pasa a la función lógica
        boton = tk.Button(self.window, text="Armar tabla", command=self.get_parametros)
        boton.pack()
