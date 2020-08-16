a=str(input("digite palabra a invertir: "))

def palabra_invertida(s):
    if len(s) == 1:
        return s
    else:
        return s[len(s)-1]+palabra_invertida(s[:-1])

print("palabra invertida:", palabra_invertida(a))