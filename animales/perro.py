from animal import Animal


class Perro(Animal):
    def emitir_sonido(self):
        print(f"{self.nombre}: Guaf")

    def __init__(self, nombre, genero, edad, peso, color, mejor_amigo):
        super().__init__(nombre, genero, edad, peso, color)
        self.mejor_amigo = mejor_amigo
