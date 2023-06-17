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
  
  def search_nodo(self,nodo_actual:Nodo,parent:any)->Nodo:
    """Este método busca si existe el padre de un nodo

    :param nodo_actual: nodo al que se quiere agregar al arbol
    :type nodo_actual: Nodo
    :param parent: supuesto padre del nodo
    :type parent: any
    :return: Si encuentra el nodo padre lo returna , de lo contrario retorna None
    :rtype: Nodo
    """
    if nodo_actual.element == parent:
      return nodo_actual
    for hijo in nodo_actual.children:
      nodo_encontrado = self.search_nodo(hijo,parent)
      if nodo_encontrado:
        return nodo_encontrado
    return None
  
  def add(self,element:any,parent=None) -> None:
    """Este método agrega nodos al árbol

    :param element: elemento a agregar al árbol
    :type element: any
    :param parent: padre del elemento a gregar, defaults to None
    :type parent: any
    """
    new_nodo=Nodo(element,parent)
    if self.peso==0:
      self.root=new_nodo
      self.peso+=1
      self.altura+=1
    else:
      parent_nodo=self.search_nodo(self.root,parent)
      if parent_nodo is not None:
        new_nodo.parent=parent_nodo
        parent_nodo.add_children(new_nodo)
        self.peso+=1
      else:
        raise 'No se ha encontrado el nodo padre'
    
  def get_altura(self)->int:
    """Método que retorna la altura del árbol

    :return: altura del arbol
    :rtype: int
    """
    return self.calcular_altura(self.root)
  
  def calcular_altura(self,current:any)->int:
    if current is None:
      return 0
    elif len(current.children)==0:
      return 1
    else:
      altura_max=0
      for h in current.children:
        altura_hijo=self.calcular_altura(h)
        altura_max=max(altura_max,altura_hijo)
      return altura_max+1
        
  def get_height(self)->str:
    """Retorna el peso del árbol

    :return: _description_
    :rtype: str
    """
    return f'El peso del árbol es {self.peso}'
      
  def get_nodos(self,current='xd') -> None:
    pass
    # print(f'  {self.root.element}   ')
    # if len(self.root.children)>0:
    #   for h1 in self.root.children:
    #     print(h1.element,end='   ')
    #     if len(h1.children)>0:
    #         for h2 in h1.children:
    #           print(h2.element,end='   ')
    
  #   current_nodo=current
  #   print(current_nodo.element)
  #   if current_nodo.children:
  #     for h in current_nodo.children:
  #       self.get_nodos(h)
      
  # def get_arbol(self) -> None:
  #   self.get_nodos(self.root) 
      
    

if __name__=='__main__':
  ##some class test
  a=Arbol()
  a.add(20)
  print(a.root.element)
  a.add(30,20)
  a.add(10,20)
  hijo=a.root.children
  print(f'los hijos de la raiz {a.root.element} del arbol son :')
  for ele in hijo:
    print(ele.element)
  a.add(40,30)
  print(f'La altura del árbol es : {a.get_altura()}')
  print(f'el peso del arbol es {a.get_height()}')
  # a.get_nodos()
  # a.add(10,20)
  # a.add(40,20)
  # a.devolver()