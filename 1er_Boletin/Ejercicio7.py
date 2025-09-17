'''
. Implementar algoritmos que resolvan os seguintes problemas:
1. Dados dous números, indicar a suma, resta, división e multiplicación de ambos.
2. Dado un número enteiro N, imprimir súa táboa de multiplicar.
3. Dado un número enteiro N, imprimir seu factorial.
'''

def num_op(a,b):
    suma = a + b
    resta = a - b
    multiplacion = a * b
    division = a / b
    return suma, resta, multiplacion, division
    #Casos de prueba
num_op(5,3)
num_op(6,3)
num_op(4,8)

def tabla_mult(n):
 for i in range(1,11):
     print(f"{n} x {i} = {n*i}")
#Casos de prueba
tabla_mult(5)
tabla_mult(8)
tabla_mult(12)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
#Casos de prueba
factorial(5)
factorial(3)
factorial(0)
factorial(1)
factorial(6)

def main():
    print(f"Operaciones basicas:")

    print(num_op(5,3))
    print(num_op(6,3))
    print(num_op(4,8))

    print("\n")
    print("Tabla de multiplicar:")
    tabla_mult(5)
    print("\n")
    tabla_mult(8)
    print("\n")
    tabla_mult(12)
    print("\n")
    print("Factoriales:")
    print(factorial(5))
    print(factorial(3))
    print(factorial(0))
    print(factorial(1))
    print(factorial(6))

if __name__ == "__main__":
    main()