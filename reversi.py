from tkinter import *

class reversi:
    def __init__(self):
        self.principal = Tk()
        self.principal.title("conchetumare")
        self.casillas = []
        self.vacio = PhotoImage(file="vacio.png")
        for i in range(6):
            fila=[]
            for j in range(6):
                b1=Button(self.principal, image=self.vacio, width="80", height="80")
                b1.bind("<Button-1>")
                b1.x=i
                b1.y=j
                b1.grid(row=i,column=j)
                fila.append(self.vacio)
        self.casillas.append(fila)


juego = reversi()
mainloop()