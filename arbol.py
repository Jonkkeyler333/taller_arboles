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
        raise ValueError('No se ha encontrado el Nodo padre')
    
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
  
  def get_arbol(self,nodo_actual=None,nivel=0)->None:
    if not nodo_actual:
      nodo_actual = self.root
    if nivel > 0:
      print("    " * nivel + str(nodo_actual.element))
    for hijo in nodo_actual.children:
      self.get_arbol(hijo,nivel+1)
      
    """
    Recorrido pre-orden : el recorrido inicia en la Raíz y 
    luego se recorre en pre-orden cada unos de los 
    sub-árboles de izquierda a derecha
    """
  def buscar_preorden(self,element:any,current_nodo=None)->Nodo:
    if not(current_nodo):
      current_nodo=self.root
    if current_nodo.element==element:
      return current_nodo
    for hijo in current_nodo.children:
      result=self.buscar_preorden(element,hijo)
      if result:
        return result
    return None
  
if __name__=='__main__':
  ##Programa principal
  import os
  arbol=Arbol()
  def seguir()->bool:
    print('\n Desea realizar otra operación ? \n 1->Si \n 2->No')
    opc=int(input('-> '))
    if opc==1:
      print('\n')
      os.system('cls')
      return False
    else:
      print('El arbol registrado fue : ')
      print(arbol.root.element)
      arbol.get_arbol()
      return True
  
  print('Bienvenido')
  salida=False
  while not(salida):
    print('ingrese la opción que desea realizar :')
    print('1 -> Ingresar nodo','2 -> Calcular peso del árbol','3 ->Calcular altura del árbol','4 ->Realizar una busqueda en el árbol','5 ->Ver el árbol actual','Otra opción númerica ->Salir',sep='\n')
    opc=int(input('->'))
    if opc==1:
      ele=input('Ingrese el nodo \n-> ')
      if (arbol.get_height())==0:
        arbol.add(ele)
      else:
        try:
          padre=input('Ingrese el padre de dicho nodo \n-> ')
          arbol.add(ele,padre)
        except ValueError as err:
          print(err)
          padre=input('Ingrese el padre de dicho nodo \n-> ')
          arbol.add(ele,padre)
      salida=seguir()
      pass
    elif opc==2:
      print(f'El peso del árbol ingresado es : {arbol.get_height()}')
      salida=seguir()
    elif opc==3:
      print(f'La altura del árbol ingresado es : {arbol.get_altura()}')
      salida=seguir()
    elif opc==4:
      node=input('Ingrese el nodo a buscar -> ')
      busqueda=arbol.buscar_preorden(node)
      if not(busqueda):
        print('No se ha encontrado dicho valor')
      else:
        print(f'Se ha encontrado el nodo{busqueda.element} ,cuyo padre es {busqueda.parent.element}')
      salida=seguir()
    elif opc==5:
      print(arbol.root.element)
      arbol.get_arbol()
      salida=seguir()
    else:
      salida=True
      print('El árbol registrado fue : ')
      print(arbol.root.element)
      arbol.get_arbol()