'''
An array-based list implementation with O(1+n-i) amortized update time.

Stores the list in an array, a, so that the i'th list item is stored
at a[(j+i)%len(a)].

Uses a doubling strategy for resizing a when it becomes full or too empty.
'''
from utils import new_array

from base import BaseList

class ArrayStack(BaseList):
    def __init__(self, iterable=[]):
        self._initialize()
        self.add_all(iterable)
        
    def _initialize(self):
        self.a = new_array(1)
        self.n = 0

    def get(self, i):
        if i < 0 or i >= self.n: raise IndexError()
        return self.a[i]

    def set(self, i, x):
        if i < 0 or i >= self.n: raise IndexError()
        y = self.a[i]
        self.a[i] = x
        return y

    def add(self, i, x): 
        if i < 0 or i > self.n: 
            raise IndexError()
        if self.n == len(self.a): self._resize()
        self.a[i+1:self.n+1] = self.a[i:self.n]
        self.a[i] = x
        self.n += 1

    def remove(self, i): 
        if i < 0 or i >= self.n: 
            raise IndexError()
        x = self.a[i]
        self.a[i:self.n-1] = self.a[i+1:self.n]
        self.n -= 1
        if len(self.a) >= 3*self.n: 
            self._resize()
        return x
  
    def _resize(self):
        b = new_array(max(1, 2*self.n))
        b[0:self.n] = self.a[0:self.n]
        self.a = b

    '''1- O método de Lista add_all(i,c) insere todos os elementos de uma coleção c na posição i da lista. 
    (O método add(i,x) é um caso especial onde c=x.) Explique por que, para as estruturas desta aula, 
    não seria eficiente implementar add_all(i,c) com chamadas repetidas a add(i,x). Projete e implemente uma forma mais eficiente.'''
    
    def add_all(self, i, c=[]): #adiciona c a partir da posição i, deslocando os outros itens
        if type(i) == int:
            if i < 0 or i > self.n: 
                raise IndexError()
            tam = len(c) #guardando o tamanho de c
            if self.n + tam > len(self.a): #verifica o tamanho de n é maior que o vetor alocado
                self._resize_all(tam) #modificar resize pois se colocar muitos itens ele não suporta
            self.a[i+ tam :self.n + tam] = self.a[i:self.n] #aloca os itens na posição i + tam
            self.a[i : i + tam] = c[0:]
            self.n += tam
        else:
            for x in i:
                self.append(x)
        
    def _resize_all(self, i):
        b = new_array(max(1, max(2 * self.n, self.n + i)))
        b[0 : self.n] = self.a[0 : self.n]
        self.a = b


