from conjunto import Conjunto

a = Conjunto()
b = Conjunto()

a.modificar()
b.modificar()

print(a.mostrar())
print(b.mostrar())

c = a.unir(b)
print(c.mostrar())
