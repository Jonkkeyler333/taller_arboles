class Nodo:
  def __init__(self,element:any,parent=None) -> None:
    self.element=element
    self.parent=parent
    
class Arbol:
  def __init__(self,root:Nodo) -> None:
    self.root=root
    self.peso=0
    self.altura=0
    self.orden=0
  
  def add(self,element:any,parent=None) -> None:
    new_nodo=Nodo(element,parent)
    if self.peso==0:
      self.root=new_nodo
    else:
      pass