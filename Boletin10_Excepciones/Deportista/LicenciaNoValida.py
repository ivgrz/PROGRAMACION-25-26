class LicenciaNoValida(Exception):
	def __init__(self, mensaje, licencia):
		super().__init__()
		self.mensaje = mensaje
		self.licencia = licencia

	def __str__(self):
		return "Error: " + str(self.mensaje) + (f" (licencia={self.licencia})" if self.licencia else "")

	@staticmethod
	def validar(licencia):

		if not isinstance(licencia, str):
			raise LicenciaNoValida(f"La licencia no tiene formato valido", licencia)

		s = licencia.strip().upper()
		if len(s) != 13:
			raise LicenciaNoValida(f"Las licencias deben tener 13 caracteres, se han recibido {len(s)}", licencia)
		n_licencia = s[7:13]
		deportes = ["FUT","BAL","VOL","NAT","ATL"]
		deport = s[4:7]
		anho = s[:4]
		if not anho.isdigit():
			raise LicenciaNoValida("El año debe ser un entero", licencia)
		if deport not in deportes:
			raise LicenciaNoValida("Añade uno de los deportes disponibles", licencia)
		if not n_licencia.isdigit():
			raise LicenciaNoValida("Numero de licencia no valido", licencia)
		return True