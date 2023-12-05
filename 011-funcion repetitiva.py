# 3 en raya
# por Vicente Carratalá
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
    global casilla11,casilla12,casilla13
    global casilla21,casilla22,casilla23
    global casilla31,casilla32,casilla33
    fila = input("introduce la fila para el jugador 1 (1-3) (X)")
    print("La fila que has escogido es: "+fila)

    columna = input("introduce la columna para el jugador 1 (1-3) (X)")
    print("La columna que has escogido es: "+columna)

    if int(fila) == 1 and int(columna) == 1:
        casilla11 = "X"
    elif int(fila) == 1 and int(columna) == 2:
        casilla12 = "X"
    elif int(fila) == 1 and int(columna) == 3:
        casilla13 = "X"
    elif int(fila) == 2 and int(columna) == 1:
        casilla21 = "X"
    elif int(fila) == 2 and int(columna) == 2:
        casilla22 = "X"
    elif int(fila) == 2 and int(columna) == 3:
        casilla23 = "X"
    elif int(fila) == 3 and int(columna) == 1:
        casilla31 = "X"
    elif int(fila) == 3 and int(columna) == 2:
        casilla32 = "X"
    elif int(fila) == 3 and int(columna) == 3:
        casilla33 = "X"

    pintaTablero()
    turno()
    
turno()
