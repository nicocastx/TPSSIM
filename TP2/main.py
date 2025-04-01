import tkinter as tk

#todo : exponencial intarfaces -- Joaco
#todo : exponencial logica -- Caillou
#todo : normal logica -- Jere
#todo : completar la tabla -- Simon (revisar si la logica esta bien) Hecho (Ahora genera dsitribucion entre A y B)
#todo : revisar completar grafico uniforme -- Nico (verificar distribucion) Hecho
#todo : reutilizar tabla y grafico de la uniforme para la exponencial y normal -- el ultimo en pushear

#todo : normal interfaz -- Leisa -- hecho
#todo: Validaciones del campo uniforme tamano muestras -- Ale -- hecho
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