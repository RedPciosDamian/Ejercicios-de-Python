temperatura = float(input("ingresar la temperatura a convertir: ")) 

medida = input("la temperatura actual se mide en C o F?: ").lower() # ingresa el string en minuscula


if medida == "c":
   print(f"la temperatura en °F = {(temperatura * 9/5) + 32}")
elif medida == "f":
   print(f"la temperatura en °C = {(temperatura - 32) * 5/9}")
else:
   print(f"el dato ingresado no es correcto: ")