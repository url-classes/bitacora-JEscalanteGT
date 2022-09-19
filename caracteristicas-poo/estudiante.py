class Estudiante:
    def __init__(self, nombre, carnet, edad):
        self.__nombre = nombre
        self.__carnet = carnet
        self.__edad = edad

    def saludar(self):
        print(f"Hola soy {self.__nombre} y mi carnet es {self.__carnet}")
