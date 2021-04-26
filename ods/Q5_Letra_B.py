"""Letra B -  Tabela hash de tamanho 7 e sem redimensionamento"""
from utils import new_array
from base import BaseSet


class Hash(BaseSet):
    def __init__(self):
        self._initialize()

    def _initialize(self):
        self.array = new_array(7) #recebe um array vazio de tamanho 7
        #print(self.array[0])
        
    def rehash(self, oldhash):
        return (oldhash+1)%7 #para procurar uma posição vazia caso inicial esteja ocupada, sondagem linear

    def func_hash(self, key): 
        return key%7 #posição inicial do valor

#insere por sondagem linear evitando colisões
    def insere(self, item): 
        pos=self.func_hash(item)
        if self.array[pos] == None: #se o local estiver vazio ele recebe a chave
            #print(item)
            self.array[pos] = item
        else: #se nao estiver vazio chama rehash para a prox casa
            nextpos=self.rehash(pos)
            while self.array[nextpos] != None:
                nextpos=self.rehash(nextpos)
            self.array[nextpos] = item
    
    def imprimir(self):
        print(self.array)
        for i in range(len(self.array)):
            print("Hash[%d] = " %i, end="")
            print(self.array[i])
        
        
# ---------->apenas para efeitos de testar a tabela hash<----------
"""
x = Hash()#([2341, 4234, 2839, 430, 22, 397, 3920])

x.insere(2341)
x.insere(4234)
x.insere(2839)
x.insere(430)
x.insere(22)
x.insere(397)
x.insere(3920)
x.imprimir()
"""