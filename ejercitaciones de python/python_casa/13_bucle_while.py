lenguajes = ["phyton","Ruby","java","javascrip","C++"]
# BUCLE MIENTRAS
n = 1
while n <= 5:   # el bucle se repite hasta que i sea igual a 5 y luego termina
    print(n)
    n = n + 1

p = 1
while p <= 5:   # el bucle se repite hasta que i sea igual a 5 y luego termina
    print(p * "Damian")
    p = p + 1

i = 0           # el indice es 0 ya que las listas comienzan desde el mismo
while i < len(lenguajes):   # len es una funcion que devuelve un entero, el numero de cada elemento de una lista o contenedor
    print(lenguajes[i])     # imprime cada elemento de la lista en orden
    i = i + 1

print("vamos a obtener el mismo resultado utilizando el bucle for:")
for leng in lenguajes: #imprime cada elemento "leng" que este dentro de lenguajes, lo podemos llamar de cualquier manera.
 print(leng)  


print("vamos a obtener el mismo resultado utilizando el bucle for con otra variable:")
for n in lenguajes: #imprime cada elemento "n" que este dentro de lenguajes, lo podemos llamar de cualquier manera.
 print(n)  

