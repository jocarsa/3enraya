# 3 en raya
# por Vicente Carratalá

import os

casilla11 = casilla12 = casilla13 = ' '
casilla21 = casilla22 = casilla23 = ' '
casilla31 = casilla32 = casilla33 = ' '

def pintaTablero(): 
    print(casilla11+'|'+casilla12+'|'+casilla13)
    print('-+-+-')
    print(casilla21+'|'+casilla22+'|'+casilla23)
    print('-+-+-')
    print(casilla31+'|'+casilla32+'|'+casilla33)

jugador = 1
def turno():
    global jugador
    global casilla11,casilla12,casilla13
    global casilla21,casilla22,casilla23
    global casilla31,casilla32,casilla33

    if jugador == 1:
        jugador = 2
        ficha = "O"
    else:
        jugador = 1
        ficha = "X"
    
    fila = input("introduce la fila para el jugador "+str(jugador)+" (1-3) ("+str(ficha)+")")
    print("La fila que has escogido es: "+fila)

    columna = input("introduce la columna para el jugador "+str(jugador)+" (1-3) ("+str(ficha)+")"
    print("La columna que has escogido es: "+columna)  

    if int(fila) == 1 and int(columna) == 1:
        casilla11 = ficha
    elif int(fila) == 1 and int(columna) == 2:
        casilla12 = ficha
    elif int(fila) == 1 and int(columna) == 3:
        casilla13 = ficha
    elif int(fila) == 2 and int(columna) == 1:
        casilla21 = ficha
    elif int(fila) == 2 and int(columna) == 2:
        casilla22 = ficha
    elif int(fila) == 2 and int(columna) == 3:
        casilla23 = ficha
    elif int(fila) == 3 and int(columna) == 1:
        casilla31 = ficha
    elif int(fila) == 3 and int(columna) == 2:
        casilla32 = ficha
    elif int(fila) == 3 and int(columna) == 3:
        casilla33 = ficha

    os.system("clear")

    pintaTablero()
    turno()
    
turno()
