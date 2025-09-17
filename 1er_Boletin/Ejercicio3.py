'''
La salida del programa potencia es poco informativa.
 Escribe una función num_cadrados que muestre el número junto a su potencia (cuadrado).
 Ejecuta el programa de nuevo.
'''
# Programa que calcule la potencia de dos numeros

def potencia_depuracion(base, exponente):
        x = 1

        for i in range(exponente):
            x = x * base
            print(f"Vuelta {i + 1}: x = {x}")  # Depuración: mostrar el valor de x en cada iteración (vuelta)
        print(f"Valor final de x después del ciclo: {x}")  # Depuración: mostrar el valor final de x
        return x
def num_cuadrados(n):
    for i in range(1, n+1):
        print(f"Número: {i}, Cuadrado: {i**2}")

# ----MENU PRINCIPAL ----

def menu():
 while True:
    print("===MENU===")
    print("1. Calcular potencia con depuración")
    print("2. Mostrar números y sus cuadrados")
    print("3. Salir")

    opcion = input("Elige una opcion:")

    if opcion == "1":
        base = int(input("Ingresa la base:"))
        exponente = int(input("Ingresa el exponente:"))
        print(f"Resultado: {potencia_depuracion(base, exponente)}")
    elif opcion == "2":
        n = int(input("ingresa un numero"))
        num_cuadrados(n)
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida, intenta de nuevo.")

# Ejecutar el menu
if __name__ == "__main__":
    menu()