import avisoTormenta
import swowpy

api_key = "fd9783118e7563a98a7f7b3f2acd4d7b"

for i in range(10):
	nombreCiudad = input("Introduzca una ciudad: ")

	mycity = swowpy.Swowpy(api_key, nombreCiudad)

	print("----------------------------------------------")
	print("Ciudad: " + nombreCiudad)
	print("Tiempo: " + str(mycity.current_weather()))
	print("Temperatura: " + str(mycity.temperature(unit="Celsius")))

	presion = mycity.pressure()
	print("Presion: " + str(presion))

	avisoTormenta.aviso(presion)
	print("----------------------------------------------")
