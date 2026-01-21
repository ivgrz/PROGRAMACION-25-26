archivos_notas = "notas.txt"

opcion = ""

while opcion != "4":
	print("\n-- Gestor de notas --\n")
	print("1. Añadir nota")
	print("2. listar notas")
	print("3. Buscar notas")
	print("4. salir")

	opcion = input("Escribe una opción: ")


	if opcion == "1":
		nueva_nota = input("Escribe tu nota: ")

		fichero = open(archivos_notas, "a")
		fichero.write(nueva_nota + "\n")
		fichero.close()
		print("Fichero guardado correctamente")
	elif opcion == "2":
		print("--- Todas las notas ---")
		fichero = open(archivos_notas, "r")

		for linea in fichero:
			print(" -" + linea.strip())
		fichero.close()

	elif opcion == "3":
		palabra = input("Escribe la palabra clave: ")
		fichero = open(archivos_notas, "r")
		for linea in fichero:
			if palabra.lower() in linea.lower():
				print(" -" + linea.strip())
		fichero.close()

