from gato import Gato
from perro import Perro
from animal import Animal


# True - Masculino
# False - Femenino
mascota1 = Gato('Gardfield', True, 3, 25.5, "Gris", False)
mascota2 = Perro('Bruno', True, 2, 50, "Blanco", "Jorge")
mascota3 = Gato('Misha', False, 1, 10, "Negro", True)
mascota4 = Perro('Laika', False, 0, 20, "Café", "Jorge")

animales: list[Animal] = []
animales.append(mascota1)
animales.append(mascota2)
animales.append(mascota3)
animales.append(mascota4)

for animal in animales:
    animal.emitir_sonido()
