'''
La salida del programa potencia es poco informativa.
 Escribe una función num_cadrados que muestre el número junto a su potencia (cuadrado).
 Ejecuta el programa de nuevo.
'''
# Programa que calcule la potencia de dos numeros

def potencia_depuracion(base, exponente):
        x = 1

        for i in range(exponente):
            x *= base
            print(f"{base} ^ {i + 1} = {x}")  # Depuración: mostrar el valor de x en cada iteración (vuelta)
        print(f"Valor final: {x}")  # Depuración: mostrar el valor final de x
        return x
def num_cuadrados(base):
    x = 1.0
    for i in range(2):
        x *= base
        print(f"Vuelta {i + 1}: {base} ^ 2 = {x}")  # Depuración: mostrar el valor de x en cada iteración (vuelta)
    print(f"{base} ^ 2 = {x}")  # Depuración: mostrar el valor final de x
    return round(x, 3)


# ----MENU PRINCIPAL ----

def menu():
 while True:
    print("===MENU===")
    print("1. Calcular potencia con depuración")
    print("2. Mostrar números y sus cuadrados")
    print("3. Salir")

    opcion = input("Elige una opcion:")

    if opcion == "1":
        base = float(input("Ingresa la base:"))
        exponente = int(input("Ingresa el exponente:"))
        print(f"Resultado:", round(potencia_depuracion(base, exponente), 3))
    elif opcion == "2":
        n = float(input("ingresa un numero: "))
        num_cuadrados(n)
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida, intenta de nuevo.")

# Ejecutar el menu
if __name__ == "__main__":
    menu()