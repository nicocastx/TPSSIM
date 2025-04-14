# uniforme.py
import tkinter as tk
from tkinter import messagebox

from TP2.logicaHistograma.uniforme import GenerarUniforme


class Uniforme(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Distribucion uniforme para n muestras")
        self.geometry("600x450")  # ajusta el tamaño de la ventana

        # aquí puedes agregar campos y lógica para operar
        self.campos = []
        self.nLabel = tk.Label(self, text="Ingresa una cantidad n de muestras a simular: \n(1000000 max.)")
        self.nLabel.pack()
        self.nval = tk.Entry(self)
        self.nval.pack()

        # Campos para los valores A y B
        self.aLabel = tk.Label(self, text="Ingrese el valor A:")
        self.aLabel.pack()
        self.aVal = tk.Entry(self)
        self.aVal.pack()

        self.bLabel = tk.Label(self, text="Ingrese el valor B:")
        self.bLabel.pack()
        self.bVal = tk.Entry(self)
        self.bVal.pack()

        # Agregamos un OptionMenu para seleccionar una opción
        self.opcionLabel = tk.Label(self, text="Ingrese una cantidad de intervalos:")
        self.opcionLabel.pack()
        self.opcionIntervalo = tk.StringVar(self)
        self.opcionIntervalo.set("10")  # valor por defecto
        self.opciones = ["10", "15", "20", "30"]
        for opcionIntervalo in self.opciones:
            tk.Radiobutton(self, text=opcionIntervalo, variable=self.opcionIntervalo, value=opcionIntervalo).pack()

        #Logica para mostrar distribucion
        self.boton = tk.Button(self, text="Operar", command=self.operar)
        self.boton.pack()

    def operar(self):
        n_str = self.nval.get().strip()  # Eliminar espacios en blanco
        a_str = self.aVal.get().strip()
        b_str = self.bVal.get().strip()
        opcionIntervalo = self.opcionIntervalo.get()

        # Validar que n sea un número entero
        if not n_str.isdigit():
            messagebox.showerror("Error", "Debe ingresar un número entero positivo.")
            return  # Sale de la función sin continuar

        n = int(n_str)

        # Validar que esté dentro del rango permitido
        if n <= 0 or n > 1000000:
            messagebox.showerror("Error", "El número debe estar entre 1 y 1.000.000.")
            return

        # Validar que A y B sean números válidos
        try:
            a = float(a_str)
            b = float(b_str)
        except ValueError:
            messagebox.showerror("Error", "Los valores de A y B deben ser números válidos.")
            return

        # Validar que A < B
        if a >= b:
            messagebox.showerror("Error", "El valor de A debe ser menor que el valor de B.")
            return

        print(f"✅ Número válido: {n}, A: {a}, B: {b}, opción de intervalos: {opcionIntervalo}")

        # Si `n` es válido, almacenarlo y ejecutar la simulación
        self.campos = []
        self.campos.append(n)
        self.campos.append(a)
        self.campos.append(b)
        self.campos.append(opcionIntervalo)

        tabla = GenerarUniforme(self)
        tabla.mainloop()