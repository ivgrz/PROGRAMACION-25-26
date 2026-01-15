from Boletin10_Excepciones.Deportista.Persona import Persona
from LicenciaNoValida import LicenciaNoValida

class Deportista(Persona):
	def __init__(self, nombre, direccion, dni, deporte, club, licencia):
		super().__init__(nombre, direccion, dni)
		self.set_deporte(deporte)
		self.set_club(club)
		self.set_licencia(licencia)

	#SETTERS
	def set_deporte(self,deporte):
		if not isinstance(deporte, str):
			self.__deporte = None
			return
		self.__deporte = deporte

	def set_club(self, club):
		if not isinstance(club, str):
			self.__club = None
			return
		self.__club = club

	def set_licencia(self, licencia):
		LicenciaNoValida.validar(licencia)
		self.__licencia = licencia


	# GETTERS
	def get_deporte(self):
		return self.__deporte
	def get_club(self):
		return self.__club
	def get_licencia(self):
		return self.__licencia

	def __str__(self):
		return(f"Nombre: {self.get_nombre()}\nEdad: {self.get_direccion()}\nDNI:{self.get_dni()}\n"
			   f"Deporte: {self.get_deporte()}\nClub: {self.get_club()}\nLicencia: {self.get_licencia()}")

	deporte = property(get_deporte, set_deporte)
	club= property(get_club, set_club)
	licencia = property(get_licencia, set_licencia)