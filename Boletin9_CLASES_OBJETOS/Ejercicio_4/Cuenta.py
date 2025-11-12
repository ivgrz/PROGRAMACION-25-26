class Cuenta:
	def __init__(self, nombre, ncuenta, tinteres, saldo):
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
		self._saldo += cantidad
		return self._saldo
	def reintegro(self, mcantidad):
		self._saldo += mcantidad
		return self._saldo
	def transferencia(self,cuenta_destino,importe,):
		cuenta_destino = self._saldo - importe
		return cuenta_destino
