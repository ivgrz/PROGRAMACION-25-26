"""
 Utiliza o operador ternario para calcular o valor absoluto dun número
que se solicita o usuario por teclado.
"""
def v_absoluto():
    n = float(input("Dame un numero: "))
# ESTE ES EL OPERADOR TERNARIO
    abs = n if n >= 0 else -n

    print(f"El valor absoluto de {n} es {abs}")
v_absoluto()