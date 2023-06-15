class Nodo:
  def __init__(self,element:any,parent=None) -> None:
    self.element=element
    self.parent=parent
    self.children=[]
  
  def add_children(self,element):
    self.children.append(element)
    
class Arbol:
  def __init__(self,root=None) -> None:
    self.root=root
    self.peso=0
    self.altura=0
    self.orden=0
  
  def search_nodo(self,nodo_actual:Nodo,parent:any):
    if nodo_actual.element == parent:
      return nodo_actual
    for hijo in nodo_actual.children:
      nodo_encontrado = self.search_nodo(hijo,parent)
      if nodo_encontrado:
        return nodo_encontrado
    return None
  
  def add(self,element:any,parent=None) -> None:
    new_nodo=Nodo(element,parent)
    if self.peso==0:
      self.root=new_nodo
      self.peso+=1
    else:
      parent_nodo=self.search_nodo(self.root,parent)
      if parent_nodo is not None:
        new_nodo.parent=parent_nodo
        parent_nodo.add_children(new_nodo)
        self.peso+=1
      else:
        raise 'No se ha encontrado el nodo padre'
      
  def devolver(self) -> None:
    print(self.root.element)
    

if __name__=='__main__':
  ##some class test
  a=Arbol()
  a.add(20)
  print(a.root.element)
  a.add(30,20)
  a.add(10,20)
  hijo=a.root.children
  print(f'los hijos de la raiz del arbol {a.root.element} son :')
  for ele in hijo:
    print(ele.element)
  # a.add(10,20)
  # a.add(40,20)
  # a.devolver()