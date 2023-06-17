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
  
  def search_Nodo(self,Nodo_actual:Nodo,parent:any)->Nodo:
    """Este método busca si existe el padre de un Nodo

    :param Nodo_actual: Nodo al que se quiere agregar al arbol
    :type Nodo_actual: Nodo
    :param parent: supuesto padre del Nodo
    :type parent: any
    :return: Si encuentra el Nodo padre lo returna , de lo contrario retorna None
    :rtype: Nodo
    """
    if Nodo_actual.element == parent:
      return Nodo_actual
    for hijo in Nodo_actual.children:
      Nodo_encontrado = self.search_Nodo(hijo,parent)
      if Nodo_encontrado:
        return Nodo_encontrado
    return None
  
  def add(self,element:any,parent=None) -> None:
    """Este método agrega Nodos al árbol

    :param element: elemento a agregar al árbol
    :type element: any
    :param parent: padre del elemento a gregar, defaults to None
    :type parent: any
    """
    new_Nodo=Nodo(element,parent)
    if self.peso==0:
      self.root=new_Nodo
      self.peso+=1
      self.altura+=1
    else:
      parent_Nodo=self.search_Nodo(self.root,parent)
      if parent_Nodo is not None:
        new_Nodo.parent=parent_Nodo
        parent_Nodo.add_children(new_Nodo)
        self.peso+=1
      else:
        raise 'No se ha encontrado el Nodo padre'
    
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
        
  def get_height(self)->int:
    """Retorna el peso del árbol

    :return: _description_
    :rtype: str
    """
    return self.peso
  
  def get_arbol(self, nodo_actual=None,nivel=0):
    if not nodo_actual:
      nodo_actual = self.root
    if nivel > 0:
      print("    " * nivel + str(nodo_actual.element))
    for hijo in nodo_actual.children:
      self.get_arbol(hijo,nivel+1)
  
    
if __name__=='__main__':
  ##some class test
  a=Arbol()
  a.add(20)
  print(a.root.element)
  a.add(30,20)
  a.add(10,20)
  print(f'La altura del árbol es : {a.get_altura()}')
  print(f'El peso del arbol es :{a.get_height()}')
  a.add(9,20)
  a.add(322,20)
  a.add(40,30)
  a.add(44000,40)
  a.add(312,10)
  a.add(232,9)
  a.add(69,322)
  hijo=a.root.children
  print(f'los hijos de la raiz {a.root.element} del arbol son :')
  for ele in hijo:
    print(ele.element,end=' ')
  print(f'La altura del árbol es : {a.get_altura()}')
  print(f'El peso del arbol es :{a.get_height()}')
  print('XDDDDD')
  print(a.root.element)
  a.get_arbol(a.root)
  ##Programa principal
  