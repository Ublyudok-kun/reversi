from tkinter import *
from tkinter.ttk import Combobox
import reversi


class Configuracion:
    def __init__(self):
        # ventana del menu
        self.dprincipal = Tk()
        self.dprincipal.title("configuraciones")
        self.dprincipal.iconbitmap = ("./images/tom_cino.ico")
        self.dprincipal.geometry("300x150")

        # Label de las opciones dimension
        self.dimension_label = Label(self.dprincipal, text="Dimensión del tablero: ")
        self.dimension_label.place(x=10, y=10)

        # Drop opciones de la dimension
        self.dimension_combo = Combobox(self.dprincipal, state="readonly")
        self.dimension_combo.place(x=150, y=10)
        self.dimension_combo["values"] = ('6x6', '8x8')
        self.dimension_combo.current(0)

        # Label opciones dificultad
        self.dificultad_label = Label(self.dprincipal, text="Selecciona dificultad: ")
        self.dificultad_label.place(x=10, y=50)

        # Drop opciones de la dificultad
        self.dificultad_combo = Combobox(self.dprincipal, state="readonly")
        self.dificultad_combo.place(x=150, y=50)
        self.dificultad_combo["values"] = ("Fácil", "Normal", "Difícil")
        self.dificultad_combo.current(1)

        # boton OK
        self.boton = Button(self.dprincipal, text="OK", width="3", height="1")
        self.boton.place(x=130, y=100)
        self.boton.bind("<Button-1>", self.click)

    def click(self, evento):
        self.dimension = int(self.dimension_combo.get()[0])
        self.dificultad = self.dificultad_combo.get()
        #print(self.dimension, self.dificultad)
        self.dprincipal.withdraw()
        self.juego = reversi.reversi(self.dimension)

        # mainloop()


a = Configuracion()
mainloop()
