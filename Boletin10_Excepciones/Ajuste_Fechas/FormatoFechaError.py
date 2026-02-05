class FormatoFechaError(Exception):
	def __init__(self, mensaje, dia=None, mes=None, anho=None):
		super().__init__(mensaje)
		self.mensaje = mensaje
		self.dia = dia
		self.mes = mes
		self.anho = anho

	def __str__(self):
		fecha_str = f" ({self.dia}/{self.mes}/{self.anho})" if self.dia is not None else ""
		return f"Error de Formato: {self.mensaje}{fecha_str}"

	@staticmethod
	def validar(dia, mes, anho):
		# Validación mínima de ejemplo; la validación completa se realiza en Fecha
		if not (1970 <= int(anho) <= 2999):
			raise FormatoFechaError(f"El año está fuera de rango (1970-2999): {anho}", dia, mes, anho)
		if not (1 <= int(mes) <= 12):
			raise FormatoFechaError(f"El mes está fuera de rango (1-12): {mes}", dia, mes, anho)
