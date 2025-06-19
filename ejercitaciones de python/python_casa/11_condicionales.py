numero = float(input("ingresa un numero: "))

if numero > 0:                                  #Condicional: SI el numero es positivo?
    print(f"El numero {numero} es positivo")

elif numero < 0:                                #Condicional: O SI el numero es negativo?
    print(f"El numero {numero} es negativo")

else:                                           #Condicional: no es positivo, ni negativo. (negación del SI, y del O SI)
    print("el numero es igual a 0")


puntaje = 58

if puntaje >= 95:                               #Condicional: SI la nota es mayor o igual a 95?                             
    print("aprobado, Excelente")
elif puntaje >= 60:                             #Condicional: O SI el numero es mayor o igual a 60?
    print("aprobaste")
else:                                           #Condicional: negación del SI, y del O SI
    print("desaprobaste, esfuerzate más para la próxima")

print(f"tu nota del examen fue : {puntaje}")                          