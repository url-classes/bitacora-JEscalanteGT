class Gato:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edad = 0
        self.salud = 20
        self.energia = 50

    def respirar(self):
        if self.energia > 0:
            self.energia -= 1
        else:
            if self.salud <= 0:
                print("Estoy murido x_x")
            else:
                self.salud -= 2

    def saludar(self):
        if self.energia >= 3:
            self.energia -= 3
            print('Meoooow')

    def __str__(self):
        return f"Mi mascota es: {self.nombre}"
