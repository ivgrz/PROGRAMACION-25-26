"""
Crea una clase llamada Libro que contenga los siguientes atributos:

String titulo;

String autor;

int ano; (año)

short numPaginas; (númPaginas)

float valoracion; (valoración)

La clase debe tener el método de inicialización (constructor).

Establecer los métodos de acceso para todos los atributos (getters).

Codificar el método mostrarLibro, que devuelva una cadena de texto (String) y muestre todas las características de un libro.

Crear una clase Principal con el método main. Crear un libro con cada constructor (se entiende que uno con el constructor con todos los parámetros y, opcionalmente, uno con el constructor por defecto) y mostrar por consola su información.
"""



class Libro:
	def __init__(self, titulo: str, autor: str, anho: int, numpaginas: int, valoracion: float):

		self._titulo = titulo
		self._autor = autor
		self._anho = anho
		self._numpaginas = numpaginas
		self._valoracion = valoracion

# -------- GETTERS ---------

	@property
	def titulo(self):
		print(f"Accediendo al titulo...")
		return self._titulo
	@property
	def autor(self):
		print(f"Accediendo al autor...")
		return  self._autor

	@property
	def anho(self):
		print(f"Accediendo al año...")
		return self._anho

	@property
	def numpaginas(self):
		print(f"Accediendo al numero de paginas...")
		return self._numpaginas
	@property
	def valoracion(self):
		print(f"Accediendo a la valoracion...")
		return self._valoracion
# ------- GETTERS ------------------


	def mostrar_libro(self):
		cadena = (f"El titulo de este libro es: {self.titulo}\n"
				  f"El autor de este libro es: {self.autor}\n"
				  f"El año de publicacion de este libro es: {self.anho}\n"
				  f"El numero de paginas de este libro es: {self.numpaginas}\n"
				  f"La valoracion de este libro es: {self.valoracion}")
		return cadena





