from stack import Stack

pila_numeros = Stack()
print(pila_numeros.size)

pila_numeros.insert(7)
print(pila_numeros.size)

pila_numeros.insert(11)
pila_numeros.insert(14)

pila_numeros.insert(102)
pila_numeros.insert(23)
pila_numeros.insert(50)
pila_numeros.insert(37)

print('Tamaño actual:', pila_numeros.size)
print('Máximo de nodos:', pila_numeros.max)
