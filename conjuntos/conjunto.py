import random


class Conjunto:
    def __init__(self):
        self.__elementos = []

    def agregar(self, n):
        self.__elementos.append(n)

    def obtener_elementos(self):
        return self.__elementos

    def mostrar(self):
        resultado = ''
        for elemento in self.__elementos:
            resultado += f"{elemento}, "

        return resultado

    def modificar(self):
        self.__elementos = []
        numeros = random.randint(1, 10)
        for i in range(0, numeros):
            n = random.randint(1, 100)
            self.__elementos.append(n)

    def unir(self, b):
        c = Conjunto()
        # Recorrer elementos de conjunto A
        for elemento in self.__elementos:
            c.agregar(elemento)

        # Recorrer elementos de conjunto B
        for elemento in b.obtener_elementos():
            c.agregar(elemento)

        return c
