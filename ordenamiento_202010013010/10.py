matriz=[[1,2,2,2,3,4],[1,2,3,3,4,5],[3,4,4,4,4,6],[4,5,6,7,8,9]]
a=int(input("ingrese elemento a buscar: "))
b=0
c=0
for n in range(4):
    for i in range(6):
        if a==matriz[n][i]:
            print("Numero encontrado en fila",n+1," y columna",i+1)