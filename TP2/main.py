import tkinter as tk

# todo : copiar los valores no copia los valores decimales la funcion
# todo : encontrar la manera de que se puedan reingresar datos en las tablas de formulario (u ocultarlos)
# todo : validar campos de normal y exponencial
# todo : revisar si el uso de la funcion de distribucion para normal es correcto


#exponencial logica -- Caillou -- hecho
#normal logica -- Jere -- hecho
#exponencial intarfaces -- Joaco -- hecho
#completar la tabla -- Simon (revisar si la logica esta bien) Hecho (Ahora genera dsitribucion entre A y B)
#revisar completar grafico uniforme -- Nico (verificar distribucion) Hecho
#normal interfaz -- Leisa -- hecho

#Validaciones del campo uniforme tamano muestras -- Ale -- hecho
#revisar logica truncate ultimo intervalo -- ale archivo uniforme linea 40 !IMPORTANT -- hecho

#reutilizar tabla y grafico de la uniforme para la exponencial y normal -- el ultimo en pushear -- Kevin
#distribuir valores entre los intervalos -- Kevin -- hecho
#Abstraer utilidades -- Kevin -- hecho

from componentes.menu import Menu
from estilo import estilo


root = tk.Tk()
root.title("Interfaz básica")
root.minsize(400, 300)  # Establece el tamaño mínimo de la ventana

menu = Menu(root)

menu.aplicar_estilo(estilo)

# Iniciamos la aplicación
root.mainloop()