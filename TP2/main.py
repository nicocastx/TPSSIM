import tkinter as tk
from tkinter import ttk

#todo : exponencial intarfaces -- Joaco
#todo : normal interfaz -- Leisa
#todo : exponencial logica -- Caillou
#todo : normal logica -- Jere
#todo : completar la tabla -- Simon (revisar si la logica esta bien)
#todo : revisar completar grafico uniforme -- Nico (verificar distribucion)
#todo: Validaciones del campo uniforme tamano muestras -- Ale


#todo : revisar logica truncate ultimo intervalo -- ale archivo uniforme linea 40 !IMPORTANT -- hecho
#todo : distribuir valores entre los intervalos -- Kevin -- hecho
#todo : Abstraer utilidades -- Kevin -- hecho

from componentes.menu import Menu
from estilo import estilo


root = tk.Tk()
root.title("Interfaz básica")
root.minsize(400, 300)  # Establece el tamaño mínimo de la ventana


menu = Menu(root)

menu.aplicar_estilo(estilo)

# Iniciamos la aplicación
root.mainloop()