from tkinter import messagebox
from tkinter import *
import logica


class reversi:
    def __init__(self, dimension):
        # Tablero
        self.principal = Toplevel()
        self.principal.title("Reversi")
        self.casillas = []
        self.dimension = dimension
        self.juego = logica.Juegoreversi(dimension)

        # Imagenes
        self.principal.iconbitmap('./images/tom_cino.ico')
        self.vacio = PhotoImage(file="./images/verde.png")
        self.fichas_blancas = PhotoImage(file="./images/ficha_white.png")
        self.fichas_negras = PhotoImage(file="./images/ficha_negra.png")

        for i in range(self.dimension):
            fila = []
            for j in range(self.dimension):
                if (self.dimension == 6):
                    if ((i == 2 and j == 2) or (i == 3 and j == 3)):
                        b1 = Button(
                            self.principal, image=self.fichas_blancas, width="100", height="100")
                        b1.bind("<Button-1>", self.click)
                        b1.x = i
                        b1.y = j
                        b1.grid(row=i, column=j)
                        fila.append(self.vacio)

                    elif ((i == 3 and j == 2) or (i == 2 and j == 3)):
                        b1 = Button(
                            self.principal, image=self.fichas_negras, width="100", height="100")
                        b1.bind("<Button-1>", self.click)
                        b1.x = i
                        b1.y = j
                        b1.grid(row=i, column=j)
                        fila.append(self.vacio)

                    else:
                        b1 = Button(self.principal, image=self.vacio,
                                    width="100", height="100")
                        # evento del click pendiente
                        b1.bind("<Button-1>", self.click)
                        b1.x = i
                        b1.y = j
                        b1.grid(row=i, column=j)
                        fila.append(self.vacio)
                    self.casillas.append(fila)

                elif (self.dimension == 8):
                    if ((i == 3 and j == 3) or (i == 4 and j == 4)):
                        b1 = Button(
                            self.principal, image=self.fichas_blancas, width="50", height="50")
                        b1.bind("<Button-1>", self.click)
                        b1.x = i
                        b1.y = j
                        b1.grid(row=i, column=j)
                        fila.append(self.vacio)

                    elif ((i == 3 and j == 4) or (i == 4 and j == 3)):
                        b1 = Button(
                            self.principal, image=self.fichas_negras, width="50", height="50")
                        b1.bind("<Button-1>", self.click)
                        b1.x = i
                        b1.y = j
                        b1.grid(row=i, column=j)
                        fila.append(self.vacio)

                    else:
                        b1 = Button(self.principal, image=self.vacio, width="50", height="50")
                        # evento del click pendiente
                        b1.bind("<Button-1>", self.click)
                        b1.x = i
                        b1.y = j
                        b1.grid(row=i, column=j)
                        fila.append(self.vacio)
                    self.casillas.append(fila)

    def victoria(self):
        if self.juego.estado_final():
            if self.juego.ganador == -1:
                messagebox.showinfo("REVERSI", "Has ganado con {} fichas".format(self.juego.puntuacion[0]))
                
            elif self.juego.ganador == 0:
                messagebox.showinfo("REVERSI", "Empate")
            else:
                messagebox.showinfo("REVERSI", "Has perdido con {} vs {} fichas".format(self.juego.puntuacion[0], self.juego.puntuacion[1]))
            #print(self.juego.puntuacion)
            return True
        else:
            return False

    def click(self, evento):
        if self.juego.tablero[evento.widget.x][evento.widget.y] == 0:
            if self.juego.jugador == -1:
                evento.widget["image"] = self.fichas_negras
            else:
                evento.widget["image"] = self.fichas_blancas
            self.juego.jugar(evento.widget.x, evento.widget.y)
            self.victoria()
        
        #print(self.juego.tablero)
        #print(self.juego.puntuacion)


# juego = reversi()
# mainloop()
