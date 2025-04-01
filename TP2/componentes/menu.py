import tkinter as tk

from TP2.componentes.distribuciones.normal import Ventana_Normal
from TP2.componentes.distribuciones.uniforme import Uniforme
#from TP2.componentes.distribuciones.exponencial import Ventana_Exponencial


class Menu:
    def __init__(self, root):
        self.root = root
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack(side="top", fill="x")

        self.menu_title = tk.Label(self.menu_frame, text="Menú", font=("Helvetica", 16))
        self.menu_title.pack(side="top", padx=10, pady=10)

        self.menu_title = tk.Label(self.menu_frame, text="Seleccione una distribucion para poder continuar", font=("Helvetica", 12))
        self.menu_title.pack(side="top", padx=10, pady=10)

        self.button_frame = tk.Frame(self.menu_frame)
        self.button_frame.pack(side="top", fill="x")

        self.buttonUniforme = tk.Button(self.button_frame, text="Uniforme", command=self.abrir_ventanaUniforme)
        self.buttonUniforme.pack(side="top", fill="x", padx=10, pady=10)

        self.buttonExponencial = tk.Button(self.button_frame, text="Exponencial", command=self.abrir_ventanaExponencial)
        self.buttonExponencial.pack(side="top", fill="x", padx=10, pady=10)

        self.buttonNormal = tk.Button(self.button_frame, text="Normal", command=self.abrir_ventanaNormal)
        self.buttonNormal.pack(side="top", fill="x", padx=10, pady=10)


    def aplicar_estilo(self, estilo):
        self.menu_frame.config(bg=estilo.color_fondo)
        self.menu_title.config(bg=estilo.color_fondo, fg=estilo.color_texto)
        self.button_frame.config(bg=estilo.color_fondo)
        self.buttonUniforme.config(bg=estilo.color_boton, fg=estilo.color_texto)
        self.buttonExponencial.config(bg=estilo.color_boton, fg=estilo.color_texto)
        self.buttonNormal.config(bg=estilo.color_boton, fg=estilo.color_texto)

    def abrir_ventanaUniforme(self):
        uniforme = Uniforme(self.root)


    def abrir_ventanaExponencial(self):
        #exponencial = Ventana_Exponencial()
        pass

    def abrir_ventanaNormal(self):
        normal = Ventana_Normal()


