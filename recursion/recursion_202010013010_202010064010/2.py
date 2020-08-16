a=int(input("base:"))
b=int(input("exponente:"))

def potencia(a,b):
    if b==0:
        return 1
    else:
        p=a*potencia(a,b-1)
        return p

print("resultado:",potencia(a,b))