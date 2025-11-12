from Clase_Libro import Libro

if __name__ == '__main__':

	print(f"Introduce los datos del libro: ")

	u_titulo = str(input("Introduce el titulo: "))
	u_autor = str(input(f"Introduce el autor: "))

	try:
		u_anho = str(input(f"Introduce el año de publicacion: "))
	except ValueError:
		print(f"Error: El año debe ser un numero entero")
		u_anho = 0

	try:
		u_numpaginas = str(input(f"Introduce el numero de paginas que tiene el libro: "))
	except ValueError:
		print(f"Error: Introducir valores enteros")
		u_numpaginas = 0

	try:
		u_valoracion = str(input(f"Introduce la valoracion que tiene este libro: "))
	except ValueError:
		print(f"Error: Introduce valores numericos")
		u_valoracion = 0.0

	print("\n" + "=" * 30 + "\n")

	libro_usuario = Libro(
		u_titulo,
		u_autor,
		u_anho,
		u_numpaginas,
		u_valoracion
	)

	print(f"Libro creado correctamente...")
	print(libro_usuario.mostrar_libro())





