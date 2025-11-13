from Cuenta import Cuenta

if __name__ == '__main__':
	print(f"======== PROBANDO CLASE CUENTA =====")

	nombre = str(input(f"Añade el nombre del titular: "))
	ncuenta = int(input(f"Añade el numero de tu cuenta: "))
	tinteres = str(input(f"Pon el tipo de interes que tiene: "))
	saldo = float(input(f"Coloca el saldo disponible: "))


	cuenta1 = Cuenta(
		nombre,
		ncuenta,
		tinteres,
		saldo

	)

	cuenta2 = Cuenta(
		nombre="Mario",
		ncuenta=789412563,
		tinteres="Vehicular",
		saldo=56000
	)
# CUENTA USUARIO
	print(cuenta1.mostrar_datos())
	print(f"El aumento resulta en: {cuenta1.aumentar_saldo(20000)}")
	print(f"El reintegro resulta en: {cuenta1.reintegro(5000)}")
	print(cuenta1.transferencia(cuenta2,4000))
# CUENTA DESTINO
	print(cuenta2.mostrar_datos())
