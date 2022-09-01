# from ast import Continue


a = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

turno = -1

jugadas_posibles = []

dimension = len(a)

diccionario = {}


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

for i in range(dimension):
    for j in range(dimension):
        if(a[i][j] == turno): #si encuentra una ficha negra
            try:
                revisar_arriba(a, i, j, turno)
                revisar_abajo(a, i, j, turno)
                revisar_derecha(a, i, j, turno)
                revisar_izquierda(a, i, j, turno)
                revisar_superior_derecha(a, i, j, turno)
                revisar_inferior_derecha(a, i, j, turno)
                revisar_inferior_izquierda(a, i, j, turno)
                revisar_superior_izquierda(a, i, j, turno)
                diccionario[(i,j)] = jugadas_posibles
                jugadas_posibles = []
            except: IndexError

#print(jugadas_posibles)
#print(dimension)
print(diccionario)

# diccionario = {(1,2): [1,2,3,4], "key2": [(1,2),(3,4)]} #esto funciona

# diccionario[(3,4)] = [(0,5), (4,8), (5,5)]

# diccionario[(3,4)].append((5,1))

# print(diccionario)

# for i in diccionario:
#         print(diccionario[i])

# print(list(diccionario.values()))




def get_key(valor):
        for key, value in diccionario.items():
                if valor in value:
                        return key


#print(get_key((1,2))[0])

#probar esto
def convertir_arriba(tablero,x,y,xf,yf,turno):
    if(x>0 and x<dimension):
        try:
            #arriba
            if((tablero[x][y]  == tablero[xf][yf])):
                if((tablero[x-1][y] == (turno*-1))):
                    tablero[x-1][y] = turno
                    convertir_arriba(tablero,x-1,y,xf,yf,turno)

            else:
                return tablero

        except: IndexError

    return tablero


print(list(diccionario.values()))

for y in list(diccionario.values()):
    for z in y:
        print(z)

        #ojo despues reiniciar el diccionario