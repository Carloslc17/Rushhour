# Calcular heuristica

from rushhour.model.board import Board
from rushhour.parsing import level_parser

def calcular(cadenaNivel : str, h : int) -> int:

    SIZE = 6
    vehiculos = level_parser.crear_vehiculos(level_parser.string_to_board(cadenaNivel))
    tablero = Board(vehiculos)

    # Heuristica 0. Numero de casillas a la derecha del coche rojo (A)
    if h == 0:

        red = tablero.buscar_vehiculo('A')
        return 5 - red.posiciones()[-1][1]

    # Heuristica 1. Numero de vehiculos a la derecha del coche rojo (A)
    elif h == 1:

        grid = tablero.grid()
        red = tablero.buscar_vehiculo('A')
        row_red = red.posiciones()[0][0]
        col_red = red.posiciones()[-1][1]
        count = 0

        bloqueantes = set()
        for i in range(col_red+1, SIZE, 1):
            letra = grid[row_red][i]
            if letra != 'o' and letra not in bloqueantes:
                count += 1
                bloqueantes.add(letra)

        return count

    # Heurisitca 2. Suma de las heuristicas 0 y 1.
    elif h == 2:

        return calcular(cadenaNivel, 0) + calcular(cadenaNivel, 1)
