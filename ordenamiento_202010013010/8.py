def Omerge(unaLista):
    print("Dividir ",unaLista)
    if len(unaLista)>1:
        mitad = len(unaLista)//2
        mitadIzquierda = unaLista[:mitad]
        mitadDerecha = unaLista[mitad:]
        ## LLamada recursiva para cada lista 
        Omerge(mitadIzquierda)
        Omerge(mitadDerecha)
        i=0
        j=0
        k=0
        while i < len(mitadIzquierda) and j < len(mitadDerecha):
            if mitadIzquierda[i] < mitadDerecha[j]:
                unaLista[k]=mitadIzquierda[i]
                i=i+1
            else:
                unaLista[k]=mitadDerecha[j]
                j=j+1
            k=k+1
        while i < len(mitadIzquierda):
            unaLista[k]=mitadIzquierda[i]
            i=i+1
            k=k+1

        while j < len(mitadDerecha):
            unaLista[k]=mitadDerecha[j]
            j=j+1
            k=k+1
    print("Mezclar ",unaLista)
unaLista=[21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]
Omerge(unaLista)
print(unaLista)

#La lista queda de esta manera despues de 3 llamados recursivos del metodo de mezcla: [[21,1],[26,45],[29,28,2,9],[16,49,39,27,43,34,46,40]]
#queda asi porque el metodo lo qeu hace es al principio parte la lista a la mitad y a cada mitad les asigna derecha e izquierda.
#En la primera llamada recursiva se usa la lista de la izquierda y se hace el mismo metodo; cuando llega a la tercera vez que se llama recursivamente
#al metodo la lista queda de la manera en la qeu dije ya que siempre divide la izquierda en 2 hasta que quede un elemento y ahi empieza a ordenar la parte izquierda,
#despues se hace lo mismo con la derecha.