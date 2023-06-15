class Nodo:
  def __init__(self,element:any,parent=None) -> None:
    self.element=element
    self.parent=parent
    self.children=[]
  
  def add_children(self,element):
    self.children.append(element)
    
class Arbol:
  def __init__(self,root:Nodo) -> None:
    self.root=root
    self.peso=0
    self.altura=0
    self.orden=0
  
  def buscar_nodo(self, nodo_actual:Nodo,element:any):
    if nodo_actual.elemento == element:
      return nodo_actual
    for hijo in nodo_actual.children:
      nodo_encontrado = self.buscar_nodo(hijo,element)
      if nodo_encontrado:
        return nodo_encontrado
    return None
  
  def add(self,element:any,parent=None) -> None:
    new_nodo=Nodo(element,parent)
    if self.peso==0:
      self.root=new_nodo
    else:
      parent_nodo=self.buscar_nodo(new_nodo,parent)
      if parent_nodo:
        parent_nodo.add_children(new_nodo)
      else:
        raise 'No se ha encontrado el nodo padre'

if __name__=='__main__':
  ##Some class test