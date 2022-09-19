from animal import Animal


class Gato(Animal):
    def __init__(self, nombre, genero, edad, peso, color, es_amistoso):
        super().__init__(nombre, genero, edad, peso, color)
        self.es_amistoso = es_amistoso

    def emitir_sonido(self):
        print(f"{self.nombre}: Meooow")
