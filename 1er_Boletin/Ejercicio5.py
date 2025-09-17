'''
**Implementar las funciones que permitan:**

1. Calcular el perímetro y el área de un rectángulo dada su base y su altura.
2. Calcular el perímetro y el área de un círculo dado su radio.
3. Calcular el volumen de una esfera dado su radio.
4. Calcular el área de un rectángulo (alineado con los ejes x e y) dadas sus coordenadas x1, x2, y1, y2.
5. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

'''

#Funciones de las operaciones geometricas principales

def p_a_rectangulo(base, altura):
    perimetro = 2 * (base + altura)
    area = base * altura
    return perimetro, area
def p_a_circulo(radio):
    import math
    perimetro = 2 * math.pi * radio
    area = math.pi * radio ** 2
    return perimetro, area
def volumen_esf(radio):
    import math
    volumen = (4/3) * math.pi * radio ** 3
    return volumen
def area_rectangulo_c(x1,x2,y1,y2):
    base = abs(x1 - x2)
    altura = abs(y1 - y2)

    area = base * altura
    return area

def hipotenusa(c1,c2):
    import math
    h = math.sqrt(c1 ** 2 + c2 ** 2)
    return h

#===MENU PRINCIPAL===

def menu():
    while True:
     print(f"---MENU PRINCIPAL---")
     print(f"Elige una opcion")
     print(f"1. Perimetro y area del rectangulo")
     print(f"2. Perimetro y area del circulo")
     print(f"3. Volumen de la esfera")
     print(f"4. Area rectangulo (usando coordenadas)")
     print(f"5. Calculo hipotenusa")
     print(f"6. Salir")

     opcion = input("Elige una opcion:")

     if opcion == "1":
         base = float(input("Ingresa la base del rectangulo:"))
         altura = float(input("Ingresa la altura del rectangulo:"))
         perimetro , area = p_a_rectangulo(base, altura)
         print(f"El perimetro del rectangulo es: {round(perimetro,3)} y el area es: {round(area,3)}")
     elif opcion == "2":
         radio = float(input("Ingresa el radio del circulo:"))
         perimetro , area = p_a_circulo(radio)
         print(f"El perimetro del circulo es: {round(perimetro, 3)}")
         print(f"El area del circulo es: {round(area, 3)}")
     elif opcion == "3":
         radio = float(input("Ingresa el radio de la esfera:"))
         volumen = volumen_esf(radio)
         print(f"El volumen de la esfera es: {round(volumen,3)}")
     elif opcion == "4":
         x1 = float(input("Ingresa la coordenada x1:"))
         x2 = float(input("Ingresa la coordenada x2:"))
         y1 = float(input("Ingresa la coordenada y1:"))
         y2 = float(input("Ingresa la coordenada y2:"))
         area = area_rectangulo_c(x1, x2, y1, y2)
         print(f"El area del rectangulo es: {round(area,3)}")
     elif opcion == "5":
         c1 = float(input("Ingresa el primer cateto:"))
         c2 = float(input("Ingresa el segundo cateto:"))
         h = hipotenusa(c1, c2)
         print(f"La hipotenusa es: {round(h,3)}")
     elif opcion == "6":
            print("Saliendo del programa...")
            break
     else:
            print("Opcion no valida, intenta de nuevo.")



# Ejecutar el menu
if __name__ == "__main__":
    menu()