import tkinter as tk


# def abrir_ventanaNormal(self): esto para menu.py
#     Ventana_Normal()

from TP2.logicaHistograma.normal import TablaNormal

import tkinter as tk


class Ventana_Normal:
    def __init__(self):
        self.root = None
        self.tamanio_muestra = None
        # media - mu
        self.media_var = None
        # desviacion - sigma
        self.desviacion_var = None
        self.intervalos_var = None

        self.mu_entry = None
        self.sigma_entry = None
        self.intervalos_entry = None
        self.tamanio_muestra_entry = None
        self.abrir_ventana()

    def get_parametros(self):
        try:
            tamanio_muestra = int(self.tamanio_muestra_entry.get())
            media = float(self.mu_entry.get())
            desviacion = float(self.sigma_entry.get())
            intervalos = int(self.intervalos_entry.get())

            # ✅ Abrir la ventana de tabla con los datos
            TablaNormal(self.root, intervalos, tamanio_muestra, media, desviacion)

        except ValueError:
            print("Por favor, ingresa valores válidos.")
        #todo: pasar estos 4 valores para tabla e histograma | tabla(tamaño, mu, sigma, intervalos)
        print(self.tamanio_muestra, self.media_var, self.desviacion_var, self.intervalos_var)

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
