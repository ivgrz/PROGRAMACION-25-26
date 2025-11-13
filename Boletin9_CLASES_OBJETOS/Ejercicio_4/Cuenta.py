"""
Escribe unha clase Conta para representar unha conta bancaria. Os datos da conta son:

Atributos :
Nome do cliente.
Número de conta.
Tipo de interese.
Saldo.

A clase conterá os seguintes métodos:
Método inicializador.
Métodos setters/ getters para asignar e obter os datos da conta.
Métodos de ingreso. Un ingreso consiste en aumentar o saldo na cantidade que se indique.
Métodos de reintegro. Un reintegro consiste en diminuír o saldo nunha cantidade. A cantidade non pode ser negativa.
Método transferencia que permita pasar diñeiro dunha conta a outra Exemplo de uso do método transferencia:
 cuentaOrigen.transferencia( cuentaDestino, importe); que indica que queremos facer unha transferencia desde cuentaOrigen a cuentaDestino do importe indicado.
Proba o funcionamento da clase Conta na clase principal.

"""



class Cuenta:
	def __init__(self, nombre: str, ncuenta: int, tinteres: str, saldo: float):
		self._nombre = nombre
		self._ncuenta = ncuenta
		self._tinteres = tinteres
		self._saldo = saldo


#--------- GETTERS ----------

	def get_nombre(self):
		return self._nombre
	def get_ncuenta(self):
		return self._ncuenta
	def get_tinteres(self):
		return self._tinteres
	def get_saldo(self):
		return self._saldo

#--------- GETTERS ----------

#--------- SETTERS ----------
	def set_nombre(self,n_nombre: str):
		self._nombre = n_nombre
	def set_ncuenta(self,n_ncuenta: int):
		self._ncuenta = n_ncuenta
	def set_tinteres(self,n_tinteres: str):
		self._tinteres = n_tinteres
	def set_saldo(self,n_saldo: float):
		self._saldo = n_saldo

#--------- SETTERS ----------

	def aumentar_saldo(self, cantidad):
		if cantidad < 0:
			raise ValueError("La cantidad no puede ser negativa")
		self._saldo += cantidad
		return self._saldo
	def reintegro(self, mcantidad):
		if mcantidad < 0:
			raise ValueError("La cantidad no puede ser negativa")
		elif mcantidad > self._saldo:
			raise ValueError("La cantidad no puede ser mayor al saldo")

		self._saldo += mcantidad
		return self._saldo

	def mostrar_datos(self):
		return (f"El titular de la cuenta es don/doña: {self._nombre}\n"
				f"El numero de la cuenta es: {self._ncuenta}\n"
				f"El tipo de interes es: {self._tinteres}\n"
				f"El saldo disponible: {self._saldo}")

	def transferencia(self,cuenta_destino: 'Cuenta',importe: float) -> bool:
		if importe < 0:
			raise ValueError ("El importe no puede ser negativo")
		elif importe > self._saldo:
			raise ValueError("Saldo insuficiente")
		self._saldo -= importe
		cuenta_destino._saldo += importe
		print(f"La cuenta a la que se le ha transferido es: {cuenta_destino.get_ncuenta()}")
		return True
