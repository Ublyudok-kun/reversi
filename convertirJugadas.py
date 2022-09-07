# convertir
def convertir_arriba(tablero, x, y, xf, yf, turno, dimension):
    if (x > 0 and x < dimension):
        try:
            # arriba
            if ((y == yf) and (x > xf)):
                if ((tablero[x-1][y] == (turno*-1))):
                    tablero[x-1][y] = turno
                    convertir_arriba(tablero, x-1, y, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero


def convertir_derecha(tablero, x, y, xf, yf, turno, dimension):
    if (y >= 0 and y < dimension):
        try:
            # derecha
            if ((x == xf) and (yf > y)):
                if ((tablero[x][y+1] == (turno*-1))):
                    tablero[x][y+1] = turno
                    convertir_derecha(tablero, x, y+1, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero


def convertir_izquierda(tablero, x, y, xf, yf, turno, dimension):
    if (y >= 0 and y < dimension):
        try:
            # izq
            if ((x == xf) and (y > yf)):
                if ((tablero[x][y-1] == (turno*-1))):
                    tablero[x][y-1] = turno
                    convertir_izquierda(tablero, x, y-1, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero


def convertir_abajo(tablero, x, y, xf, yf, turno, dimension):
    if (x >= 0 and x < dimension):
        try:
            # abajo
            if ((y == yf) and (xf > x)):
                if ((tablero[x+1][y] == (turno*-1))):
                    tablero[x+1][y] = turno
                    convertir_abajo(tablero, x+1, y, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero


def convertir_superior_derecha(tablero, x, y, xf, yf, turno, dimension):
    if ((x > 0 and x < dimension) and (y >= 0 and y < dimension)):
        try:
            # arriba der
            if ((x > xf) and (yf > y)):
                if ((tablero[x-1][y+1] == (turno*-1))):
                    tablero[x-1][y+1] = turno
                    convertir_superior_derecha(tablero, x-1, y+1, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero


def convertir_superior_izquierda(tablero, x, y, xf, yf, turno, dimension):
    if ((x > 0 and x < dimension) and (y >= 0 and y < dimension)):
        try:
            # arriba izq
            if ((y > yf) and (x > xf)):
                if ((tablero[x-1][y-1] == (turno*-1))):
                    tablero[x-1][y-1] = turno
                    convertir_superior_izquierda(tablero, x-1, y-1, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero


def convertir_inferior_izquierda(tablero, x, y, xf, yf, turno, dimension):
    if ((x >= 0 and x < dimension) and (y >= 0 and y < dimension)):
        try:
            # arriba
            if ((xf > x) and (yf < y)):
                if ((tablero[x+1][y-1] == (turno*-1))):
                    tablero[x+1][y-1] = turno
                    convertir_inferior_izquierda(tablero, x+1, y-1, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero


def convertir_inferior_derecha(tablero, x, y, xf, yf, turno, dimension):
    if ((x >= 0 and x < dimension) and (y >= 0 and y < dimension)):
        try:
            # abajo der
            if ((xf > x) and (y < yf)):
                if ((tablero[x+1][y+1] == (turno*-1))):
                    tablero[x+1][y+1] = turno
                    convertir_inferior_derecha(tablero, x+1, y+1, xf, yf, turno, dimension)
            else:
                return tablero
        except:
            IndexError
    return tablero
