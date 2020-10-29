"""
	Autor: Leire Requena Garcia
	Nombre: tarea1.py
	Descripción: Se recibe un usuario y una contraseña y se comprueba si coinciden
				 con alguno ya definido en un diccionario con anterioridad
"""


usuarios = {"laura":"patata", "juanito":"granada", "jose":"contraseña", "arturo":"hola"}

usuario = input("Introduzca su usuario por favor: ")
continua = False

try:
	usuarios[usuario]
	continua = True
except:
	print("El usuario " + usuario + " no existe por favor compruebe que sea correcto\n")

if continua:
	contrasena = input("Introduzca ahora su contraseña: ")

	if usuarios[usuario] == contrasena:
		print("El usuario y la contraseña coinciden con los almacenados. Buenas tardes\n")
	else:
		print("La contraseña introducida no es la del usuario " + usuario)
		print("Compruebe los datos y vuelva a intentarlo\n")
