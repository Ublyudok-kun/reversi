#negro = -1
#blanco = 1
#vacio = 0

class Juegoreversi:
    def __init__(self, estado=[0]*36, turno=-1):
        self.tablero=estado
        self.tablero[14] = -1
        self.tablero[21] = -1
        self.tablero[15] = 1
        self.tablero[20] = 1
        self.jugador = turno

    def jugar(self, jugada):
        self.tablero[jugada]=self.jugador   #tanblero[coordenada de jugada] = que jugador es para saber la ficha. aqui modifica el tablero lista
        self.jugador*=-1

