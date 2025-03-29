import tkinter as tk
from tkinter import ttk

from componentes.menu import Menu
from estilo import estilo


root = tk.Tk()
root.title("Interfaz básica")
root.minsize(400, 300)  # Establece el tamaño mínimo de la ventana


menu = Menu(root)

menu.aplicar_estilo(estilo)

# Iniciamos la aplicación
root.mainloop()