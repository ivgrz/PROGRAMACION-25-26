from DniNoValido import DniNoValido
class Persona:
	def __init__(self, nombre, direccion, dni):
		self.set_nombre(nombre)
		self.set_direccion(direccion)
		self.set_dni(dni)


	# GETTERS
	def get_nombre(self):
		return self.__nombre
	def get_dni(self):
		return self.__dni
	def get_direccion(self):
		return self.__direccion

	# SETTERS

	def set_nombre(self, nombre):
		if not isinstance(nombre, str):
			raise TypeError("El nombre debe ser un string")
		self.__nombre = nombre

	def set_dni(self, dni):
		if dni is None:
			self.__dni = None
			return
		DniNoValido.validar_dni(dni)
		self.__dni = dni

	def set_direccion(self, direccion):
		if not isinstance(direccion, str):
			raise TypeError("La direccion no tiene el formato valido")
		self.__direccion = direccion



	nombre = property(get_nombre, set_nombre)
	dni = property(get_dni,set_dni)
	direccion = property(get_direccion,set_direccion)
