from node import Node


class Stack:
    def __init__(self, max=-1):
        self.size = 0
        # Si max = -1 entonces el número de nodos es ilimitado
        # De lo contrario:
        # Por ejemplo si max = 5 (como máximo 5 nodos)
        # Por ejemplo si max = 15 (como máximo 15 nodos)
        self.max = max
        self.head = None

    def insert(self, data):
        if self.max == -1 or self.size < self.max:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
        else:
            raise OverflowError("Desbordamiento de pila")

    def delete(self):
        raise NotImplementedError

    def transversal(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError
