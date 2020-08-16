a=int(input("Numero pequeño:"))
b=int(input("Numero grande:"))

def MCD(a,b):
    if b%a == 0:
        return a
    else:
        return MCD(b,a%b)

print("MCD = ", MCD(a,b))