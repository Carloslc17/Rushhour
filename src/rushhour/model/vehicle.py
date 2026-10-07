class Vehicle:

    def __init__(self, id, fila, columna, longitud, orientacion):
        self.__id = id
        self.__fila = fila                   # Primera fila del vehiculo
        self.__columna = columna             # Primera columna del vehiculo
        self.__longitud = longitud           # Longitud del vehiculo (Numero de casillas)
        self.__orientacion = orientacion     # Horizontal (H) o Vertical (V)

    def get_id(self):
        return self.__id

    def get_fila(self):
        return self.__fila

    def get_columna(self):
        return self.__columna

    def get_longitud(self):
        return self.__longitud

    def get_orientacion(self):
        return self.__orientacion

    def posiciones(self) -> list:

        posiciones = []

        if self.__orientacion == 'H':

            for i in range(self.__longitud):
                posicion = (self.__fila, self.__columna + i)
                posiciones.append(posicion)

        else:

            for i in range(self.__longitud):
                posicion = (self.__fila + i, self.__columna)
                posiciones.append(posicion)

        return posiciones

    def mover(self, distancia):
        if self.__orientacion == 'H':
            self.__columna += distancia
        elif self.__orientacion == 'V':
            self.__fila -= distancia     # Mover hacia arriba

    def __str__(self):
        return f"Vehiculo: {self.__id}, posicion inicial: {self.__fila,self.__columna}, longitud: {self.__longitud}, orientacion: {self.__orientacion}"
