"""
Codifica un programa que, utilizando un menú de opcións, calcule a
superficie de distinto tipo de figuras.
O usuario seleccionará a opción desexada escribindo a opción.
Segundo esta, o programa pediralle os datos necesarios para realizar o
cálculo, visualizará o resultado .
No caso de premer unha opción que non teña o menú visualizar unha
mensaxe de “Opción incorrecta “.
1…. Cadrado
2…. Triangulo
3…. Círculo
"""
import math


def menu():
    while True:
        print(f"====MENU====")
        print(f"Elija de cual figura quiere saber su superficie: ")
        print(f"1. Cuadrado")
        print(f"2. Triangulo")
        print(f"3. Circulo")
        opcion = int(input(":"))
        if opcion == 1:
            lado = float(input("Dame la medida del lado: "))
            s_cuad = lado ** 2
            print(f"La superficie de su cuadrado es de {s_cuad:3.f} m^2")
        elif opcion == 2:
            base = float(input(f"Dame la medida de la base: "))
            altura = float(input(f"Que altura tiene? "))
            s_t = (float(base) * float(altura))/2
            print(f"La superficie de su triangulo es: {s_t:3.f} m^2")
        elif opcion == 3:
            radio = float(input(f"Dame la medida del radio: "))
            s_circ = math.pi * (radio ** 2)
            print(f"La superficie del circulo es {s_circ:3.f} m^2")


menu()

