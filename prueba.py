# from ast import Continue


# a = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

# turno = -1

# jugadas_posibles = []

# dimension = len(a)


def revisar_arriba(tablero,x,y, turno):
    if(x>0 and x<dimension):
        try:
            #arriba
            if((tablero[x-1][y] == 0 and tablero[x][y] == (turno*-1))):
                jugadas_posibles.append((x-1, y))
                

            elif(tablero[x-1][y] == (turno*-1)):
                revisar_arriba(tablero, x-1, y, turno)

        except: IndexError
        
    return jugadas_posibles

def revisar_abajo(tablero, x, y, turno):
    if(x>=0 and x<dimension):
        try:
            #abajo
            if(tablero[x+1][y] == 0 and tablero[x][y] == (turno*-1)):
                jugadas_posibles.append((x+1,y)) 

            elif(tablero[x+1][y] == (turno*-1)):
                revisar_abajo(tablero, x+1, y, turno)
        except: IndexError

    return jugadas_posibles

def revisar_derecha(tablero, x, y, turno):
    if(y>=0 and y<dimension):
        try:
            #derecha
            if(tablero[x][y+1] == 0 and tablero[x][y] == (turno*-1)):
                jugadas_posibles.append((x,y+1))
            
            elif(tablero[x][y+1] == (turno*-1)):
                revisar_derecha(tablero, x, y+1, turno)
        except: IndexError

    return jugadas_posibles
        
def revisar_izquierda(tablero, x, y, turno):
    if(y>=0 and y<dimension):
        try:
            #izquierda
            if(tablero[x][y-1] == 0 and tablero[x][y] == (turno*-1)):
                jugadas_posibles.append((x,y-1))
            
            elif(tablero[x][y-1] == (turno*-1)):
                revisar_izquierda(tablero, x, y-1, turno)
        except: IndexError

    return jugadas_posibles

def revisar_superior_derecha(tablero, x, y, turno):
    if((x>0 and x<dimension) and (y>=0 and y<dimension)):
        try:
            #diagonal superior derecha
            if(tablero[x-1][y+1] == 0 and tablero[x][y] == (turno*-1)):
                jugadas_posibles.append((x-1,y+1))
            
            elif(tablero[x-1][y+1] == (turno*-1)):
                revisar_superior_derecha(tablero, x-1, y+1, turno)
        except: IndexError

    return jugadas_posibles

def revisar_inferior_derecha(tablero, x, y, turno):
    if((x>=0 and x<dimension) and (y>=0 and y<dimension)):
        try:
            #diagonal inferior derecha
            if(tablero[x+1][y+1] == 0 and tablero[x][y] == (turno*-1)):
                jugadas_posibles.append((x+1,y+1))
            
            elif(tablero[x+1][y+1] == (turno*-1)):
                revisar_inferior_derecha(tablero, x+1, y+1, turno)
        except: IndexError

    return jugadas_posibles

def revisar_inferior_izquierda(tablero, x, y, turno):
    if((x>=0 and x<dimension) and (y>=0 and y<dimension)):
        try:
            #diagonal inferior izquierda
            if(tablero[x+1][y-1] == 0 and tablero[x][y] == (turno*-1)):
                jugadas_posibles.append((x+1,y-1))
            
            elif(tablero[x+1][y-1] == (turno*-1)):
                revisar_inferior_izquierda(tablero, x+1, y-1, turno)
        except: IndexError

    return jugadas_posibles

def revisar_superior_izquierda(tablero, x, y, turno):
    if((x>0 and x<dimension) and (y>=0 and y<dimension)):
        try:
            #diagonal superior izquierdo
            if(tablero[x-1][y-1] == 0 and tablero[x][y] == (turno*-1)):
                jugadas_posibles.append((x-1,y-1))
            
            elif(tablero[x-1][y-1] == (turno*-1)):
                revisar_superior_izquierda(tablero, x-1, y-1, turno)
        except: IndexError

    return jugadas_posibles

# for i in range(dimension):
#     for j in range(dimension):
#         if(a[i][j] == turno): #si encuentra una ficha negra
#             revisar_arriba(a, i, j, turno)
#             revisar_abajo(a, i, j, turno)
#             revisar_derecha(a, i, j, turno)
#             revisar_izquierda(a, i, j, turno)
#             revisar_superior_derecha(a, i, j, turno)
#             revisar_inferior_derecha(a, i, j, turno)
#             revisar_inferior_izquierda(a, i, j, turno)
#             revisar_superior_izquierda(a, i, j, turno)

# print(jugadas_posibles)
# print(dimension)