"""A basic binary tree implementation"""

from arrayqueue import ArrayQueue

class BinaryTree(object):
    class Node(object):
        def __init__(self):
            self.left = self.right = self.parent = None

    def __init__(self):
        super(BinaryTree, self).__init__()
        self.nil = None
        self.r = None #marcação da raiz
        self.initialize()
        
    def initialize(self):
        self.r = None
        
    def depth(self, u): #calcular a profundidade do nó
        d = 0
        while (u != self.r): #enquanto o nó nao for a raiz ele vai subindo
            u = u.parent #nó pai
            d += 1
        return d
    
    def size(self):
        return self._size(self.r)
    
    def _size(self, u): #calcular o numero de nós  da arvore
        if u == self.nil: #soma o tamnho das arvores menores, da esquerda e da direita
            return 0
        return 1 + self._size(u.left) + self._size(u.right) #fica chamando _size recursivamente para a esquerda e a direita
        #o numero é 1 mais o item da frente, e assim sucessivamente
    
    def size2(self): #tamanho da arvore sem recursão -> mais complexo <-
        u = self.r
        prv = self.nil
        n = 0
        while u != self.nil:
            if prv == u.parent:
                n += 1
                if u.left != self.nil: 
                    nxt = u.left
                elif u.right != self.nil: 
                    nxt = u.right
                else: nxt = u.parent
            elif prv == u.left:
                if u.right != self.nil: 
                    nxt = u.right
                else: nxt = u.parent
            else:
                nxt = u.parent
            prv = u
            u = nxt
        return n 
    
    def height(self):
        return self._height(self.r)
    
    def _height(self, u):
        if u == self.nil: return -1 
        return 1 + max(self._height(u.left), self._height(u.right))
    
    def traverse(self, u): #processar a informação de cada nó, percorre a arvore inteira recursivamente
        if u == self.nil: 
            return
        self.traverse(u.left)
        self.traverse(u.right)
        
    def traverse2(self): #processa a arvore sem recursão -> mais complexo <-
        u = self.r
        prv = self.nil
        while u != self.nil:
            if prv == u.parent:
                if u.left != self.nil: 
                    nxt = u.left
                elif u.right != self.nil: 
                    nxt = u.right
                else: 
                    nxt = u.parent
            elif prv == u.left:
                if u.right != self.nil: nxt = u.right
                else: nxt = u.parent
            else:
                nxt = u.parent
            prv = u
            u = nxt

    def bf_traverse(self):
        q = ArrayQueue()
        if self.r != self.nil: 
            q.add(self.r)
        while q.size() > 0:
            u = q.remove()
            if u.left != self.nil: 
                q.add(u.left)
            if u.right != self.nil: 
                q.add(u.right)
        return q
            
    def first_node(self):
        """Find the first node in an in-order traversal"""
        w = self.r
        if w == self.nil: 
            return self.nil
        while w.left != self.nil:
            w = w.left
        return w
    
    def next_node(self, w):
        """Find the node that follows w in an in-order traversal"""
        if w.right != self.nil:
            w = w.right
            while w.left != self.nil:
                w = w.left
        else:
            while w.parent != self.nil and w.parent.left != w:
                w = w.parent
            w = w.parent
        return w

        
    