'''
Insertar instrucciones de depuración que permitan ver el valor asociado con la variable x en el cuerpo del ciclo for
y después de que se sale de dicho ciclo. Volver a ejecutar tres veces el
programa potencia con valores de entrada (3,5), (3,3) y (5,3) respectivamente, y explicar lo que sucede.
'''


# Depuración del código

def potencia_depuracion(base,exponente):
    x = 1
    resultado = 1
    for i in range(exponente):
        x = x*base
        print(f"Vuelta {i+1}: x = {x}")  # Depuración: mostrar el valor de x en cada iteración (vuelta)
    print(f"Valor final de x después del ciclo: {x}")  # Depuración: mostrar el valor final de x
    return x
# Pruebas con diferentes valores de entrada
print("Prueba con (3,5):",potencia_depuracion(3,5))

print("Prueba con (3,3):",potencia_depuracion(3,3))

print("Prueba con (5,3):",potencia_depuracion(5,3))



