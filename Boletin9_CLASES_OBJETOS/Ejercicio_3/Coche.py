"""
class Coche:
def __init__(self){
self.velocidade =0 ;
}

Engade a clase Coche os seguintes métodos:
getVelocidade() . Este método devolve a velocidade actual
acelerar (valor). Este método incrementa a velocidade na cantidade valor.
frenar (menos). Este método diminue a velocidade na cantidade menos.
Crea unha clase Boletin 9_3 para comprobar que o programa execútase ben, dandolle os valores que precises.

"""

class Coche:
	def __init__(self, velocidad: int = 0):
		self._velocidad = max(0, int(velocidad))


	def get_velocidad(self):
		return self._velocidad

	def acelerar(self, valor: int = 15):
		self._velocidad += int(valor)
		return self._velocidad

	def frenar(self, menos: int = 10):
		self._velocidad -= int(menos)
		if self._velocidad < 0:
			self._velocidad = 0
		return self._velocidad
