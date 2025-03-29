# uniforme.py
import tkinter as tk

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
        self.campos.append(self.nval.get())
        self.campos.append(self.opcionIntervalo.get())
        # aquí puedes agregar la lógica para operar con los campos
        n = self.nval.get()
        opcionIntervalo = self.opcionIntervalo.get()
        print(f"n: {n}, opción: {opcionIntervalo}")
        tabla = Tabla(self)
        tabla.mainloop()