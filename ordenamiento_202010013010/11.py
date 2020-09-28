A=[5,6,4,10,3,9,8,2,1,7]
B=[5,3,4,2,6,1]
C=[]
def quick_sort(unaLista):
    izquierda = []
    derecha = []
    centro = [] #pivote
    if len(unaLista) > 1:
        pivote = unaLista[0]
        for i in unaLista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            else:
                derecha.append(i)
        return quick_sort(izquierda)+centro+quick_sort(derecha)
    else:
        return unaLista

C=quick_sort(A)+quick_sort(B)
print(quick_sort(C))