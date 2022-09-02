from tkinter import messagebox
from tkinter import *
import logica
#import prueba
#from reversi.prueba import revisar_abajo, revisar_arriba, revisar_derecha, revisar_inferior_derecha, revisar_inferior_izquierda, revisar_izquierda, revisar_superior_derecha, revisar_superior_izquierda


class reversi:
    def __init__(self, dimension):
        # Tablero
        self.principal = Toplevel()
        self.principal.title("Reversi")
        self.casillas = []
        self.dimension = dimension
        self.juego = logica.Juegoreversi(dimension)
        self.jugadas_posibles = []
        self.diccionario = {}
        self.jugadas_compartidas = []

        # Imagenes
        self.principal.iconbitmap('./images/chinese_tom.ico')
        self.vacio = PhotoImage(file="./images/verde.png")
        self.fichas_blancas = PhotoImage(file="./images/ficha_white.png")
        self.fichas_negras = PhotoImage(file="./images/ficha_negra.png")



        for i in range(self.dimension):
            fila = []
            for j in range(self.dimension):
                if (self.dimension == 6):
                    if ((i == 2 and j == 2) or (i == 3 and j == 3)):
                        b1 = Button(self.principal, image=self.fichas_blancas, width="80", height="80")
                        b1.bind("<Button-1>", self.click)
                        b1.x = i
                        b1.y = j
                        b1.grid(row=i, column=j)
                        fila.append(self.vacio)

                    elif ((i == 3 and j == 2) or (i == 2 and j == 3)):
                        b1 = Button(
                            self.principal, image=self.fichas_negras, width="80", height="80")
                        b1.bind("<Button-1>", self.click)
                        b1.x = i
                        b1.y = j
                        b1.grid(row=i, column=j)
                        fila.append(self.vacio)

                    else:
                        b1 = Button(self.principal, image=self.vacio,
                                    width="80", height="80")
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
                            self.principal, image=self.fichas_blancas, width="80", height="80")
                        b1.bind("<Button-1>", self.click)
                        b1.x = i
                        b1.y = j
                        b1.grid(row=i, column=j)
                        fila.append(self.vacio)

                    elif ((i == 3 and j == 4) or (i == 4 and j == 3)):
                        b1 = Button(
                            self.principal, image=self.fichas_negras, width="80", height="80")
                        b1.bind("<Button-1>", self.click)
                        b1.x = i
                        b1.y = j
                        b1.grid(row=i, column=j)
                        fila.append(self.vacio)

                    else:
                        b1 = Button(self.principal, image=self.vacio, width="80", height="80")
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
                self.principal.destroy()
            else:
                messagebox.showinfo("REVERSI", "Has perdido con {} vs {} fichas".format(self.juego.puntuacion[0], self.juego.puntuacion[1]))
            #print(self.juego.puntuacion)
            return True
        else:
            return False

    def click(self, evento):
        def revisar_arriba(tablero,x, y, turno):
            if(x>0 and x<self.dimension):
                    try:
                        #arriba
                        if((tablero[x-1][y] == 0 and tablero[x][y] == (turno*-1))):
                            self.jugadas_posibles.append((x-1, y))
                                
                        elif(tablero[x-1][y] == (turno*-1)):
                            revisar_arriba(tablero, x-1, y, turno)

                    except: IndexError
                        
                    return self.jugadas_posibles

        def revisar_abajo(tablero, x, y, turno):
            if(x>=0 and x<self.dimension):
                try:
                    #abajo
                    if(tablero[x+1][y] == 0 and tablero[x][y] == (turno*-1)):
                        self.jugadas_posibles.append((x+1,y)) 

                    elif(tablero[x+1][y] == (turno*-1)):
                        revisar_abajo(tablero, x+1, y, turno)
                except: IndexError

            return self.jugadas_posibles

        def revisar_derecha(tablero, x, y, turno):
            if(y>=0 and y<self.dimension):
                try:
                    #derecha
                    if(tablero[x][y+1] == 0 and tablero[x][y] == (turno*-1)):
                        self.jugadas_posibles.append((x,y+1))
                    
                    elif(tablero[x][y+1] == (turno*-1)):
                        revisar_derecha(tablero, x, y+1, turno)
                except: IndexError

            return self.jugadas_posibles

        def revisar_izquierda(tablero, x, y, turno):
            if(y>0 and y<self.dimension):
                try:
                    #izquierda
                    if(tablero[x][y-1] == 0 and tablero[x][y] == (turno*-1)):
                        self.jugadas_posibles.append((x,y-1))
                    
                    elif(tablero[x][y-1] == (turno*-1)):
                        revisar_izquierda(tablero, x, y-1, turno)
                except: IndexError

            return self.jugadas_posibles

        def revisar_superior_derecha(tablero, x, y, turno):
            if((x>0 and x<self.dimension) and (y>=0 and y<self.dimension)):
                try:
                    #diagonal superior derecha
                    if(tablero[x-1][y+1] == 0 and tablero[x][y] == (turno*-1)):
                        self.jugadas_posibles.append((x-1,y+1))
                    
                    elif(tablero[x-1][y+1] == (turno*-1)):
                        revisar_superior_derecha(tablero, x-1, y+1, turno)
                except: IndexError

            return self.jugadas_posibles

        def revisar_inferior_derecha(tablero, x, y, turno):
            if((x>=0 and x<self.dimension) and (y>=0 and y<self.dimension)):
                try:
                    #diagonal inferior derecha
                    if(tablero[x+1][y+1] == 0 and tablero[x][y] == (turno*-1)):
                        self.jugadas_posibles.append((x+1,y+1))
                    
                    elif(tablero[x+1][y+1] == (turno*-1)):
                        revisar_inferior_derecha(tablero, x+1, y+1, turno)
                except: IndexError

            return self.jugadas_posibles

        def revisar_inferior_izquierda(tablero, x, y, turno):
            if((x>=0 and x<self.dimension) and (y>0 and y<self.dimension)):
                try:
                    #diagonal inferior izquierda
                    if(tablero[x+1][y-1] == 0 and tablero[x][y] == (turno*-1)):
                        self.jugadas_posibles.append((x+1,y-1))
                    
                    elif(tablero[x+1][y-1] == (turno*-1)):
                        revisar_inferior_izquierda(tablero, x+1, y-1, turno)
                except: IndexError

            return self.jugadas_posibles

        def revisar_superior_izquierda(tablero, x, y, turno):
            if((x>0 and x<self.dimension) and (y>0 and y<self.dimension)):
                try:
                    #diagonal superior izquierdo
                    if(tablero[x-1][y-1] == 0 and tablero[x][y] == (turno*-1)):
                        self.jugadas_posibles.append((x-1,y-1))
                    
                    elif(tablero[x-1][y-1] == (turno*-1)):
                        revisar_superior_izquierda(tablero, x-1, y-1, turno)
                except: IndexError

            return self.jugadas_posibles

        def get_key(valor):
            keys = []
            for key, value in self.diccionario.items():
                    if valor in value:
                        keys.append(key)
            return keys


        #convertir
        def convertir_arriba(tablero,x,y,xf,yf,turno):
            if(x>0 and x<self.dimension):
                try:
                    #arriba
                    if((y==yf) and (x>xf)):
                        if((tablero[x-1][y] == (turno*-1))):
                            tablero[x-1][y] = turno
                            convertir_arriba(tablero,x-1,y,xf,yf,turno)

                    else:
                        return tablero

                except: IndexError

            return tablero

        def convertir_derecha(tablero,x,y,xf,yf,turno):
            if(y>=0 and y<self.dimension):
                try:
                    #derecha
                    if((x == xf) and (yf>y)):
                        if((tablero[x][y+1] == (turno*-1))):
                            tablero[x][y+1] = turno
                            convertir_derecha(tablero,x,y+1,xf,yf,turno)

                    else:
                        return tablero

                except: IndexError

            return tablero

        def convertir_izquierda(tablero,x,y,xf,yf,turno):
            if(y>=0 and y<self.dimension):
                try:
                    #izq
                    if((x==xf) and (y>yf)):
                        if((tablero[x][y-1] == (turno*-1))):
                            tablero[x][y-1] = turno
                            convertir_izquierda(tablero,x,y-1,xf,yf,turno)

                    else:
                        return tablero

                except: IndexError

            return tablero

        def convertir_abajo(tablero,x,y,xf,yf,turno):
            if(x>=0 and x<self.dimension):
                try:
                    #abajo
                    if((y==yf) and (xf>x)):
                        if((tablero[x+1][y] == (turno*-1))):
                            tablero[x+1][y] = turno
                            convertir_abajo(tablero,x+1,y,xf,yf,turno)

                    else:
                        return tablero

                except: IndexError

            return tablero

        def convertir_superior_derecha(tablero,x,y,xf,yf,turno):
            if((x>0 and x<self.dimension) and (y>=0 and y<self.dimension)):
                try:
                    #arriba der
                    if((x>xf) and (yf>y)):
                        if((tablero[x-1][y+1] == (turno*-1))):
                            tablero[x-1][y+1] = turno
                            convertir_superior_derecha(tablero,x-1,y+1,xf,yf,turno)

                    else:
                        return tablero

                except: IndexError

            return tablero

        def convertir_superior_izquierda(tablero,x,y,xf,yf,turno):
            if((x>0 and x<self.dimension) and (y>=0 and y<self.dimension)):
                try:
                    #arriba izq
                    if((y>yf) and (x>xf)):
                        if((tablero[x-1][y-1] == (turno*-1))):
                            tablero[x-1][y-1] = turno
                            convertir_superior_izquierda(tablero,x-1,y-1,xf,yf,turno)

                    else:
                        return tablero

                except: IndexError

            return tablero

        def convertir_inferior_izquierda(tablero,x,y,xf,yf,turno):
            if((x>=0 and x<self.dimension) and (y>=0 and y<self.dimension)):
                try:
                    #arriba
                    if((xf>x) and (yf<y)):
                        if((tablero[x+1][y-1] == (turno*-1))):
                            tablero[x+1][y-1] = turno
                            convertir_inferior_izquierda(tablero,x+1,y-1,xf,yf,turno)

                    else:
                        return tablero

                except: IndexError

            return tablero

        def convertir_inferior_derecha(tablero,x,y,xf,yf,turno):
            if((x>=0 and x<self.dimension) and (y>=0 and y<self.dimension)):
                try:
                    #abajo der
                    if((xf > x) and (y<yf)):
                        if((tablero[x+1][y+1] == (turno*-1))):
                            tablero[x+1][y+1] = turno
                            convertir_inferior_derecha(tablero,x+1,y+1,xf,yf,turno)

                    else:
                        return tablero

                except: IndexError

            return tablero

        for a in range(self.dimension):
            for b in range(self.dimension):
                if(self.juego.tablero[a][b] == self.juego.jugador):
                    revisar_arriba(self.juego.tablero, a, b, self.juego.jugador)
                    revisar_abajo(self.juego.tablero, a, b, self.juego.jugador)
                    revisar_derecha(self.juego.tablero, a, b, self.juego.jugador)
                    revisar_izquierda(self.juego.tablero, a, b, self.juego.jugador)
                    revisar_superior_derecha(self.juego.tablero, a, b, self.juego.jugador)
                    revisar_inferior_derecha(self.juego.tablero, a, b, self.juego.jugador)
                    revisar_inferior_izquierda(self.juego.tablero, a, b, self.juego.jugador)
                    revisar_superior_izquierda(self.juego.tablero, a, b, self.juego.jugador)
                    self.diccionario[(a,b)] = self.jugadas_posibles
                    self.jugadas_posibles = []
        
        for y in list(self.diccionario.values()):
            for z in y:
                self.jugadas_posibles.append(z)
        print(self.jugadas_posibles)
        if (self.juego.tablero[evento.widget.x][evento.widget.y] == 0 and ((evento.widget.x, evento.widget.y)) in self.jugadas_posibles):
            if self.juego.jugador == -1:
                evento.widget["image"] = self.fichas_negras
                self.juego.jugar(evento.widget.x, evento.widget.y)
                self.jugadas_compartidas = get_key((evento.widget.x, evento.widget.y))

                for d in self.jugadas_compartidas:
                    self.juego.tablero = convertir_arriba(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, -1)
                    self.juego.tablero = convertir_derecha(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, -1)
                    self.juego.tablero = convertir_abajo(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, -1)
                    self.juego.tablero = convertir_izquierda(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, -1)
                    self.juego.tablero = convertir_superior_derecha(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, -1)
                    self.juego.tablero = convertir_inferior_derecha(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, -1)
                    self.juego.tablero = convertir_inferior_izquierda(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, -1)
                    self.juego.tablero = convertir_superior_izquierda(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, -1)
                self.jugadas_compartidas = []

                for b in range(self.dimension):
                    for c in range(self.dimension):
                        if (self.juego.tablero[b][c] == -1):
                            self.casillas[b][c] = Button(self.principal, image=self.fichas_negras, width="80", height="80")
                            self.casillas[b][c].x = b
                            self.casillas[b][c].y = c
                            self.casillas[b][c].grid(row=b, column=c)
                #print(self.jugadas_posibles)
                #print(get_key((evento.widget.x, evento.widget.y))[0], get_key((evento.widget.x, evento.widget.y))[1])
                self.jugadas_posibles = []
                self.diccionario = {}


            elif(self.juego.jugador == 1):
                evento.widget["image"] = self.fichas_blancas
                self.juego.jugar(evento.widget.x, evento.widget.y)
                self.jugadas_compartidas = get_key((evento.widget.x, evento.widget.y))
                for d in self.jugadas_compartidas:
                    self.juego.tablero = convertir_arriba(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, 1)
                    self.juego.tablero = convertir_derecha(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, 1)
                    self.juego.tablero = convertir_abajo(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, 1)
                    self.juego.tablero = convertir_izquierda(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, 1)
                    self.juego.tablero = convertir_superior_derecha(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, 1)
                    self.juego.tablero = convertir_inferior_derecha(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, 1)
                    self.juego.tablero = convertir_inferior_izquierda(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, 1)
                    self.juego.tablero = convertir_superior_izquierda(self.juego.tablero, d[0], d[1], evento.widget.x, evento.widget.y, 1)
                self.jugadas_compartidas = []
                
                
                for b in range(self.dimension):
                    for c in range(self.dimension):
                        if (self.juego.tablero[b][c] == 1):
                            self.casillas[b][c] = Button(self.principal, image=self.fichas_blancas, width="80", height="80")
                            self.casillas[b][c].x = b
                            self.casillas[b][c].y = c
                            self.casillas[b][c].grid(row=b, column=c)

                #print(self.jugadas_posibles)
                #print(get_key((evento.widget.x, evento.widget.y))[0], get_key((evento.widget.x, evento.widget.y))[1])
                self.jugadas_posibles = []
                self.diccionario = {}
            
            #self.juego.jugar(evento.widget.x, evento.widget.y)
            self.victoria()



        
        self.jugadas_posibles = []
        self.diccionario = {}
        
        
        
        #print(self.juego.tablero)
        #print(self.juego.puntuacion)


# juego = reversi()
# mainloop()
