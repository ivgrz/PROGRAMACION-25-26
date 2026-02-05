from Boletin10_Excepciones.Ajuste_Fechas.FormatoFechaError import FormatoFechaError

class Fecha:
	MIN_ANHO = 1970
	MAX_ANHO = 2999

	def __init__(self, dia, mes, anho):
		# Validar tipos básicos (se permiten enteros o cadenas numéricas)
		try:
			dia = int(dia)
			mes = int(mes)
			anho = int(anho)
		except Exception:
			raise FormatoFechaError("Día, mes y año deben ser enteros", dia, mes, anho)

		# Validar rango
		if not (self.MIN_ANHO <= anho <= self.MAX_ANHO):
			raise FormatoFechaError(f"Año inválido: {anho}. Debe estar entre {self.MIN_ANHO} y {self.MAX_ANHO}.", dia, mes, anho)
		if not (1 <= mes <= 12):
			raise FormatoFechaError(f"Mes inválido: {mes}. Debe estar entre 1 y 12.", dia, mes, anho)
		max_dia = self.dias_del_mes(mes, anho)
		if not (1 <= dia <= max_dia):
			raise FormatoFechaError(f"Día inválido: {dia} para mes {mes} y año {anho} (máx {max_dia}).", dia, mes, anho)

		# Asignar atributos privados
		self.__dia = dia
		self.__mes = mes
		self.__anho = anho

	# SETTERS
	def set_dia(self, dia):
		try:
			dia = int(dia)
		except Exception:
			raise FormatoFechaError("Día debe ser un entero", dia, self.__mes, self.__anho)
		max_dia = self.dias_del_mes(self.__mes, self.__anho)
		if not (1 <= dia <= max_dia):
			raise FormatoFechaError(f"Día inválido: {dia} para mes {self.__mes} y año {self.__anho} (máx {max_dia}).", dia, self.__mes, self.__anho)
		self.__dia = dia

	def set_mes(self, mes):
		try:
			mes = int(mes)
		except Exception:
			raise FormatoFechaError("Mes debe ser un entero", self.__dia, mes, self.__anho)
		if not (1 <= mes <= 12):
			raise FormatoFechaError(f"Mes inválido: {mes}. Debe estar entre 1 y 12.", self.__dia, mes, self.__anho)
		# Si el día actual no es válido en el nuevo mes, lanzar excepción (decisión: setters estrictos)
		max_dia = self.dias_del_mes(mes, self.__anho)
		if self.__dia > max_dia:
			raise FormatoFechaError(f"Operación inválida: al cambiar mes el día actual ({self.__dia}) no es válido para {mes}/{self.__anho}.", self.__dia, mes, self.__anho)
		self.__mes = mes

	def set_ano(self, anho):
		try:
			anho = int(anho)
		except Exception:
			raise FormatoFechaError("Año debe ser un entero", self.__dia, self.__mes, anho)
		if not (self.MIN_ANHO <= anho <= self.MAX_ANHO):
			raise FormatoFechaError(f"Año inválido: {anho}. Debe estar entre {self.MIN_ANHO} y {self.MAX_ANHO}.", self.__dia, self.__mes, anho)
		# Si el día actual no es válido en el nuevo año (29/2), lanzar excepción
		max_dia = self.dias_del_mes(self.__mes, anho)
		if self.__dia > max_dia:
			raise FormatoFechaError(f"Operación inválida: al cambiar año el día actual ({self.__dia}) no es válido para {self.__mes}/{anho}.", self.__dia, self.__mes, anho)
		self.__anho = anho

	# GETTERS
	def get_dia(self):
		return self.__dia
	def get_mes(self):
		return self.__mes
	def get_anho(self):
		return self.__anho

	# Helpers
	@staticmethod
	def es_bisiesto(anho):
		return (anho % 4 == 0 and (anho % 100 != 0 or anho % 400 == 0))

	@classmethod
	def dias_del_mes(cls, mes, anho):
		if mes in (1,3,5,7,8,10,12):
			return 31
		if mes in (4,6,9,11):
			return 30
		# febrero
		return 29 if cls.es_bisiesto(anho) else 28

	# Metodos
	def __eq__(self, otraf):
		if not isinstance(otraf, Fecha):
			return False
		return (self.__dia == otraf.get_dia() and
		self.__mes == otraf.get_mes() and
		self.__anho == otraf.get_anho())

	def incrementar_dia(self, n=1):
		for _ in range(n):
			self.__dia += 1
			max_dia = self.dias_del_mes(self.__mes, self.__anho)
			if self.__dia > max_dia:
				self.__dia = 1
				self.incrementar_mes(1)

	def incrementar_mes(self, n=1):
		# sumar meses y ajustar año
		total_meses = self.__mes + n
		# calcular nuevo año y mes
		anho_incremento = (total_meses - 1) // 12
		nuevo_mes = ((total_meses - 1) % 12) + 1
		nuevo_anho = self.__anho + anho_incremento
		if nuevo_anho > self.MAX_ANHO:
			raise FormatoFechaError(f"Operación inválida: año resultado {nuevo_anho} supera el máximo {self.MAX_ANHO}.", self.__dia, nuevo_mes, nuevo_anho)
		# ajustar día si es mayor que el max del nuevo mes
		max_dia = self.dias_del_mes(nuevo_mes, nuevo_anho)
		if self.__dia > max_dia:
			self.__dia = max_dia
		self.__mes = nuevo_mes
		self.__anho = nuevo_anho

	def incrementar_ano(self, n=1):
		nuevo_anho = self.__anho + n
		if nuevo_anho > self.MAX_ANHO:
			raise FormatoFechaError(f"Operación inválida: año resultado {nuevo_anho} supera el máximo {self.MAX_ANHO}.", self.__dia, self.__mes, nuevo_anho)
		# ajustar día si 29/2 deja de ser válido
		max_dia = self.dias_del_mes(self.__mes, nuevo_anho)
		if self.__dia > max_dia:
			self.__dia = max_dia
		self.__anho = nuevo_anho

	def __str__(self):
		return (f"Fecha: {self.get_dia():02d}/{self.get_mes():02d}/{self.get_anho():04d}")
