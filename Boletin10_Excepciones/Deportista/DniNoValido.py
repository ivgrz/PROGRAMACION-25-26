class DniNoValido(Exception):

	def __init__(self, mensaje, dni):
		super().__init__()
		self.mensaje = mensaje
		self.dni = dni


	def __str__(self):
		return "Error: " + str(self.mensaje) + (f" (dni={self.dni})" if self.dni else "")

	@staticmethod
	def validar_dni(dni):
		import re
		if not isinstance(dni, str):
			raise DniNoValido(f"El DNI debe ser una cadena de caracteres", dni)

		s = dni.strip().upper()
		if not re.fullmatch(r"\d{8}[A-Z]", s):
			raise DniNoValido(f"El DNI debe ser una cadena de 8 caracteres", dni)
		numero = int(s[:8])
		tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
		letra_esperada =tabla[numero % 23]
		if s[8] != letra_esperada:
			raise DniNoValido(f"La letra del DNI {dni} no es la aecuada", dni)
		return True


