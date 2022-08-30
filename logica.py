#negro = -1
#blanco = 1
#vacio = 0

class Juegoreversi:
    def __init__(self, dimension, turno=-1):
        self.tablero=self.crear_tablero(dimension)
        self.jugador = turno
        self.ganador = None
        self.completo = False

    def jugar(self, jugadax, jugaday):
        self.tablero[jugadax][jugaday]=self.jugador   #tanblero[coordenada de jugada] = que jugador es para saber la ficha. aqui modifica el tablero lista
        self.jugador*=-1

    def reiniciar(self, dimension):
        self.tablero = [[0 for i in range(dimension)] for j in range(dimension)]
        if (dimension == 6):
            self.tablero[2][2] = 1
            self.tablero[3][3] = 1
            self.tablero[2][3] = -1
            self.tablero[3][2] = -1
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



#la variable casillas es la matriz que muestra el tkinter, pero para el juego utilizaremos la lista tablero
