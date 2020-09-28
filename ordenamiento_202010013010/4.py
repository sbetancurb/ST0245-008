def brechaOrdenamientoPorInsercion(unaLista,inicio,brecha):
    for i in range(inicio+brecha,len(unaLista),brecha):
        valorActual = unaLista[i]
        posicion = i
        while posicion>=brecha and unaLista[posicion-brecha]>valorActual:
            unaLista[posicion]=unaLista[posicion-brecha]
            posicion = posicion-brecha
        unaLista[posicion]=valorActual

pasadas=0
b=0
unaLista = [8,43,17,6,40,16,18,97,11,7]
contadorSublistas = len(unaLista)//2
while contadorSublistas > 0:
  pasadas=pasadas+1
  for posicionInicio in range(contadorSublistas):
      brechaOrdenamientoPorInsercion(unaLista,posicionInicio,contadorSublistas)
      b=b+1
  contadorSublistas = contadorSublistas // 2
print(unaLista)
print("numero de pasadas:",pasadas)
print("numero de intercambios:",b)
