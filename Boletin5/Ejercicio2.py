"""
Escribir un programa que converta un valor dado en grados Fahrenheit a grados
Celsius. Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.
"""

def main():

    grad_f = float(input(f"Introduce la temperatura en Fahrenheit: "))
    grad_c = (grad_f -32) * 5/9

    print(f"{grad_f} grados en Farenheit son {grad_c} grado en celsius")
main()