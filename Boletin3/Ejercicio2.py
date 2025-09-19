"""
Escribe un programa no que se tecleen dous números de
tipo short. Se o primeiro é maior ou igual que o
segundo,visualizaremos a resta. En calquera caso
visualizaremos a suma.

"""

def s_r():
    n1 = int(input(f"Introduce un numero: "))
    n2 = int(input(f"Introduce otro numero: "))

    if n1 >= n2:
        print(f"La resta de estos numeros es: {n1 - n2}")
    elif n1 < n2:
        print(f"La suma de estos numeros es: {n1 + n2}")
    else:
        print(f"La suma es {n1 + n2}")
s_r()