## para frenar un bucle infinito
while True:
    resultado = input("ingrese s o n")
    if not resultado == "s" and not resultado == "n":
        print("respuesta invalida")
        continue            #así logramos saltar el resto de la iteración. Dentro del bucle del if. (misma linea de sangría)
    if resultado == "n":
        print("exelente, se detiene con break")
        break
    
    elif resultado != "n":  #no hace falta escribir este codigo, porque estoy pasando con pass.
        pass                #no hace falta escribir este codigo, porque estoy pasando con pass.
    else :                  #no hace falta escribir este codigo, porque estoy pasando con pass.
        pass                #no hace falta escribir este codigo, porque estoy pasando con pass.

    print("luego del break, se imrpime sin parar el ciclo")