#negro = -1
#blanco = 1
#vacio = 0
import revisarJugadas
import convertirJugadas
import numpy as np

class Juegoreversi:
    def __init__(self, dimension, dificultad,  turno=-1):
        self.tablero = self.crear_tablero(dimension)
        self.dimension = dimension
        self.dificultad = dificultad
        self.jugador = turno
        self.puntuacion = [0, 0]
        self.completo = None
        self.ganador = None
        self.diccionario = {}
        self.jugadas_posibles = []
        self.contador_de_profundidad = 0
        
    def jugar(self, jugadax, jugaday):
        self.tablero[jugadax][jugaday] = self.jugador
        self.jugador *= -1

    def deshacer_jugada(self, jugadax, jugaday):
        self.tablero[jugadax][jugaday] = 0
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

    def VerJugadasPosibles(self):
        print(self.jugadas_posibles)

    def revisar_jugadas(self):
        for a in range(self.dimension):
            for b in range(self.dimension):
                if(self.tablero[a][b] == self.jugador):
                    revisarJugadas.revisar_arriba(self.tablero, a, b, self.jugador, self.dimension, self.jugadas_posibles)
                    revisarJugadas.revisar_abajo(self.tablero, a, b, self.jugador, self.dimension, self.jugadas_posibles)
                    revisarJugadas.revisar_derecha(self.tablero, a, b, self.jugador, self.dimension, self.jugadas_posibles)
                    revisarJugadas.revisar_izquierda(self.tablero, a, b, self.jugador, self.dimension, self.jugadas_posibles)
                    revisarJugadas.revisar_superior_derecha(self.tablero, a, b, self.jugador, self.dimension, self.jugadas_posibles)
                    revisarJugadas.revisar_inferior_derecha(self.tablero, a, b, self.jugador, self.dimension, self.jugadas_posibles)
                    revisarJugadas.revisar_inferior_izquierda(self.tablero, a, b, self.jugador, self.dimension, self.jugadas_posibles)
                    revisarJugadas.revisar_superior_izquierda(self.tablero, a, b, self.jugador, self.dimension, self.jugadas_posibles)
                    self.diccionario[(a,b)] = self.jugadas_posibles
                    self.jugadas_posibles = []
        
        for y in list(self.diccionario.values()):
            for z in y:
                self.jugadas_posibles.append(z)

     
        return self.diccionario, self.jugadas_posibles


    def convertir_jugadas(self, jugadas_compartidas, eventoX, eventoY, turno):
        for d in jugadas_compartidas:
            self.tablero = convertirJugadas.convertir_arriba(self.tablero, d[0], d[1], eventoX, eventoY, turno, self.dimension)
            self.tablero = convertirJugadas.convertir_derecha(self.tablero, d[0], d[1], eventoX, eventoY, turno, self.dimension)
            self.tablero = convertirJugadas.convertir_abajo(self.tablero, d[0], d[1], eventoX, eventoY, turno, self.dimension)
            self.tablero = convertirJugadas.convertir_izquierda(self.tablero, d[0], d[1], eventoX, eventoY, turno, self.dimension)
            self.tablero = convertirJugadas.convertir_superior_derecha(self.tablero, d[0], d[1], eventoX, eventoY, turno, self.dimension)
            self.tablero = convertirJugadas.convertir_inferior_derecha(self.tablero, d[0], d[1], eventoX, eventoY, turno, self.dimension)
            self.tablero = convertirJugadas.convertir_inferior_izquierda(self.tablero, d[0], d[1],eventoX, eventoY, turno, self.dimension)
            self.tablero = convertirJugadas.convertir_superior_izquierda(self.tablero, d[0], d[1], eventoX, eventoY, turno, self.dimension)


    def contarFichas(self):
        if self.puntuacion[0] > self.puntuacion[1]:
            self.ganador = -1
        elif self.puntuacion[0] == self.puntuacion[1]:
            self.ganador = 0
        else:
            self.ganador = 1


    def calcular_utilidad(self):                      #esta funcion para calcular la utilidad
        for i in self.tablero:
            self.puntuacion[0] += i.count(-1)       
            self.puntuacion[1] += i.count(1)
        if (self.puntuacion[0] > self.puntuacion[1]):
            self.ganador = -1

        elif (self.puntuacion[0] < self.puntuacion[1]):
            self.ganador = 1
        
        else:
            self.ganador = 0
        
        return self.ganador


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

    
    

def minimax(juego, etapa, secuencia, secuencias):             #PENDIENTE

    if (juego.dificultad == "Easy"):
        juego.dificultad = 3
    elif (juego.dificultad == "Normal"):
        juego.dificultad = 6
    elif (juego.dificultad == "Hard"):
        juego.dificultad = 9

    #################################################################


    if(juego.contador_de_profundidad == juego.dificultad):  #caso base nodo "terminal"
        secuencias.append(secuencia.copy())
        return [juego.calcular_utilidad()]

    if etapa == 1: #IA
        valor = [np.NINF, None]
    else:           #US
        valor = [np.inf, None]

    ############### creando arbol de decisiones ###########################
    if(juego.contador_de_profundidad < juego.dificultad):
        diccionario_posibles, jugadas_posibles = juego.revisar_jugadas() ##ademas de revisar y poner la ficha hay que convertirlas y contarlas
        for jugada in jugadas_posibles:
            juego.jugar(jugada)
            jugadas_compartidas = juego.get_key((jugada[0], jugada[1]))
            for ficha in jugadas_compartidas:
                juego.convertirJugadas(juego, ficha, jugada[0], jugada[1], etapa)
            secuencia.append(jugada)
            juego.contador_de_profundidad+=1
            opcion = minimax(juego, etapa*-1, secuencia, secuencias)
        #########################################################################

        #maximizar
        if etapa == 1:
            if valor[0]<opcion[0]:
                valor=[opcion[0], jugada]
        else:
        #minimizar
            if valor[0]>opcion[0]:
                valor = [opcion[0], jugada]
        juego.deshacer_jugada(jugada)
        secuencia.pop()
    return valor

        
        
        


        



    
    

# la variable casillas es la matriz que muestra el tkinter, pero para el juego utilizaremos la lista tablero
