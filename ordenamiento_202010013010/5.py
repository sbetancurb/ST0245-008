b=int(input("numero de votos permitidos: "))
voto=[]
ID1='1'
ID2='2'
ID3='3'
cand1=0
cand2=0
cand3=0
for n in range(b):
    a=input("Ingrese el numero del candidato al que quiere votar: ")
    voto.append(a)
for n in range(len(voto)):
    if voto[n]==ID1:
        cand1=cand1+1
    elif voto[n]==ID2:
        cand2=cand2+1
    elif voto[n]==ID3:
        cand3=cand3+1

if cand1>cand2 and cand1>cand3:
    print("el candidato 1 gano las elecciones con",cand1,"votos")
elif cand2>cand1 and cand2>cand3:
    print("el candidato 2 gano las elecciones con",cand2,"votos")
elif cand3>cand1 and cand3>cand2:
    print("el candidato 3 gano las elecciones con",cand3,"votos")
elif cand1==cand2 and cand2==cand3:
    print("repetir votacion")

#El algoritmo tiene una complejidad de 13n+25