"""
Implementa una clase llamada Consumo que forma parte de la centralita electrónica de un coche y tiene las siguientes características:

Atributos:

km: Kilómetros recorridos por el coche.

litros: Litros de combustible consumidos.

vMed: Velocidad media.

pGas: Precio de la gasolina.

Métodos:

Un método que inicializa los valores de los atributos (Constructor).

getTempo: Indica el tiempo empleado en realizar el viaje (en horas).

consumoMedio: Consumo medio del vehículo (en litros cada 100 km).

consumoEuros: Consumo medio (en € cada 100 km).

setKms: Modifica el valor de los km.

setLitros: Actualiza la cantidad de litros.

setvMed: Actualiza el valor de la vMed.

setPGas: Actualiza el valor del pGas.

En la clase principal:

Crea un objeto de tipo Consumo.
"""


class Consumo:
	def __init__(self, km: float, litros: float, vmed: float, pgas: float):
		self._km = km
		self._litros = litros
		self._vmed = vmed
		self._pgas = pgas


	def gettiempo(self) -> float:


		return (self._km / self._vmed) if self._km > 0 else 0.0

	def consumo_medio(self) -> float:
		"""
		Consumo de litros cada 100 km
		:return: consumo medio
		:rtype: float
		"""

		return (self._litros / self._km) * 100 if self._km > 0 else 0.0

	def consumo_euros(self) -> float:
		"""
		Gasto euros cada 100 km
		:return: gasto
		:rtype: float
		"""

		return self.consumo_medio() * self._pgas

	def mostrar_datos(self):
		return (
			f"Km recorridos: {self._km}\n"
			f"Litros consumidos: {self._litros}\n"
			f"Velocidad media: {self._vmed}\n"
			f"Precio gasolina: {self._pgas}\n"
			f"---------------------------\n"
			f"Tiempo empleado: {self.gettiempo():.2f} horas\n"
			f"Consumo medio: {self.consumo_medio():.2f} L/100km\n"
			f"Gasto medio: {self.consumo_euros():.2f} €/100km\n"
		)


#-------- SETTERS ---------

	def setkms(self, n_km: float):
		self._km = n_km
	def setlitros(self, n_litros: float):
		self._litros = n_litros
	def set_vmed(self, n_vmed: float):
		self._vmed = n_vmed
	def set_pgas(self, n_pgas: float):
		self._pgas = n_pgas
#-------- SETTERS ----------

#-------- GETTERS ----------

	def getmved(self) -> float:
		return  self._vmed
#-------- GETTERS ----------


def pedirdatosusuario() -> Consumo:
	"""Pedimos datos al usuario para el segundo objeto"""
	print(f"Introduce los datos del estado actual de tu coche (objeto 2)")

	try:
		km = float(input(f"Introduce los km: "))
		vmed = float(input(f"Introduce la velocidad media: "))
		litros_iniciales = 0.0
		pgas_inicial = 0.0
		return  Consumo(km, litros_iniciales, vmed, pgas_inicial)
	except ValueError:
		print(f"Error en la entrada de datos, solo ingresa numeros")
		return Consumo(0.0,0.0,0.0,0.0)





