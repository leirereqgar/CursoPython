from moduloT2 import *

n = int(input("Introduzca un número: "))

fac = factorial(n)

primo = esPrimo(n)

print("El factorial de " + str(n) + " es: " + str(fac))

if primo:
	print(str(n) + " es primo")
else:
	print(str(n) + " no es primo")
