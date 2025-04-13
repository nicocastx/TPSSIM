import tkinter as tk

# todo : copiar los valores no copia los valores decimales la funcion
# todo : encontrar la manera de que se puedan reingresar datos en las tablas de formulario (u ocultarlos)
#-------------------------------------------------------------------------------
#NOVEDADES: by Ale

#===================
#todo Cambios en la Normal:

# Hecho : revisar si el uso de la funcion de distribucion para normal es correcto/ (SI PERO NO por random.gauss)
# Cambie la distribucion Normal y la hice por el metodo de Box-Muller-- Hecho
# Hecho : validar campos de normal
# ACLARACION: La generacion del RND esta dentro de utilidades en logicaDistribuciones
#===================
# todo Cambios en la Exponencial:
#Ale: hice una validacion de los campos de la exponencial, pero no se si es la correcta --todo Verificar
# Le pedi al decimo integrante ;) que haga una Interfaz para la exponencial en donde me permita seleccionar si voy
#a usar lambda o mu, y que me haga la conversion de lambda a mu. (no manejo tkinter)

#--------------------------------------------------------------------------------

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