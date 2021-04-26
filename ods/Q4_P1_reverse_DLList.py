"""questão 4 P1<----------"""
from base import BaseList

class DLList(BaseList):
    
    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None
            self.prev = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):
        self.n = 0
        self.dummy = DLList.Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def get_node(self, i):
        if i < self.n/2:
            p = self.dummy.next    
            for _ in range(i): 
                p = p.next
        else:
            p = self.dummy
            for _ in range(self.n, i, -1): 
                p = p.prev
        return p

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.get_node(i).x

    def set(self, i, x): #@ReservedAssignment
        if i < 0 or i >= self.n: raise IndexError()
        u = self.get_node(i)
        y = u.x
        u.x = x
        return y

    def _remove(self, w):
        w.prev.next = w.next
        w.next.prev = w.prev
        self.n -= 1    

    def remove(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        self._remove(self.get_node(i))

    def add_before(self, w, x):
        u = DLList.Node(x)
        u.prev = w.prev
        u.next = w
        u.next.prev = u
        u.prev.next = u
        self.n += 1
        return u

    def add(self, i, x):
        if i < 0 or i > self.n:    raise IndexError()
        self.add_before(self.get_node(i), x)

    def __iter__(self):
        u = self.dummy.next
        while u != self.dummy:
            yield u.x
            u = u.next

#4. [2 pontos] Escreva um metodo, reverse(), que inverta a ordem dos elementos em uma DLList.


    def reverse(self):
        temp = None
        current = self.dummy.next #posição inicial
        for i in range(self.n):
            temp = current.next #salva a prox posição
            current.next = current.prev #inverte as direções
            current.prev = temp #coloca o que seria o proximo como anterior
            current = current.prev #salva a nova posição atual
        temp = self.dummy.next
        self.dummy.next = self.dummy.prev
        self.dummy.prev = temp


# ---------->apenas para efeitos de testar a tabela hash<----------
"""
a = DLList()
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)

print(a)

a.reverse()

print(a)

"""