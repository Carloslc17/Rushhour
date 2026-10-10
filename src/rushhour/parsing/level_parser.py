from rushhour.model.vehicle import Vehicle
from rushhour.model.board import Board

SIZE = 6

def string_to_board(cadenaNivel) -> list[list[int]]:

    Tablero = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

    for i in range(SIZE * SIZE):
        Tablero[i // SIZE][i % SIZE] = cadenaNivel[i]

    return Tablero

def board_to_string(tablero):

    cadenaNivel = ""
    for i in range(SIZE):
        for j in range(SIZE):
            cadenaNivel += tablero[i][j]

    return cadenaNivel
    


def crear_vehiculos(tablero) -> list:
    Vehiculos = []

    for i in range(0, SIZE, 1):
        for j in range(0, SIZE, 1):

            letra = tablero[i][j]

            if letra == 'o':
                continue

            # Comprobar si el vehiculo ya esta creado
            existe = False
            for v in Vehiculos:
                if letra == v.get_id():
                    existe = True
                    break

            if existe: 
                continue

            # Determinar longitud y orientacion

            if j+1 < SIZE and tablero[i][j+1] == letra:
                orientacion = 'H'
                longitud = 0
                k = j

                while k < SIZE and tablero[i][k] == letra:
                    longitud += 1
                    k +=1

            else:
                orientacion = 'V'
                longitud = 0
                k = i

                while k < SIZE and tablero[k][j] == letra:
                    longitud += 1
                    k += 1

            Vehiculos.append(Vehicle(letra, i, j, longitud, orientacion))

    return Vehiculos
        


            
