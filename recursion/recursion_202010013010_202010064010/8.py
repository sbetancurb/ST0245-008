x=int(input("digite numero de filas: "))
n=0
k=0
import math
while (n<=x):
    while(k<=n):
        c=n-k
        k1=math.factorial(c)*math.factorial(k)
        respuesta=int(math.factorial(n)/k1)
        k=k+1
        print(respuesta, end=" ")
    print("")
    n=n+1
    k=0