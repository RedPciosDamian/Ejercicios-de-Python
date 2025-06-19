print("---Bienvenido a la Tabla de multiplicar---")

numero = int(input("---ingresar un numero: "))  #en el input le convertimos el string a entero
print(f"{numero} x 0 = {numero*0} ")            #hice esta linea para poder ver el producto por cero
for n in range(1,11): #la variable n con paso igual a 1, por 11 repeticiones.
    calculo = numero * n
    print(f"{numero} x {n} = {calculo}")  #son 10 repeticiones 
    

lenguajes=["ingles", "guaraní", "español"]    
for n in lenguajes: #imprime cada elemento "n" que este dentro de lenguajes, lo podemos llamar de cualquier manera.
 print(n)  