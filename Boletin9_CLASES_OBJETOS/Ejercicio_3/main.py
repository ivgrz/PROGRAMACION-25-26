from Coche import Coche

if __name__ == '__main__':

    coche1 = Coche(
		velocidad=50
	)

print(f"La velocidad actual del coche es: {coche1.get_velocidad()}\n"
	  f"Acelerando...\n"
	  f"Nueva velocidad: {coche1.acelerar()}\n"
	  f"Frenando...\n"
	  f"Velocidad final: {coche1.frenar()}")