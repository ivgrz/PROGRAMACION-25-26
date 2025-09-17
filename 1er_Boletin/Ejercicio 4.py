'''
Escribe una función que le pregunte al usuario:

su nombre y luego lo salude;

dos números y después muestre el producto.
'''
def saludo():
    nombre = input("¿Cual es tu nombre?:").strip()
    print(f"Hola {nombre}")

def producto():
    num1 = float(input("Ingresa el primer numero:"))
    num2 = float(input("Ingresa el segundo numero:"))
    producto = num1 * num2
    print(f"El producto de {num1} y {num2} es : {producto}")
if __name__ == "__main__":
    saludo()
    producto()