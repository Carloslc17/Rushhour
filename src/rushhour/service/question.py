# Comando question

from rushhour.parsing import level_parser
from rushhour.model.vehicle import Vehicle
from rushhour.model.board import Board
from rushhour.parsing.errors import InvalidLevelError


def run(cadenaNivel, quest, arg):

    grid = level_parser.string_to_board(cadenaNivel)
    vehiculos = level_parser.crear_vehiculos(grid)
    tablero = Board(vehiculos)

    match quest:
        case "--whereis":
            vehiculo = tablero.buscar_vehiculo(arg)
            return vehiculo.posiciones()

        case "--what":
            if not (0 <= arg[0] < 6 and 0 <= arg[1] < 6):
                raise InvalidLevelError("Posicion fuera del tablero")
            return (grid[arg[0]][arg[1]])

        case "--size":
            vehiculo = tablero.buscar_vehiculo(arg)
            return vehiculo.get_longitud()

        case "--howmany":
            cantidad = len(tablero.get_vehiculos())
            return cantidad

        case "--goal":
            if grid[2][5] == 'A':
                return True
            else:
                return False

        case _:
            raise InvalidLevelError("Pregunta no valida")

            
