class Fecha:
	def __init__(self, dia, mes, anho):

	#SETTERS
	def set_dia(self, dia):

	def set_mes(self, mes):

	def set_ano(self, anho):

	#GETTERS

	def get_dia(self):
		return self.__dia
	def get_mes(self):
		return self.__mes
	def get_anho(self):
		return self.__anho




	#Metodos
	def __eq__(self, otraf):
		if not isinstance(otraf, Fecha):
			return False
		return (self.__dia == otraf.get_dia() and
		self.__mes == otraf.get_mes() and
		self.__anho == otraf.get_anho())
	def incrementar_dia(self):

		self.__dia += 1
		if self.__dia > 31:  # Esto es una versión básica
			self.__dia = 1
			self.incrementar_mes()

	def incrementar_mes(self):
		self.__mes += 1
		if self.__mes > 12:
			self.__mes = 1
			self.incrementar_ano()

	def incrementar_ano(self):
		self.__ano += 1

	def __str__(self):
		return (f"Fecha: {self.get_dia()}/{self.get_mes()}/{self.get_anho()}")
