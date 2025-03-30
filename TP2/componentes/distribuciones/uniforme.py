# uniforme.py
import tkinter as tk
from tkinter import messagebox

from TP2.logicaHistograma.uniforme import Tabla


class Uniforme(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Distribucion uniforme para n muestras")
        self.geometry("300x250")  # ajusta el tamaño de la ventana

        # aquí puedes agregar campos y lógica para operar
        self.campos = []
        self.nLabel = tk.Label(self, text="Ingresa una cantidad n de muestras a simular: \n(1000000 max.)")
        self.nLabel.pack()
        self.nval = tk.Entry(self)
        self.nval.pack()
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

        print(f"✅ Número válido: {n}, opción de intervalos: {opcionIntervalo}")

        # Si `n` es válido, almacenarlo y ejecutar la simulación
        self.campos.append(n)
        self.campos.append(opcionIntervalo)

        tabla = Tabla(self)
        tabla.mainloop()