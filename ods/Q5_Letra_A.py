"""Letra A -  Tabela hash de tamanho 7 e sem redimensionamento"""
from utils import new_array
from base import BaseSet
from arraystack import ArrayStack


class Hash(BaseSet):
    def __init__(self):
        self._initialize()
        

    def _initialize(self):
        self.array = new_array(7) #recebe um array vazio de tamanho 7
        self.n=0 #numero de itens alocados na lista
        #self.hash_table = new_array(1)
        #print(self.array[0])

    def func_hash(self, key): 
        return key%7 #posição inicial do valor
    
    

    def insere(self, item): 
        pos = self.func_hash(item)
        if self.array[pos] == None: #adiciona o item se estiver vazio na posição
            self.array[pos] = item
        
        else:
            a = []   #cria uma lista para adicionar na posição que houver colisão
            a.append(self.array[pos]) #a lista recebe os valores ja alocados
            a.append(item) #adicionando o novo item que ocorreu colisão
            self.array[pos] = a #colocando a lista na posição que houve a colisão
            
    
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