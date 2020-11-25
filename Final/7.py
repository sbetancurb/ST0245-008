  
class Alumno:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
    def __str__(self):
       return self.nombre+' - '+str(self.edad)+' años :'+str(self.nota)
class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

primero = None
alumno = Alumno('Alex', 30, 8.9)
nodo = Nodo(alumno)
nodo.siguiente = primero
primero = nodo
alumno = Alumno('Pepe', 27, 3.7)
nodo = Nodo(alumno)
nodo.siguiente = primero
primero = nodo
n = primero
while n != None:
 print(n.datos)
 n = n.siguiente

#7.1	que estructura se utilizó para almacenar los datos de los estudiantes?
#se utilizaron nodos para almacenar los datos de los estudiantes
#7.2	que complejidad tiene este algoritmo
#complejidad lineal = O(n)
#7.3	Realice las optimizaciones de código a este algoritmo
#7.4	Que complejidad tiene después de la mejora realizada en 7.3