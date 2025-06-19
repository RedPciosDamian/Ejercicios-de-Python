password = input("ingresa tu contraseña, por favor: ")


while password != "1234":     # Mientras la contraseña no es igual a 1234 se repite el print y el pedido de nuevo ingreso
   password = input("contraseña incorrecta, volve a ingresarla: ")   #Es interesante como la variable imprime y toma un valor en la misma linea de código


print("contraseña correcta")