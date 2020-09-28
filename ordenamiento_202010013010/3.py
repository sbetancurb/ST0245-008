lista = [47,3,21,32,56,92]
unaLista = [47,3,21,32,56,92]
lista_a = [47,3,21,32,56,92]
#Insercion
def insercion(lista_a):
    a=1
    for i in range(1,len(lista_a)):
        valor_a_ordenar = lista_a[i]
        while lista_a[i-1] > valor_a_ordenar and i >0:
            lista_a[i], lista_a[i-1] = lista_a[i-1], lista_a[i]
            i = i-1
            print("#Pasada:",a," ",lista_a)
            a=a+1
#burbuja
def burbuja(unaLista):
    b=1
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
                print("#Pasada:",b,"",unaLista)
                b=b+1
#seleccion
def seleccion(lista):
    c=1
    d=0
    nb = len(lista)
    for actual in range(0,nb):    
        mas_pequeno = actual
        for j in range(actual+1,nb) :
            if lista[j] < lista[mas_pequeno] :
                mas_pequeno = j
                d=d+1
        if min is not actual :
            temp = lista[actual]
            lista[actual] = lista[mas_pequeno]
            lista[mas_pequeno] = temp
        if d>0:
            print("#Pasada:",c,"",lista)
            c=c+1
            d=0
print("seleccion")
seleccion(lista)
print(" ")
print("insercion")
insercion(lista_a)
print(" ")
print("burbuja")
burbuja(unaLista)

#Se puede usar cualquira de los 3 metodos de ordenamienmto mencionados, ya que al usar cualquier metodo despues de la 2da pasada la lista va a quedar igual al ejemplo
#Se puede ejecutar el algoritmo para comprobar la respuesta