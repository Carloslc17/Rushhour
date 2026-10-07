from rushhour.model.vehicle import Vehicle

class Board:
    def __init__(self, vehiculos):
        self.__vehiculos = vehiculos   # Lista de vehiculos

    def get_vehiculos(self) -> list:
        return self.__vehiculos

    def buscar_vehiculo(self, letra) -> Vehicle:
        for v in self.__vehiculos:
            if letra == v.get_id():
                return v

    # Comprobar si la posicion de un vehiculo es valida
    def posicion_valida(self, vehiculo) -> bool:
        ocupadas = set()
        for v in self.__vehiculos:
            if v is not vehiculo:
                ocupadas.update(v.posiciones())

        # Comprobar si esta dentro del tablero y no se solapa con otro vehiculo
        for row, col in vehiculo.posiciones():
            if not (0 <= row < 6 and 0 <= col < 6):
                return False
            if (row, col) in ocupadas:
                return False
        return True

    # Mover vehiculo
    def mover(self, letra, distancia) -> bool:

        v = self.buscar_vehiculo(letra)
        if v == None:
            return False
        
        v.mover(distancia)
        if not self.posicion_valida(v):
            v.mover(-distancia)
            return False
        return True

    # Devuelve el tablero en formato lista doble
    def grid(self) -> list:

        tablero = [['o' for _ in range(6)] for _ in range(6)]

        for v in self.__vehiculos:
            for row, col in v.posiciones():
                tablero[row][col] = v.get_id()

        return tablero

        
    