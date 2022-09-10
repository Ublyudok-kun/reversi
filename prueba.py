tablero = [[0, 0, 0, 0, 0, 0], 
           [0, 0, -1, 1, 0, 0], 
           [0, -1, -1, -1, 0, 0],
           [0, 1, -1, -1, -1, 0], 
           [0, 0, 0, 0, 0, 0], 
           [0, 0, 0, 0, 0, 0]]


def ver(tablero):
    for i in range(len(tablero)):
      print(tablero[i])

# con respecto a la ficha de la jugada
def deshacer_arriba(tablero, x, y, xf, yf):
    for aux in range(xf, x):
        if aux == xf: 
          tablero[aux][y] = 0
        else: 
          tablero[aux][y] *= -1
    return tablero



def deshacer_abajo(tablero, x, y, xf, yf):
    for aux in range(x, xf+1):
        if aux == xf: 
          tablero[aux][y] = 0
        elif aux != x: 
          tablero[aux][y] *= -1
    return tablero



def deshacer_derecha(tablero, x, y, xf, yf):
    for aux in range(y, yf+1):
        if aux > y and aux < yf: 
          tablero[x][aux] *=-1
        elif aux == yf: 
          tablero[x][aux] = 0
    return tablero


def deshacer_izquierda(tablero, x, y, xf, yf):
  for aux in range(yf, y):
    if aux == yf: tablero[x][aux] = 0
    else: tablero[x][aux] *= -1
  return tablero

# 
# 4 1 - 3 2 - 2 3 - 1 4
def deshacer_diagonal_derecha_sup(tablero, x, y, xf, yf):
  for aux in range(xf, x):
   if x-aux == xf and y+aux == yf: tablero[x-aux][y+aux]=0
   else: tablero[x-aux][y+aux]*=-1
  return tablero

def deshacer_diagonal_izquierda_inf(tablero, x, y, xf, yf):
  for aux in range(x, xf):
   if x+aux == xf and y-aux == yf: tablero[x+aux][y-aux]=0
   else: tablero[x+aux][y-aux]*=-1
  return tablero


# 2 2 - 3 3 - 4 4 - 5 5 
def deshacer_diagonal_derecha_inf(tablero, x, y, xf, yf):
    try:
        if x == xf and y == yf: 
            tablero[x][y] = 0
            return tablero
        else:
            tablero[x+1][y+1] =-1
            tablero = deshacer_diagonal_derecha_inf(tablero, x+1, y+1, xf, yf)
        return tablero
    except: IndexError

def deshacer_diagonal_izquierda_sup(tablero, x, y, xf, yf):
  if x == xf and y == yf: 
    tablero[x][y] = 0
    return tablero
  else:
    tablero[x-1][y-1]=-1
    tablero = deshacer_diagonal_izquierda_sup(tablero, x-1, y-1, xf, yf)
  return tablero

deshacer_arriba(tablero, 3, 2, 1, 2)
deshacer_diagonal_derecha_inf(tablero, 3, 4, 1, 2)

ver(tablero)

#for i in range(0, 3):
    #print(i)
