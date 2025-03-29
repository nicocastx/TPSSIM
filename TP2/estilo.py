import tkinter as tk
from tkinter import ttk


class Estilo:
    def __init__(self):
        # Color de fondo de la ventana principal y de los elementos
        self.color_fondo = "#f0f0f0"
        # Color del texto de los elementos
        self.color_texto = "#333333"
        # Color del botón de búsqueda normal
        self.color_boton = "#37C4B6"
        # Color del botón de búsqueda al pasar el mouse por encima
        self.color_boton_hover = "#3e8e41"
        # Fuente de los elementos
        self.fuente = "Helvetica"

    def aplicar_estilo(self, root, frame, entry, button, tree):
        # Configuramos el estilo de la ventana principal
        root.configure(bg=self.color_fondo)

        # Configuramos el estilo del frame
        frame.configure(bg=self.color_fondo)

        # Configuramos el estilo de la barra de campo de texto
        entry.configure(bg=self.color_fondo, fg=self.color_texto, font=self.fuente)

        # Configuramos el estilo del botón de búsqueda
        button.configure(bg=self.color_boton, fg=self.color_texto, font=self.fuente)
        button.configure(activebackground=self.color_boton_hover)

        # Configuramos el estilo de la tabla básica
        style = ttk.Style()
        style.configure("Treeview", background=self.color_fondo, foreground=self.color_texto,
                        fieldbackground=self.color_fondo)
        tree.heading("Columna 1", text="Columna 1")
        tree.heading("Columna 2", text="Columna 2")
        tree.column("Columna 1", anchor="w")
        tree.column("Columna 2", anchor="w")

estilo = Estilo()