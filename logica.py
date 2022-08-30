#negro = -1
#blanco = 1
#vacio = 0

class Juegoreversi:
    def __init__(self, dimension, turno=-1):
        self.tablero = self.crear_tablero(dimension)
        self.jugador = turno
        self.puntuacion = [0, 0]
        self.completo = None
        self.ganador = None

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
