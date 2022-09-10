


def ver(tablero):
    for i in range(len(tablero)):
        print(tablero[i])

# 3 2 - 2 2 - 1 2


def deshacer_arriba(tablero, x, y, xf, yf, turno, dimension):
    if (x > 0 and x < dimension):
        try:
            # arriba
            if ((y == yf) and (x > xf+1)):
                tablero[x-1][y] = turno*-1
                deshacer_arriba(tablero, x-1, y, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero

def deshacer_abajo(tablero, x, y, xf, yf, turno, dimension):
    if (x >= 0 and x < dimension):
        try:
            # abajo
            if ((y == yf) and (xf-1 > x)):
                tablero[x+1][y] = turno*-1
                deshacer_abajo(tablero, x+1, y, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero


def deshacer_derecha(tablero, x, y, xf, yf, turno, dimension):
    if (y >= 0 and y < dimension):
        try:
            # derecha
            if ((x == xf) and (yf-1 > y)):
                tablero[x][y+1] = turno*-1
                deshacer_derecha(tablero, x, y+1, xf, yf, turno, dimension)             
            else:
                return tablero
        except:
            IndexError
    return tablero



def deshacer_izquierda(tablero, x, y, xf, yf, turno, dimension):
    if (y >= 0 and y < dimension):
        try:
            # izq
            if ((x == xf) and (y > yf+1)):
                tablero[x][y-1] = turno*-1
                deshacer_izquierda(tablero, x, y-1, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero   







def deshacer_superior_izquierda(tablero, x, y, xf, yf, turno, dimension):
    if ((x > 0 and x < dimension) and (y >= 0 and y < dimension)):
        try:
            # arriba izq
            if ((y > yf+1) and (x > xf+1)):
                tablero[x-1][y-1] = turno*-1
                deshacer_superior_izquierda(tablero, x-1, y-1, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero




def deshacer_superior_derecha(tablero, x, y, xf, yf, turno, dimension):
    if ((x > 0 and x < dimension) and (y >= 0 and y < dimension)):
        try:
            # arriba der
            if ((x > xf+1) and (yf-1 > y)):
                tablero[x-1][y+1] = turno*-1
                deshacer_superior_derecha(tablero, x-1, y+1, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero


def deshacer_inferior_izquierda(tablero, x, y, xf, yf, turno, dimension):
    if ((x >= 0 and x < dimension) and (y >= 0 and y < dimension)):
        try:
            # arriba
            if ((xf-1 > x) and (yf+1 < y)):
                tablero[x+1][y-1] = turno*-1
                deshacer_inferior_izquierda(tablero, x+1, y-1, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero




def deshacer_inferior_derecha(tablero, x, y, xf, yf, turno, dimension):
    if ((x >= 0 and x < dimension) and (y >= 0 and y < dimension)):
        try:
            # abajo der
            if ((xf-1 > x) and (y < yf-1)):
                tablero[x+1][y+1] = turno*-1
                deshacer_inferior_derecha(tablero, x+1, y+1, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero




def deshacer_jugadas(tablero, jugadas_compartidas, eventoX, eventoY, turno):
    for aux in jugadas_compartidas:
        tablero = deshacer_arriba(tablero, aux[0], aux[1], eventoX, eventoY, turno, len(tablero))
        tablero = deshacer_abajo(tablero, aux[0], aux[1], eventoX, eventoY, turno, len(tablero))
        tablero = deshacer_derecha(tablero, aux[0], aux[1], eventoX, eventoY, turno, len(tablero))
        tablero = deshacer_izquierda(tablero, aux[0], aux[1], eventoX, eventoY, turno, len(tablero))
        tablero = deshacer_superior_izquierda(tablero, aux[0], aux[1], eventoX, eventoY, turno, len(tablero))
        tablero = deshacer_inferior_izquierda(tablero, aux[0], aux[1], eventoX, eventoY, turno, len(tablero))
        tablero = deshacer_superior_derecha(tablero, aux[0], aux[1], eventoX, eventoY, turno, len(tablero))
        tablero = deshacer_inferior_derecha(tablero, aux[0], aux[1], eventoX, eventoY, turno, len(tablero))
    tablero[eventoX][eventoY] = 0
    return tablero

# tablero = [[0, 0, 0, 0, 0, 0],
#            [0, 1, -1, 1, 0, 0],
#            [0, 1, 1, -1, -1, 0],
#            [0, 1, 1, 1, 0, 0],
#            [0, 0, 0, 0, 0, 0],
#            [0, 0, 0, 0, 0, 0]]


# shared = [(1,1), (1,3), (3,3)]

# tablero = deshacer_jugadas(tablero, shared, 3, 1, 1)
# ver(tablero)