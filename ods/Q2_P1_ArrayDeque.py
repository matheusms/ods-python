"""questao 2 - ArrayDeque utilizando k mod length(a) = k & (length(a)-1)"""

"""2. [2 pontos] Modique a implementac~ao ArrayDeque para que ele n~ao use o operador mod (que
tem alto custo em alguns sistemas). Em vez disso, deve fazer uso do fato de que, se length(a) e
uma pot^encia de 2, ent~ao"""

from utils import new_array
from base import BaseList

class ArrayDeque(BaseList):
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)

    def _initialize(self):
        self.a = new_array(1)
        self.j = 0
        self.n = 0

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.a[(i+self.j)&len(self.a)-1]

    def set(self, i, x):
        if i < 0 or i >= self.n: raise IndexError()
        y = self.a[(i+self.j)&len(self.a)-1]
        self.a[(i+self.j)&len(self.a)-1] = x
        return y

    def add(self, i, x): 
        if i < 0 or i > self.n: raise IndexError()
        if self.n == len(self.a): self._resize()
        if i < self.n/2:
            self.j = (self.j-1) & len(self.a) -1
            #print("self j: ", self.j)
            for k in range(i):
                self.a[(self.j+k)&len(self.a)-1] = self.a[(self.j+k+1)&len(self.a)-1]
                
        else:
            for k in range(self.n, i, -1):
                #print("self j: ", self.j)
                self.a[(self.j+k)&len(self.a)-1] = self.a[(self.j+k-1)&len(self.a)-1]
                
        self.a[(self.j+i)&len(self.a)-1] = x
        self.n += 1

    def remove(self, i): 
        if i < 0 or i >= self.n: raise IndexError()
        x = self.a[(self.j+i)&len(self.a)-1]
        if i < self.n / 2:
            for k in range(i, 0, -1):
                self.a[(self.j+k)&len(self.a)-1] = self.a[(self.j+k-1)&len(self.a)-1]
            self.j = (self.j+1) & len(self.a) -1
        else:
            for k in range(i, self.n-1): 
                self.a[(self.j+k)&len(self.a)-1] = self.a[(self.j+k+1)&len(self.a)-1]
        self.n -= 1
        if len(self.a) >= 3*self.n: self._resize()
        return x
  
    def _resize(self):
        b = new_array(max(1, 2*self.n))
        #print("B: ", b)
        for k in range(self.n):
            #print("k: ", k)
            b[k] = self.a[(self.j+k)&len(self.a)-1]
            
            #print("b[k]: ", b[k])
        self.a = b
        #print("Self a depois: ", self.a)
        self.j = 0
    

# ---------->apenas para efeitos de testar a tabela hash<----------
x = ArrayDeque()
x.add(0, 1)
#print(x)
x.add(1, 2)
#print(x)
x.add(2, 3)
#print(x)
x.add(3, 4)
#print(x)
x.add(4, 5)
print(x)