# Comando verify

from rushhour.parsing import level_parser
from rushhour.model.vehicle import Vehicle
from rushhour.model.board import Board

def run(cadenaNivel) -> int:

    # 1. Tamano no 6x6
    if len(cadenaNivel) != 36:
        return 1

    # 2. Caracteres no validos
    for c in cadenaNivel:
        if c != 'o' and not ('A' <= c <= 'Z'):
            return 2

    # 3. No esta el vehiculo rojo
    if 'A' not in cadenaNivel:
        return 3

    Vehiculos = level_parser.crear_vehiculos(level_parser.string_to_board(cadenaNivel))
    Tablero = Board(Vehiculos)

    # 4. Vehiculo rojo no esta en fila de salida

    rojo = Tablero.buscar_vehiculo('A')

    if rojo.get_fila() != 2:
        return 4

    # 5. Vehiculo rojo no esta situado horizontalmente

    if rojo.get_orientacion() != 'H':
        return 5

    # 6. Vehiculos con longitud ilegal (Mayor que 3 o menor que 2)

    for vehiculo in Tablero.get_vehiculos():
        if vehiculo.get_longitud() < 2 or vehiculo.get_longitud() > 3:
            return 6

    # 7. Vehiculos duplicados (Misma letra)
    for vehiculo in Tablero.get_vehiculos():
        pass

    return 0

    


    