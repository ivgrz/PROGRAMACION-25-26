"""
Codificar o programa que o teclear un número por teclado,
mostre por consola o signo “ + “ se o número é positivo, o signo
“ –“ se é negativo e “ 0 “ se é cero.
"""

def mostrar_signos():
    numero = float(input(f"Introduce un numero:"))
    if numero > 0:
        print(f"+")
    elif numero < 0:
        print(f"-")
    else:
        print(f"Que escribiste??")
mostrar_signos()