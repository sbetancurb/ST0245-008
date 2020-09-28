import time
lista=[-1,-45,-96,-5,-13,-50,-3,-11,-55,-28,-70]
def velocidad(lista):
    negativos=[]
    for n in lista:
        if n<0:
            negativos.append(n)
    return negativos
#El peor de los casos es cuando en la lista todos los numeros son negativos
print(velocidad(lista))

start_time = time.time()
velocidad(lista)
print("tiempo ejecucion del peor caso: %s segundos" % (time.time()-start_time))