from Deportista import Deportista
from LicenciaNoValida import LicenciaNoValida
from Persona import Persona
from DniNoValido import DniNoValido

if __name__ == '__main__':

	try:
		dp1 = Deportista(nombre="Fran",
						 direccion="Calle A",
						 dni="12345678Z",
						 deporte="Futbol", club="A",
						 licencia="2024FUT123456")
		print(f"Se ha creado la licencia {dp1.licencia} para el usuario {dp1.nombre} con exito!\n"
			  f"USUARIO: \n{dp1}")
	except (LicenciaNoValida, DniNoValido) as e:
		print(f"No se ha podido registrar el usuario: {e}")


