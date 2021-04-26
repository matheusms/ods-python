""" questão 3 P1 <--------
"""
from arraystack import ArrayStack

class Pilha(ArrayStack):
  def push(self, x):
    self.add_last(x)
  
  def pop(self):
    return self.remove_last()

  # 3. [1 ponto] Implemente uma func~ao transferir(A, B) que transra os elementos da pilha A para
  #a pilha B, de tal modo que o elemento no topo de A seja o primeiro a ser inserido em B e oelemento na base de A seja o topo de B.

  def transferir(self, A, B): #transferir itens de A para B de forma que A entre invertido em B
    for i in range(len(A)):
      B.push(A.pop())
    print("Nova pilha B: -> ultimo item ", B, "<- primeiro item")
    
# ---------->apenas para efeitos de testar a tabela hash<----------

"""
A = Pilha()
B = Pilha()
A.push(6)
A.push(5)
A.push(1)
B.push(4)
B.push(3)


print("Pilha A: ", A)
print("Pilha B: ", B)


A.transferir(A, B) #chamando a função transferir

#apenas testanto se é FIFO
print("Removido: ", B.pop())
print("Removido: ", B.pop())


print("Nova pilha B: -> ultimo item ", B, "<- primeiro item")

"""