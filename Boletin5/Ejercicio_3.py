"""
Utiliza o programa anterior para xerar unha táboa de conversión de temperaturas,
dende 0º F ata 120º F, de 10 en 10.
"""
def tabla_conversion():

    grad_f = 0


    for i in range (0, 121, 10): # 121 porque el rango no incluye el último número y 10 porque es el incremento
        grad_c = (grad_f - 32) * 5 / 9
# El formato .3f limita a 3 decimales
        print(f"{grad_f} grados en Farenheit son {grad_c:.3f} grado en celsius")


        grad_f += 10
tabla_conversion()