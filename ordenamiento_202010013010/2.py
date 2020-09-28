lista=[4,7,11,4,9,5,11,7,3,5]
duplicados=[]
lista2=[]
def quick_sort(lista):
    izquierda = []
    derecha = []
    centro = [] #pivote
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            else:
                derecha.append(i)
        return quick_sort(izquierda)+centro+quick_sort(derecha)
    else:
        return lista
lista2=quick_sort(lista)
print()

for i in lista2:
    if i not in duplicados:
        duplicados.append(i)

print(duplicados)