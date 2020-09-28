futbolistasTop = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),(14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]
futbolistasTop.sort(key=lambda futbolista: futbolista[0])
#a) se obtiene la misma lista, pero ordenada
print("A")
print(futbolistasTop)

#b) lo que hace es que ordena la lista segun el tipo de variable de la posicion ingresada, es decir, si en la posicion ingresada se pone 0 y hay un int a lista se arregla en orden numerico
#si hay un string se arregla segun el alfabeto

#c)se concluye que las listas se ordenan efectivamente
print("C")
lista_1 =[4,7,11,4,9,5,11,7,3,5]
lista_3 =[47,3,21,32,56,92]
lista_4 =[8,43,17,6,40,16,18,97,11,7] 

lista_1.sort(key=lambda hola: hola)
print(lista_1)
lista_3.sort(key=lambda mundo: mundo)
print(lista_3)
lista_4.sort(key=lambda xD: xD)
print(lista_4)

#d)Top 5 mejores inventos 2019
print("D")
inventos=[[3,"Gharged-Up Play"],[1,"Analogue Mega SG"],[4,"Helm Personal Server"],[5,"OR Black Box"],[2,"Postmates Serve"]]
inventos.sort(key=lambda invento: invento[0])
print(inventos)