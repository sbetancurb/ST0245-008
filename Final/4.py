x = int(input("Cuantos nuggets desea llevar: "))

cont=0
if x%6==0:
    cont = cont+1
elif x%9==0:
    cont = cont+1
elif x%20==0:
    cont = cont+1
else:
    while (x>=6):
        if x%3==0:
            x=x-9
            if x%6==0 or x%9==0:
                cont=cont+1
            else:
                x=x+9
        if x%6==0 or x%9==0: 
            cont=cont+1
        x=x-20
if cont>0:
    print("Se puede pedir esa cantidad de nuggets")
else:
    print("No se puede pedir esa cantidad de nuggets")