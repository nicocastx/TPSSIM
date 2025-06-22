import tkinter as tk
import openpyxl
from openpyxl import Workbook

from TP5.Objetos.LogicaPrincipal import LogicaPrincipal
from TP5.enums.EnumEventos import EnumEventos

# Elementos parametrizables
# --- Formulario 1: Tiempo de llegada (Uniforme) ---
# Formulario 2: Tiempo de atención (Fijo)

# Objetos posibles:
# VectorEstados - Sera cada una de las filas, donde llevaran la logica para la simulacion
# VectorEstados tendra:
# Reloj, Evento, RND, Tiempo llegada, Hora, ...
# Cliente - Abstraemos del vector a los clientes en una lista, para mejor manejo y facilitar logica y busqueda

#La idea va a ser que la logica se lleva en principal, haya 2 vector estado, y se vaya armando la cadena para
#alimentar la tabla, ya que solo necesita una lista de cadenas
"""
Se deberá simular X tiempo (parámetro solicitado al inicio) generando N cantidad de iteraciones 
en total. El aplicativo debe permitir simular hasta 100000 iteraciones del vector de estado ó 
hasta el tiempo X, lo que ocurra primero.
--- De esto se entiende que como X es tiempo y dice parametro, las iteraciones van a hacerse hasta ese tiempo

Se mostrará en el vector de estado i iteraciones a partir de una hora j (valores i y j ingresados 
por parámetro). 
-- por lo que entiendo, a partir de una hora, ejemplo 20, se deben cargar a partir de ese minuto 20, las iteraciones pedidas
-- es decir, se pasa i 30 iteraciones, desde un minuto 30, a partir de la fila reloj del minuto 30, se cargan 30 filas

TODO poner en el footer la ultima linea de la tabla

El vector de estado debe mostrar como mínimo la siguiente información:  
- número de fila - hora simulada 
- nombre del evento simulado 
- próximos eventos a ejecutarse 

- Objetos considerados en la simulación, cada uno con sus atributos: 
- nombre, por ser estático podrá estar en el encabezado 
- estado  - otros atributos necesarios 
- Variables auxiliares (acumuladores, contadores,...)

"""


from TP5.tabla.TablaPrincipal import TablaPrincipal


class CafetinApp:

    def __init__(self, root):

        self.root = root
        self.root.title("Cafetin Literario - Grupo 14")
        self.root.minsize(1400, 600)  # Aumenté el tamaño mínimo de la ventana

        # Componentes
        self.tabla = None
        self.logica = None

        # Valores predeterminados
        self.min_llegada = 0
        self.max_llegada = 0
        self.tiempo_atencion = 0
        self.tiempo_limite = 0
        self.iteraciones = 0
        self.hora_desde = 0
        self.k_primer_intervalo = 0
        self.k_segundo_intervalo = 0
        self.k_tercer_intervalo = 0
        self.step = 0

        # --- Contenedor principal ---
        main_container = tk.Frame(self.root, padx=20, pady=10)  # Aumenté el padding
        main_container.pack(fill="both", expand=True)

        # --- Fila superior (formularios + botones) ---
        top_row = tk.Frame(main_container, pady=15)  # Aumenté el espacio vertical
        top_row.pack(fill="x", pady=(0, 15))

        # --- Contenedor de formularios (izquierda) ---
        form_container = tk.Frame(top_row)
        form_container.pack(side="left", fill="both", expand=True, padx=10)

        # --- Contenedor de botones (derecha) ---
        btn_frame = tk.Frame(top_row, bg="#f0f0f0", padx=15, pady=15)  # Aumenté el padding
        btn_frame.pack(side="right", fill="y")

        # Configuración de fuente para los botones
        button_font = ('Arial', 10, 'bold')
        button_padx = 15
        button_pady = 8

        self.btn_iniciar = tk.Button(btn_frame, text="Iniciar Simulación", bg="#4CAF50", fg="white",
                                     font=button_font, padx=button_padx, pady=button_pady,
                                     command=self.cargar_datos_ejemplo)
        self.btn_iniciar.pack(fill="x", pady=5)

        self.btn_limpiar = tk.Button(btn_frame, text="Limpiar Datos", bg="#f44336", fg="white",
                                     font=button_font, padx=button_padx, pady=button_pady,
                                     command=self.limpiar_tabla)
        self.btn_limpiar.pack(fill="x", pady=5)

        # --- Formularios ---
        # Frame para organizar los formularios en dos columnas
        form_columns = tk.Frame(form_container)
        form_columns.pack(fill="both", expand=True)

        # Ajustar el espacio entre columnas
        form_columns.columnconfigure(0, weight=1, pad=20)
        form_columns.columnconfigure(1, weight=1, pad=20)

        # Columna izquierda (Tiempo de llegada y atención)
        left_form = tk.LabelFrame(form_columns, text="Parámetros de Simulación", padx=15, pady=15)
        left_form.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Aumentar el tamaño de las etiquetas
        label_style = {'font': ('Arial', 14), 'pady': 4}
        entry_style = {'width': 15, 'font': ('Arial', 12)}

        # Formulario 1: Tiempo de llegada (Uniforme)
        tk.Label(left_form, text="Tiempo de Llegada (min):", **label_style).grid(row=0, column=0, sticky="w")
        tk.Label(left_form, text="Mínimo:").grid(row=1, column=0, sticky="w")
        self.entry_min = tk.Entry(left_form, **entry_style)
        self.entry_min.grid(row=1, column=1, padx=5, pady=3, sticky="w")
        tk.Label(left_form, text="Máximo:").grid(row=2, column=0, sticky="w")
        self.entry_max = tk.Entry(left_form, **entry_style)
        self.entry_max.grid(row=2, column=1, padx=5, pady=3, sticky="w")

        # Formulario 2: Tiempo de atención (Fijo)
        tk.Label(left_form, text="Tiempo de Atención:", **label_style).grid(row=3, column=0, sticky="w",
                                                                                  pady=(10, 0))
        tk.Label(left_form, text="Tiempo de atención de fernando:").grid(row=4, column=0, sticky="w")
        self.entry_fijo = tk.Entry(left_form, **entry_style)
        self.entry_fijo.grid(row=4, column=1, padx=5, pady=3, sticky="w")

        # Formulario 3: K para Tiempo de lectura
        tk.Label(left_form, text="Tiempo de lectura (k):", **label_style).grid(row=6, column=0, sticky="w")
        tk.Label(left_form, text="Entre 10 y 20 páginas [10, 20):").grid(row=7, column=0, sticky="w")
        self.entry_first_interval = tk.Entry(left_form, **entry_style)
        self.entry_first_interval.grid(row=7, column=1, padx=5, pady=3, sticky="w")
        tk.Label(left_form, text="Entre 20 y 30 páginas [20, 30):").grid(row=8, column=0, sticky="w")
        self.entry_second_interval = tk.Entry(left_form, **entry_style)
        self.entry_second_interval.grid(row=8, column=1, padx=5, pady=3, sticky="w")
        tk.Label(left_form, text="Más de 30 páginas [30, 40):").grid(row=9, column=0, sticky="w")
        self.entry_third_interval = tk.Entry(left_form, **entry_style)
        self.entry_third_interval.grid(row=9, column=1, padx=5, pady=3, sticky="w")

        # Formulario 4: H para paso de integración
        tk.Label(left_form, text="Paso de ingegración (h):", **label_style).grid(row=10, column=0, sticky="w")
        tk.Label(left_form, text="Paso de integración:").grid(row=11, column=0, sticky="w")
        self.step = tk.Entry(left_form, **entry_style)
        self.step.grid(row=11, column=1, padx=5, pady=3, sticky="w")

        # Columna derecha (Configuración de visualización)
        right_form = tk.LabelFrame(form_columns, text="Configuración de Visualización", padx=15, pady=15)
        right_form.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        # Formulario 3: Tiempo límite de simulación
        tk.Label(right_form, text="Tiempo Límite (min):", **label_style).grid(row=0, column=0, sticky="w")
        self.entry_tiempo_limite = tk.Entry(right_form, **entry_style)
        self.entry_tiempo_limite.grid(row=0, column=1, padx=5, pady=3, sticky="w")

        # Formulario 4: Iteraciones a mostrar
        tk.Label(right_form, text="Iteraciones a Mostrar:", **label_style).grid(row=1, column=0, sticky="w",
                                                                                pady=(10, 0))
        tk.Label(right_form, text="Cantidad:").grid(row=2, column=0, sticky="w")
        self.entry_iteraciones = tk.Entry(right_form, **entry_style)
        self.entry_iteraciones.grid(row=2, column=1, padx=5, pady=3, sticky="w")
        tk.Label(right_form, text="Hora desde (min):").grid(row=3, column=0, sticky="w")
        self.entry_hora_desde = tk.Entry(right_form, **entry_style)
        self.entry_hora_desde.grid(row=3, column=1, padx=5, pady=3, sticky="w")

        # Configurar el peso de las filas y columnas para mejor distribución
        for frame in [left_form, right_form]:
            for i in range(10):  # Asegurar que hay suficientes filas
                frame.rowconfigure(i, weight=1)
            for i in range(2):  # Dos columnas
                frame.columnconfigure(i, weight=1)

        # --- Tabla ---
        self.tabla = TablaPrincipal(main_container)
        self.tabla.pack(fill="both", expand=True, padx=10, pady=5)

        # --- Footer (Botones de control) ---
        footer = tk.Frame(self.root, pady=10)
        footer.pack(fill="x")

    def validar_formulario(self):
        # Obtener valores de los formularios
        try:
            self.min_llegada = float(self.entry_min.get() or 0)
            self.max_llegada = float(self.entry_max.get() or 0)
            self.tiempo_atencion = float(self.entry_fijo.get() or 0)
            self.tiempo_limite = float(self.entry_tiempo_limite.get() or 0)
            self.iteraciones = int(self.entry_iteraciones.get() or 0)
            self.hora_desde = float(self.entry_hora_desde.get() or 0)
            self.k_primer_intervalo = float(self.entry_first_interval.get() or 0)
            self.k_segundo_intervalo = float(self.entry_second_interval.get() or 0)
            self.k_tercer_intervalo = float(self.entry_third_interval.get() or 0)
            self.step = float(self.step.get() or 0)



        except ValueError:
            print("Error: Por favor ingrese valores numéricos válidos")
            return

    def cargar_datos_ejemplo(self):
        self.validar_formulario()
        # Mostrar los valores en consola
        print("\n--- Valores del formulario ---")
        print(f"Tiempo de llegada: {self.min_llegada} - {self.max_llegada} minutos")
        print(f"Tiempo de atención: {self.tiempo_atencion} minutos")
        print(f"Tiempo límite de simulación: {self.tiempo_limite} minutos")
        print(f"Mostrar {self.iteraciones} iteraciones desde la hora: {self.hora_desde}")
        print("------------------------------\n")

        self.logica = LogicaPrincipal(
            self.min_llegada,
            self.max_llegada,
            self.tiempo_atencion,
            self.tiempo_limite,
            self.iteraciones,
            self.hora_desde,
            self.k_primer_intervalo,
            self.k_segundo_intervalo,
            self.k_tercer_intervalo,
            self.step
        )
        self.logica.simular()
        print(self.logica.cadenaTabla)
        self.tabla.set_datos(self.logica.cadenaTabla)

    #Limpio la tabla de datos
    def limpiar_tabla(self):
        # Reinicio Componentes
        self.logica = None
        self.tabla.set_datos([])


# --- Ejecutar aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CafetinApp(root)
    root.mainloop()
