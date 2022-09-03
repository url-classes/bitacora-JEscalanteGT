import random


class Reloj:
    def __init__(self):
        self.__horas = random.randint(0, 23)
        self.__minutos = random.randint(0, 59)
        self.__segundos = random.randint(0, 59)

    def definir_alarma(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def estandarizar(self, tiempo):
        if tiempo < 10:
            return f"0{tiempo}"
        else:
            return str(tiempo)

    @property
    def horas(self):
        return self.estandarizar(self.__horas)

    @horas.setter
    def horas(self, nueva_hora):
        if 0 <= nueva_hora <= 23:
            self.__horas = nueva_hora
        else:
            print('ERROR: La hora no está dentro de los límites')

    @property
    def minutos(self):
        return self.estandarizar(self.__minutos)

    @minutos.setter
    def minutos(self, nueva_hora):
        if 0 <= nueva_hora <= 59:
            self.__minutos = nueva_hora
        else:
            print('ERROR: La hora no está dentro de los límites')

    @property
    def segundos(self):
        return self.estandarizar(self.__segundos)

    @segundos.setter
    def segundos(self, nueva_hora):
        if 0 <= nueva_hora <= 59:
            self.__segundos = nueva_hora
        else:
            print('ERROR: La hora no está dentro de los límites')

    def __str__(self):
        return f"{self.horas}:{self.minutos}:{self.segundos}"
