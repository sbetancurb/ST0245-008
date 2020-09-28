lista=[4,7,11,4,9,5,11,7,3,5,6,6]
duplicados=[]
for i in lista:
    if i not in duplicados:
        duplicados.append(i)

print(duplicados)