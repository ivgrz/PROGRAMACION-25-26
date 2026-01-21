continuar = "si"
while continuar.lower() == "si":
	nombre_archivo = input("Ingresa el nombre del archivo de texto (Con la extension .txt): ")
	fichero= open(nombre_archivo, "r")
	contenido = fichero.read()

	contenido = contenido.lower()
	contenido = contenido.replace(";","").replace(",","").replace(".","")
	lista_palabras = contenido.split()

	frecuencias = {}
	for p in lista_palabras:
		if p in frecuencias:
			frecuencias[p] += 1
		else:
			frecuencias[p] = 1

		fichero.close()

	print(f"La palabra {palabra} aparece {Contador_P} vez/veces en este txt")

	fichero_1 = open("resumen_palabras.txt","w")
	print("--- RESUMEN DE LAS PALABRAS REPETIDAS ----")
	for palabra in frecuencias:
		resultado = f"{palabra}: {frecuencias[palabra]}"
		print(resultado)
		fichero_1.write(resultado + "\n")
	fichero_1.close()
	print("El resumen se ha guardado correctamente}")
	continuar = input("Quieres analizar otro archivo?(si/no): ")
print("Programa finalizado.")
