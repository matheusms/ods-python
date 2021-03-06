"""An implementation of a binary search tree"""
from arraydeque import ArrayDeque
from arrayqueue import ArrayQueue
from binarytree import BinaryTree
from base import BaseSet

class BinarySearchTree(BinaryTree,BaseSet):
    """Base classs for all our binary search trees"""
    
    class Node(BinaryTree.Node):
        def __init__(self, x):
            super(BinarySearchTree.Node, self).__init__()
            self.x = x
            
    def _new_node(self, x):
        u = BinarySearchTree.Node(x)
        u.left = u.right = u.parent = self.nil
        return u
        
    def __init__(self, iterable=[], nil=None):
        super(BinarySearchTree, self).__init__()
        self._initialize()
        self.nil = nil
        self.add_all(iterable)
        
    def _initialize(self):
        self.n = 0
        
    def clear(self):
        self.r = self.nil
        self.n = 0
        
    def _find_last(self, x):
        w = self.r
        prev = self.nil
        while w is not self.nil: 
            prev = w
            if (x < w.x):
                w = w.left
            elif (x > w.x):
                w = w.right
            else:
                return w
        return prev
        
    def _add_child(self, p, u):
        if p == self.nil:
            self.r = u # inserting into empty tree
        else:
            if u.x < p.x:
                p.left = u
            elif u.x > p.x:
                p.right = u
            else:
                return False # u.x is already in the tree
            u.parent = p
        self.n += 1
        return True  

    def find_eq(self, x):
        w = self.r
        while w != self.nil:
            if x < w.x:
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.x
        return None
    
    def find(self, x):
        w = self.r
        z = self.nil
        while w != self.nil:
            if x < w.x:
                z = w
                w = w.left
            elif x > w.x:
                w = w.right
            else:
                return w.x
        if z == self.nil: return None 
        return z.x
        
    def add(self, x):
        p = self._find_last(x)
        return self._add_child(p, self._new_node(x))
        
    def add_node(self, u):
        p = self._find_last(u.x)
        return self._add_child(p, u)
    
    def splice(self, u):
        if u.left != self.nil:
            s = u.left
        else:
            s = u.right
        if u == self.r:
            self.r = s
            p = self.nil
        else:
            p = u.parent
            if p.left == u:
                p.left = s
            else:
                p.right = s 
        if s != self.nil: 
            s.parent = p
        self.n -= 1

    def _remove_node(self, u):
        if u.left == self.nil or u.right == self.nil:
            self.splice(u)
        else: 
            w = u.right
            while w.left != self.nil: 
                    w = w.left
            u.x = w.x
            self.splice(w)

    def remove(self, x):
        u = self._find_last(x)
        if u != self.nil and x == u.x:
            self._remove_node(u)
            return True
        return False
    
    def rotate_left(self, u):
        w = u.right
        w.parent = u.parent
        if w.parent != self.nil:
            if w.parent.left == u:
                w.parent.left = w
            else:
                w.parent.right = w
        u.right = w.left
        if u.right != self.nil:
            u.right.parent = u
        u.parent = w
        w.left = u
        if u == self.r: 
            self.r = w
            self.r.parent = self.nil
            
    def rotate_right(self, u):
        w = u.left
        w.parent = u.parent
        if w.parent != self.nil:
            if w.parent.left == u:
                w.parent.left = w
            else:
                w.parent.right = w
        u.left = w.right
        if u.left != self.nil:
            u.left.parent = u
        u.parent = w
        w.right = u
        if u == self.r:
            self.r = w
            self.r.parent = self.nil
                    
    def __iter__(self):
        u = self.first_node()
        while u != self.nil:
            yield u.x
            u = self.next_node(u)

# --------> Constru????o N??O recursiva de travessas exerc??cio 2

    def prox_preOrdem(self): #arvore da esquerda -> depois da direita
        u = self.r
        prv = self.nil
        a = ArrayDeque()
        while u != self.nil:
            if prv == u.parent: #u pai (anterior) 
                #salva a ordem do n??
                #salvar cada n?? e o seu pai, depois ir removendo as folhas
                #pensar em como fazer isso
                if u.left != None:
                    nxt = u.left
                elif u.right != None:
                    nxt = u.right
                else:
                    nxt = u.parent
            elif prv == u.left:
                if u.right != None:
                    nxt = u.right
                else:
                    nxt = u.parent
            else:
                nxt = u.parent
            prv = u
            u = nxt
            if u.left == None:
                a.append(u.x)
        print(a)


            
        
    

# para aplica????o das travessias usar essa fun????o abaixo

    def atravessar(self):
        #print("Em ordem: ")
        #self.numero_emOrdem(self.r)
        #print("\n")
        print("Em pr??-ordem: ")
        self.prox_preOrdem()
        #print("\n")
        #print("Em pr??s-ordem: ")
        #self.numero_posOrdem(self.r)

            
