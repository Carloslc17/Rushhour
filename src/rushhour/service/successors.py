# Comando successors

from rushhour.parsing import level_parser
from rushhour.model.vehicle import Vehicle
from rushhour.model.board import Board

def run(cadenaNivel) -> list:

    SIZE = 6

    vehiculos = level_parser.crear_vehiculos(level_parser.string_to_board(cadenaNivel))
    tablero = Board(vehiculos)
    successors = []

    for vehiculo in tablero.get_vehiculos():
        for distancia in range(1,SIZE):
            if tablero.mover(vehiculo.get_id(), distancia):
                movimiento = f"{vehiculo.get_id()}+{distancia}"
                sucessor = (movimiento, level_parser.board_to_string(tablero.grid()), SIZE - distancia)
                successors.append(sucessor)
                tablero.mover(vehiculo.get_id(), -distancia) # Revertir movimiento
            else: 
                break

        for distancia in range(1,SIZE):
            if tablero.mover(vehiculo.get_id(), -distancia):
                movimiento = f"{vehiculo.get_id()}-{distancia}"
                sucessor = (movimiento, level_parser.board_to_string(tablero.grid()), SIZE - distancia)
                successors.append(sucessor)
                tablero.mover(vehiculo.get_id(), distancia) # Revertir movimiento
            else:
                break

    successors.sort()
    return successors




