#negro = -1
#blanco = 1
#vacio = 0



class Juegoreversi:
    def __init__(self, dimension, turno=-1):
        self.tablero = self.crear_tablero(dimension)
        self.dimension = dimension
        self.jugador = turno
        self.puntuacion = [0, 0]
        self.completo = None
        self.ganador = None
        self.diccionario = {}
        self.jugadas_posibles = []
        

    def jugar(self, jugadax, jugaday):
        # tanblero[coordenada de jugada] = que jugador es para saber la ficha. aqui modifica el tablero lista
        self.tablero[jugadax][jugaday] = self.jugador
        self.jugador *= -1

    def reiniciar(self, dimension):
        self.tablero = self.crear_tablero(dimension)
        self.jugador = -1

    def crear_tablero(self, dimension):
        self.tablero = [[0 for i in range(dimension)] for j in range(dimension)]
        if (dimension == 6):
            self.tablero[2][2] = 1
            self.tablero[3][3] = 1
            self.tablero[2][3] = -1
            self.tablero[3][2] = -1
            
        elif (dimension == 8):
            self.tablero[3][3] = 1
            self.tablero[4][4] = 1
            self.tablero[3][4] = -1
            self.tablero[4][3] = -1

        return self.tablero

    def revisar_jugadas(self):

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

        for a in range(self.dimension):
            for b in range(self.dimension):
                if(self.tablero[a][b] == self.jugador):
                    revisar_arriba(self.tablero, a, b, self.jugador)
                    revisar_abajo(self.tablero, a, b, self.jugador)
                    revisar_derecha(self.tablero, a, b, self.jugador)
                    revisar_izquierda(self.tablero, a, b, self.jugador)
                    revisar_superior_derecha(self.tablero, a, b, self.jugador)
                    revisar_inferior_derecha(self.tablero, a, b, self.jugador)
                    revisar_inferior_izquierda(self.tablero, a, b, self.jugador)
                    revisar_superior_izquierda(self.tablero, a, b, self.jugador)
                    self.diccionario[(a,b)] = self.jugadas_posibles
                    self.jugadas_posibles = []

        return self.diccionario

    def contarFichas(self):
        if self.puntuacion[0] > self.puntuacion[1]:
            self.ganador = -1
        elif self.puntuacion[0] == self.puntuacion[1]:
            self.ganador = 0
        else:
            self.ganador = 1

    def evaluar(self):
        aux = len(self.tablero)
        for i in self.tablero:
            if 0 not in i:
                aux -= 1

        if aux == 0:
            self.completo = True
        else:
            self.completo = False

        if self.completo:
            for i in self.tablero:
                self.puntuacion[0] += i.count(-1)
                self.puntuacion[1] += i.count(1)

    def estado_final(self):
        self.evaluar()
        if self.completo:
            self.contarFichas()
            return True
        else:
            return False

    
    

# la variable casillas es la matriz que muestra el tkinter, pero para el juego utilizaremos la lista tablero
