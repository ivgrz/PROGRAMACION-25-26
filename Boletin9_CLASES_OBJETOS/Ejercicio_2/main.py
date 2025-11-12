from Boletin9_CLASES_OBJETOS.Ejercicio_2.Consumo import pedirdatosusuario
from Consumo import Consumo

if __name__ == '__main__':

	consumo1 = Consumo(
					km=300.0,
					litros=50.0,
					vmed= 90.0,
					pgas= 1.57
	)
	print(f"--- DATOS DEL PRIMER OBJETO ----")
	print(consumo1.mostrar_datos())
	print("=" * 40)



	consumo2 = pedirdatosusuario()

	consumo2.setlitros(50.0)
	consumo2.set_pgas(1.57)
	print(f"Valores de litros y precio de gas asignados...")
	print(f"\nDetalle de datos: "
		  f"Consumo medio del segundo objeto: {consumo2.consumo_medio():.2f}"
		  )
# ACTUALIZAMOS DATOS
	try:
		nuevos_litros = float(input(f"Introduce los litros actualizados: "))
		consumo2.setlitros(nuevos_litros)
		print(f"Nuevos litros cosumidos: {consumo2.consumo_medio():.2f} (L/100km)")
	except ValueError:
		print(f"Error: Entrada no valida, no se modifican los datos")

	print(f"Velocidad media del 2do objeto: {consumo2.getmved():.2f} km/h"
		  f"\nNuevo consumo medio: {consumo2.consumo_medio():.2f} L/100km")






