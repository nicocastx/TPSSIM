import tkinter as tk
from TP2.logicaHistograma.exponencial import TablaExponencial

class Ventana_Exponencial:
    def __init__(self, parent):
        self.parent = parent
        self.root = tk.Toplevel(parent)

        # Entradas
        self.tamanio_muestra_entry = None
        self.mu_entry = None
        self.lambda_entry = None
        self.intervalos_entry = None

        # Opción seleccionada: mu o lambda
        self.parametro_var = tk.StringVar(value="mu")

        self.root.title("Distribución Exponencial")
        self.mostrar_valores()

    def alternar_campos(self):
        if self.parametro_var.get() == "mu":
            self.mu_entry.config(state="normal")
            self.lambda_entry.config(state="disabled")
        else:
            self.mu_entry.config(state="disabled")
            self.lambda_entry.config(state="normal")

    def get_parametros(self):
        try:
            nMuestras = int(self.tamanio_muestra_entry.get())
            numIntervalos = int(self.intervalos_entry.get())

            if nMuestras <= 0 or nMuestras > 1000000:
                raise ValueError("La cantidad de muestras debe estar entre 1 y 1.000.000")

            if self.parametro_var.get() == "mu":
                mu = float(self.mu_entry.get())
                if mu <= 0:
                    raise ValueError("μ debe ser mayor a 0")
            else:
                lamb = float(self.lambda_entry.get())
                if lamb <= 0:
                    raise ValueError("λ debe ser mayor a 0")
                mu = 1 / lamb  # Lo transformamos a mu

            self.crear_tabla([numIntervalos, nMuestras, mu])

        except ValueError as e:
            print("Error:", e)

    def crear_tabla(self, campos):
        numIntervalos = campos[0]
        nMuestras = campos[1]
        mu = campos[2]
        TablaExponencial(self.root, numIntervalos, nMuestras, mu)

    def mostrar_valores(self):
        # Entrada de muestra
        tk.Label(self.root, text="Cantidad de muestras:").grid(row=0, column=0, sticky="w")
        self.tamanio_muestra_entry = tk.Entry(self.root)
        self.tamanio_muestra_entry.grid(row=0, column=1)

        # Selección entre mu o lambda
        tk.Label(self.root, text="Selecciona el parámetro:").grid(row=1, column=0, sticky="w")
        tk.Radiobutton(self.root, text="Usar μ (media)", variable=self.parametro_var, value="mu", command=self.alternar_campos).grid(row=1, column=1, sticky="w")
        tk.Radiobutton(self.root, text="Usar λ (tasa)", variable=self.parametro_var, value="lambda", command=self.alternar_campos).grid(row=2, column=1, sticky="w")

        # Entrada para mu
        tk.Label(self.root, text="Valor de μ:").grid(row=3, column=0, sticky="w")
        self.mu_entry = tk.Entry(self.root)
        self.mu_entry.grid(row=3, column=1)

        # Entrada para lambda (inicialmente deshabilitada)
        tk.Label(self.root, text="Valor de λ:").grid(row=4, column=0, sticky="w")
        self.lambda_entry = tk.Entry(self.root, state="disabled")
        self.lambda_entry.grid(row=4, column=1)

        # Selección de intervalos
        tk.Label(self.root, text="Número de intervalos:").grid(row=5, column=0, sticky="w")
        self.intervalos_entry = tk.StringVar(self.root)
        self.intervalos_entry.set("10")
        opciones = ["10", "15", "20", "30"]
        for i, opcion in enumerate(opciones):
            tk.Radiobutton(self.root, text=opcion, variable=self.intervalos_entry, value=opcion).grid(row=6 + i, column=0, sticky="w")

        # Botón para generar tabla
        boton = tk.Button(self.root, text="Generar tabla", command=self.get_parametros)
        boton.grid(row=11, column=0, columnspan=2)
