from arraystack import ArrayStack

class Pilha(ArrayStack):
  def push(self, x):
    self.add_last(x)
  
  def pop(self):
    return self.remove_last()