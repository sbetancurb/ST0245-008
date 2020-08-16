a = int(input("digite la posicion: "))

def fibonacci(a):
    if a==0 or a==1:
        return 1
    else:
        return fibonacci(a-1)+fibonacci(a-2)

print("el valor en la posicion",a,"es:",fibonacci(a))