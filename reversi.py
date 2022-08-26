from tkinter import *

class reversi:
    def __init__(self):
        self.principal = Tk()
        self.principal.title("reversi")
        self.casillas = []
        self.vacio = PhotoImage(file="./images/verde.png")
        self.fichas_blancas = PhotoImage(file="./images/ficha_white.png")
        self.fichas_negras = PhotoImage(file="./images/ficha_nigga.png")
        for i in range(6):
            fila=[]
            for j in range(6):
                if ((i==2 and j==2) or (i==3 and j==3)):
                    b1 = Button(self.principal, image=self.fichas_negras, width="100", height="100")
                    b1.bind("<Button-1>")
                    b1.x=i
                    b1.y=j
                    b1.grid(row=i,column=j)
                    fila.append(self.vacio)

                elif ((i==3 and j==2) or (i==2 and j==3)):
                    b1 = Button(self.principal, image=self.fichas_blancas, width="100", height="100")
                    b1.bind("<Button-1>")
                    b1.x=i
                    b1.y=j
                    b1.grid(row=i,column=j)
                    fila.append(self.vacio)

                else:
                    b1=Button(self.principal, image=self.vacio, width="100", height="100")
                    b1.bind("<Button-1>") #evento del click pendiente
                    b1.x=i
                    b1.y=j
                    b1.grid(row=i,column=j)
                    fila.append(self.vacio)
            self.casillas.append(fila)
        

juego = reversi()
mainloop()