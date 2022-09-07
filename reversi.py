from tkinter import messagebox
from tkinter import *
import logica
import convertirJugadas

class reversi:
    def __init__(self, dimension, dificultad):
        # Tablero
        self.principal = Toplevel()
        self.principal.title("Reversi")
        self.casillas = []
        self.dimension = dimension
        if(self.dimension == 6):
            self.principal.geometry("680x520")
        else:
            self.principal.geometry("850x690")
        self.dificultad = dificultad
        self.juego = logica.Juegoreversi(self.dimension, self.dificultad)


        #LABELS
        #turno jugador
        if((self.juego.jugador == -1) and self.dimension == 6):
            self.turno_label = Label(self.principal, text="turno del jugador: negro")
            self.turno_label.place(x=520, y=10)

        elif((self.juego.jugador == -1) and self.dimension == 8):
            self.turno_label = Label(self.principal, text="turno del jugador: negro")
            self.turno_label.place(x=700, y=10)


        # Imagenes
        self.principal.iconbitmap('./images/chinese_tom.ico')
        self.vacio = PhotoImage(file="./images/verde.png")
        self.fichas_blancas = PhotoImage(file="./images/ficha_white.png")
        self.fichas_negras = PhotoImage(file="./images/ficha_negra.png")

        for i in range(dimension):
            fila = []
            for j in range(dimension):
                if (((i == 2 and j == 2) or (i == 3 and j == 3)) and dimension == 6) or (((i == 3 and j == 3) or (i == 4 and j == 4)) and dimension==8):
                    b1 = Button(self.principal, image=self.fichas_blancas, width="80", height="80")
                    b1.bind("<Button-1>", self.click)
                    b1.x = i
                    b1.y = j
                    b1.grid(row=i, column=j)
                    fila.append(self.vacio)
                elif (((i == 3 and j == 2) or (i == 2 and j == 3)) and dimension == 6) or (((i == 3 and j == 4) or (i == 4 and j == 3)) and dimension==8):
                    b1 = Button(self.principal, image=self.fichas_negras, width="80", height="80")
                    b1.bind("<Button-1>", self.click)
                    b1.x = i
                    b1.y = j
                    b1.grid(row=i, column=j)
                    fila.append(self.vacio)
                else:
                    b1 = Button(self.principal, image=self.vacio, width="80", height="80")
                    b1.bind("<Button-1>", self.click)
                    b1.x = i
                    b1.y = j
                    b1.grid(row=i, column=j)
                    fila.append(self.vacio)
                self.casillas.append(fila)

        self.juego.diccionario, self.juego.jugadas_posibles = self.juego.revisar_jugadas()
        print("posibles jugadas: {}".format(self.juego.jugadas_posibles)) 

    def get_key(self, valor):
            keys = []
            for key, value in self.juego.diccionario.items():
                    if valor in value:
                        keys.append(key)
            return keys           
            
        
    def victoria(self):
        if self.juego.estado_final():
            if self.juego.ganador == -1:
                messagebox.showinfo("REVERSI", "Has ganado con {} fichas".format(self.juego.puntuacion[0]))
                self.principal.destroy()
            elif self.juego.ganador == 0:
                messagebox.showinfo("REVERSI", "Empate")
                self.principal.destroy()
            else:
                messagebox.showinfo("REVERSI", "Has perdido con {} vs {} fichas".format(self.juego.puntuacion[0], self.juego.puntuacion[1]))
                self.principal.destroy()
            return True
        else:
            return False


    def click(self, evento):    
        self.juego.diccionario = {}
        self.juego.jugadas_posibles = []
        
        self.juego.diccionario, self.juego.jugadas_posibles = self.juego.revisar_jugadas()

                
        if (self.juego.tablero[evento.widget.x][evento.widget.y] == 0 and ((evento.widget.x, evento.widget.y)) in self.juego.jugadas_posibles):
            if self.juego.jugador == -1:
                evento.widget["image"] = self.fichas_negras
                self.juego.jugar(evento.widget.x, evento.widget.y)
                #LABELS
                #turno jugador
                self.turno_label.destroy()
                if ((self.juego.jugador == 1) and self.dimension == 6):
                    self.turno_label = Label(self.principal, text="turno del jugador: blanco")
                    self.turno_label.place(x=520, y=10)
                elif ((self.juego.jugador == 1) and self.dimension == 8):
                    self.turno_label = Label(self.principal, text = "turno del jugador: blanco")
                    self.turno_label.place(x=700, y=10)
                elif ((self.juego.jugador == -1) and self.dimension == 6):
                    self.turno_label = Label(self.principal, text = "turno del jugador: negro")
                    self.turno_label.place(x=520, y=10)
                elif ((self.juego.jugador == -1) and self.dimension == 8):
                    self.turno_label = Label(self.principal, text = "turno del jugador: negro")
                    self.turno_label.place(x=700, y=10)
                self.jugadas_compartidas = self.get_key((evento.widget.x, evento.widget.y))
                
                self.juego.convertir_jugadas(self.jugadas_compartidas, evento.widget.x, evento.widget.y, -1)
                self.jugadas_compartidas = []

                for b in range(self.dimension):
                    for c in range(self.dimension):
                        if (self.juego.tablero[b][c] == -1):
                            self.casillas[b][c] = Button(self.principal, image=self.fichas_negras, width="80", height="80")
                            self.casillas[b][c].x = b
                            self.casillas[b][c].y = c
                            self.casillas[b][c].grid(row=b, column=c)
              
            
            else:
                evento.widget["image"] = self.fichas_blancas
                self.juego.jugar(evento.widget.x, evento.widget.y)
                #LABELS
                #turno jugador
                self.turno_label.destroy()
                if ((self.juego.jugador == 1) and self.dimension == 6):
                    self.turno_label = Label(self.principal, text="turno del jugador: blanco")
                    self.turno_label.place(x=520, y=10)
                elif ((self.juego.jugador == 1) and self.dimension == 8):
                    self.turno_label = Label(self.principal, text = "turno del jugador: blanco")
                    self.turno_label.place(x=700, y=10)
                elif ((self.juego.jugador == -1) and self.dimension == 6):
                    self.turno_label = Label(self.principal, text = "turno del jugador: negro")
                    self.turno_label.place(x=520, y=10)
                elif ((self.juego.jugador == -1) and self.dimension == 8):
                    self.turno_label = Label(self.principal, text = "turno del jugador: negro")
                    self.turno_label.place(x=700, y=10)
                

                self.jugadas_compartidas = self.get_key((evento.widget.x, evento.widget.y))
                self.juego.convertir_jugadas(self.jugadas_compartidas, evento.widget.x, evento.widget.y, 1)
                self.jugadas_compartidas = []
                
                for b in range(self.dimension):
                    for c in range(self.dimension):
                        if (self.juego.tablero[b][c] == 1):
                            self.casillas[b][c] = Button(self.principal, image=self.fichas_blancas, width="80", height="80")
                            self.casillas[b][c].x = b
                            self.casillas[b][c].y = c
                            self.casillas[b][c].grid(row=b, column=c)

            self.victoria()
        else:
            if(len(self.juego.jugadas_posibles) == 0):
                messagebox.showinfo("REVERSI", "El jugador {} no tiene jugadas posibles. \nCambio de Turno".format(self.juego.jugador))
                self.juego.jugador= self.juego.jugador*-1
        
        
        self.juego.jugadas_posibles = []
        self.juego.diccionario = {}

        self.juego.diccionario, self.juego.jugadas_posibles = self.juego.revisar_jugadas()
        print("posibles jugadas: {}".format(self.juego.jugadas_posibles))