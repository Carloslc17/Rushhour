from vehicle import Vehicle

class Board:
    def __init__(self, vehiculos):
        self.vehiculos = vehiculos   # Lista de vehiculos

    def posicion_valida(self, vehiculo):
        ocupadas = set()
        for c in self.vehiculos:
            if c is not vehiculo:
                ocupadas.update(c.posiciones())

        # Comprobar si esta dentro del tablero y no se solapa con otro vehiculo
        for row, col in vehiculo.posiciones():
            if not (0 <= row < 6 and 0 <= c < 6):
                return False
            if (row, col) in ocupadas:
                return False
        return True


    def mover(self, letra, distancia):

        for v in self.vehiculos:
            if v.id == letra:
                v.mover(distancia)
                if not self.posicion_valida():
                    v.mover(-distancia)
                    return False
                return True
        return False

    