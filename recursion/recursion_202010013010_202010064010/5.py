a=str(input("digite una palabra: "))
def palabra_invertida(s):
    if len(s) == 1:
        return s
    else:
        return s[len(s)-1]+palabra_invertida(s[:-1])

if palabra_invertida(a)==a:
    print(a,"es un palindromo")
else:
    print(a,"no es un palindromo")