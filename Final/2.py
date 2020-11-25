Pila = []

Pila.append(1)
Pila.append(2)
Pila.append(3)
Pila.append(4)
print(Pila)

x= len(Pila)

suma = 0

while(len(Pila)!=0):
    suma=suma+Pila.pop()

promedio = suma / x

print("el promedio de la pila es: ",promedio)