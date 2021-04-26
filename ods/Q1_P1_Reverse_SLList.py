"""questão 1 - SLList"""
from base import BaseList

class SLList(BaseList):
    
    class Node(object):
        def __init__(self, x):
            self.x = x
            self.next = None

    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):
        self.n = 0
        self.head = None
        self.tail = None

    def new_node(self, x):
        return SLList.Node(x)

    def _add(self,x):
        u = self.new_node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1
        return True

    def push(self,x):
        u = self.new_node(x)
        u.next = self.head
        self.head = u
        if self.n == 0:
            self.tail = u
        self.n += 1
        return x

    def append(self, x):
        u = self.new_node(x)
        if self.n == 0:
            self.head = u
        else:
            self.tail.next = u
        self.tail = u
        self.n += 1
        return True

    def get_node(self, i):
        u = self.head
        for _ in range(i):
            u = u.next
        return u
    
    def get(self, i):
        if i < 0 or i > self.n-1: 
            raise IndexError()
        return self.get_node(i).x

    def set(self, i, x):
        if i < 0 or i > self.n-1: 
            raise IndexError()
        u = self.get_node(i)
        y, u.x = u.x, x
        return y
        
    def add(self, i, x):
        if i < 0 or i > self.n: 
            raise IndexError()
        if i == 0: 
            self.push(x) 
            return True
        u = self.head
        for _ in range(i-1):
            u = u.next
        w = self.new_node(x)
        w.next = u.next
        u.next = w
        self.n += 1
        return True
    
    def remove(self, i):
        if i < 0 or i > self.n-1: 
            raise IndexError()
        if i == 0: 
            return self.pop()
        u = self.head
        for _ in range(i-1):
            u = u.next
        w = u.next
        u.next = u.next.next
        self.n -= 1
        return w.x
        
    def pop(self):
        if self.n == 0: 
            return None
        x = self.head.x
        self.head = self.head.next
        self.n -= 1
        if self.n == 0:
            self.tail = None
        return x

    def _remove(self):
        return self.pop()

    def __str__(self):
        s = "["
        u = self.head
        while u is not None:
            s += "%r" % u.x
            u = u.next
            if u is not None:
                s += ","
        return s + "]"

    def __len__(self):
        return self.size()

#1. [2 pontos] Projete e implemente um metodo para a SLList, reverse() que inverte a ordem dos
#elementos em SLList. Este metodo deve ser executado em tempo O(n), n~ao deve usar recurs~ao,
#n~ao deve usar nenhuma estrutura de dados secundaria e n~ao deve criar novos nos.

    def reverse(self):
        prev = None #aponta para o item anterior, vazio no caso do inicio da lista
        current = self.head #aponta para a cabeça, posição atual
        
        while (current is not None):
            next = current.next #define o prox nodo
            current.next = prev #prox nodo recebe o anterior
            prev = current #item anterios salva o valor do item atual, passando para o prox
            current = next #atual vai para o prov
        self.head = prev #altera a cabeça item anterior, que nesse caso é o ultimo item

'''a função executa na lista toda e efetua a troca das variaveis, invertendo suas indicações, o que apontava para o prox nodo agora
aponta para o noto anterior, fazendo assim invertendo todas as  direções dos nodos '''

# ---------->apenas para efeitos de testar a tabela hash<----------
"""
a = SLList() #lista para teste
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)
a.append(7)

print(a) #verificando a lista

a.reverse()    

print(a) #nova lista reversa da outra

"""
