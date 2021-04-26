from pilha import Pilha
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

#testanto se é FIFO
print("Removido: ", B.pop())
print("Removido: ", B.pop())


print("Nova pilha B: -> ultimo item ", B, "<- primeiro item")