import tkinter as tk
import random
import time
import threading

tiempo = False
pais = random.randint(1, 2)
year = random.randint(1984, 1985)
month = random.randint(1,12)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Máquina Enigma")
        self.geometry("1700x1300")

        # Contenedor donde estarán los frames
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # Diccionario de frames
        self.frames = {}

        # Inicializar pantallas
        for F in (Mainview, Exitoview):
            nombre = F.__name__
            frame = F(container, self)
            self.frames[nombre] = frame
            frame.place(relwidth=1, relheight=1)

        # Mostrar pantalla inicial
        self.mostrar_frame("Mainview")

    def mostrar_frame(self, nombre):
        frame = self.frames[nombre]
        frame.tkraise()

class Mainview(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, bg="gray")
        label = tk.Label(self, text="Máquina Enigma", font=("Arial", 16))
        label.pack(pady=10)
        self.parent = parent
        self.controller = controller

        label = tk.Label(self, text="Nuestros lideres de estado no se encuentran", font=("Arial", 10))
        label.place(x=150, y=50)

        label = tk.Label(self, text="Resuelva los codigos y evite la guerra", font=("Arial", 10))
        label.place(x=150, y=80)

        self.tiemporestante = tk.Label(self, text="Tiempo restante: 60", font=("Arial", 10))
        self.tiemporestante.place(x=500, y=50)

        self.opc = tk.Label(self, text="Pais identificado", font=("Arial", 10))
        self.opc.place(x=150, y=380)

        opcion = tk.IntVar(value=0)
        opc1=tk.Radiobutton(self, text="Eurasia", variable=opcion, value=1)
        opc1.place(x=150, y=410)
        opc2=tk.Radiobutton(self, text="Eastasia", variable=opcion, value=2)
        opc2.place(x=150, y=440)
        opc3=tk.Radiobutton(self, text="Anarquia", variable=opcion, value=3)
        opc3.place(x=150, y=470)
        opc3=tk.Radiobutton(self, text="Akhista", variable=opcion, value=4)
        opc3.place(x=150, y=500)

        agregar = tk.Button(self, text="CONFIRMAR DEFINITIVAMENTE", bg="lightgray", command=lambda: verificarpais(self, opcion.get()))
        agregar.place(x=120, y=530)

        if pais == 1:
            pista1 = tk.Label(self, text="Nuestro objetivo se encuentra al oeste (West) del sector 1, observe el mapa encriptado", font=("Arial", 10))
            pista1.place(x=120, y=110)

            self.imagen1 = tk.PhotoImage(file = "Ejemplo-de-acertijo-con-Threads/map.png")
            self.imagen1 = self.imagen1.subsample(2, 2)
            self.map = tk.Label(self, image=self.imagen1)
            self.map.place(x=150, y=140)

        elif pais == 2:
            pista1 = tk.Label(self, text="Nuestro enemigo se encuentra al otro lado de la frontera del sector 3, observe el mapa encriptado", font=("Arial", 10))
            pista1.place(x=120, y=110)

            self.imagen2 = tk.PhotoImage(file="Ejemplo-de-acertijo-con-Threads/map2.png")
            self.imagen2_sub = self.imagen2.subsample(2, 2)
            self.map2 = tk.Label(self, image=self.imagen2_sub)
            self.map2.place(x=150, y=140)

        def guerraeurasia():
            perder = tk.Label(self, text="País equivocado. La guerra con Eurasia no pudo ser evitada, La guerra empezó desprevenidamente", font=("Arial", 10), bg="red")
            perder.place(x=150, y=560)

            self.imagen2 = tk.PhotoImage(file="Ejemplo-de-acertijo-con-Threads/image2.png")
            self.imagen2_sub = self.imagen2.subsample(2, 2)
            self.map2 = tk.Label(self, image=self.imagen2_sub)
            self.map2.place(x=150, y=590)

        def guerraanarquia():
            perder = tk.Label(self, text="País equivocado. La guerra con Anarquia no pudo ser evitada, Nuestras defensas recurrieron a las armas nucleares", font=("Arial", 10), bg="red")
            perder.place(x=150, y=560)

            self.imagen2 = tk.PhotoImage(file="Ejemplo-de-acertijo-con-Threads/image.png")
            self.imagen2_sub = self.imagen2.subsample(2, 2)
            self.map2 = tk.Label(self, image=self.imagen2_sub)
            self.map2.place(x=150, y=590)

        def guerraeurasia2():
            perder = tk.Label(self, text="País equivocado. La guerra con Eurasia no pudo ser evitada, La guerra empezó desprevenidamente", font=("Arial", 10), bg="red")
            perder.place(x=700, y=350)

            self.imagen2 = tk.PhotoImage(file="Ejemplo-de-acertijo-con-Threads/image2.png")
            self.imagen2_sub = self.imagen2.subsample(2, 2)
            self.map2 = tk.Label(self, image=self.imagen2_sub)
            self.map2.place(x=700, y=380)

        def guerraanarquia2():
            perder = tk.Label(self, text="País equivocado. La guerra con Anarquia no pudo ser evitada, Nuestras defensas recurrieron a las armas nucleares", font=("Arial", 10), bg="red")
            perder.place(x=700, y=560)

            self.imagen2 = tk.PhotoImage(file="Ejemplo-de-acertijo-con-Threads/image.png")
            self.imagen2_sub = self.imagen2.subsample(2, 2)
            self.map2 = tk.Label(self, image=self.imagen2_sub)
            self.map2.place(x=700, y=380)

        def verificarpais(self, opcion):
            if pais == 1 and opcion == 1 or pais == 2 and opcion == 3:
                verificarcodigo(pais)
            elif pais == 2 and opcion == 1 or pais == 2 and opcion == 2 or pais == 2 and opcion == 4:
                guerraanarquia()

            elif pais == 1 and opcion == 2 or pais == 1 and opcion == 3 or pais == 1 and opcion == 4:
                guerraeurasia()

        def verificarcodigo(pais):
            code = tk.Label(self, text=f"Mes {month} del {year}", font=("Arial", 10))
            code.place(x=700, y=50)

            code = tk.Label(self, text="La instrucción que dejaron los lideres es clara pero codificada por seguridad", font=("Arial", 10))
            code.place(x=700, y=80)

            code = tk.Label(self, text="Si el país obtenido es Eurasia, use la diplomacia, si es cualquier otro, haga caso omiso a este mensaje", font=("Arial", 10))
            code.place(x=700, y=110)

            code = tk.Label(self, text="Si el país obtenido NO es Eurasia, y la fecha es un mes par de 1984, ordene intervención armada, si el mes es impar de 1984, ordene invasión.", font=("Arial", 10))
            code.place(x=700, y=140)

            code = tk.Label(self, text="Si el país obtenido NO es Eurasia, y la fecha es de 1985, solicite uso de armas nucleares.", font=("Arial", 10))
            code.place(x=700, y=170)

            opcion = tk.IntVar(value=0)
            opc1=tk.Radiobutton(self, text="Usar medios diplomáticos", variable=opcion, value=1)
            opc1.place(x=700, y=200)
            opc2=tk.Radiobutton(self, text="Ordenar intervención armada", variable=opcion, value=2)
            opc2.place(x=700, y=230)
            opc3=tk.Radiobutton(self, text="Ordenar invasión irreversible", variable=opcion, value=3)
            opc3.place(x=700, y=260)
            opc3=tk.Radiobutton(self, text="Solicitar uso de armas nucleares", variable=opcion, value=4)
            opc3.place(x=700, y=290)

            confirm = tk.Button(self, text="CONFIRMAR DEFINITIVAMENTE", bg="lightgray", command=lambda: verificardatos(opcion.get(), pais=pais, year=year, month=month))
            confirm.place(x=700, y=320)

        def verificardatos(opcion, pais, year, month):
            if pais == 1 and opcion != 1:
                guerraeurasia2()
            elif pais == 2 and year == 1985 and opcion != 4:
                guerraanarquia2()
            elif pais == 2 and year == 1984 and month not in (1,3,5,7,9,11) and opcion != 2:
                guerraanarquia2()
            elif pais == 2 and year == 1984 and month not in (2,4,6,8,10,12) and opcion != 3:
                guerraanarquia2()
            else:
                victoria()

        def victoria():
            ganar = tk.Label(self, text="La dominación mundial es inminente, será recompensado apropiadamente por el Estado", font=("Arial", 10), bg="green")
            ganar.place(x=700, y=350)

            self.imagen2 = tk.PhotoImage(file="final.png")
            self.imagen2_sub = self.imagen2.subsample(2, 2)
            self.map2 = tk.Label(self, image=self.imagen2_sub)
            self.map2.place(x=700, y=380)
        

    def iniciar(self):
        h1 = threading.Thread(target=self.actualizar, args=(60,))
        h1.start()
        h1.join()

    def actualizar(self, seg):
        for t in range(seg, 0, -1):
            self.tiemporestante.config(text=f"Tiempo restante: {t}")
        self.controller.mostrar_frame("Guerraview")

class Exitoview(tk.Frame):
    def __init__(self, parent, controller=None):
        super().__init__(parent, bg="maroon")
        label = tk.Label(self, text="Máquina Enigma", font=("Arial", 16))
        label.pack(pady=10)
        self.parent = parent

        self.controller = controller
