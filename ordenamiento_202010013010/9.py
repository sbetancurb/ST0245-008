#Este clase hace una implementación del Set ADT usando una lista ordenada
class Set:
    #Este metodo crea una instancia de conjunto vacía
    def __init__(self):
        self.theElements = list()
    #Este metodo devuelve el número de elementos del conjunto
    def __len__(self):
        return len(self._theElements)
    #Este metodo determina si un elemento está en el conjunto
    def __contains__(self,element):
        ndx=self._findPosition(element)
        self._theElements.insert(ndx,element)
    #Este metodo elimina un elemento del conjunto
    def remove(self,element):
        assert element in self, "the element must be in the set."
        ndx=self._finPosition(element)
        self._theElements.pop(ndx)
    #Este metodo agrega un nuevo elemento único al conjunto
    def add(self, element):
        if element not in self:
            ndx=self._findPosition(element)
            self._theElements.insert(ndx,element)
    #Este metodo determina si este conjunto es un subconjunto del conjunto B
    def isSubsetOf(self,setB):
        for element in self:
            if element not in setB:
                return False
        return True
    #Este metodo devuelve un iterador para recorrer la lista de elementos
    def __iter__(self):
        return _SetIterator(self._theElements)

    #Este metodo encuentra la posición del elemento dentro de la lista ordenada
    def _findPosition(self, element):
        low=0
        high=len(theList) - 1 
        while low<=high:
            mid=(high+low)/2
            if theList[mid]==target:
                return mid
            elif target<theList[mid]:
                high=mid-1
            else:
                low=mid+1
        return low

#Lo que hace este algoritmo es que usa diferentes metodos para realizar diferentes acciones en una lista tales como: 
#adicionar algo, eliminar algo, crear la lista, recorrer la lista,...,etc