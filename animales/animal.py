import abc


class Animal:
    def __init__(self, nombre, genero, edad, peso, color):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.peso = peso
        self.color = color

    def respirar(self):
        print(f"{self.nombre}: Estoy respirando...")

    def correr(self):
        print(f"{self.nombre}: ¡Estoy corriendo!")

    def comer(self):
        print(f"{self.nombre}: Estoy comiendo :)")

    def dormir(self):
        print(f"{self.nombre}: Estoy durmiendo... zzZzz")

    @abc.abstractmethod
    def emitir_sonido(self):
        pass
