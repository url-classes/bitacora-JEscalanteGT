class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


a = Persona("Eduardo", 17)
b = Persona("René", 18)
c = Persona("Iris", 18)

d = a
e = c

print(a.nombre)
print(c.edad)

d.nombre = "José"
e.edad = 20

print(a.nombre)
print(c.edad)
