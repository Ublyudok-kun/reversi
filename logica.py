#negro = -1
#blanco = 1
#vacio = 0

class Juegoreversi:
    def __init__(self, estado=[[0 for i in range(6)] for j in range(6)], turno=-1):
        self.tablero=estado
        self.tablero[2][2] = -1
        self.tablero[3][3] = -1
        self.tablero[2][3] = 1
        self.tablero[3][2] = 1
        self.jugador = turno

    def jugar(self, jugadax, jugaday):
        self.tablero[jugadax][jugaday]=self.jugador   #tanblero[coordenada de jugada] = que jugador es para saber la ficha. aqui modifica el tablero lista
        self.jugador*=-1


#la variable casillas es la matriz que muestra el tkinter, pero para el juego utilizaremos la lista tablero
